# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

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
  name='config.proto',
  package='proto',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x63onfig.proto\x12\x05proto\"#\n\x04\x44\x61ta\x12\x0e\n\x06tokens\x18\x01 \x03(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"4\n\x05JobID\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\nbatch_size\x18\x03 \x01(\x05\"\x07\n\x05\x45mpty\" \n\x03\x41\x63k\x12\t\n\x01n\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\x08\x32\x90\x02\n\x06Tokens\x12\"\n\x03Get\x12\x0c.proto.JobID\x1a\x0b.proto.Data\"\x00\x12\"\n\x04\x44one\x12\x0c.proto.JobID\x1a\n.proto.Ack\"\x00\x12#\n\x05Reset\x12\x0c.proto.Empty\x1a\n.proto.Ack\"\x00\x12$\n\x06Rescan\x12\x0c.proto.Empty\x1a\n.proto.Ack\"\x00\x12%\n\x07Shuffle\x12\x0c.proto.Empty\x1a\n.proto.Ack\"\x00\x12#\n\x04Show\x12\x0c.proto.Empty\x1a\x0b.proto.Data\"\x00\x12\'\n\tHeartBeat\x12\x0c.proto.JobID\x1a\n.proto.Ack\"\x00\x62\x06proto3')
)




_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='proto.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tokens', full_name='proto.Data.tokens', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.Data.key', index=1,
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
  serialized_start=23,
  serialized_end=58,
)


_JOBID = _descriptor.Descriptor(
  name='JobID',
  full_name='proto.JobID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='proto.JobID.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.JobID.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='proto.JobID.batch_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=60,
  serialized_end=112,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='proto.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=114,
  serialized_end=121,
)


_ACK = _descriptor.Descriptor(
  name='Ack',
  full_name='proto.Ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='proto.Ack.n', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.Ack.status', index=1,
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
  serialized_start=123,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['JobID'] = _JOBID
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Ack'] = _ACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:proto.Data)
  ))
_sym_db.RegisterMessage(Data)

JobID = _reflection.GeneratedProtocolMessageType('JobID', (_message.Message,), dict(
  DESCRIPTOR = _JOBID,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:proto.JobID)
  ))
_sym_db.RegisterMessage(JobID)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:proto.Empty)
  ))
_sym_db.RegisterMessage(Empty)

Ack = _reflection.GeneratedProtocolMessageType('Ack', (_message.Message,), dict(
  DESCRIPTOR = _ACK,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:proto.Ack)
  ))
_sym_db.RegisterMessage(Ack)



_TOKENS = _descriptor.ServiceDescriptor(
  name='Tokens',
  full_name='proto.Tokens',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=158,
  serialized_end=430,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='proto.Tokens.Get',
    index=0,
    containing_service=None,
    input_type=_JOBID,
    output_type=_DATA,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Done',
    full_name='proto.Tokens.Done',
    index=1,
    containing_service=None,
    input_type=_JOBID,
    output_type=_ACK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Reset',
    full_name='proto.Tokens.Reset',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_ACK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Rescan',
    full_name='proto.Tokens.Rescan',
    index=3,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_ACK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Shuffle',
    full_name='proto.Tokens.Shuffle',
    index=4,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_ACK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Show',
    full_name='proto.Tokens.Show',
    index=5,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_DATA,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HeartBeat',
    full_name='proto.Tokens.HeartBeat',
    index=6,
    containing_service=None,
    input_type=_JOBID,
    output_type=_ACK,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TOKENS)

DESCRIPTOR.services_by_name['Tokens'] = _TOKENS

# @@protoc_insertion_point(module_scope)
