# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/errors/feed_item_validation_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v8/errors/feed_item_validation_error.proto\x12\x1egoogle.ads.googleads.v8.errors\x1a\x1cgoogle/api/annotations.proto\"\xee\x1b\n\x1b\x46\x65\x65\x64ItemValidationErrorEnum\"\xce\x1b\n\x17\x46\x65\x65\x64ItemValidationError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x14\n\x10STRING_TOO_SHORT\x10\x02\x12\x13\n\x0fSTRING_TOO_LONG\x10\x03\x12\x17\n\x13VALUE_NOT_SPECIFIED\x10\x04\x12(\n$INVALID_DOMESTIC_PHONE_NUMBER_FORMAT\x10\x05\x12\x18\n\x14INVALID_PHONE_NUMBER\x10\x06\x12*\n&PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY\x10\x07\x12#\n\x1fPREMIUM_RATE_NUMBER_NOT_ALLOWED\x10\x08\x12\x1a\n\x16\x44ISALLOWED_NUMBER_TYPE\x10\t\x12\x16\n\x12VALUE_OUT_OF_RANGE\x10\n\x12*\n&CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY\x10\x0b\x12.\n*CUSTOMER_NOT_IN_ALLOWLIST_FOR_CALLTRACKING\x10\x63\x12\x18\n\x14INVALID_COUNTRY_CODE\x10\r\x12\x12\n\x0eINVALID_APP_ID\x10\x0e\x12!\n\x1dMISSING_ATTRIBUTES_FOR_FIELDS\x10\x0f\x12\x13\n\x0fINVALID_TYPE_ID\x10\x10\x12\x19\n\x15INVALID_EMAIL_ADDRESS\x10\x11\x12\x15\n\x11INVALID_HTTPS_URL\x10\x12\x12\x1c\n\x18MISSING_DELIVERY_ADDRESS\x10\x13\x12\x1d\n\x19START_DATE_AFTER_END_DATE\x10\x14\x12 \n\x1cMISSING_FEED_ITEM_START_TIME\x10\x15\x12\x1e\n\x1aMISSING_FEED_ITEM_END_TIME\x10\x16\x12\x18\n\x14MISSING_FEED_ITEM_ID\x10\x17\x12#\n\x1fVANITY_PHONE_NUMBER_NOT_ALLOWED\x10\x18\x12$\n INVALID_REVIEW_EXTENSION_SNIPPET\x10\x19\x12\x19\n\x15INVALID_NUMBER_FORMAT\x10\x1a\x12\x17\n\x13INVALID_DATE_FORMAT\x10\x1b\x12\x18\n\x14INVALID_PRICE_FORMAT\x10\x1c\x12\x1d\n\x19UNKNOWN_PLACEHOLDER_FIELD\x10\x1d\x12.\n*MISSING_ENHANCED_SITELINK_DESCRIPTION_LINE\x10\x1e\x12&\n\"REVIEW_EXTENSION_SOURCE_INELIGIBLE\x10\x1f\x12\'\n#HYPHENS_IN_REVIEW_EXTENSION_SNIPPET\x10 \x12-\n)DOUBLE_QUOTES_IN_REVIEW_EXTENSION_SNIPPET\x10!\x12&\n\"QUOTES_IN_REVIEW_EXTENSION_SNIPPET\x10\"\x12\x1f\n\x1bINVALID_FORM_ENCODED_PARAMS\x10#\x12\x1e\n\x1aINVALID_URL_PARAMETER_NAME\x10$\x12\x17\n\x13NO_GEOCODING_RESULT\x10%\x12(\n$SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT\x10&\x12-\n)CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED\x10\'\x12 \n\x1cINVALID_PLACEHOLDER_FIELD_ID\x10(\x12\x13\n\x0fINVALID_URL_TAG\x10)\x12\x11\n\rLIST_TOO_LONG\x10*\x12\"\n\x1eINVALID_ATTRIBUTES_COMBINATION\x10+\x12\x14\n\x10\x44UPLICATE_VALUES\x10,\x12%\n!INVALID_CALL_CONVERSION_ACTION_ID\x10-\x12!\n\x1d\x43\x41NNOT_SET_WITHOUT_FINAL_URLS\x10.\x12$\n APP_ID_DOESNT_EXIST_IN_APP_STORE\x10/\x12\x15\n\x11INVALID_FINAL_URL\x10\x30\x12\x18\n\x14INVALID_TRACKING_URL\x10\x31\x12*\n&INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL\x10\x32\x12\x12\n\x0eLIST_TOO_SHORT\x10\x33\x12\x17\n\x13INVALID_USER_ACTION\x10\x34\x12\x15\n\x11INVALID_TYPE_NAME\x10\x35\x12\x1f\n\x1bINVALID_EVENT_CHANGE_STATUS\x10\x36\x12\x1b\n\x17INVALID_SNIPPETS_HEADER\x10\x37\x12\x1c\n\x18INVALID_ANDROID_APP_LINK\x10\x38\x12;\n7NUMBER_TYPE_WITH_CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY\x10\x39\x12\x1a\n\x16RESERVED_KEYWORD_OTHER\x10:\x12\x1b\n\x17\x44UPLICATE_OPTION_LABELS\x10;\x12\x1d\n\x19\x44UPLICATE_OPTION_PREFILLS\x10<\x12\x18\n\x14UNEQUAL_LIST_LENGTHS\x10=\x12\x1f\n\x1bINCONSISTENT_CURRENCY_CODES\x10>\x12*\n&PRICE_EXTENSION_HAS_DUPLICATED_HEADERS\x10?\x12.\n*ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION\x10@\x12%\n!PRICE_EXTENSION_HAS_TOO_FEW_ITEMS\x10\x41\x12\x15\n\x11UNSUPPORTED_VALUE\x10\x42\x12\x1c\n\x18INVALID_FINAL_MOBILE_URL\x10\x43\x12%\n!INVALID_KEYWORDLESS_AD_RULE_LABEL\x10\x44\x12\'\n#VALUE_TRACK_PARAMETER_NOT_SUPPORTED\x10\x45\x12*\n&UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE\x10\x46\x12\x18\n\x14INVALID_IOS_APP_LINK\x10G\x12,\n(MISSING_IOS_APP_LINK_OR_IOS_APP_STORE_ID\x10H\x12\x1a\n\x16PROMOTION_INVALID_TIME\x10I\x12\x39\n5PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF\x10J\x12>\n:PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT\x10K\x12%\n!TOO_MANY_DECIMAL_PLACES_SPECIFIED\x10L\x12\x1e\n\x1a\x41\x44_CUSTOMIZERS_NOT_ALLOWED\x10M\x12\x19\n\x15INVALID_LANGUAGE_CODE\x10N\x12\x18\n\x14UNSUPPORTED_LANGUAGE\x10O\x12\x1b\n\x17IF_FUNCTION_NOT_ALLOWED\x10P\x12\x1c\n\x18INVALID_FINAL_URL_SUFFIX\x10Q\x12#\n\x1fINVALID_TAG_IN_FINAL_URL_SUFFIX\x10R\x12#\n\x1fINVALID_FINAL_URL_SUFFIX_FORMAT\x10S\x12\x30\n,CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED\x10T\x12\'\n#ONLY_ONE_DELIVERY_OPTION_IS_ALLOWED\x10U\x12\x1d\n\x19NO_DELIVERY_OPTION_IS_SET\x10V\x12&\n\"INVALID_CONVERSION_REPORTING_STATE\x10W\x12\x14\n\x10IMAGE_SIZE_WRONG\x10X\x12+\n\'EMAIL_DELIVERY_NOT_AVAILABLE_IN_COUNTRY\x10Y\x12\'\n#AUTO_REPLY_NOT_AVAILABLE_IN_COUNTRY\x10Z\x12\x1a\n\x16INVALID_LATITUDE_VALUE\x10[\x12\x1b\n\x17INVALID_LONGITUDE_VALUE\x10\\\x12\x13\n\x0fTOO_MANY_LABELS\x10]\x12\x15\n\x11INVALID_IMAGE_URL\x10^\x12\x1a\n\x16MISSING_LATITUDE_VALUE\x10_\x12\x1b\n\x17MISSING_LONGITUDE_VALUE\x10`\x12\x15\n\x11\x41\x44\x44RESS_NOT_FOUND\x10\x61\x12\x1a\n\x16\x41\x44\x44RESS_NOT_TARGETABLE\x10\x62\x12\x14\n\x10INVALID_ASSET_ID\x10\x64\x12\x1b\n\x17INCOMPATIBLE_ASSET_TYPE\x10\x65\x12\x1f\n\x1bIMAGE_ERROR_UNEXPECTED_SIZE\x10\x66\x12(\n$IMAGE_ERROR_ASPECT_RATIO_NOT_ALLOWED\x10g\x12\x1e\n\x1aIMAGE_ERROR_FILE_TOO_LARGE\x10h\x12\"\n\x1eIMAGE_ERROR_FORMAT_NOT_ALLOWED\x10i\x12$\n IMAGE_ERROR_CONSTRAINTS_VIOLATED\x10j\x12\x1c\n\x18IMAGE_ERROR_SERVER_ERROR\x10kB\xf7\x01\n\"com.google.ads.googleads.v8.errorsB\x1c\x46\x65\x65\x64ItemValidationErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V8.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V8\\Errors\xea\x02\"Google::Ads::GoogleAds::V8::Errorsb\x06proto3')



