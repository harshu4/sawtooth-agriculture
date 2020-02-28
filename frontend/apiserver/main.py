from flask_cors import CORS, cross_origin
from flask import Flask
from flask import request
from addresser import get_otp_address
import requests
import pymongo
from helper import getRandom,get_OtpPayload_bytes,getTransactionHeader,getTxn,getBatchHeader,getBatch,sendBatch,getDisBetween
import json
import string
from sawtooth_signing import create_context
from sawtooth_signing.secp256k1 import Secp256k1PublicKey
from sawtooth_signing import CryptoFactory
import argparse
import sys
import base64
import copy

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()


mydb = myclient["sawtooth_agriculture"]
otpmcol = mydb["otpmanager"]
assets_info = mydb["assets_info"]
pincode_location = mydb["pincode_location"]
buy_order=mydb["buy_order"]
sell_order=mydb["sell_order"]
nounce=mydb["nounce"]

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

context = create_context('secp256k1')
private_key = context.new_random_private_key()
signer = CryptoFactory(context).new_signer(private_key)

devmod=False



@app.route('/',methods=['GET'])
@cross_origin()
def helloWOrld():
    return "Welecome to sawtooth agriculture API!"

@app.route('/nounce/<publicKey>',methods=['GET'])
@cross_origin()
def securenounce(publicKey):
    mydoc = nounce.find({"publicKey":publicKey})
    for x in mydoc:
        nounce.delete_one(x)
    nouncex=getRandom(6,string.digits+string.ascii_lowercase)
    nounce.insert_one({"publicKey":publicKey,"nounce":nouncex})
    return json.dumps({"status":"sucess","nounce":nouncex})



@app.route('/searchOrder',methods=['POST'])
@cross_origin()
def searchOrder():
    data=request.json
    myquery = {"assetValue":data["assetValue"],"assetType":data["assetType"],"price":{"$lte":int(data["price"])}}
    if data['ordertype']=='sell':
        mydoc=sell_order.find(myquery)
    else:
        mydoc=buy_order.find(myquery)
    mydocx=pincode_location.find_one({"pincode":data['pincode']})
    lat1=float(mydocx['latitude'])
    lon1=float(mydocx['longitude'])
    temp=[]
    for x in mydoc:
        mydocxx = pincode_location.find_one({"pincode": x['pincode']})
        x['distance']=getDisBetween(lat1,lon1,float(mydocxx['latitude']),float(mydocxx['longitude']))
        temp.append(x)
    a=sorted(temp, key=lambda i: i['distance'])
    j=[]
    for x in a:
        del x['_id']
        j.append(x)
    for x in a:
        if x['assetType']=="vegetable_short":
            if x['distance']>100:
                j.remove(x)
        elif x['assetType']=="vegetable_long":
            if x['assetType']>600:
                j.remove(x)
        elif x['assetType'] == "fruits_short":
            if x['assetType'] > 100:
                j.remove(x)
        elif x['assetType']=="fruits_long":
            if x['assetType']>500:
                j.remove(x)
        elif x['assetType'] == "grains":
            if x['assetType']>1000:
                j.remove(x)
        elif x['assetType'] == "pulses":
            if x['assetType']>1000:
                j.remove(x)
        out={"status":"sucess","message":"Order searched...","data": a }
    return json.dumps(out)

@app.route('/makeSellOrder',methods=['POST'])
@cross_origin()
def makeSellOrder():
    allow=True
    data=request.json
    lol=data['payload']
    data['payload']=json.loads(base64.b64decode(lol).decode())
    try:
        mydoc = nounce.find_one({"publicKey":data['publicKey']})
        if mydoc:
            if mydoc['nounce']!=data['payload']['nounce']:
                allow=False
        else:
            allow=False
        mydoc = nounce.find({"publicKey": data['publicKey']})
        for x in mydoc:
            nounce.delete_one(x)
        if not allow:
            #print("not allowed")
            return json.dumps({"status": "fail", "message": "unauthorised request....."})
        #print(lol)
        public_key = Secp256k1PublicKey.from_hex(data['publicKey'])
        if context.verify(data['signature'], lol.encode(), public_key):
            data['payload']['publick_key']=data['publicKey']
            a=sell_order.insert_one(data['payload'])
            _id=str(a.inserted_id)
            return json.dumps({"status":"sucess","message":"Order placed sucessfully...","orderId":_id})
        else:
            #print("problem")
            return json.dumps({"status":"fail","message":"unauthorised request....."})
    except Exception as e:
        print("Error, line 63:",e)
        return json.dumps({"status":"fail","message":"Error while requesting make buy order..."})

