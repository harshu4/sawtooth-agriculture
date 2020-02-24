from flask_cors import CORS, cross_origin
from flask import Flask
from flask import request
from addresser import get_otp_address
import requests
import pymongo
from helper import getRandom,get_OtpPayload_bytes,getTransactionHeader,getTxn,getBatchHeader,getBatch,sendBatch
import json
import string
from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()


mydb = myclient["hexahive"]
otpmcol = mydb["otpmanager"]

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

context = create_context('secp256k1')
private_key = context.new_random_private_key()
signer = CryptoFactory(context).new_signer(private_key)




@app.route('/',methods=['GET'])
@cross_origin()
def helloWOrld():
    return "Welecome to sawtooth agriculture API!"


@app.route('/otp/<mobilenum>',methods=['GET'])
@cross_origin()
def register(mobilenum):
    try:
        otpnum=getRandom(6,chars=string.digits)
        r=requests.get("http://2factor.in/API/V1/ab7006ba-5252-11ea-9fa5-0200cd936042/SMS/{}/{}".format(mobilenum,otpnum))
        res=r.json()
        res={"Status":"Success"}
        if res['Status']=="Success":
            try:
                mobilenum=int(mobilenum)
                otpnum=int(otpnum)
                payloadBytes=get_OtpPayload_bytes(otpnum,mobilenum)
                txnHeader=getTransactionHeader(signer,payloadBytes,get_otp_address(mobilenum,otpnum))
                trans_id , txn =getTxn(signer,payloadBytes,txnHeader)
                batchHeader=getBatchHeader(signer,[txn])
                batch_id,batch=getBatch(signer,batchHeader,[txn])
                if sendBatch(batch):
                    return json.dumps({"status": True, "message": "Otp sent sucessfully...", "txnid" : trans_id})
                else:
                    return json.dumps({"status": False, "message": "error while sending batch to sawtooth api"})
            except Exception as e:
                print("Error, line 59:",e)
                return json.dumps({"status": False, "message": "error while making batch"})
        else:
            print("Error line 57\n, False sucess from otp vendor:",res)
            return  json.dumps({"status": False, "message" : "error from otp vendor"})
    except Exception as e:
        print("Error line 60:\n",e)
        return json.dumps({"status": False, "message": "something wrong"})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6060)

