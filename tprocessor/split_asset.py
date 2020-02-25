import sys
sys.path.insert(0, "../proto")   #used relative imports for future docker implementation
import agpayload_pb2
import enums_pb2
from hashlib import sha512
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader
from sawtooth_sdk.protobuf.transaction_pb2 import Transaction
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader,Batch,BatchList
from sawtooth_signing import create_context
from sawtooth_signing.secp256k1 import Secp256k1PrivateKey
from sawtooth_signing import CryptoFactory
import urllib.request
from urllib.error import HTTPError
import addresser


PRIVATE_KEY = '347bd546500cdc8c41cf577406c4d3ed84d7bf7a4550848373b6aaf6ae5a14b2'
PUBLIC_KEY = '03bf808bdfe9cd5bf861d8b79b6eea8acbc65c4a5bb080f2ec4081cad34ed1f705'

PRIVATE_KEY_ASSET = 'b5086b76968a86b137b26490295075c3cb4bd039daee6ac052d0b05db57849fb'
PUBLIC_KEY_ASSET = '03b5d33a56bb507b7948e9972ab80bb58ec8cb1981d5eb70b8aba06139e1566668'

PRIVATE_KEY_ASSET1 = 'd23a4adff01c60168c82517f1417d3c75f0b29b4d9282db95de1bc63b9b04833'
PUBLIC_KEY_ASSET1 = '028c6c1b3a6564e6106c2346eba65e0184daad36cb6f729775d94d8bafe17a3d92'

PRIVATE_KEY_ASSET2 = '483dcdf8c18dbde1f61bb9664c6888a221ab94cf5133ba2643cc4eef8b0a8fde'
PUBLIC_KEY_ASSET2 =  '032ea4793531c82d428dbde1bc313871e156e0772ed9ba3853afa7db8df30c2b0d'


context = create_context('secp256k1')
private_key = Secp256k1PrivateKey.from_hex(PRIVATE_KEY)
private_key_asset = Secp256k1PrivateKey.from_hex(PRIVATE_KEY_ASSET)
signer = CryptoFactory(context).new_signer(private_key)
signer_asset = CryptoFactory(context).new_signer(private_key_asset)
public_key_asset = PUBLIC_KEY_ASSET
public_key = PUBLIC_KEY

payload = agpayload_pb2.Realpayload()
payload.Action = agpayload_pb2.action.Value('split_asset')
payload.spl_ass.weight = 3
payload.spl_ass.public_key = public_key_asset
payload.spl_ass.public_key1 = PUBLIC_KEY_ASSET1
payload.spl_ass.public_key2 = PUBLIC_KEY_ASSET2
payload.spl_ass.public_key_farmer = PUBLIC_KEY

input = [addresser.get_farmer_address(PUBLIC_KEY),addresser.get_asset_address(PUBLIC_KEY_ASSET),
         addresser.get_asset_address(PUBLIC_KEY_ASSET1),addresser.get_asset_address(PUBLIC_KEY_ASSET2)]

payload_bytes = payload.SerializeToString()
txn_header_bytes = TransactionHeader(
    family_name='agriculture_market',
    family_version='0.1',
    inputs=input,
    outputs=input,
    signer_public_key=signer.get_public_key().as_hex(),
    # In this example, we're signing the batch with the same private key,
    # but the batch can be signed by another party, in which case, the
    # public key will need to be associated with that key.
    batcher_public_key=signer.get_public_key().as_hex(),
    # In this example, there are no dependencies.  This list should include
    # an previous transaction header signatures that must be applied for
    # this transaction to successfully commit.
    # For example,
    # dependencies=['540a6803971d1880ec73a96cb97815a95d374cbad5d865925e5aa0432fcf1931539afe10310c122c5eaae15df61236079abbf4f258889359c4d175516934484a'],
    dependencies=[],
    payload_sha512=sha512(payload_bytes).hexdigest()
).SerializeToString()


signature = signer.sign(txn_header_bytes)

txn = Transaction(
    header=txn_header_bytes,
    header_signature=signature,
    payload=payload_bytes
)

txns = [txn]

batch_header_bytes = BatchHeader(
    signer_public_key=signer.get_public_key().as_hex(),
    transaction_ids=[txn.header_signature for txn in txns],
).SerializeToString()


signature = signer.sign(batch_header_bytes)

batch = Batch(
    header=batch_header_bytes,
    header_signature=signature,
    transactions=txns
)

batch_list_bytes = BatchList(batches=[batch]).SerializeToString()



try:
    request = urllib.request.Request(
        'http://localhost:8008/batches',
        batch_list_bytes,
        method='POST',
        headers={'Content-Type': 'application/octet-stream'})
    response = urllib.request.urlopen(request)
    print(response.read())
except HTTPError as e:
    response = e.file
