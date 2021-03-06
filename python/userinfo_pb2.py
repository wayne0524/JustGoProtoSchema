# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: userinfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='userinfo.proto',
  package='user',
  syntax='proto3',
  serialized_pb=_b('\n\x0euserinfo.proto\x12\x04user\"t\n\x08UserInfo\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x0e\n\x06origin\x18\x02 \x01(\t\x12\x11\n\tminBudget\x18\x03 \x01(\x02\x12\x11\n\tmaxBudget\x18\x04 \x01(\x02\x12\"\n\nprefMatrix\x18\x05 \x01(\x0b\x32\x0e.user.UserPref\"\xcd\x02\n\x08UserPref\x12\r\n\x05\x61rtsy\x18\x01 \x01(\x08\x12\x12\n\nadrenaline\x18\x02 \x01(\x08\x12\x12\n\nbackpacker\x18\x03 \x01(\x08\x12\r\n\x05\x62\x65\x61\x63h\x18\x04 \x01(\x08\x12\x0e\n\x06\x62udget\x18\x05 \x01(\x08\x12\x0e\n\x06\x66\x61mily\x18\x06 \x01(\x08\x12\x0e\n\x06\x66oodie\x18\x07 \x01(\x08\x12\r\n\x05green\x18\x08 \x01(\x08\x12\x0f\n\x07history\x18\t \x01(\x08\x12\r\n\x05local\x18\n \x01(\x08\x12\x0e\n\x06luxury\x18\x0b \x01(\x08\x12\x0e\n\x06nature\x18\x0c \x01(\x08\x12\x11\n\tnightlife\x18\r \x01(\x08\x12\x0e\n\x06serene\x18\x0e \x01(\x08\x12\x10\n\x08shopping\x18\x0f \x01(\x08\x12\x0f\n\x07student\x18\x10 \x01(\x08\x12\x13\n\x0btrendsetter\x18\x11 \x01(\x08\x12\r\n\x05urban\x18\x12 \x01(\x08\x12\x12\n\nvegetarian\x18\x13 \x01(\x08\x42\x34\n\"com.expedia.www.packagefinder.userB\x0eUserInfoProtosb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='user.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='user.UserInfo.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='origin', full_name='user.UserInfo.origin', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minBudget', full_name='user.UserInfo.minBudget', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxBudget', full_name='user.UserInfo.maxBudget', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prefMatrix', full_name='user.UserInfo.prefMatrix', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=140,
)


_USERPREF = _descriptor.Descriptor(
  name='UserPref',
  full_name='user.UserPref',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='artsy', full_name='user.UserPref.artsy', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adrenaline', full_name='user.UserPref.adrenaline', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backpacker', full_name='user.UserPref.backpacker', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beach', full_name='user.UserPref.beach', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='budget', full_name='user.UserPref.budget', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='family', full_name='user.UserPref.family', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='foodie', full_name='user.UserPref.foodie', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='green', full_name='user.UserPref.green', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='history', full_name='user.UserPref.history', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local', full_name='user.UserPref.local', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='luxury', full_name='user.UserPref.luxury', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nature', full_name='user.UserPref.nature', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nightlife', full_name='user.UserPref.nightlife', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serene', full_name='user.UserPref.serene', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shopping', full_name='user.UserPref.shopping', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='student', full_name='user.UserPref.student', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trendsetter', full_name='user.UserPref.trendsetter', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='urban', full_name='user.UserPref.urban', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vegetarian', full_name='user.UserPref.vegetarian', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=476,
)

_USERINFO.fields_by_name['prefMatrix'].message_type = _USERPREF
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['UserPref'] = _USERPREF

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERINFO,
  __module__ = 'userinfo_pb2'
  # @@protoc_insertion_point(class_scope:user.UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)

UserPref = _reflection.GeneratedProtocolMessageType('UserPref', (_message.Message,), dict(
  DESCRIPTOR = _USERPREF,
  __module__ = 'userinfo_pb2'
  # @@protoc_insertion_point(class_scope:user.UserPref)
  ))
_sym_db.RegisterMessage(UserPref)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.expedia.www.packagefinder.userB\016UserInfoProtos'))
# @@protoc_insertion_point(module_scope)
