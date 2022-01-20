# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/customer_manager_link.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.enums import manager_link_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_manager__link__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v8/resources/customer_manager_link.proto\x12!google.ads.googleads.v8.resources\x1a\x37google/ads/googleads/v8/enums/manager_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\x94\x04\n\x13\x43ustomerManagerLink\x12Z\n\rresource_name\x18\x01 \x01(\tB5\xe2\x41\x01\x05\xfa\x41.\n,googleads.googleapis.com/CustomerManagerLinkR\x0cresourceName\x12Z\n\x10manager_customer\x18\x06 \x01(\tB*\xe2\x41\x01\x03\xfa\x41#\n!googleads.googleapis.com/CustomerH\x00R\x0fmanagerCustomer\x88\x01\x01\x12\x31\n\x0fmanager_link_id\x18\x07 \x01(\x03\x42\x04\xe2\x41\x01\x03H\x01R\rmanagerLinkId\x88\x01\x01\x12^\n\x06status\x18\x05 \x01(\x0e\x32\x46.google.ads.googleads.v8.enums.ManagerLinkStatusEnum.ManagerLinkStatusR\x06status:\x88\x01\xea\x41\x84\x01\n,googleads.googleapis.com/CustomerManagerLink\x12Tcustomers/{customer_id}/customerManagerLinks/{manager_customer_id}~{manager_link_id}B\x13\n\x11_manager_customerB\x12\n\x10_manager_link_idB\x85\x02\n%com.google.ads.googleads.v8.resourcesB\x18\x43ustomerManagerLinkProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_CUSTOMERMANAGERLINK = DESCRIPTOR.message_types_by_name['CustomerManagerLink']
CustomerManagerLink = _reflection.GeneratedProtocolMessageType('CustomerManagerLink', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERMANAGERLINK,
  '__module__' : 'google.ads.googleads.v8.resources.customer_manager_link_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.CustomerManagerLink)
  })
_sym_db.RegisterMessage(CustomerManagerLink)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\030CustomerManagerLinkProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _CUSTOMERMANAGERLINK.fields_by_name['resource_name']._options = None
  _CUSTOMERMANAGERLINK.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A.\n,googleads.googleapis.com/CustomerManagerLink'
  _CUSTOMERMANAGERLINK.fields_by_name['manager_customer']._options = None
  _CUSTOMERMANAGERLINK.fields_by_name['manager_customer']._serialized_options = b'\342A\001\003\372A#\n!googleads.googleapis.com/Customer'
  _CUSTOMERMANAGERLINK.fields_by_name['manager_link_id']._options = None
  _CUSTOMERMANAGERLINK.fields_by_name['manager_link_id']._serialized_options = b'\342A\001\003'
  _CUSTOMERMANAGERLINK._options = None
  _CUSTOMERMANAGERLINK._serialized_options = b'\352A\204\001\n,googleads.googleapis.com/CustomerManagerLink\022Tcustomers/{customer_id}/customerManagerLinks/{manager_customer_id}~{manager_link_id}'
  _CUSTOMERMANAGERLINK._serialized_start=248
  _CUSTOMERMANAGERLINK._serialized_end=780
# @@protoc_insertion_point(module_scope)
