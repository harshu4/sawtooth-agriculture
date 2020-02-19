import sys
sys.path.insert(0, "../proto")   #used relative imports for future docker implementation
import agpayload_pb2
import payload
payloada = agpayload_pb2.Realpayload()
payloada.Action = agpayload_pb2.action.Value('otp_transaction')
payloada.otp_tra.mobilenumber = 'aolfjsf'
payloada.otp_tra.otp = 1234
payloada.otp_tra.public_key = 'abc'

obc = payload.AgricultureMarketPayload(payloada.SerializeToString())
print(obc.data)
