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

PRIVATE_KEY_ASSET1 = ''
