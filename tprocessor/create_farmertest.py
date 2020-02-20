import sys
sys.path.insert(0, "../proto")   #used relative imports for future docker implementation
import agpayload_pb2
import enums_pb2
from hashlib import sha512
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader
from sawtooth_sdk.protobuf.transaction_pb2 import Transaction
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader,Batch,BatchList
from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory
import urllib.request
from urllib.error import HTTPError
import addresser


context = create_context('secp256k1')
private_key = context.new_random_private_key()
signer = CryptoFactory(context).new_signer(private_key)
public_key = signer.get_public_key().as_hex()
payload = agpayload_pb2.Realpayload()
payload.Action = agpayload_pb2.action.Value('register_farmer')
payload.reg_far.public_key = public_key
payload.reg_far.aadhar_card = 'dfv98fsdff98s83'
payload.reg_far.timestamp = 12242343535
payload.reg_far.full_name  = 'Bro Code'
payload.reg_far.State = enums_pb2.state.Value('Gujarat')
payload.reg_far.pincode = 123456
payload.reg_far.mobilenumber = 394834585
payload.reg_far.district = 'sachin'
input = addresser.get_farmer_address(public_key)
print(input)
payload_bytes = payload.SerializeToString()
txn_header_bytes = TransactionHeader(
    family_name='agriculture_market',
    family_version='0.1',
    inputs=[input],
    outputs=[input],
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
