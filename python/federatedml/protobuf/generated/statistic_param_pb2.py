# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: statistic-param.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15statistic-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"T\n\x1bStatisticSingleFeatureValue\x12\x0e\n\x06values\x18\x01 \x03(\x01\x12\x11\n\tcol_names\x18\x02 \x03(\t\x12\x12\n\nvalue_name\x18\x03 \x01(\t\"o\n\x17StatisticOnePartyResult\x12T\n\x07results\x18\x01 \x03(\x0b\x32\x43.com.webank.ai.fate.core.mlmodel.buffer.StatisticSingleFeatureValue\"\xc3\x02\n\nModelParam\x12T\n\x0bself_values\x18\x01 \x01(\x0b\x32?.com.webank.ai.fate.core.mlmodel.buffer.StatisticOnePartyResult\x12W\n\x0bhost_values\x18\x02 \x03(\x0b\x32\x42.com.webank.ai.fate.core.mlmodel.buffer.ModelParam.HostValuesEntry\x12\x12\n\nmodel_name\x18\x03 \x01(\t\x1ar\n\x0fHostValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0b\x32?.com.webank.ai.fate.core.mlmodel.buffer.StatisticOnePartyResult:\x02\x38\x01\x42\x15\x42\x13StatisticParamProtob\x06proto3')



_STATISTICSINGLEFEATUREVALUE = DESCRIPTOR.message_types_by_name['StatisticSingleFeatureValue']
_STATISTICONEPARTYRESULT = DESCRIPTOR.message_types_by_name['StatisticOnePartyResult']
_MODELPARAM = DESCRIPTOR.message_types_by_name['ModelParam']
_MODELPARAM_HOSTVALUESENTRY = _MODELPARAM.nested_types_by_name['HostValuesEntry']
StatisticSingleFeatureValue = _reflection.GeneratedProtocolMessageType('StatisticSingleFeatureValue', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICSINGLEFEATUREVALUE,
  '__module__' : 'statistic_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.StatisticSingleFeatureValue)
  })
_sym_db.RegisterMessage(StatisticSingleFeatureValue)

StatisticOnePartyResult = _reflection.GeneratedProtocolMessageType('StatisticOnePartyResult', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICONEPARTYRESULT,
  '__module__' : 'statistic_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.StatisticOnePartyResult)
  })
_sym_db.RegisterMessage(StatisticOnePartyResult)

ModelParam = _reflection.GeneratedProtocolMessageType('ModelParam', (_message.Message,), {

  'HostValuesEntry' : _reflection.GeneratedProtocolMessageType('HostValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _MODELPARAM_HOSTVALUESENTRY,
    '__module__' : 'statistic_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.ModelParam.HostValuesEntry)
    })
  ,
  'DESCRIPTOR' : _MODELPARAM,
  '__module__' : 'statistic_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.ModelParam)
  })
_sym_db.RegisterMessage(ModelParam)
_sym_db.RegisterMessage(ModelParam.HostValuesEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\023StatisticParamProto'
  _MODELPARAM_HOSTVALUESENTRY._options = None
  _MODELPARAM_HOSTVALUESENTRY._serialized_options = b'8\001'
  _STATISTICSINGLEFEATUREVALUE._serialized_start=65
  _STATISTICSINGLEFEATUREVALUE._serialized_end=149
  _STATISTICONEPARTYRESULT._serialized_start=151
  _STATISTICONEPARTYRESULT._serialized_end=262
  _MODELPARAM._serialized_start=265
  _MODELPARAM._serialized_end=588
  _MODELPARAM_HOSTVALUESENTRY._serialized_start=474
  _MODELPARAM_HOSTVALUESENTRY._serialized_end=588
# @@protoc_insertion_point(module_scope)
