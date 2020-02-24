import enum
import hashlib


FAMILY_NAME = 'agriculture_market'
FAMILY_VERSION = '0.1'
NAMESPACE = hashlib.sha512(FAMILY_NAME.encode('utf-8')).hexdigest()[:6]
FARMER_PREFIX = '00'
BUYER_PREFIX = '01'
TRANSPORTER_PREFIX = '02'
OTP_PREFIX = '03'

@enum.unique
class AddressSpace(enum.IntEnum):
    FARMER = 0
    BUYER = 1
    TRANSPORTER = 2
    OTP = 3
    OTHER_FAMILY = 100
#   BUY_ORDER = 3
#   SELL_ORDER = 4
#    = 5y
#   ASSET = 6


def get_farmer_address(public_key):
    return NAMESPACE + FARMER_PREFIX + hashlib.sha512(
    public_key.encode('utf-8')).hexdigest()[:62]

def get_buyer_address(public_key):
    return NAMESPACE + BUYER_PREFIX + hashlib.sha512(
    public_key.encode('utf-8')).hexdigest()[:62]

def get_transporter_address(public_key):
    return NAMESPACE + TRANSPORTER_PREFIX + hashlib.sha512(
    public_key.encode('utf-8')).hexdigest()[:62]


def get_otp_address(mobilenumber,otp):
    """smart enough to handle mobile number with +91 and otp of random length"""
    #ask obd otp size and remind him to keep mobile number to 10 digit
    return NAMESPACE + OTP_PREFIX + str(mobilenumber)[0:10] + str(otp) + hashlib.sha512(
    str(mobilenumber).encode('UTF-8')).hexdigest()[:52-len(str(otp))]


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
    if infix == '03':
        return AddressSpace.OTP

    return AddressSpace.OTHER_FAMILY
