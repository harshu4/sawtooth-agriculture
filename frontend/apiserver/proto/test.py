import buyer_pb2
import farmer_pb2
import transporter_pb2
import enums_pb2

farmer = Farmer_pb2.Farmer()
farmer.public_key = '123131'
farmer.aadhar_card = '1232424'
farmer.timestamp = 123232
farmer.full_name = 'johndoe'
farmer.State = enums_pb2.state.Value('Gujarat')
farmer.pincode = 123242
farmer.mobilenumber = 12313
farmer.district = 'fdflsjfs'
a = open('hsfsf.txt','wb')
a.write(farmer.SerializeToString())
print(str(farmer.SerializeToString()))
