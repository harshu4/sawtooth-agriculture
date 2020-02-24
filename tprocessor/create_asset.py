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
private_key_asset = context.new_random_private_key()
signer_asset = CryptoFactory(context).new_signer(private_key_asset)
public_key_asset = signer_asset.get_public_key().as_hex()
public_key = signer.get_public_key().as_hex()
print(f"public key of famer {public_key} and public key of asset {public_key_asset}")
payload = agpayload_pb2.Realpayload()
payload.Action = agpayload_pb2.action.Value('create_asset')
payload.cre_ass.public_key = public_key_asset
payload.cre_ass.weight = 5
payload.cre_ass.current_owner_pubkey  = '03b36c150df64c40c42c11f9f45b0be5aa406df7404696e0d9ca947fc227a43bf1'
payload.cre_ass.current_owner_pincode = 394230
payload.cre_ass.type_of_food = enums_pb2.type.Value('vegetable_shortt')
payload.cre_ass.Vegetable_short = enums_pb2.vegetable_short.Value('Tomato')
payload.cre_ass.timestamp = 00000
payload.cre_ass.Status = enums_pb2.status.Value('OrderAdded')
input = ['add8ab009179875ea87b8760c805a1bc0c8cfc4d9b36a0acc08defd2452894a8833b58',addresser.get_asset_address(public_key_asset)]
print(input)

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
