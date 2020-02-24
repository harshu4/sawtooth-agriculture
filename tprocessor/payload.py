from sawtooth_sdk.processor.exceptions import InvalidTransaction

import sys
sys.path.insert(0, "../proto")   #used relative imports for future docker implementation
import agpayload_pb2


class AgricultureMarketPayload(object):
    def __init__(self,payload):
        self._transaction = agpayload_pb2.Realpayload()
        self._transaction.ParseFromString(payload)


    @property
    def action(self):
        return self._transaction.Action

    @property
    def data(self):
        if self._transaction.HasField('reg_far') and \
            self._transaction.Action == \
                agpayload_pb2.action.Value('register_farmer'):
                return self._transaction.reg_far
        elif self._transaction.HasField('reg_buy') and \
            self._transaction.Action == \
                agpayload_pb2.action.Value('register_buyer'):
            return self._transaction.reg_buy

        elif self._transaction.HasField('reg_tra') and \
            self._transaction.Action == \
                agpayload_pb2.action.Value('register_transporter'):
            return self._transaction.reg_tra

        elif self._transaction.HasField('otp_tra') and \
            self._transaction.Action == \
                agpayload_pb2.action.Value('otp_transaction'):
            return self._transaction.otp_tra
        elif self_transaction.HasField('tra_ass') and \
            self._transaction.Action == \
                agpayload_pb2.action.Value('transfer_asset'):
            return self._transaction.tra_ass
        elif self_transaction.HasField('cre_ass') and \
            self._transaction.Action == \
                agpayload_pb2.action.Value('create_asset'):
            return agpayload_pb2.action.cre_ass
        raise InvalidTransaction('Action does not match payload data')

    