@app.route('/makeBuyOrder',methods=['POST'])
@cross_origin()
def makeBuyOrder():
    allow=True
    data=request.json
    lol=data['payload']
    data['payload']=json.loads(base64.b64decode(lol).decode())
    try:
        mydoc = nounce.find_one({"publicKey":data['publicKey']})
        if mydoc:
            if mydoc['nounce']!=data['payload']['nounce']:
                allow=False
        else:
            allow=False
        mydoc = nounce.find({"publicKey": data['publicKey']})
        for x in mydoc:
            nounce.delete_one(x)
        if not allow:
            #print("not allowed")
            return json.dumps({"status": "fail", "message": "unauthorised request....."})
        #print(lol)
        public_key = Secp256k1PublicKey.from_hex(data['publicKey'])
        if context.verify(data['signature'], lol.encode(), public_key):
            data['payload']['publick_key']=data['publicKey']
            a=buy_order.insert_one(data['payload'])
            _id=str(a.inserted_id)
            return json.dumps({"status":"sucess","message":"Order placed sucessfully...","orderId":_id})
        else:
            #print("problem")
            return json.dumps({"status":"fail","message":"unauthorised request....."})
    except Exception as e:
        print("Error, line 63:",e)
        return json.dumps({"status":"fail","message":"Error while requesting make buy order..."})

@app.route('/getAssetTypes',methods=['GET'])
@cross_origin()
def getAssetTypes():
    return json.dumps({"status":"sucess","types" : ["vegetable_short", "vegetable_long", "fruits_short", "fruits_long", "grains", "pulses"]})

@app.route('/getAssetTypes/<typ>',methods=['GET'])
@cross_origin()
def getAssetTypesSpecific(typ):
    mydoc = assets_info.find({"type":typ})
    out=[]
    for x in mydoc:
        out.append(x['value'])
    return json.dumps({"status":"sucess","values":out})



@app.route('/otp/<mobilenum>',methods=['GET'])
@cross_origin()
def register(mobilenum):
    try:
        otpnum=getRandom(6,chars=string.digits)
        if not devmod:
            r=requests.get("http://2factor.in/API/V1/ab7006ba-5252-11ea-9fa5-0200cd936042/SMS/{}/{}".format(mobilenum,otpnum))
            res=r.json()
        else:
            print("OTP:",otpnum)
            res={"Status":"Success"}
        if res['Status']=="Success":
            try:
                mobilenum=int(mobilenum)
                otpnum=int(otpnum)
                payloadBytes=get_OtpPayload_bytes(otpnum,mobilenum)
                txnHeader=getTransactionHeader(signer,payloadBytes,[get_otp_address(mobilenum,otpnum)])
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


@app.route('/batches',methods=['POST'])
@cross_origin()
def submit_batches():
    try:
        sendBatch(request.data)
        return json.dumps({"status":"sucess","message":"Data sent to block chain..."})
    except Exception as e:
        print(e)
        return json.dumps({"status":"fail","message":"Error while sending data to block chain..."})




def parse_args(args):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        '-d', '--devmod',
        action='store_true',
        help='Enable devmod')

    parser.add_argument(
        '-p', '--port',
        default=6060,
        help='Port number')

    return parser.parse_args(args)

if __name__ == '__main__':
    args = sys.argv[1:]
    opts = parse_args(args)
    if opts.devmod:
        devmod=True
    app.run(host="0.0.0.0",port=opts.port)

