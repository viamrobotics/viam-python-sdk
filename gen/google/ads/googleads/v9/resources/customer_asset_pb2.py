# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/customer_asset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_asset__field__type__pb2
from google.ads.googleads.v9.enums import asset_link_status_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_asset__link__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v9/resources/customer_asset.proto\x12!google.ads.googleads.v9.resources\x1a\x34google/ads/googleads/v9/enums/asset_field_type.proto\x1a\x35google/ads/googleads/v9/enums/asset_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xd6\x03\n\rCustomerAsset\x12T\n\rresource_name\x18\x01 \x01(\tB/\xe2\x41\x01\x05\xfa\x41(\n&googleads.googleapis.com/CustomerAssetR\x0cresourceName\x12>\n\x05\x61sset\x18\x02 \x01(\tB(\xe2\x41\x02\x02\x05\xfa\x41 \n\x1egoogleads.googleapis.com/AssetR\x05\x61sset\x12\x66\n\nfield_type\x18\x03 \x01(\x0e\x32@.google.ads.googleads.v9.enums.AssetFieldTypeEnum.AssetFieldTypeB\x05\xe2\x41\x02\x02\x05R\tfieldType\x12Z\n\x06status\x18\x04 \x01(\x0e\x32\x42.google.ads.googleads.v9.enums.AssetLinkStatusEnum.AssetLinkStatusR\x06status:k\xea\x41h\n&googleads.googleapis.com/CustomerAsset\x12>customers/{customer_id}/customerAssets/{asset_id}~{field_type}B\xff\x01\n%com.google.ads.googleads.v9.resourcesB\x12\x43ustomerAssetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3')



_CUSTOMERASSET = DESCRIPTOR.message_types_by_name['CustomerAsset']
CustomerAsset = _reflection.GeneratedProtocolMessageType('CustomerAsset', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERASSET,
  '__module__' : 'google.ads.googleads.v9.resources.customer_asset_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.CustomerAsset)
  })
_sym_db.RegisterMessage(CustomerAsset)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v9.resourcesB\022CustomerAssetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources'
  _CUSTOMERASSET.fields_by_name['resource_name']._options = None
  _CUSTOMERASSET.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A(\n&googleads.googleapis.com/CustomerAsset'
  _CUSTOMERASSET.fields_by_name['asset']._options = None
  _CUSTOMERASSET.fields_by_name['asset']._serialized_options = b'\342A\002\002\005\372A \n\036googleads.googleapis.com/Asset'
  _CUSTOMERASSET.fields_by_name['field_type']._options = None
  _CUSTOMERASSET.fields_by_name['field_type']._serialized_options = b'\342A\002\002\005'
  _CUSTOMERASSET._options = None
  _CUSTOMERASSET._serialized_options = b'\352Ah\n&googleads.googleapis.com/CustomerAsset\022>customers/{customer_id}/customerAssets/{asset_id}~{field_type}'
  _CUSTOMERASSET._serialized_start=293
  _CUSTOMERASSET._serialized_end=763
# @@protoc_insertion_point(module_scope)
