from sawtooth_sdk.processor.exceptions import InvalidTransaction
import sys
sys.path.insert(0, "../proto")
import farmer_pb2
import buyer_pb2
import otp_pb2
import enums_pb2
import transporter_pb2
import addresser



class AgricultureMarketState(object):
    def __init__(self, context, timeout=2):
        self._context = context
        self._timeout = timeout

    def set_farmer(self, public_key, data, timestamp=000):
        """Creates a new farmer in state"""

        address = addresser.get_farmer_address(public_key)
        otper = otp_pb2.Otp()
        address_otp = addresser.get_otp_address(data.mobilenumber,data.otp)
        state_entries_otp = self._context.get_state(
            addresses=[address_otp], timeout=self._timeout)
        if not state_entries_otp:
            raise InvalidTransaction('No otp was verified on this number')
        otper.ParseFromString(state_entries_otp[0].data)
        if otper.otp != data.otp :
            raise InvalidTransaction('Wrong otp retry dude')

        farmer = farmer_pb2.Farmer(
            public_key=public_key, full_name=data.full_name, timestamp=data.timestamp
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
        otper = otp_pb2.Otp()
        address_otp = addresser.get_otp_address(data.mobilenumber,data.otp)
        state_entries_otp = self._context.get_state(
            addresses=[address_otp], timeout=self._timeout)
        otper.ParseFromString(state_entries_otp[0].data)

        if not state_entries_otp:
            raise InvalidTransaction('No otp was verified on this number')

        elif otper.otp != data.otp :
            raise InvalidTransaction('Wrong otp retry dude')

        buyer = buyer_pb2.Buyer(
        public_key=public_key, full_name=data.full_name, timestamp=data.timestamp
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
        address = addresser.get_transporter_address(public_key)
        otper = otp_pb2.Otp()
        address_otp = addresser.get_otp_address(data.mobilenumber,data.otp)
        state_entries_otp = self._context.get_state(
            addresses=[address_otp], timeout=self._timeout)
        otper.ParseFromString(state_entries_otp[0].data)

        if not state_entries_otp:
            raise InvalidTransaction('No otp was verified on this number')

        elif otper.otp != data.otp :
            raise InvalidTransaction('Wrong otp retry dude')

        transporter = transoporter_pb2.Transporter(
        public_key=public_key, full_name=data.full_name, timestamp=data.timestamp
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

    def set_otp(self,public_key,data,timestamp=000):
        """Creates an otp state for otp verification
            # TODO: verify that it came from otp server """

        address = addresser.get_otp_address(data.mobilenumber,data.otp)    #this is called good practice

        otpPayload = otp_pb2.Otp(
            otp = data.otp, mobilenumber= data.mobilenumber , timestamp = data.timestamp
        )
        state_enties = self._context.get_state(
        addresses = [address], timeout=self._timeout)
        payloada = otpPayload.SerializeToString()
        updated_state = {}
        updated_state[address] = payloada
        self._context.set_state(updated_state,timeout=self._timeout)


    def create_asset(self,public_key,data,timestamp=000):
        """It creates asset can't you read dumbo !"""
        address = addresser.get_asset_address(data.public_key)
        address_farmer = addresser.get_farmer_address(data.current_owner_pubkey)

        data_type = typee(data)

        farmer =  farmer_pb2.Farmer()
        assetPayload = enums_pb2.assets(
            weight = data.weight,current_owner_pubkey = data.current_owner_pubkey,
                current_owner_pincode = data.current_owner_pincode,type_of_food = data.type_of_food,
            timestamp = timestamp , Status = enums_pb2.status.Value('OrderAdded')
            ,public_key = data.public_key)

        if (data_type[1] == 1):
            assetPayload.Pulses = data_type[0]
        elif (data_type[1] == 2):
            assetPayload.Vegetable_short = data_type[0]
        elif (data_type[1] == 3):
            assetPayload.Vegetable_long = data_type[0]
        elif (data_type[1] == 4):
            assetPayload.Fruits_long = data_type[0]
        elif (data_type[1] == 5):
            assetPayload.Fruits_short = data_type[0]
        elif (data_type[1] == 6):
            assetPayload.Grains = data_type[0]
        else:
            raise InvalidTransaction('Wrong type_of_food')

        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        state_entries_farm = self._context.get_state(
            addresses=[address_farmer] ,timeout=self._timeout)

        if state_entries:
            raise InvalidTransaction('Already exist , asset already used')
        if not state_entries_farm:
            raise InvalidTransaction('No farmer by this pubkey exist')
        farmer.ParseFromString(state_entries_farm[0].data)
        add_asset = farmer.assets_sold.extend([assetPayload])
        data_farm = farmer.SerializeToString()
        data = assetPayload.SerializeToString()
        updated_state_farm = {}
        updated_state_farm[address_farmer] = data_farm
        updated_state = {}
        updated_state[address] = data
        self._context.set_state(updated_state, timeout=self._timeout)
        self._context.set_state(updated_state_farm, timeout=self._timeout)

    def get_farmer(self,public_key):
        """Fetches data of the farmer
            only for testing mode dev build may not include this"""
        address = addresser.get_farmer_address(public_key)
        farmer = farmer_pb2.Farmer()
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            return farmer.ParseFromString(state_entries[0].data)

    def transfer_asset(self,public_key,data,timeout=000):
        """Transfers assets use farmers key to sign"""
        address = addresser.get_asset_address(data.public_key)
        address_farmer = addresser.get_farmer_address(public_key)
        address_buyer = addresser.get_buyer_address(data.current_owner_pubkey)
        farmer =  farmer_pb2.Farmer()
        asset = enums_pb2.assets()
        buyer = buyer_pb2.Buyer()
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        state_entries_farm = self._context.get_state(
            addresses=[address_farmer] ,timeout=self._timeout)
        state_entries_buy = self._context.get_state(
            addresses=[address_buyer] , timeout = self._timeout)
        if not state_entries or not state_entries_farm or not state_entries_buy:
            raise InvalidTransaction("No No that is so wrong !")
        farmer.ParseFromString(state_entries_farm[0].data)
        asset.ParseFromString(state_entries[0].data)
        buyer.ParseFromString(state_entries[0].data)
        i = 0
        index = None
        while i < len(farmer.assets_sold):
            if farmer.assets_sold[i].public_key == data.public_key:
                index = i
        if not index:
            raise InvalidTransaction("No You don't have the asset")
        asset.previous_owner_pubkey.extend(asset.current_owner_pubkey)
        asset.previous_owner_pincode.extend(asset.current_owner_pincode)
        asset.current_owner_pubkey = data.current_owner_pubkey
        asset.current_owner_pincode = data.current_owner_pincode
        buyer.assets_bought.extend(asset)
        del farmer.assets_sold[index]
def typee(data):

    if data.HasField('Pulses') and \
        data.type_of_food == \
            enums_pb2.type.Value('pulsess'):
        return [data.Pulses,1]
    elif data.HasField('Vegetable_short') and \
        data.type_of_food == \
            enums_pb2.type.Value('vegetable_shortt'):
        return [data.Vegetable_short,2]
    elif data.HasField('Vegetable_long') and \
        data.type_of_food == \
            enums_pb2.type.Value('vegetable_longg'):
        return [data.Vegetable_long,3]
    elif data.HasField('Fruits_long') and \
        data.type_of_food == \
            enums_pb2.type.Value('fruits_longg'):
        return [data.Fruits_long,4]
    elif data.HasField('Fruits_short') and \
        data.type_of_food == \
            enums_pb2.type.Value('fruits_shortt'):
        return [data.Fruits_short,5]
    elif data.HasField('Grains') and \
        data.type_of_food == \
            enums_pb2.type.Value('grainss'):
        return [data.Grains,6]
    raise InvalidTransaction("THE FRUIT TYPE IS WRONG")
