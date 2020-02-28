import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["sawtooth_agriculture"]
mycol = mydb["pincode_location"]

with open('IN.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data={}
        data['pincode']=row[0].split("/")[1]
        data['place_name']=row[1]
        data['admin_name']=row[2]
        data['latitude']=row[3]
        data['longitude']=row[4]
        mycol.insert_one(data)
