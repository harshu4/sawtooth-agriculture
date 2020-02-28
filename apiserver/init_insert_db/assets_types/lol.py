import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["sawtooth_agriculture"]
mycol = mydb["assets_info"]
a='''enum vegetable_short {
  Tomato = 0;
  Lemons = 1;
  Cauliflower = 2;
  Spinach = 3;
}

enum vegetable_long {
  Potato = 0;
  Onion = 1;
  Garlic = 2;
  Cabbage = 3;
  Beets = 4;
}

enum fruits_short{
  Strawberries =0;
  Cherries = 1;
  Bananas =2 ;
  Pineapple = 3;
}

enum fruits_long{
  Apples = 0;
  Orange = 1;
  Pomegranate = 2;
}

enum grains{
  Wheat = 0;
  Rice = 1;
  Maize =2;
  Barley = 3;
}

enum pulses{
  Mung = 0;
  ToovarDaal = 1;
  Rajma = 2;
  Urad = 3;
  Vatana = 4;
}'''

#mycol.insert_one(data)
c=a.split("enum")
c.pop(0)
j=[]
for x in c:
    j.append(x.replace("\n",""))

for e in j:
    f=e.split("{")
    fd=f[1].split(";")
    fd.pop()
    for ts in fd:
        ts=ts.split("=")[0]
        ts=ts.strip()
        oul={}
        oul["value"]=ts
        oul["type"]=f[0].strip()
        mycol.insert_one(oul)

