# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: column-expand-meta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63olumn-expand-meta.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"_\n\x10\x43olumnExpandMeta\x12\x15\n\rappend_header\x18\x01 \x03(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x12\n\nfill_value\x18\x03 \x03(\t\x12\x10\n\x08need_run\x18\x04 \x01(\x08\x42\x17\x42\x15\x43olumnExpandMetaProtob\x06proto3')



_COLUMNEXPANDMETA = DESCRIPTOR.message_types_by_name['ColumnExpandMeta']
ColumnExpandMeta = _reflection.GeneratedProtocolMessageType('ColumnExpandMeta', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNEXPANDMETA,
  '__module__' : 'column_expand_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.ColumnExpandMeta)
  })
_sym_db.RegisterMessage(ColumnExpandMeta)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\025ColumnExpandMetaProto'
  _COLUMNEXPANDMETA._serialized_start=68
  _COLUMNEXPANDMETA._serialized_end=163
# @@protoc_insertion_point(module_scope)
