# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agpayload.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import enums_pb2 as enums__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='agpayload.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x61gpayload.proto\x1a\x0b\x65nums.proto\"\xb8\x01\n\x0fRegister_farmer\x12\x13\n\x0b\x61\x61\x64har_card\x18\x01 \x02(\t\x12\x11\n\ttimestamp\x18\x02 \x02(\x04\x12\x11\n\tfull_name\x18\x03 \x02(\t\x12\x15\n\x05State\x18\x04 \x02(\x0e\x32\x06.state\x12\x0f\n\x07pincode\x18\x05 \x02(\r\x12\x14\n\x0cmobilenumber\x18\x06 \x02(\x04\x12\x10\n\x08\x64istrict\x18\x07 \x02(\t\x12\r\n\x05photo\x18\x08 \x01(\x0c\x12\x0b\n\x03otp\x18\t \x02(\r\"\xb7\x01\n\x0eRegister_buyer\x12\x13\n\x0b\x61\x61\x64har_card\x18\x01 \x02(\t\x12\x11\n\ttimestamp\x18\x02 \x02(\x04\x12\x11\n\tfull_name\x18\x03 \x02(\t\x12\x15\n\x05State\x18\x04 \x02(\x0e\x32\x06.state\x12\x0f\n\x07pincode\x18\x05 \x02(\r\x12\x14\n\x0cmobilenumber\x18\x06 \x02(\x04\x12\x10\n\x08\x64istrict\x18\x07 \x02(\t\x12\r\n\x05photo\x18\x08 \x01(\x0c\x12\x0b\n\x03otp\x18\t \x02(\r\"\xd6\x01\n\x14Register_transporter\x12\x13\n\x0b\x61\x61\x64har_card\x18\x01 \x02(\t\x12\x11\n\ttimestamp\x18\x02 \x02(\x04\x12\x11\n\tfull_name\x18\x03 \x02(\t\x12\x15\n\x05State\x18\x04 \x02(\x0e\x32\x06.state\x12\x0f\n\x07pincode\x18\x05 \x02(\r\x12\x14\n\x0cmobilenumber\x18\x06 \x02(\x04\x12\x10\n\x08\x64istrict\x18\x07 \x02(\t\x12\x17\n\x0f\x64riving_license\x18\x08 \x02(\t\x12\r\n\x05photo\x18\t \x01(\x0c\x12\x0b\n\x03otp\x18\n \x02(\r\"G\n\x0fOtp_transaction\x12\x14\n\x0cmobilenumber\x18\x01 \x02(\x04\x12\x0b\n\x03otp\x18\x02 \x02(\r\x12\x11\n\ttimestamp\x18\x03 \x02(\r\"\xc1\x03\n\x0c\x43reate_asset\x12\x12\n\npublic_key\x18\x01 \x02(\t\x12\x0e\n\x06weight\x18\x02 \x02(\r\x12\x1d\n\x15\x63urrent_owner_pincode\x18\x03 \x02(\r\x12\x1c\n\x14\x63urrent_owner_pubkey\x18\x04 \x02(\t\x12\x1b\n\x0ctype_of_food\x18\x05 \x02(\x0e\x32\x05.type\x12\x17\n\x06Pulses\x18\x06 \x01(\x0e\x32\x07.pulses\x12\x17\n\x06Grains\x18\x07 \x01(\x0e\x32\x07.grains\x12!\n\x0b\x46ruits_Long\x18\x08 \x01(\x0e\x32\x0c.fruits_long\x12#\n\x0c\x46ruits_short\x18\t \x01(\x0e\x32\r.fruits_short\x12)\n\x0fVegetable_short\x18\n \x01(\x0e\x32\x10.vegetable_short\x12\'\n\x0eVegetable_long\x18\x0b \x01(\x0e\x32\x0f.vegetable_long\x12\x1a\n\x12transporter_pubkey\x18\x0c \x01(\t\x12\x11\n\ttimestamp\x18\r \x02(\x04\x12\x1d\n\x15previous_asset_pubkey\x18\x0e \x03(\t\x12\x17\n\x06Status\x18\x0f \x02(\x0e\x32\x07.status\"t\n\x0eTransfer_asset\x12\x12\n\npublic_key\x18\x01 \x02(\t\x12\x1c\n\x14\x63urrent_owner_pubkey\x18\x02 \x02(\t\x12\x1d\n\x15\x63urrent_owner_pincode\x18\x03 \x02(\r\x12\x11\n\ttimestamp\x18\x04 \x02(\x04\"v\n\x0bSplit_asset\x12\x12\n\npublic_key\x18\x01 \x02(\t\x12\x0e\n\x06weight\x18\x02 \x02(\r\x12\x13\n\x0bpublic_key1\x18\x03 \x02(\t\x12\x13\n\x0bpublic_key2\x18\x04 \x02(\t\x12\x19\n\x11public_key_farmer\x18\x05 \x02(\t\"m\n\x0bMerge_asset\x12\x13\n\x0bpublic_key1\x18\x01 \x02(\t\x12\x13\n\x0bpublic_key2\x18\x02 \x02(\t\x12\x19\n\x11public_key_farmer\x18\x03 \x02(\t\x12\x19\n\x11public_key_merged\x18\x04 \x02(\t\"\xb6\x02\n\x0bRealpayload\x12\x17\n\x06\x41\x63tion\x18\x01 \x02(\x0e\x32\x07.action\x12!\n\x07reg_far\x18\x02 \x01(\x0b\x32\x10.Register_farmer\x12 \n\x07reg_buy\x18\x03 \x01(\x0b\x32\x0f.Register_buyer\x12&\n\x07reg_tra\x18\x04 \x01(\x0b\x32\x15.Register_transporter\x12!\n\x07otp_tra\x18\x05 \x01(\x0b\x32\x10.Otp_transaction\x12 \n\x07tra_ass\x18\x06 \x01(\x0b\x32\x0f.Transfer_asset\x12\x1e\n\x07\x63re_ass\x18\x07 \x01(\x0b\x32\r.Create_asset\x12\x1d\n\x07spl_ass\x18\x08 \x01(\x0b\x32\x0c.Split_asset\x12\x1d\n\x07mer_ass\x18\t \x01(\x0b\x32\x0c.Merge_asset*\xbf\x01\n\x06\x61\x63tion\x12\x13\n\x0fregister_farmer\x10\x00\x12\x12\n\x0eregister_buyer\x10\x01\x12\x18\n\x14register_transporter\x10\x02\x12\x13\n\x0fotp_transaction\x10\x03\x12\x10\n\x0c\x63reate_asset\x10\x04\x12\x12\n\x0etransfer_asset\x10\x05\x12\x15\n\x11transporter_asset\x10\x06\x12\x0f\n\x0bsplit_asset\x10\x07\x12\x0f\n\x0bmerge_asset\x10\x08')
  ,
  dependencies=[enums__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ACTION = _descriptor.EnumDescriptor(
  name='action',
  full_name='action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='register_farmer', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='register_buyer', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='register_transporter', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='otp_transaction', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='create_asset', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='transfer_asset', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='transporter_asset', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='split_asset', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='merge_asset', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1810,
  serialized_end=2001,
)
_sym_db.RegisterEnumDescriptor(_ACTION)

action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
register_farmer = 0
register_buyer = 1
register_transporter = 2
otp_transaction = 3
create_asset = 4
transfer_asset = 5
transporter_asset = 6
split_asset = 7
merge_asset = 8



_REGISTER_FARMER = _descriptor.Descriptor(
  name='Register_farmer',
  full_name='Register_farmer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aadhar_card', full_name='Register_farmer.aadhar_card', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Register_farmer.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='Register_farmer.full_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='State', full_name='Register_farmer.State', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pincode', full_name='Register_farmer.pincode', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mobilenumber', full_name='Register_farmer.mobilenumber', index=5,
      number=6, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='district', full_name='Register_farmer.district', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='photo', full_name='Register_farmer.photo', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='otp', full_name='Register_farmer.otp', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=217,
)


_REGISTER_BUYER = _descriptor.Descriptor(
  name='Register_buyer',
  full_name='Register_buyer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aadhar_card', full_name='Register_buyer.aadhar_card', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Register_buyer.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='Register_buyer.full_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='State', full_name='Register_buyer.State', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pincode', full_name='Register_buyer.pincode', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mobilenumber', full_name='Register_buyer.mobilenumber', index=5,
      number=6, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='district', full_name='Register_buyer.district', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='photo', full_name='Register_buyer.photo', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='otp', full_name='Register_buyer.otp', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=403,
)


_REGISTER_TRANSPORTER = _descriptor.Descriptor(
  name='Register_transporter',
  full_name='Register_transporter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aadhar_card', full_name='Register_transporter.aadhar_card', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Register_transporter.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='Register_transporter.full_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='State', full_name='Register_transporter.State', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pincode', full_name='Register_transporter.pincode', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mobilenumber', full_name='Register_transporter.mobilenumber', index=5,
      number=6, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='district', full_name='Register_transporter.district', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='driving_license', full_name='Register_transporter.driving_license', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='photo', full_name='Register_transporter.photo', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='otp', full_name='Register_transporter.otp', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=620,
)


_OTP_TRANSACTION = _descriptor.Descriptor(
  name='Otp_transaction',
  full_name='Otp_transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mobilenumber', full_name='Otp_transaction.mobilenumber', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='otp', full_name='Otp_transaction.otp', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Otp_transaction.timestamp', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=622,
  serialized_end=693,
)


_CREATE_ASSET = _descriptor.Descriptor(
  name='Create_asset',
  full_name='Create_asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='Create_asset.public_key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight', full_name='Create_asset.weight', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_owner_pincode', full_name='Create_asset.current_owner_pincode', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_owner_pubkey', full_name='Create_asset.current_owner_pubkey', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_of_food', full_name='Create_asset.type_of_food', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pulses', full_name='Create_asset.Pulses', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Grains', full_name='Create_asset.Grains', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Fruits_Long', full_name='Create_asset.Fruits_Long', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Fruits_short', full_name='Create_asset.Fruits_short', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Vegetable_short', full_name='Create_asset.Vegetable_short', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Vegetable_long', full_name='Create_asset.Vegetable_long', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transporter_pubkey', full_name='Create_asset.transporter_pubkey', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Create_asset.timestamp', index=12,
      number=13, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='previous_asset_pubkey', full_name='Create_asset.previous_asset_pubkey', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Status', full_name='Create_asset.Status', index=14,
      number=15, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=696,
  serialized_end=1145,
)


_TRANSFER_ASSET = _descriptor.Descriptor(
  name='Transfer_asset',
  full_name='Transfer_asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='Transfer_asset.public_key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_owner_pubkey', full_name='Transfer_asset.current_owner_pubkey', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_owner_pincode', full_name='Transfer_asset.current_owner_pincode', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Transfer_asset.timestamp', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1147,
  serialized_end=1263,
)


_SPLIT_ASSET = _descriptor.Descriptor(
  name='Split_asset',
  full_name='Split_asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='Split_asset.public_key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight', full_name='Split_asset.weight', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_key1', full_name='Split_asset.public_key1', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_key2', full_name='Split_asset.public_key2', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_key_farmer', full_name='Split_asset.public_key_farmer', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1265,
  serialized_end=1383,
)


_MERGE_ASSET = _descriptor.Descriptor(
  name='Merge_asset',
  full_name='Merge_asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key1', full_name='Merge_asset.public_key1', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_key2', full_name='Merge_asset.public_key2', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_key_farmer', full_name='Merge_asset.public_key_farmer', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_key_merged', full_name='Merge_asset.public_key_merged', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1385,
  serialized_end=1494,
)


_REALPAYLOAD = _descriptor.Descriptor(
  name='Realpayload',
  full_name='Realpayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Action', full_name='Realpayload.Action', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reg_far', full_name='Realpayload.reg_far', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reg_buy', full_name='Realpayload.reg_buy', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reg_tra', full_name='Realpayload.reg_tra', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='otp_tra', full_name='Realpayload.otp_tra', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tra_ass', full_name='Realpayload.tra_ass', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cre_ass', full_name='Realpayload.cre_ass', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spl_ass', full_name='Realpayload.spl_ass', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mer_ass', full_name='Realpayload.mer_ass', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1497,
  serialized_end=1807,
)

_REGISTER_FARMER.fields_by_name['State'].enum_type = enums__pb2._STATE
_REGISTER_BUYER.fields_by_name['State'].enum_type = enums__pb2._STATE
_REGISTER_TRANSPORTER.fields_by_name['State'].enum_type = enums__pb2._STATE
_CREATE_ASSET.fields_by_name['type_of_food'].enum_type = enums__pb2._TYPE
_CREATE_ASSET.fields_by_name['Pulses'].enum_type = enums__pb2._PULSES
_CREATE_ASSET.fields_by_name['Grains'].enum_type = enums__pb2._GRAINS
_CREATE_ASSET.fields_by_name['Fruits_Long'].enum_type = enums__pb2._FRUITS_LONG
_CREATE_ASSET.fields_by_name['Fruits_short'].enum_type = enums__pb2._FRUITS_SHORT
_CREATE_ASSET.fields_by_name['Vegetable_short'].enum_type = enums__pb2._VEGETABLE_SHORT
_CREATE_ASSET.fields_by_name['Vegetable_long'].enum_type = enums__pb2._VEGETABLE_LONG
_CREATE_ASSET.fields_by_name['Status'].enum_type = enums__pb2._STATUS
_REALPAYLOAD.fields_by_name['Action'].enum_type = _ACTION
_REALPAYLOAD.fields_by_name['reg_far'].message_type = _REGISTER_FARMER
_REALPAYLOAD.fields_by_name['reg_buy'].message_type = _REGISTER_BUYER
_REALPAYLOAD.fields_by_name['reg_tra'].message_type = _REGISTER_TRANSPORTER
_REALPAYLOAD.fields_by_name['otp_tra'].message_type = _OTP_TRANSACTION
_REALPAYLOAD.fields_by_name['tra_ass'].message_type = _TRANSFER_ASSET
_REALPAYLOAD.fields_by_name['cre_ass'].message_type = _CREATE_ASSET
_REALPAYLOAD.fields_by_name['spl_ass'].message_type = _SPLIT_ASSET
_REALPAYLOAD.fields_by_name['mer_ass'].message_type = _MERGE_ASSET
DESCRIPTOR.message_types_by_name['Register_farmer'] = _REGISTER_FARMER
DESCRIPTOR.message_types_by_name['Register_buyer'] = _REGISTER_BUYER
DESCRIPTOR.message_types_by_name['Register_transporter'] = _REGISTER_TRANSPORTER
DESCRIPTOR.message_types_by_name['Otp_transaction'] = _OTP_TRANSACTION
DESCRIPTOR.message_types_by_name['Create_asset'] = _CREATE_ASSET
DESCRIPTOR.message_types_by_name['Transfer_asset'] = _TRANSFER_ASSET
DESCRIPTOR.message_types_by_name['Split_asset'] = _SPLIT_ASSET
DESCRIPTOR.message_types_by_name['Merge_asset'] = _MERGE_ASSET
DESCRIPTOR.message_types_by_name['Realpayload'] = _REALPAYLOAD
DESCRIPTOR.enum_types_by_name['action'] = _ACTION

Register_farmer = _reflection.GeneratedProtocolMessageType('Register_farmer', (_message.Message,), dict(
  DESCRIPTOR = _REGISTER_FARMER,
  __module__ = 'agpayload_pb2'
  # @@protoc_insertion_point(class_scope:Register_farmer)
  ))
_sym_db.RegisterMessage(Register_farmer)

Register_buyer = _reflection.GeneratedProtocolMessageType('Register_buyer', (_message.Message,), dict(
  DESCRIPTOR = _REGISTER_BUYER,
  __module__ = 'agpayload_pb2'
  # @@protoc_insertion_point(class_scope:Register_buyer)
  ))
_sym_db.RegisterMessage(Register_buyer)

Register_transporter = _reflection.GeneratedProtocolMessageType('Register_transporter', (_message.Message,), dict(
  DESCRIPTOR = _REGISTER_TRANSPORTER,
  __module__ = 'agpayload_pb2'
  # @@protoc_insertion_point(class_scope:Register_transporter)
  ))
_sym_db.RegisterMessage(Register_transporter)

Otp_transaction = _reflection.GeneratedProtocolMessageType('Otp_transaction', (_message.Message,), dict(
  DESCRIPTOR = _OTP_TRANSACTION,
  __module__ = 'agpayload_pb2'
  # @@protoc_insertion_point(class_scope:Otp_transaction)
  ))
_sym_db.RegisterMessage(Otp_transaction)

Create_asset = _reflection.GeneratedProtocolMessageType('Create_asset', (_message.Message,), dict(
  DESCRIPTOR = _CREATE_ASSET,
  __module__ = 'agpayload_pb2'
  # @@protoc_insertion_point(class_scope:Create_asset)
  ))
_sym_db.RegisterMessage(Create_asset)

Transfer_asset = _reflection.GeneratedProtocolMessageType('Transfer_asset', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFER_ASSET,
  __module__ = 'agpayload_pb2'
  # @@protoc_insertion_point(class_scope:Transfer_asset)
  ))
_sym_db.RegisterMessage(Transfer_asset)

Split_asset = _reflection.GeneratedProtocolMessageType('Split_asset', (_message.Message,), dict(
  DESCRIPTOR = _SPLIT_ASSET,
  __module__ = 'agpayload_pb2'
  # @@protoc_insertion_point(class_scope:Split_asset)
  ))
_sym_db.RegisterMessage(Split_asset)

Merge_asset = _reflection.GeneratedProtocolMessageType('Merge_asset', (_message.Message,), dict(
  DESCRIPTOR = _MERGE_ASSET,
  __module__ = 'agpayload_pb2'
  # @@protoc_insertion_point(class_scope:Merge_asset)
  ))
_sym_db.RegisterMessage(Merge_asset)

Realpayload = _reflection.GeneratedProtocolMessageType('Realpayload', (_message.Message,), dict(
  DESCRIPTOR = _REALPAYLOAD,
  __module__ = 'agpayload_pb2'
  # @@protoc_insertion_point(class_scope:Realpayload)
  ))
_sym_db.RegisterMessage(Realpayload)


# @@protoc_insertion_point(module_scope)
