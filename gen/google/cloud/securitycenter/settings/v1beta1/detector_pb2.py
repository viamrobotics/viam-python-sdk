# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/securitycenter/settings/v1beta1/detector.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.securitycenter.settings.v1beta1 import billing_settings_pb2 as google_dot_cloud_dot_securitycenter_dot_settings_dot_v1beta1_dot_billing__settings__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/securitycenter/settings/v1beta1/detector.proto\x12,google.cloud.securitycenter.settings.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x43google/cloud/securitycenter/settings/v1beta1/billing_settings.proto\x1a\x1cgoogle/api/annotations.proto\"\xe3\x01\n\x08\x44\x65tector\x12 \n\x08\x64\x65tector\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x08\x64\x65tector\x12\"\n\tcomponent\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\tcomponent\x12\x62\n\x0c\x62illing_tier\x18\x03 \x01(\x0e\x32\x39.google.cloud.securitycenter.settings.v1beta1.BillingTierB\x04\xe2\x41\x01\x03R\x0b\x62illingTier\x12-\n\x0f\x64\x65tector_labels\x18\x04 \x03(\tB\x04\xe2\x41\x01\x03R\x0e\x64\x65tectorLabelsB\xae\x02\n0com.google.cloud.securitycenter.settings.v1beta1B\x0e\x44\x65tectorsProtoP\x01ZTgoogle.golang.org/genproto/googleapis/cloud/securitycenter/settings/v1beta1;settings\xf8\x01\x01\xaa\x02,Google.Cloud.SecurityCenter.Settings.V1Beta1\xca\x02,Google\\Cloud\\SecurityCenter\\Settings\\V1beta1\xea\x02\x30Google::Cloud::SecurityCenter::Settings::V1beta1b\x06proto3')



_DETECTOR = DESCRIPTOR.message_types_by_name['Detector']
Detector = _reflection.GeneratedProtocolMessageType('Detector', (_message.Message,), {
  'DESCRIPTOR' : _DETECTOR,
  '__module__' : 'google.cloud.securitycenter.settings.v1beta1.detector_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.settings.v1beta1.Detector)
  })
_sym_db.RegisterMessage(Detector)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n0com.google.cloud.securitycenter.settings.v1beta1B\016DetectorsProtoP\001ZTgoogle.golang.org/genproto/googleapis/cloud/securitycenter/settings/v1beta1;settings\370\001\001\252\002,Google.Cloud.SecurityCenter.Settings.V1Beta1\312\002,Google\\Cloud\\SecurityCenter\\Settings\\V1beta1\352\0020Google::Cloud::SecurityCenter::Settings::V1beta1'
  _DETECTOR.fields_by_name['detector']._options = None
  _DETECTOR.fields_by_name['detector']._serialized_options = b'\342A\001\003'
  _DETECTOR.fields_by_name['component']._options = None
  _DETECTOR.fields_by_name['component']._serialized_options = b'\342A\001\003'
  _DETECTOR.fields_by_name['billing_tier']._options = None
  _DETECTOR.fields_by_name['billing_tier']._serialized_options = b'\342A\001\003'
  _DETECTOR.fields_by_name['detector_labels']._options = None
  _DETECTOR.fields_by_name['detector_labels']._serialized_options = b'\342A\001\003'
  _DETECTOR._serialized_start=242
  _DETECTOR._serialized_end=469
# @@protoc_insertion_point(module_scope)
