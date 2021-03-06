# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: store.proto

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
  name='store.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0bstore.proto\"&\n\x0fInitCoordinator\x12\x13\n\x0b\x63oordinator\x18\x01 \x01(\r\"$\n\x06GetMsg\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05level\x18\x02 \x01(\r\"1\n\x06PutMsg\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x0b\n\x03val\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\r\"\x1a\n\x0bStringValue\x12\x0b\n\x03val\x18\x01 \x01(\t\"\x1a\n\x07Success\x12\x0f\n\x07success\x18\x02 \x01(\x08\"$\n\x08PairRead\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x0b\n\x03val\x18\x02 \x01(\t\"%\n\tPairWrite\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x0b\n\x03val\x18\x02 \x01(\t\"*\n\x04Hint\x12\x0f\n\x07hintKey\x18\x01 \x03(\x05\x12\x11\n\thintValue\x18\x02 \x03(\t\"\x18\n\tTimestamp\x12\x0b\n\x03key\x18\x01 \x01(\x05\"\x95\x02\n\x03Msg\x12 \n\x04init\x18\x01 \x01(\x0b\x32\x10.InitCoordinatorH\x00\x12\x16\n\x03put\x18\x02 \x01(\x0b\x32\x07.PutMsgH\x00\x12\x16\n\x03get\x18\x03 \x01(\x0b\x32\x07.GetMsgH\x00\x12\"\n\nstring_val\x18\x04 \x01(\x0b\x32\x0c.StringValueH\x00\x12\x1e\n\tpair_read\x18\x05 \x01(\x0b\x32\t.PairReadH\x00\x12 \n\npair_write\x18\x06 \x01(\x0b\x32\n.PairWriteH\x00\x12\x17\n\x03suc\x18\x07 \x01(\x0b\x32\x08.SuccessH\x00\x12\x15\n\x04hint\x18\x08 \x01(\x0b\x32\x05.HintH\x00\x12\x1f\n\ttimestamp\x18\t \x01(\x0b\x32\n.TimestampH\x00\x42\x05\n\x03msgb\x06proto3')
)




_INITCOORDINATOR = _descriptor.Descriptor(
  name='InitCoordinator',
  full_name='InitCoordinator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coordinator', full_name='InitCoordinator.coordinator', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=15,
  serialized_end=53,
)


_GETMSG = _descriptor.Descriptor(
  name='GetMsg',
  full_name='GetMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='GetMsg.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='GetMsg.level', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=55,
  serialized_end=91,
)


_PUTMSG = _descriptor.Descriptor(
  name='PutMsg',
  full_name='PutMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PutMsg.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val', full_name='PutMsg.val', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='PutMsg.level', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=93,
  serialized_end=142,
)


_STRINGVALUE = _descriptor.Descriptor(
  name='StringValue',
  full_name='StringValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='StringValue.val', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=144,
  serialized_end=170,
)


_SUCCESS = _descriptor.Descriptor(
  name='Success',
  full_name='Success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='Success.success', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=172,
  serialized_end=198,
)


_PAIRREAD = _descriptor.Descriptor(
  name='PairRead',
  full_name='PairRead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PairRead.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val', full_name='PairRead.val', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=200,
  serialized_end=236,
)


_PAIRWRITE = _descriptor.Descriptor(
  name='PairWrite',
  full_name='PairWrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PairWrite.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val', full_name='PairWrite.val', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=238,
  serialized_end=275,
)


_HINT = _descriptor.Descriptor(
  name='Hint',
  full_name='Hint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hintKey', full_name='Hint.hintKey', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hintValue', full_name='Hint.hintValue', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=277,
  serialized_end=319,
)


_TIMESTAMP = _descriptor.Descriptor(
  name='Timestamp',
  full_name='Timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Timestamp.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=321,
  serialized_end=345,
)


_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='init', full_name='Msg.init', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='put', full_name='Msg.put', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get', full_name='Msg.get', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_val', full_name='Msg.string_val', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pair_read', full_name='Msg.pair_read', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pair_write', full_name='Msg.pair_write', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suc', full_name='Msg.suc', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hint', full_name='Msg.hint', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Msg.timestamp', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='msg', full_name='Msg.msg',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=348,
  serialized_end=625,
)

_MSG.fields_by_name['init'].message_type = _INITCOORDINATOR
_MSG.fields_by_name['put'].message_type = _PUTMSG
_MSG.fields_by_name['get'].message_type = _GETMSG
_MSG.fields_by_name['string_val'].message_type = _STRINGVALUE
_MSG.fields_by_name['pair_read'].message_type = _PAIRREAD
_MSG.fields_by_name['pair_write'].message_type = _PAIRWRITE
_MSG.fields_by_name['suc'].message_type = _SUCCESS
_MSG.fields_by_name['hint'].message_type = _HINT
_MSG.fields_by_name['timestamp'].message_type = _TIMESTAMP
_MSG.oneofs_by_name['msg'].fields.append(
  _MSG.fields_by_name['init'])
