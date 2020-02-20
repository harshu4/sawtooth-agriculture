from sawtooth_sdk.processor.exceptions import InvalidTransaction
import sys
sys.path.insert(0, "../proto")
import farmer_pb2
import buyer_pb2
import transporter_pb2
import addresser



class AgricultureMarketState(object):
    def __init__(self, context, timeout=2):
        self._context = context
        self._timeout = timeout

    def set_farmer(self, public_key, data, timestamp=000):
        """Creates a new farmer in state"""

        address = addresser.get_farmer_address(public_key)
        farmer = farmer_pb2.Farmer(
            public_key=data.public_key, full_name=data.full_name, timestamp=data.timestamp
            ,aadhar_card=data.aadhar_card,State=data.State,pincode=data.pincode,mobilenumber=data.mobilenumber
            ,district = data.district)

        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            raise InvalidTransaction('Action does not match payload data')
        data = farmer.SerializeToString()

        updated_state = {}
        updated_state[address] = data
        print(farmer.ParseFromString(data))
        self._context.set_state(updated_state, timeout=self._timeout)
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        print(farmer.ParseFromString(state_entries[0].data))
    def get_farmer(self,public_key):
        """Fetches data of the farmer
            only for testing mode dev build may not include this"""
        address = addresser.get_farmer_address(public_key)
        farmer = farmer_pb2.Farmer()
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            return farmer.ParseFromString(state_entries[0].data)
