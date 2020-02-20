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
            raise InvalidTransaction('Already exist , you have an account')
        data = farmer.SerializeToString()

        updated_state = {}
        updated_state[address] = data
        self._context.set_state(updated_state, timeout=self._timeout)

    def set_buyer(self,public_key,data,timestamp=000):
        """Creates a new buyer in state"""
        address = addresser.get_buyer_address(public_key)
        buyer = buyer_pb2.Buyer(
        public_key=data.public_key, full_name=data.full_name, timestamp=data.timestamp
        ,aadhar_card=data.aadhar_card,State=data.State,pincode=data.pincode,mobilenumber=data.mobilenumber
        ,district = data.district)

        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            raise InvalidTransaction('Already exist , you have an account')
        data = buyer.SerializeToString()

        updated_state = {}
        updated_state[address] = data
        self._context.set_state(updated_state, timeout=self._timeout)

    def set_transporter(self,public_key,data,timestamp=000):
        """Creates a new transoporter in state"""
        address = addresser.get_transporter_address
        transporter = transoporter_pb2.Transporter(
        public_key=data.public_key, full_name=data.full_name, timestamp=data.timestamp
        ,aadhar_card=data.aadhar_card,State=data.State,pincode=data.pincode,mobilenumber=data.mobilenumber
        ,district = data.district , driving_license = data.driving_license
        )
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            raise InvalidTransaction('Already exist , you have an account')
        data = transoporter.SerializeToString()

        updated_state = {}
        updated_state[address] = data
        self._context.set_state(updated_state, timeout=self._timeout)



    def get_farmer(self,public_key):
        """Fetches data of the farmer
            only for testing mode dev build may not include this"""
        address = addresser.get_farmer_address(public_key)
        farmer = farmer_pb2.Farmer()
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            return farmer.ParseFromString(state_entries[0].data)