_MSG.fields_by_name['init'].containing_oneof = _MSG.oneofs_by_name['msg']
_MSG.oneofs_by_name['msg'].fields.append(
  _MSG.fields_by_name['put'])
_MSG.fields_by_name['put'].containing_oneof = _MSG.oneofs_by_name['msg']
_MSG.oneofs_by_name['msg'].fields.append(
  _MSG.fields_by_name['get'])
_MSG.fields_by_name['get'].containing_oneof = _MSG.oneofs_by_name['msg']
_MSG.oneofs_by_name['msg'].fields.append(
  _MSG.fields_by_name['string_val'])
_MSG.fields_by_name['string_val'].containing_oneof = _MSG.oneofs_by_name['msg']
_MSG.oneofs_by_name['msg'].fields.append(
  _MSG.fields_by_name['pair_read'])
_MSG.fields_by_name['pair_read'].containing_oneof = _MSG.oneofs_by_name['msg']
_MSG.oneofs_by_name['msg'].fields.append(
  _MSG.fields_by_name['pair_write'])
_MSG.fields_by_name['pair_write'].containing_oneof = _MSG.oneofs_by_name['msg']
_MSG.oneofs_by_name['msg'].fields.append(
  _MSG.fields_by_name['suc'])
_MSG.fields_by_name['suc'].containing_oneof = _MSG.oneofs_by_name['msg']
_MSG.oneofs_by_name['msg'].fields.append(
  _MSG.fields_by_name['hint'])
_MSG.fields_by_name['hint'].containing_oneof = _MSG.oneofs_by_name['msg']
_MSG.oneofs_by_name['msg'].fields.append(
  _MSG.fields_by_name['timestamp'])
_MSG.fields_by_name['timestamp'].containing_oneof = _MSG.oneofs_by_name['msg']
DESCRIPTOR.message_types_by_name['InitCoordinator'] = _INITCOORDINATOR
DESCRIPTOR.message_types_by_name['GetMsg'] = _GETMSG
DESCRIPTOR.message_types_by_name['PutMsg'] = _PUTMSG
DESCRIPTOR.message_types_by_name['StringValue'] = _STRINGVALUE
DESCRIPTOR.message_types_by_name['Success'] = _SUCCESS
DESCRIPTOR.message_types_by_name['PairRead'] = _PAIRREAD
DESCRIPTOR.message_types_by_name['PairWrite'] = _PAIRWRITE
DESCRIPTOR.message_types_by_name['Hint'] = _HINT
DESCRIPTOR.message_types_by_name['Timestamp'] = _TIMESTAMP
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitCoordinator = _reflection.GeneratedProtocolMessageType('InitCoordinator', (_message.Message,), dict(
  DESCRIPTOR = _INITCOORDINATOR,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:InitCoordinator)
  ))
_sym_db.RegisterMessage(InitCoordinator)

GetMsg = _reflection.GeneratedProtocolMessageType('GetMsg', (_message.Message,), dict(
  DESCRIPTOR = _GETMSG,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:GetMsg)
  ))
_sym_db.RegisterMessage(GetMsg)

PutMsg = _reflection.GeneratedProtocolMessageType('PutMsg', (_message.Message,), dict(
  DESCRIPTOR = _PUTMSG,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:PutMsg)
  ))
_sym_db.RegisterMessage(PutMsg)

StringValue = _reflection.GeneratedProtocolMessageType('StringValue', (_message.Message,), dict(
  DESCRIPTOR = _STRINGVALUE,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:StringValue)
  ))
_sym_db.RegisterMessage(StringValue)

Success = _reflection.GeneratedProtocolMessageType('Success', (_message.Message,), dict(
  DESCRIPTOR = _SUCCESS,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:Success)
  ))
_sym_db.RegisterMessage(Success)

PairRead = _reflection.GeneratedProtocolMessageType('PairRead', (_message.Message,), dict(
  DESCRIPTOR = _PAIRREAD,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:PairRead)
  ))
_sym_db.RegisterMessage(PairRead)

PairWrite = _reflection.GeneratedProtocolMessageType('PairWrite', (_message.Message,), dict(
  DESCRIPTOR = _PAIRWRITE,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:PairWrite)
  ))
_sym_db.RegisterMessage(PairWrite)

Hint = _reflection.GeneratedProtocolMessageType('Hint', (_message.Message,), dict(
  DESCRIPTOR = _HINT,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:Hint)
  ))
_sym_db.RegisterMessage(Hint)

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), dict(
  DESCRIPTOR = _TIMESTAMP,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:Timestamp)
  ))
_sym_db.RegisterMessage(Timestamp)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), dict(
  DESCRIPTOR = _MSG,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:Msg)
  ))
_sym_db.RegisterMessage(Msg)


# @@protoc_insertion_point(module_scope)
