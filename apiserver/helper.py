import addresser
from proto import agpayload_pb2
import string
import random
import time
from proto import agpayload_pb2
import addresser
from hashlib import sha512
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader
from sawtooth_sdk.protobuf.transaction_pb2 import Transaction
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader
from sawtooth_sdk.protobuf.batch_pb2 import Batch
from sawtooth_sdk.protobuf.batch_pb2 import BatchList
import urllib.request
from urllib.error import HTTPError


def getRandom(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_OtpPayload_bytes(otpnum,monilenum):
    payload = agpayload_pb2.Realpayload()
    payload.Action = agpayload_pb2.action.Value('otp_transaction')
    payload.otp_tra.timestamp = int(time.time())
    payload.otp_tra.mobilenumber = monilenum
    payload.otp_tra.otp = otpnum
    payload_bytes = payload.SerializeToString()
    return payload_bytes

def getSig(signer,payload):
    return signer.sign(payload)


def getBatchHeader(signer,txns):
    batch_header_bytes = BatchHeader(
        signer_public_key=signer.get_public_key().as_hex(),
        transaction_ids=[txn.header_signature for txn in txns],
    ).SerializeToString()
    return batch_header_bytes

def getBatch(signer,batch_header_bytes,txns):
    batch_id=getSig(signer,batch_header_bytes)
    batch = Batch(
        header=batch_header_bytes,
        header_signature=batch_id,
        transactions=txns
    )
    batch_list_bytes = BatchList(batches=[batch]).SerializeToString()
    return [batch_id , batch_list_bytes]


def getTxn(signer,payload_bytes,txn_header_bytes):
    txn_id=getSig(signer,txn_header_bytes)
    txn = Transaction(
        header=txn_header_bytes,
        header_signature=txn_id,
        payload=payload_bytes
    )
    return [txn_id,txn]

def sendBatch(batch_list_bytes):
    try:
        request = urllib.request.Request(
            'http://localhost:8008/batches',
            batch_list_bytes,
            method='POST',
            headers={'Content-Type': 'application/octet-stream'})
        response = urllib.request.urlopen(request)
        print(response.read())
        return True
    except HTTPError as e:
        print("Error, helper.py line 73:",e)
        return False
    except Exception as e:
        print("Error, helper.py line 76:",e)
        return False


def getTransactionHeader(signer,payload_bytes,tokey,dependencies=[]):
    txn_header_bytes = TransactionHeader(
        family_name='agriculture_market',
        family_version='0.1',
        inputs=tokey,
        outputs=tokey,
        signer_public_key=signer.get_public_key().as_hex(),
        batcher_public_key=signer.get_public_key().as_hex(),
        dependencies=dependencies,
        payload_sha512=sha512(payload_bytes).hexdigest()
    ).SerializeToString()
    return txn_header_bytes