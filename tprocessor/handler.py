import datetime
import time

from sawtooth_sdk.processor.handler import TransactionHandler
from sawtooth_sdk.processor.exceptions import InvalidTransaction
import sys
sys.path.insert(0, "../proto")
import payload as pld
import agpayload_pb2
import enums_pb2
import addresser
import state as ste



class MarketTransactionHandler(TransactionHandler):

    @property
    def family_name(self):
        return addresser.FAMILY_NAME

    @property
    def family_versions(self):
        return [addresser.FAMILY_VERSION]

    @property
    def namespaces(self):
        return [addresser.NAMESPACE]

    def apply(self, transaction, context):
        header = transaction.header
        payload = pld.AgricultureMarketPayload(transaction.payload)
        state = ste.AgricultureMarketState(context)


        print('hello')
        if payload.action == agpayload_pb2.action.Value('register_farmer'):
            _create_farmer(
                state=state,
                public_key=header.signer_public_key,
                payload=payload)

def _create_farmer(state,public_key,payload):
    state.set_farmer(

        public_key=public_key,
        data=payload.data,
        )


def _get_farmer(state,public_key):
    data = state.get_farmer(
        public_key = public_key)
    print(data)
