# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: general_classify_client.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='general_classify_client.proto',
  package='vis.generalclassifyclient',
  syntax='proto3',
  serialized_options=_b('\200\001\001'),
  serialized_pb=_b('\n\x1dgeneral_classify_client.proto\x12\x19vis.generalclassifyclient\"1\n\x0c\x43lassifyType\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x0e\n\x06topnum\x18\x02 \x01(\x05\"g\n\x16GeneralClassifyRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\x12>\n\rclassify_type\x18\x02 \x03(\x0b\x32\'.vis.generalclassifyclient.ClassifyType\")\n\tPointData\x12\r\n\x05index\x18\x01 \x01(\x05\x12\r\n\x05score\x18\x02 \x01(\x02\"F\n\x0eTop_gen970Data\x12\x34\n\x06points\x18\x01 \x03(\x0b\x32$.vis.generalclassifyclient.PointData\"\x18\n\x03\x42ox\x12\x11\n\tbox_coord\x18\x01 \x03(\x02\"\xdd\x01\n\x0e\x43lassifyResult\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x10\n\x08\x63lass_id\x18\x02 \x03(\x05\x12\x13\n\x0bprobability\x18\x03 \x03(\x02\x12\x41\n\x0e\x63lassifyfamily\x18\x04 \x03(\x0b\x32).vis.generalclassifyclient.Top_gen970Data\x12\x0f\n\x07imshape\x18\x05 \x03(\x02\x12\x0e\n\x06scores\x18\x06 \x03(\x02\x12-\n\x05\x62oxes\x18\x07 \x03(\x0b\x32\x1e.vis.generalclassifyclient.Box\"T\n\x17GeneralClassifyResponse\x12\x39\n\x06result\x18\x01 \x03(\x0b\x32).vis.generalclassifyclient.ClassifyResultB\x03\x80\x01\x01\x62\x06proto3')
)




_CLASSIFYTYPE = _descriptor.Descriptor(
  name='ClassifyType',
  full_name='vis.generalclassifyclient.ClassifyType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_name', full_name='vis.generalclassifyclient.ClassifyType.type_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topnum', full_name='vis.generalclassifyclient.ClassifyType.topnum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=109,
)


_GENERALCLASSIFYREQUEST = _descriptor.Descriptor(
  name='GeneralClassifyRequest',
  full_name='vis.generalclassifyclient.GeneralClassifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='vis.generalclassifyclient.GeneralClassifyRequest.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classify_type', full_name='vis.generalclassifyclient.GeneralClassifyRequest.classify_type', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=214,
)


_POINTDATA = _descriptor.Descriptor(
  name='PointData',
  full_name='vis.generalclassifyclient.PointData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='vis.generalclassifyclient.PointData.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='vis.generalclassifyclient.PointData.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=257,
)


_TOP_GEN970DATA = _descriptor.Descriptor(
  name='Top_gen970Data',
  full_name='vis.generalclassifyclient.Top_gen970Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='vis.generalclassifyclient.Top_gen970Data.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=329,
)


_BOX = _descriptor.Descriptor(
  name='Box',
  full_name='vis.generalclassifyclient.Box',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='box_coord', full_name='vis.generalclassifyclient.Box.box_coord', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=355,
)


_CLASSIFYRESULT = _descriptor.Descriptor(
  name='ClassifyResult',
  full_name='vis.generalclassifyclient.ClassifyResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_name', full_name='vis.generalclassifyclient.ClassifyResult.type_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_id', full_name='vis.generalclassifyclient.ClassifyResult.class_id', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='probability', full_name='vis.generalclassifyclient.ClassifyResult.probability', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classifyfamily', full_name='vis.generalclassifyclient.ClassifyResult.classifyfamily', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imshape', full_name='vis.generalclassifyclient.ClassifyResult.imshape', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scores', full_name='vis.generalclassifyclient.ClassifyResult.scores', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boxes', full_name='vis.generalclassifyclient.ClassifyResult.boxes', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=579,
)


