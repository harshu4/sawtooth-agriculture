import enum
import hashlib


FAMILY_NAME = 'agriculture_market'
FAMILY_VERSION = '0.1'
NAMESPACE = hashlib.sha512(FAMILY_NAME.encode('utf-8')).hexdigest()[:6]
FARMER_PREFIX = '00'
BUYER_PREFIX = '01'
TRANSPORTER_PREFIX = '02'

@enum.unique
class AddressSpace(enum.IntEnum):
    FARMER = 0
    BUYER = 1
    TRANSPORTER = 2
    OTHER_FAMILY = 100
#   ORDER = 3
#   REQUEST = 4
#   SOLD = 5
#   ASSET = 6


def get_farmer_address(public_key):
    return NAMESPACE + FARMER_PREFIX + hashlib.sha512(
    public_key.encode('utf-8')).hexdigest()[:62]

def get_agent_address(public_key):
    return NAMESPACE + AGENT_PREFIX + hashlib.sha512(
    public_key.encode('utf-8')).hexdigest()[:62]

def get_transporter_address(public_key):
    return NAMESPACE + TRANSPORTER_PREFIX + hashlib.sha512(
    public_key.encode('utf-8')).hexdigest()[:62]

def get_address_type(address):
    if address[:len(NAMESPACE)] != NAMESPACE:
        return AddressSpace.OTHER_FAMILY

    infix = address[6:8]

    if infix == '00':
        return AddressSpace.FARMER
    if infix == '01':
        return AddressSpace.BUYER
    if infix == '02':
        return AddressSpace.TRANSPORTER

    return AddressSpace.OTHER_FAMILY
