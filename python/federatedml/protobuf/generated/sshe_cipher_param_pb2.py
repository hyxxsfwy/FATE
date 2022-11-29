# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sshe-cipher-param.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17sshe-cipher-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\xa4\x01\n\x06\x43ipher\x12K\n\npublic_key\x18\x01 \x01(\x0b\x32\x37.com.webank.ai.fate.core.mlmodel.buffer.CipherPublicKey\x12M\n\x0bprivate_key\x18\x02 \x01(\x0b\x32\x38.com.webank.ai.fate.core.mlmodel.buffer.CipherPrivateKey\"\x1c\n\x0f\x43ipherPublicKey\x12\t\n\x01n\x18\x01 \x01(\t\"(\n\x10\x43ipherPrivateKey\x12\t\n\x01p\x18\x01 \x01(\t\x12\t\n\x01q\x18\x02 \x01(\t\"\x97\x01\n\nCipherText\x12K\n\npublic_key\x18\x01 \x01(\x0b\x32\x37.com.webank.ai.fate.core.mlmodel.buffer.CipherPublicKey\x12\x13\n\x0b\x63ipher_text\x18\x02 \x01(\t\x12\x10\n\x08\x65xponent\x18\x03 \x01(\t\x12\x15\n\ris_obfuscator\x18\x04 \x01(\x08\x42\x12\x42\x10\x43ipherParamProtob\x06proto3')



_CIPHER = DESCRIPTOR.message_types_by_name['Cipher']
_CIPHERPUBLICKEY = DESCRIPTOR.message_types_by_name['CipherPublicKey']
_CIPHERPRIVATEKEY = DESCRIPTOR.message_types_by_name['CipherPrivateKey']
_CIPHERTEXT = DESCRIPTOR.message_types_by_name['CipherText']
Cipher = _reflection.GeneratedProtocolMessageType('Cipher', (_message.Message,), {
  'DESCRIPTOR' : _CIPHER,
  '__module__' : 'sshe_cipher_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.Cipher)
  })
_sym_db.RegisterMessage(Cipher)

CipherPublicKey = _reflection.GeneratedProtocolMessageType('CipherPublicKey', (_message.Message,), {
  'DESCRIPTOR' : _CIPHERPUBLICKEY,
  '__module__' : 'sshe_cipher_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.CipherPublicKey)
  })
_sym_db.RegisterMessage(CipherPublicKey)

CipherPrivateKey = _reflection.GeneratedProtocolMessageType('CipherPrivateKey', (_message.Message,), {
  'DESCRIPTOR' : _CIPHERPRIVATEKEY,
  '__module__' : 'sshe_cipher_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.CipherPrivateKey)
  })
_sym_db.RegisterMessage(CipherPrivateKey)

CipherText = _reflection.GeneratedProtocolMessageType('CipherText', (_message.Message,), {
  'DESCRIPTOR' : _CIPHERTEXT,
  '__module__' : 'sshe_cipher_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.CipherText)
  })
_sym_db.RegisterMessage(CipherText)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\020CipherParamProto'
  _CIPHER._serialized_start=68
  _CIPHER._serialized_end=232
  _CIPHERPUBLICKEY._serialized_start=234
  _CIPHERPUBLICKEY._serialized_end=262
  _CIPHERPRIVATEKEY._serialized_start=264
  _CIPHERPRIVATEKEY._serialized_end=304
  _CIPHERTEXT._serialized_start=307
  _CIPHERTEXT._serialized_end=458
# @@protoc_insertion_point(module_scope)
