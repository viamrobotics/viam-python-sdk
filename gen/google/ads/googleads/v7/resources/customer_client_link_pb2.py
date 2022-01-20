# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/resources/customer_client_link.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.enums import manager_link_status_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_manager__link__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v7/resources/customer_client_link.proto\x12!google.ads.googleads.v7.resources\x1a\x37google/ads/googleads/v7/enums/manager_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xb4\x04\n\x12\x43ustomerClientLink\x12Y\n\rresource_name\x18\x01 \x01(\tB4\xe2\x41\x01\x05\xfa\x41-\n+googleads.googleapis.com/CustomerClientLinkR\x0cresourceName\x12X\n\x0f\x63lient_customer\x18\x07 \x01(\tB*\xe2\x41\x01\x05\xfa\x41#\n!googleads.googleapis.com/CustomerH\x00R\x0e\x63lientCustomer\x88\x01\x01\x12\x31\n\x0fmanager_link_id\x18\x08 \x01(\x03\x42\x04\xe2\x41\x01\x03H\x01R\rmanagerLinkId\x88\x01\x01\x12^\n\x06status\x18\x05 \x01(\x0e\x32\x46.google.ads.googleads.v7.enums.ManagerLinkStatusEnum.ManagerLinkStatusR\x06status\x12\x1b\n\x06hidden\x18\t \x01(\x08H\x02R\x06hidden\x88\x01\x01:\x85\x01\xea\x41\x81\x01\n+googleads.googleapis.com/CustomerClientLink\x12Rcustomers/{customer_id}/customerClientLinks/{client_customer_id}~{manager_link_id}B\x12\n\x10_client_customerB\x12\n\x10_manager_link_idB\t\n\x07_hiddenB\x84\x02\n%com.google.ads.googleads.v7.resourcesB\x17\x43ustomerClientLinkProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V7.Resources\xca\x02!Google\\Ads\\GoogleAds\\V7\\Resources\xea\x02%Google::Ads::GoogleAds::V7::Resourcesb\x06proto3')



_CUSTOMERCLIENTLINK = DESCRIPTOR.message_types_by_name['CustomerClientLink']
CustomerClientLink = _reflection.GeneratedProtocolMessageType('CustomerClientLink', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERCLIENTLINK,
  '__module__' : 'google.ads.googleads.v7.resources.customer_client_link_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.resources.CustomerClientLink)
  })
_sym_db.RegisterMessage(CustomerClientLink)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v7.resourcesB\027CustomerClientLinkProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V7.Resources\312\002!Google\\Ads\\GoogleAds\\V7\\Resources\352\002%Google::Ads::GoogleAds::V7::Resources'
  _CUSTOMERCLIENTLINK.fields_by_name['resource_name']._options = None
  _CUSTOMERCLIENTLINK.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A-\n+googleads.googleapis.com/CustomerClientLink'
  _CUSTOMERCLIENTLINK.fields_by_name['client_customer']._options = None
  _CUSTOMERCLIENTLINK.fields_by_name['client_customer']._serialized_options = b'\342A\001\005\372A#\n!googleads.googleapis.com/Customer'
  _CUSTOMERCLIENTLINK.fields_by_name['manager_link_id']._options = None
  _CUSTOMERCLIENTLINK.fields_by_name['manager_link_id']._serialized_options = b'\342A\001\003'
  _CUSTOMERCLIENTLINK._options = None
  _CUSTOMERCLIENTLINK._serialized_options = b'\352A\201\001\n+googleads.googleapis.com/CustomerClientLink\022Rcustomers/{customer_id}/customerClientLinks/{client_customer_id}~{manager_link_id}'
  _CUSTOMERCLIENTLINK._serialized_start=247
  _CUSTOMERCLIENTLINK._serialized_end=811
# @@protoc_insertion_point(module_scope)