_GENERALCLASSIFYRESPONSE = _descriptor.Descriptor(
  name='GeneralClassifyResponse',
  full_name='vis.generalclassifyclient.GeneralClassifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='vis.generalclassifyclient.GeneralClassifyResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=665,
)

_GENERALCLASSIFYREQUEST.fields_by_name['classify_type'].message_type = _CLASSIFYTYPE
_TOP_GEN970DATA.fields_by_name['points'].message_type = _POINTDATA
_CLASSIFYRESULT.fields_by_name['classifyfamily'].message_type = _TOP_GEN970DATA
_CLASSIFYRESULT.fields_by_name['boxes'].message_type = _BOX
_GENERALCLASSIFYRESPONSE.fields_by_name['result'].message_type = _CLASSIFYRESULT
DESCRIPTOR.message_types_by_name['ClassifyType'] = _CLASSIFYTYPE
DESCRIPTOR.message_types_by_name['GeneralClassifyRequest'] = _GENERALCLASSIFYREQUEST
DESCRIPTOR.message_types_by_name['PointData'] = _POINTDATA
DESCRIPTOR.message_types_by_name['Top_gen970Data'] = _TOP_GEN970DATA
DESCRIPTOR.message_types_by_name['Box'] = _BOX
DESCRIPTOR.message_types_by_name['ClassifyResult'] = _CLASSIFYRESULT
DESCRIPTOR.message_types_by_name['GeneralClassifyResponse'] = _GENERALCLASSIFYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassifyType = _reflection.GeneratedProtocolMessageType('ClassifyType', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFYTYPE,
  __module__ = 'general_classify_client_pb2'
  # @@protoc_insertion_point(class_scope:vis.generalclassifyclient.ClassifyType)
  ))
_sym_db.RegisterMessage(ClassifyType)

GeneralClassifyRequest = _reflection.GeneratedProtocolMessageType('GeneralClassifyRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENERALCLASSIFYREQUEST,
  __module__ = 'general_classify_client_pb2'
  # @@protoc_insertion_point(class_scope:vis.generalclassifyclient.GeneralClassifyRequest)
  ))
_sym_db.RegisterMessage(GeneralClassifyRequest)

PointData = _reflection.GeneratedProtocolMessageType('PointData', (_message.Message,), dict(
  DESCRIPTOR = _POINTDATA,
  __module__ = 'general_classify_client_pb2'
  # @@protoc_insertion_point(class_scope:vis.generalclassifyclient.PointData)
  ))
_sym_db.RegisterMessage(PointData)

Top_gen970Data = _reflection.GeneratedProtocolMessageType('Top_gen970Data', (_message.Message,), dict(
  DESCRIPTOR = _TOP_GEN970DATA,
  __module__ = 'general_classify_client_pb2'
  # @@protoc_insertion_point(class_scope:vis.generalclassifyclient.Top_gen970Data)
  ))
_sym_db.RegisterMessage(Top_gen970Data)

Box = _reflection.GeneratedProtocolMessageType('Box', (_message.Message,), dict(
  DESCRIPTOR = _BOX,
  __module__ = 'general_classify_client_pb2'
  # @@protoc_insertion_point(class_scope:vis.generalclassifyclient.Box)
  ))
_sym_db.RegisterMessage(Box)

ClassifyResult = _reflection.GeneratedProtocolMessageType('ClassifyResult', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFYRESULT,
  __module__ = 'general_classify_client_pb2'
  # @@protoc_insertion_point(class_scope:vis.generalclassifyclient.ClassifyResult)
  ))
_sym_db.RegisterMessage(ClassifyResult)

GeneralClassifyResponse = _reflection.GeneratedProtocolMessageType('GeneralClassifyResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERALCLASSIFYRESPONSE,
  __module__ = 'general_classify_client_pb2'
  # @@protoc_insertion_point(class_scope:vis.generalclassifyclient.GeneralClassifyResponse)
  ))
_sym_db.RegisterMessage(GeneralClassifyResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
