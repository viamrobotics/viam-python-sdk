"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/rpc/error_details.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egoogle/rpc/error_details.proto\x12\ngoogle.rpc\x1a\x1egoogle/protobuf/duration.proto"\xb9\x01\n\tErrorInfo\x12\x16\n\x06reason\x18\x01 \x01(\tR\x06reason\x12\x16\n\x06domain\x18\x02 \x01(\tR\x06domain\x12?\n\x08metadata\x18\x03 \x03(\x0b2#.google.rpc.ErrorInfo.MetadataEntryR\x08metadata\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"G\n\tRetryInfo\x12:\n\x0bretry_delay\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationR\nretryDelay"H\n\tDebugInfo\x12#\n\rstack_entries\x18\x01 \x03(\tR\x0cstackEntries\x12\x16\n\x06detail\x18\x02 \x01(\tR\x06detail"\x8e\x04\n\x0cQuotaFailure\x12B\n\nviolations\x18\x01 \x03(\x0b2".google.rpc.QuotaFailure.ViolationR\nviolations\x1a\xb9\x03\n\tViolation\x12\x18\n\x07subject\x18\x01 \x01(\tR\x07subject\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12\x1f\n\x0bapi_service\x18\x03 \x01(\tR\napiService\x12!\n\x0cquota_metric\x18\x04 \x01(\tR\x0bquotaMetric\x12\x19\n\x08quota_id\x18\x05 \x01(\tR\x07quotaId\x12b\n\x10quota_dimensions\x18\x06 \x03(\x0b27.google.rpc.QuotaFailure.Violation.QuotaDimensionsEntryR\x0fquotaDimensions\x12\x1f\n\x0bquota_value\x18\x07 \x01(\x03R\nquotaValue\x121\n\x12future_quota_value\x18\x08 \x01(\x03H\x00R\x10futureQuotaValue\x88\x01\x01\x1aB\n\x14QuotaDimensionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01B\x15\n\x13_future_quota_value"\xbd\x01\n\x13PreconditionFailure\x12I\n\nviolations\x18\x01 \x03(\x0b2).google.rpc.PreconditionFailure.ViolationR\nviolations\x1a[\n\tViolation\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x18\n\x07subject\x18\x02 \x01(\tR\x07subject\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription"\x8c\x02\n\nBadRequest\x12P\n\x10field_violations\x18\x01 \x03(\x0b2%.google.rpc.BadRequest.FieldViolationR\x0ffieldViolations\x1a\xab\x01\n\x0eFieldViolation\x12\x14\n\x05field\x18\x01 \x01(\tR\x05field\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12\x16\n\x06reason\x18\x03 \x01(\tR\x06reason\x12I\n\x11localized_message\x18\x04 \x01(\x0b2\x1c.google.rpc.LocalizedMessageR\x10localizedMessage"O\n\x0bRequestInfo\x12\x1d\n\nrequest_id\x18\x01 \x01(\tR\trequestId\x12!\n\x0cserving_data\x18\x02 \x01(\tR\x0bservingData"\x90\x01\n\x0cResourceInfo\x12#\n\rresource_type\x18\x01 \x01(\tR\x0cresourceType\x12#\n\rresource_name\x18\x02 \x01(\tR\x0cresourceName\x12\x14\n\x05owner\x18\x03 \x01(\tR\x05owner\x12 \n\x0bdescription\x18\x04 \x01(\tR\x0bdescription"o\n\x04Help\x12+\n\x05links\x18\x01 \x03(\x0b2\x15.google.rpc.Help.LinkR\x05links\x1a:\n\x04Link\x12 \n\x0bdescription\x18\x01 \x01(\tR\x0bdescription\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url"D\n\x10LocalizedMessage\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\x12\x18\n\x07message\x18\x02 \x01(\tR\x07messageBl\n\x0ecom.google.rpcB\x11ErrorDetailsProtoP\x01Z?google.golang.org/genproto/googleapis/rpc/errdetails;errdetails\xa2\x02\x03RPCb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.rpc.error_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.rpcB\x11ErrorDetailsProtoP\x01Z?google.golang.org/genproto/googleapis/rpc/errdetails;errdetails\xa2\x02\x03RPC'
    _globals['_ERRORINFO_METADATAENTRY']._loaded_options = None
    _globals['_ERRORINFO_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_QUOTAFAILURE_VIOLATION_QUOTADIMENSIONSENTRY']._loaded_options = None
    _globals['_QUOTAFAILURE_VIOLATION_QUOTADIMENSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_ERRORINFO']._serialized_start = 79
    _globals['_ERRORINFO']._serialized_end = 264
    _globals['_ERRORINFO_METADATAENTRY']._serialized_start = 205
    _globals['_ERRORINFO_METADATAENTRY']._serialized_end = 264
    _globals['_RETRYINFO']._serialized_start = 266
    _globals['_RETRYINFO']._serialized_end = 337
    _globals['_DEBUGINFO']._serialized_start = 339
    _globals['_DEBUGINFO']._serialized_end = 411
    _globals['_QUOTAFAILURE']._serialized_start = 414
    _globals['_QUOTAFAILURE']._serialized_end = 940
    _globals['_QUOTAFAILURE_VIOLATION']._serialized_start = 499
    _globals['_QUOTAFAILURE_VIOLATION']._serialized_end = 940
    _globals['_QUOTAFAILURE_VIOLATION_QUOTADIMENSIONSENTRY']._serialized_start = 851
    _globals['_QUOTAFAILURE_VIOLATION_QUOTADIMENSIONSENTRY']._serialized_end = 917
    _globals['_PRECONDITIONFAILURE']._serialized_start = 943
    _globals['_PRECONDITIONFAILURE']._serialized_end = 1132
    _globals['_PRECONDITIONFAILURE_VIOLATION']._serialized_start = 1041
    _globals['_PRECONDITIONFAILURE_VIOLATION']._serialized_end = 1132
    _globals['_BADREQUEST']._serialized_start = 1135
    _globals['_BADREQUEST']._serialized_end = 1403
    _globals['_BADREQUEST_FIELDVIOLATION']._serialized_start = 1232
    _globals['_BADREQUEST_FIELDVIOLATION']._serialized_end = 1403
    _globals['_REQUESTINFO']._serialized_start = 1405
    _globals['_REQUESTINFO']._serialized_end = 1484
    _globals['_RESOURCEINFO']._serialized_start = 1487
    _globals['_RESOURCEINFO']._serialized_end = 1631
    _globals['_HELP']._serialized_start = 1633
    _globals['_HELP']._serialized_end = 1744
    _globals['_HELP_LINK']._serialized_start = 1686
    _globals['_HELP_LINK']._serialized_end = 1744
    _globals['_LOCALIZEDMESSAGE']._serialized_start = 1746
    _globals['_LOCALIZEDMESSAGE']._serialized_end = 1814