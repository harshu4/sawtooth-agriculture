from flask_cors import CORS, cross_origin
from flask import Flask
from flask import request
import requests
import pymongo
from sawtooth_signing import create_context
from sawtooth_signing.secp256k1 import Secp256k1PublicKey
from sawtooth_signing import CryptoFactory


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
mydb = myclient["sawtooth_agriculture"]
assets_info = mydb["assets_info"]

context = create_context('secp256k1')
private_key = context.new_random_private_key()
signer = CryptoFactory(context).new_signer(private_key)

@app.route('/manage',methods=['POST'])
@cross_origin()
def sell():
    data=request.json
    return "sell"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=7777)