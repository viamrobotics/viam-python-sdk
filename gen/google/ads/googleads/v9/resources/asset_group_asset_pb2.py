# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/asset_group_asset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.common import policy_summary_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_common_dot_policy__summary__pb2
from google.ads.googleads.v9.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_asset__field__type__pb2
from google.ads.googleads.v9.enums import asset_link_status_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_asset__link__status__pb2
from google.ads.googleads.v9.enums import asset_performance_label_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_asset__performance__label__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v9/resources/asset_group_asset.proto\x12!google.ads.googleads.v9.resources\x1a\x33google/ads/googleads/v9/common/policy_summary.proto\x1a\x34google/ads/googleads/v9/enums/asset_field_type.proto\x1a\x35google/ads/googleads/v9/enums/asset_link_status.proto\x1a;google/ads/googleads/v9/enums/asset_performance_label.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\x97\x06\n\x0f\x41ssetGroupAsset\x12V\n\rresource_name\x18\x01 \x01(\tB1\xe2\x41\x01\x05\xfa\x41*\n(googleads.googleapis.com/AssetGroupAssetR\x0cresourceName\x12M\n\x0b\x61sset_group\x18\x02 \x01(\tB,\xe2\x41\x01\x05\xfa\x41%\n#googleads.googleapis.com/AssetGroupR\nassetGroup\x12=\n\x05\x61sset\x18\x03 \x01(\tB\'\xe2\x41\x01\x05\xfa\x41 \n\x1egoogleads.googleapis.com/AssetR\x05\x61sset\x12_\n\nfield_type\x18\x04 \x01(\x0e\x32@.google.ads.googleads.v9.enums.AssetFieldTypeEnum.AssetFieldTypeR\tfieldType\x12Z\n\x06status\x18\x05 \x01(\x0e\x32\x42.google.ads.googleads.v9.enums.AssetLinkStatusEnum.AssetLinkStatusR\x06status\x12\x81\x01\n\x11performance_label\x18\x06 \x01(\x0e\x32N.google.ads.googleads.v9.enums.AssetPerformanceLabelEnum.AssetPerformanceLabelB\x04\xe2\x41\x01\x03R\x10performanceLabel\x12Z\n\x0epolicy_summary\x18\x07 \x01(\x0b\x32-.google.ads.googleads.v9.common.PolicySummaryB\x04\xe2\x41\x01\x03R\rpolicySummary:\x80\x01\xea\x41}\n(googleads.googleapis.com/AssetGroupAsset\x12Qcustomers/{customer_id}/assetGroupAssets/{asset_group_id}~{asset_id}~{field_type}B\x81\x02\n%com.google.ads.googleads.v9.resourcesB\x14\x41ssetGroupAssetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3')



_ASSETGROUPASSET = DESCRIPTOR.message_types_by_name['AssetGroupAsset']
AssetGroupAsset = _reflection.GeneratedProtocolMessageType('AssetGroupAsset', (_message.Message,), {
  'DESCRIPTOR' : _ASSETGROUPASSET,
  '__module__' : 'google.ads.googleads.v9.resources.asset_group_asset_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.AssetGroupAsset)
  })
_sym_db.RegisterMessage(AssetGroupAsset)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v9.resourcesB\024AssetGroupAssetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources'
  _ASSETGROUPASSET.fields_by_name['resource_name']._options = None
  _ASSETGROUPASSET.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A*\n(googleads.googleapis.com/AssetGroupAsset'
  _ASSETGROUPASSET.fields_by_name['asset_group']._options = None
  _ASSETGROUPASSET.fields_by_name['asset_group']._serialized_options = b'\342A\001\005\372A%\n#googleads.googleapis.com/AssetGroup'
  _ASSETGROUPASSET.fields_by_name['asset']._options = None
  _ASSETGROUPASSET.fields_by_name['asset']._serialized_options = b'\342A\001\005\372A \n\036googleads.googleapis.com/Asset'
  _ASSETGROUPASSET.fields_by_name['performance_label']._options = None
  _ASSETGROUPASSET.fields_by_name['performance_label']._serialized_options = b'\342A\001\003'
  _ASSETGROUPASSET.fields_by_name['policy_summary']._options = None
  _ASSETGROUPASSET.fields_by_name['policy_summary']._serialized_options = b'\342A\001\003'
  _ASSETGROUPASSET._options = None
  _ASSETGROUPASSET._serialized_options = b'\352A}\n(googleads.googleapis.com/AssetGroupAsset\022Qcustomers/{customer_id}/assetGroupAssets/{asset_group_id}~{asset_id}~{field_type}'
  _ASSETGROUPASSET._serialized_start=410
  _ASSETGROUPASSET._serialized_end=1201
# @@protoc_insertion_point(module_scope)
