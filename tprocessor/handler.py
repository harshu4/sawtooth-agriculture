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



        if payload.action == agpayload_pb2.action.Value('register_farmer'):
            _create_farmer(
                state=state,
                public_key=header.signer_public_key,
                payload=payload)
        elif payload.action == agpayload_pb2.action.Value('register_buyer'):
            _create_buyer(
                state=state,
                public_key=header.signer_public_key,
                payload=payload)
        elif payload.action == agpayload_pb2.action.Value('register_transporter'):
            _create_transporter (
                state=state,
                public_key=header.signer_public_key,
                payload=payload)

        elif payload.action == agpayload_pb2.action.Value('otp_transaction'):

            _create_otp(
                state= state,
                public_key = header.signer_public_key,
                payload = payload)
        else:
            raise InvalidTransaction("Shut up your mouth!,and read your code")


def _create_farmer(state,public_key,payload):
    state.set_farmer(

        public_key=public_key,
        data=payload.data,
        )

def _create_buyer(state,public_key,payload):
    state.set_buyer(

        public_key=public_key,
        data=payload.data,
    )

def _create_transporter(state,public_key,payload):
    state.set_buyer(
        public_key=public_key,
        data=payload.data,
    )

def _create_otp(state,public_key,payload):
    state.set_otp(
        public_key = public_key,
        data = payload.data
    )

def _get_farmer(state,public_key):
    data = state.get_farmer(
        public_key = public_key)
    print(data)
