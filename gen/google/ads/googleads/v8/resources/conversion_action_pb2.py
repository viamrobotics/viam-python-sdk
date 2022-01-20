# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/conversion_action.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.common import tag_snippet_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_tag__snippet__pb2
from google.ads.googleads.v8.enums import attribution_model_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_attribution__model__pb2
from google.ads.googleads.v8.enums import conversion_action_category_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_conversion__action__category__pb2
from google.ads.googleads.v8.enums import conversion_action_counting_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_conversion__action__counting__type__pb2
from google.ads.googleads.v8.enums import conversion_action_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_conversion__action__status__pb2
from google.ads.googleads.v8.enums import conversion_action_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_conversion__action__type__pb2
from google.ads.googleads.v8.enums import data_driven_model_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_data__driven__model__status__pb2
from google.ads.googleads.v8.enums import mobile_app_vendor_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_mobile__app__vendor__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v8/resources/conversion_action.proto\x12!google.ads.googleads.v8.resources\x1a\x30google/ads/googleads/v8/common/tag_snippet.proto\x1a\x35google/ads/googleads/v8/enums/attribution_model.proto\x1a>google/ads/googleads/v8/enums/conversion_action_category.proto\x1a\x43google/ads/googleads/v8/enums/conversion_action_counting_type.proto\x1a<google/ads/googleads/v8/enums/conversion_action_status.proto\x1a:google/ads/googleads/v8/enums/conversion_action_type.proto\x1a<google/ads/googleads/v8/enums/data_driven_model_status.proto\x1a\x35google/ads/googleads/v8/enums/mobile_app_vendor.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xc2\x16\n\x10\x43onversionAction\x12W\n\rresource_name\x18\x01 \x01(\tB2\xe2\x41\x01\x05\xfa\x41+\n)googleads.googleapis.com/ConversionActionR\x0cresourceName\x12\x19\n\x02id\x18\x15 \x01(\x03\x42\x04\xe2\x41\x01\x03H\x00R\x02id\x88\x01\x01\x12\x17\n\x04name\x18\x16 \x01(\tH\x01R\x04name\x88\x01\x01\x12h\n\x06status\x18\x04 \x01(\x0e\x32P.google.ads.googleads.v8.enums.ConversionActionStatusEnum.ConversionActionStatusR\x06status\x12\x66\n\x04type\x18\x05 \x01(\x0e\x32L.google.ads.googleads.v8.enums.ConversionActionTypeEnum.ConversionActionTypeB\x04\xe2\x41\x01\x05R\x04type\x12p\n\x08\x63\x61tegory\x18\x06 \x01(\x0e\x32T.google.ads.googleads.v8.enums.ConversionActionCategoryEnum.ConversionActionCategoryR\x08\x63\x61tegory\x12V\n\x0eowner_customer\x18\x17 \x01(\tB*\xe2\x41\x01\x03\xfa\x41#\n!googleads.googleapis.com/CustomerH\x02R\rownerCustomer\x88\x01\x01\x12\x46\n\x1dinclude_in_conversions_metric\x18\x18 \x01(\x08H\x03R\x1aincludeInConversionsMetric\x88\x01\x01\x12O\n\"click_through_lookback_window_days\x18\x19 \x01(\x03H\x04R\x1e\x63lickThroughLookbackWindowDays\x88\x01\x01\x12M\n!view_through_lookback_window_days\x18\x1a \x01(\x03H\x05R\x1dviewThroughLookbackWindowDays\x88\x01\x01\x12h\n\x0evalue_settings\x18\x0b \x01(\x0b\x32\x41.google.ads.googleads.v8.resources.ConversionAction.ValueSettingsR\rvalueSettings\x12\x81\x01\n\rcounting_type\x18\x0c \x01(\x0e\x32\\.google.ads.googleads.v8.enums.ConversionActionCountingTypeEnum.ConversionActionCountingTypeR\x0c\x63ountingType\x12\x8a\x01\n\x1a\x61ttribution_model_settings\x18\r \x01(\x0b\x32L.google.ads.googleads.v8.resources.ConversionAction.AttributionModelSettingsR\x18\x61ttributionModelSettings\x12S\n\x0ctag_snippets\x18\x0e \x03(\x0b\x32*.google.ads.googleads.v8.common.TagSnippetB\x04\xe2\x41\x01\x03R\x0btagSnippets\x12\x42\n\x1bphone_call_duration_seconds\x18\x1b \x01(\x03H\x06R\x18phoneCallDurationSeconds\x88\x01\x01\x12\x1a\n\x06\x61pp_id\x18\x1c \x01(\tH\x07R\x05\x61ppId\x88\x01\x01\x12t\n\x11mobile_app_vendor\x18\x11 \x01(\x0e\x32\x42.google.ads.googleads.v8.enums.MobileAppVendorEnum.MobileAppVendorB\x04\xe2\x41\x01\x03R\x0fmobileAppVendor\x12w\n\x11\x66irebase_settings\x18\x12 \x01(\x0b\x32\x44.google.ads.googleads.v8.resources.ConversionAction.FirebaseSettingsB\x04\xe2\x41\x01\x03R\x10\x66irebaseSettings\x12\xa4\x01\n\"third_party_app_analytics_settings\x18\x13 \x01(\x0b\x32R.google.ads.googleads.v8.resources.ConversionAction.ThirdPartyAppAnalyticsSettingsB\x04\xe2\x41\x01\x03R\x1ethirdPartyAppAnalyticsSettings\x1a\x9d\x02\n\x18\x41ttributionModelSettings\x12q\n\x11\x61ttribution_model\x18\x01 \x01(\x0e\x32\x44.google.ads.googleads.v8.enums.AttributionModelEnum.AttributionModelR\x10\x61ttributionModel\x12\x8d\x01\n\x18\x64\x61ta_driven_model_status\x18\x02 \x01(\x0e\x32N.google.ads.googleads.v8.enums.DataDrivenModelStatusEnum.DataDrivenModelStatusB\x04\xe2\x41\x01\x03R\x15\x64\x61taDrivenModelStatus\x1a\xf9\x01\n\rValueSettings\x12(\n\rdefault_value\x18\x04 \x01(\x01H\x00R\x0c\x64\x65\x66\x61ultValue\x88\x01\x01\x12\x37\n\x15\x64\x65\x66\x61ult_currency_code\x18\x05 \x01(\tH\x01R\x13\x64\x65\x66\x61ultCurrencyCode\x88\x01\x01\x12<\n\x18\x61lways_use_default_value\x18\x06 \x01(\x08H\x02R\x15\x61lwaysUseDefaultValue\x88\x01\x01\x42\x10\n\x0e_default_valueB\x18\n\x16_default_currency_codeB\x1b\n\x19_always_use_default_value\x1a\x84\x01\n\x10\x46irebaseSettings\x12(\n\nevent_name\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\teventName\x88\x01\x01\x12(\n\nproject_id\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03H\x01R\tprojectId\x88\x01\x01\x42\r\n\x0b_event_nameB\r\n\x0b_project_id\x1a\x84\x01\n\x1eThirdPartyAppAnalyticsSettings\x12(\n\nevent_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\teventName\x88\x01\x01\x12)\n\rprovider_name\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x0cproviderNameB\r\n\x0b_event_name:p\xea\x41m\n)googleads.googleapis.com/ConversionAction\x12@customers/{customer_id}/conversionActions/{conversion_action_id}B\x05\n\x03_idB\x07\n\x05_nameB\x11\n\x0f_owner_customerB \n\x1e_include_in_conversions_metricB%\n#_click_through_lookback_window_daysB$\n\"_view_through_lookback_window_daysB\x1e\n\x1c_phone_call_duration_secondsB\t\n\x07_app_idB\x82\x02\n%com.google.ads.googleads.v8.resourcesB\x15\x43onversionActionProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_CONVERSIONACTION = DESCRIPTOR.message_types_by_name['ConversionAction']
_CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS = _CONVERSIONACTION.nested_types_by_name['AttributionModelSettings']
_CONVERSIONACTION_VALUESETTINGS = _CONVERSIONACTION.nested_types_by_name['ValueSettings']
_CONVERSIONACTION_FIREBASESETTINGS = _CONVERSIONACTION.nested_types_by_name['FirebaseSettings']
_CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS = _CONVERSIONACTION.nested_types_by_name['ThirdPartyAppAnalyticsSettings']
ConversionAction = _reflection.GeneratedProtocolMessageType('ConversionAction', (_message.Message,), {

  'AttributionModelSettings' : _reflection.GeneratedProtocolMessageType('AttributionModelSettings', (_message.Message,), {
    'DESCRIPTOR' : _CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS,
    '__module__' : 'google.ads.googleads.v8.resources.conversion_action_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.ConversionAction.AttributionModelSettings)
    })
  ,

  'ValueSettings' : _reflection.GeneratedProtocolMessageType('ValueSettings', (_message.Message,), {
    'DESCRIPTOR' : _CONVERSIONACTION_VALUESETTINGS,
    '__module__' : 'google.ads.googleads.v8.resources.conversion_action_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.ConversionAction.ValueSettings)
    })
  ,

  'FirebaseSettings' : _reflection.GeneratedProtocolMessageType('FirebaseSettings', (_message.Message,), {
    'DESCRIPTOR' : _CONVERSIONACTION_FIREBASESETTINGS,
    '__module__' : 'google.ads.googleads.v8.resources.conversion_action_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.ConversionAction.FirebaseSettings)
    })
  ,

  'ThirdPartyAppAnalyticsSettings' : _reflection.GeneratedProtocolMessageType('ThirdPartyAppAnalyticsSettings', (_message.Message,), {
    'DESCRIPTOR' : _CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS,
    '__module__' : 'google.ads.googleads.v8.resources.conversion_action_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.ConversionAction.ThirdPartyAppAnalyticsSettings)
    })
  ,
  'DESCRIPTOR' : _CONVERSIONACTION,
  '__module__' : 'google.ads.googleads.v8.resources.conversion_action_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.ConversionAction)
  })
_sym_db.RegisterMessage(ConversionAction)
_sym_db.RegisterMessage(ConversionAction.AttributionModelSettings)
_sym_db.RegisterMessage(ConversionAction.ValueSettings)
_sym_db.RegisterMessage(ConversionAction.FirebaseSettings)
_sym_db.RegisterMessage(ConversionAction.ThirdPartyAppAnalyticsSettings)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\025ConversionActionProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS.fields_by_name['data_driven_model_status']._options = None
  _CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS.fields_by_name['data_driven_model_status']._serialized_options = b'\342A\001\003'
  _CONVERSIONACTION_FIREBASESETTINGS.fields_by_name['event_name']._options = None
  _CONVERSIONACTION_FIREBASESETTINGS.fields_by_name['event_name']._serialized_options = b'\342A\001\003'
  _CONVERSIONACTION_FIREBASESETTINGS.fields_by_name['project_id']._options = None
  _CONVERSIONACTION_FIREBASESETTINGS.fields_by_name['project_id']._serialized_options = b'\342A\001\003'
  _CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS.fields_by_name['event_name']._options = None
  _CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS.fields_by_name['event_name']._serialized_options = b'\342A\001\003'
  _CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS.fields_by_name['provider_name']._options = None
  _CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS.fields_by_name['provider_name']._serialized_options = b'\342A\001\003'
  _CONVERSIONACTION.fields_by_name['resource_name']._options = None
  _CONVERSIONACTION.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A+\n)googleads.googleapis.com/ConversionAction'
  _CONVERSIONACTION.fields_by_name['id']._options = None
  _CONVERSIONACTION.fields_by_name['id']._serialized_options = b'\342A\001\003'
  _CONVERSIONACTION.fields_by_name['type']._options = None
  _CONVERSIONACTION.fields_by_name['type']._serialized_options = b'\342A\001\005'
  _CONVERSIONACTION.fields_by_name['owner_customer']._options = None
  _CONVERSIONACTION.fields_by_name['owner_customer']._serialized_options = b'\342A\001\003\372A#\n!googleads.googleapis.com/Customer'
  _CONVERSIONACTION.fields_by_name['tag_snippets']._options = None
  _CONVERSIONACTION.fields_by_name['tag_snippets']._serialized_options = b'\342A\001\003'
  _CONVERSIONACTION.fields_by_name['mobile_app_vendor']._options = None
  _CONVERSIONACTION.fields_by_name['mobile_app_vendor']._serialized_options = b'\342A\001\003'
  _CONVERSIONACTION.fields_by_name['firebase_settings']._options = None
  _CONVERSIONACTION.fields_by_name['firebase_settings']._serialized_options = b'\342A\001\003'
  _CONVERSIONACTION.fields_by_name['third_party_app_analytics_settings']._options = None
  _CONVERSIONACTION.fields_by_name['third_party_app_analytics_settings']._serialized_options = b'\342A\001\003'
  _CONVERSIONACTION._options = None
  _CONVERSIONACTION._serialized_options = b'\352Am\n)googleads.googleapis.com/ConversionAction\022@customers/{customer_id}/conversionActions/{conversion_action_id}'
  _CONVERSIONACTION._serialized_start=664
  _CONVERSIONACTION._serialized_end=3546
  _CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS._serialized_start=2436
  _CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS._serialized_end=2721
  _CONVERSIONACTION_VALUESETTINGS._serialized_start=2724
  _CONVERSIONACTION_VALUESETTINGS._serialized_end=2973
  _CONVERSIONACTION_FIREBASESETTINGS._serialized_start=2976
  _CONVERSIONACTION_FIREBASESETTINGS._serialized_end=3108
  _CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS._serialized_start=3111
  _CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS._serialized_end=3243
# @@protoc_insertion_point(module_scope)
