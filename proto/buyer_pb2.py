# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buyer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import enums_pb2 as enums__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='buyer.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x62uyer.proto\x1a\x0b\x65nums.proto\"1\n\tBuy_Order\x12\x11\n\tbuyer_key\x18\x01 \x02(\t\x12\x11\n\ttimestamp\x18\x02 \x02(\x04\"\xc6\x01\n\x05\x42uyer\x12\x12\n\npublic_key\x18\x01 \x02(\t\x12\x13\n\x0b\x61\x61\x64har_card\x18\x02 \x02(\t\x12\x11\n\ttimestamp\x18\x03 \x02(\x04\x12\x11\n\tfull_name\x18\x04 \x02(\t\x12\x15\n\x05State\x18\x05 \x02(\x0e\x32\x06.state\x12\x0f\n\x07pincode\x18\x06 \x02(\r\x12\x14\n\x0cmobilenumber\x18\x07 \x02(\x04\x12\x10\n\x08\x64istrict\x18\x08 \x02(\t\x12\x1e\n\rassets_bought\x18\t \x03(\x0b\x32\x07.assets')
  ,
  dependencies=[enums__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BUY_ORDER = _descriptor.Descriptor(
  name='Buy_Order',
  full_name='Buy_Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buyer_key', full_name='Buy_Order.buyer_key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Buy_Order.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=2,
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
  serialized_start=28,
  serialized_end=77,
)


_BUYER = _descriptor.Descriptor(
  name='Buyer',
  full_name='Buyer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='Buyer.public_key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aadhar_card', full_name='Buyer.aadhar_card', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Buyer.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='Buyer.full_name', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='State', full_name='Buyer.State', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pincode', full_name='Buyer.pincode', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mobilenumber', full_name='Buyer.mobilenumber', index=6,
      number=7, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='district', full_name='Buyer.district', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assets_bought', full_name='Buyer.assets_bought', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=80,
  serialized_end=278,
)

_BUYER.fields_by_name['State'].enum_type = enums__pb2._STATE
_BUYER.fields_by_name['assets_bought'].message_type = enums__pb2._ASSETS
DESCRIPTOR.message_types_by_name['Buy_Order'] = _BUY_ORDER
DESCRIPTOR.message_types_by_name['Buyer'] = _BUYER

Buy_Order = _reflection.GeneratedProtocolMessageType('Buy_Order', (_message.Message,), dict(
  DESCRIPTOR = _BUY_ORDER,
  __module__ = 'buyer_pb2'
  # @@protoc_insertion_point(class_scope:Buy_Order)
  ))
_sym_db.RegisterMessage(Buy_Order)

Buyer = _reflection.GeneratedProtocolMessageType('Buyer', (_message.Message,), dict(
  DESCRIPTOR = _BUYER,
  __module__ = 'buyer_pb2'
  # @@protoc_insertion_point(class_scope:Buyer)
  ))
_sym_db.RegisterMessage(Buyer)


# @@protoc_insertion_point(module_scope)
