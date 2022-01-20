# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/product_group_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.resources import product_group_view_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_product__group__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v9/services/product_group_view_service.proto\x12 google.ads.googleads.v9.services\x1a:google/ads/googleads/v9/resources/product_group_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"u\n\x1aGetProductGroupViewRequest\x12W\n\rresource_name\x18\x01 \x01(\tB2\xe2\x41\x01\x02\xfa\x41+\n)googleads.googleapis.com/ProductGroupViewR\x0cresourceName2\xb8\x02\n\x17ProductGroupViewService\x12\xd5\x01\n\x13GetProductGroupView\x12<.google.ads.googleads.v9.services.GetProductGroupViewRequest\x1a\x33.google.ads.googleads.v9.resources.ProductGroupView\"K\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x35\x12\x33/v9/{resource_name=customers/*/productGroupViews/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x83\x02\n$com.google.ads.googleads.v9.servicesB\x1cProductGroupViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETPRODUCTGROUPVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetProductGroupViewRequest']
GetProductGroupViewRequest = _reflection.GeneratedProtocolMessageType('GetProductGroupViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCTGROUPVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.product_group_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetProductGroupViewRequest)
  })
_sym_db.RegisterMessage(GetProductGroupViewRequest)

_PRODUCTGROUPVIEWSERVICE = DESCRIPTOR.services_by_name['ProductGroupViewService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\034ProductGroupViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETPRODUCTGROUPVIEWREQUEST.fields_by_name['resource_name']._options = None
  _GETPRODUCTGROUPVIEWREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A+\n)googleads.googleapis.com/ProductGroupView'
  _PRODUCTGROUPVIEWSERVICE._options = None
  _PRODUCTGROUPVIEWSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _PRODUCTGROUPVIEWSERVICE.methods_by_name['GetProductGroupView']._options = None
  _PRODUCTGROUPVIEWSERVICE.methods_by_name['GetProductGroupView']._serialized_options = b'\332A\rresource_name\202\323\344\223\0025\0223/v9/{resource_name=customers/*/productGroupViews/*}'
  _GETPRODUCTGROUPVIEWREQUEST._serialized_start=278
  _GETPRODUCTGROUPVIEWREQUEST._serialized_end=395
  _PRODUCTGROUPVIEWSERVICE._serialized_start=398
  _PRODUCTGROUPVIEWSERVICE._serialized_end=710
# @@protoc_insertion_point(module_scope)