_FEEDITEMVALIDATIONERRORENUM = DESCRIPTOR.message_types_by_name['FeedItemValidationErrorEnum']
_FEEDITEMVALIDATIONERRORENUM_FEEDITEMVALIDATIONERROR = _FEEDITEMVALIDATIONERRORENUM.enum_types_by_name['FeedItemValidationError']
FeedItemValidationErrorEnum = _reflection.GeneratedProtocolMessageType('FeedItemValidationErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _FEEDITEMVALIDATIONERRORENUM,
  '__module__' : 'google.ads.googleads.v8.errors.feed_item_validation_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.errors.FeedItemValidationErrorEnum)
  })
_sym_db.RegisterMessage(FeedItemValidationErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v8.errorsB\034FeedItemValidationErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V8.Errors\312\002\036Google\\Ads\\GoogleAds\\V8\\Errors\352\002\"Google::Ads::GoogleAds::V8::Errors'
  _FEEDITEMVALIDATIONERRORENUM._serialized_start=130
  _FEEDITEMVALIDATIONERRORENUM._serialized_end=3696
  _FEEDITEMVALIDATIONERRORENUM_FEEDITEMVALIDATIONERROR._serialized_start=162
  _FEEDITEMVALIDATIONERRORENUM_FEEDITEMVALIDATIONERROR._serialized_end=3696
# @@protoc_insertion_point(module_scope)
