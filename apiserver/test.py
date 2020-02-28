'''
from sawtooth_signing.secp256k1 import Secp256k1PublicKey
from sawtooth_signing import create_context

context = create_context('secp256k1')
public_key = Secp256k1PublicKey.from_hex("03406d5e8641ad3b214430abba3682796c323f46b558d45fe5ba7b32dc2dceeaad")
print(context.verify("fdcd91e347ec14e2c60e97af6e7ed333ff697620eeac38cf4e1612600c7efb164fa690ea3489be21a72db26422484daf71375c7fc6ae0665a2bddb986bb98621", "helloWorld!".encode(), public_key))
'''
import math

def degToRed(degree):
    return (degree * 3.14 ) / 180

def getDisBetween(lat1,lon1,lat2,lon2):
    R = 6371
    dLat = degToRed(lat2 - lat1)
    dLon = degToRed(lon2 - lon1)
    a =math.sin(dLat / 2) * math.sin(dLat / 2) +math.cos(degToRed(lat1)) * math.cos(degToRed(lat2)) *math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d= R * c
    return d

print(getDisBetween(21.9417,73.2917,21.0833,72.8833))