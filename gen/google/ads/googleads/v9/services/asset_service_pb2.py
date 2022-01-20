# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/asset_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_response__content__type__pb2
from google.ads.googleads.v9.resources import asset_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_asset__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/ads/googleads/v9/services/asset_service.proto\x12 google.ads.googleads.v9.services\x1a\x39google/ads/googleads/v9/enums/response_content_type.proto\x1a-google/ads/googleads/v9/resources/asset.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"_\n\x0fGetAssetRequest\x12L\n\rresource_name\x18\x01 \x01(\tB\'\xe2\x41\x01\x02\xfa\x41 \n\x1egoogleads.googleapis.com/AssetR\x0cresourceName\"\xe2\x02\n\x13MutateAssetsRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12V\n\noperations\x18\x02 \x03(\x0b\x32\x30.google.ads.googleads.v9.services.AssetOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x05 \x01(\x08R\x0epartialFailure\x12~\n\x15response_content_type\x18\x03 \x01(\x0e\x32J.google.ads.googleads.v9.enums.ResponseContentTypeEnum.ResponseContentTypeR\x13responseContentType\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\"\xe2\x01\n\x0e\x41ssetOperation\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12\x42\n\x06\x63reate\x18\x01 \x01(\x0b\x32(.google.ads.googleads.v9.resources.AssetH\x00R\x06\x63reate\x12\x42\n\x06update\x18\x02 \x01(\x0b\x32(.google.ads.googleads.v9.resources.AssetH\x00R\x06updateB\x0b\n\toperation\"\xad\x01\n\x14MutateAssetsResponse\x12\x46\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\x12M\n\x07results\x18\x02 \x03(\x0b\x32\x33.google.ads.googleads.v9.services.MutateAssetResultR\x07results\"x\n\x11MutateAssetResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12>\n\x05\x61sset\x18\x02 \x01(\x0b\x32(.google.ads.googleads.v9.resources.AssetR\x05\x61sset2\xd2\x03\n\x0c\x41ssetService\x12\xa9\x01\n\x08GetAsset\x12\x31.google.ads.googleads.v9.services.GetAssetRequest\x1a(.google.ads.googleads.v9.resources.Asset\"@\xda\x41\rresource_name\x82\xd3\xe4\x93\x02*\x12(/v9/{resource_name=customers/*/assets/*}\x12\xce\x01\n\x0cMutateAssets\x12\x35.google.ads.googleads.v9.services.MutateAssetsRequest\x1a\x36.google.ads.googleads.v9.services.MutateAssetsResponse\"O\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02\x30\"+/v9/customers/{customer_id=*}/assets:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\xf8\x01\n$com.google.ads.googleads.v9.servicesB\x11\x41ssetServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETASSETREQUEST = DESCRIPTOR.message_types_by_name['GetAssetRequest']
_MUTATEASSETSREQUEST = DESCRIPTOR.message_types_by_name['MutateAssetsRequest']
_ASSETOPERATION = DESCRIPTOR.message_types_by_name['AssetOperation']
_MUTATEASSETSRESPONSE = DESCRIPTOR.message_types_by_name['MutateAssetsResponse']
_MUTATEASSETRESULT = DESCRIPTOR.message_types_by_name['MutateAssetResult']
GetAssetRequest = _reflection.GeneratedProtocolMessageType('GetAssetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETASSETREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.asset_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetAssetRequest)
  })
_sym_db.RegisterMessage(GetAssetRequest)

MutateAssetsRequest = _reflection.GeneratedProtocolMessageType('MutateAssetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEASSETSREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.asset_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateAssetsRequest)
  })
_sym_db.RegisterMessage(MutateAssetsRequest)

AssetOperation = _reflection.GeneratedProtocolMessageType('AssetOperation', (_message.Message,), {
  'DESCRIPTOR' : _ASSETOPERATION,
  '__module__' : 'google.ads.googleads.v9.services.asset_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.AssetOperation)
  })
_sym_db.RegisterMessage(AssetOperation)

MutateAssetsResponse = _reflection.GeneratedProtocolMessageType('MutateAssetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEASSETSRESPONSE,
  '__module__' : 'google.ads.googleads.v9.services.asset_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateAssetsResponse)
  })
_sym_db.RegisterMessage(MutateAssetsResponse)

MutateAssetResult = _reflection.GeneratedProtocolMessageType('MutateAssetResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEASSETRESULT,
  '__module__' : 'google.ads.googleads.v9.services.asset_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateAssetResult)
  })
_sym_db.RegisterMessage(MutateAssetResult)

_ASSETSERVICE = DESCRIPTOR.services_by_name['AssetService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\021AssetServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETASSETREQUEST.fields_by_name['resource_name']._options = None
  _GETASSETREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A \n\036googleads.googleapis.com/Asset'
  _MUTATEASSETSREQUEST.fields_by_name['customer_id']._options = None
  _MUTATEASSETSREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATEASSETSREQUEST.fields_by_name['operations']._options = None
  _MUTATEASSETSREQUEST.fields_by_name['operations']._serialized_options = b'\342A\001\002'
  _ASSETSERVICE._options = None
  _ASSETSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _ASSETSERVICE.methods_by_name['GetAsset']._options = None
  _ASSETSERVICE.methods_by_name['GetAsset']._serialized_options = b'\332A\rresource_name\202\323\344\223\002*\022(/v9/{resource_name=customers/*/assets/*}'
  _ASSETSERVICE.methods_by_name['MutateAssets']._options = None
  _ASSETSERVICE.methods_by_name['MutateAssets']._serialized_options = b'\332A\026customer_id,operations\202\323\344\223\0020\"+/v9/customers/{customer_id=*}/assets:mutate:\001*'
  _GETASSETREQUEST._serialized_start=370
  _GETASSETREQUEST._serialized_end=465
  _MUTATEASSETSREQUEST._serialized_start=468
  _MUTATEASSETSREQUEST._serialized_end=822
  _ASSETOPERATION._serialized_start=825
  _ASSETOPERATION._serialized_end=1051
  _MUTATEASSETSRESPONSE._serialized_start=1054
  _MUTATEASSETSRESPONSE._serialized_end=1227
  _MUTATEASSETRESULT._serialized_start=1229
  _MUTATEASSETRESULT._serialized_end=1349
  _ASSETSERVICE._serialized_start=1352
  _ASSETSERVICE._serialized_end=1818
# @@protoc_insertion_point(module_scope)
