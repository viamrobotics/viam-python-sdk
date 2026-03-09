"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/rpc/context/attribute_context.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/rpc/context/attribute_context.proto\x12\x12google.rpc.context\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x81\x14\n\x10AttributeContext\x12A\n\x06origin\x18\x07 \x01(\x0b2).google.rpc.context.AttributeContext.PeerR\x06origin\x12A\n\x06source\x18\x01 \x01(\x0b2).google.rpc.context.AttributeContext.PeerR\x06source\x12K\n\x0bdestination\x18\x02 \x01(\x0b2).google.rpc.context.AttributeContext.PeerR\x0bdestination\x12F\n\x07request\x18\x03 \x01(\x0b2,.google.rpc.context.AttributeContext.RequestR\x07request\x12I\n\x08response\x18\x04 \x01(\x0b2-.google.rpc.context.AttributeContext.ResponseR\x08response\x12I\n\x08resource\x18\x05 \x01(\x0b2-.google.rpc.context.AttributeContext.ResourceR\x08resource\x12:\n\x03api\x18\x06 \x01(\x0b2(.google.rpc.context.AttributeContext.ApiR\x03api\x124\n\nextensions\x18\x08 \x03(\x0b2\x14.google.protobuf.AnyR\nextensions\x1a\xf3\x01\n\x04Peer\x12\x0e\n\x02ip\x18\x01 \x01(\tR\x02ip\x12\x12\n\x04port\x18\x02 \x01(\x03R\x04port\x12M\n\x06labels\x18\x06 \x03(\x0b25.google.rpc.context.AttributeContext.Peer.LabelsEntryR\x06labels\x12\x1c\n\tprincipal\x18\x07 \x01(\tR\tprincipal\x12\x1f\n\x0bregion_code\x18\x08 \x01(\tR\nregionCode\x1a9\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01\x1as\n\x03Api\x12\x18\n\x07service\x18\x01 \x01(\tR\x07service\x12\x1c\n\toperation\x18\x02 \x01(\tR\toperation\x12\x1a\n\x08protocol\x18\x03 \x01(\tR\x08protocol\x12\x18\n\x07version\x18\x04 \x01(\tR\x07version\x1a\xb6\x01\n\x04Auth\x12\x1c\n\tprincipal\x18\x01 \x01(\tR\tprincipal\x12\x1c\n\taudiences\x18\x02 \x03(\tR\taudiences\x12\x1c\n\tpresenter\x18\x03 \x01(\tR\tpresenter\x12/\n\x06claims\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\x06claims\x12#\n\raccess_levels\x18\x05 \x03(\tR\x0caccessLevels\x1a\xcf\x03\n\x07Request\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06method\x18\x02 \x01(\tR\x06method\x12S\n\x07headers\x18\x03 \x03(\x0b29.google.rpc.context.AttributeContext.Request.HeadersEntryR\x07headers\x12\x12\n\x04path\x18\x04 \x01(\tR\x04path\x12\x12\n\x04host\x18\x05 \x01(\tR\x04host\x12\x16\n\x06scheme\x18\x06 \x01(\tR\x06scheme\x12\x14\n\x05query\x18\x07 \x01(\tR\x05query\x12.\n\x04time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\x04time\x12\x12\n\x04size\x18\n \x01(\x03R\x04size\x12\x1a\n\x08protocol\x18\x0b \x01(\tR\x08protocol\x12\x16\n\x06reason\x18\x0c \x01(\tR\x06reason\x12=\n\x04auth\x18\r \x01(\x0b2).google.rpc.context.AttributeContext.AuthR\x04auth\x1a:\n\x0cHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01\x1a\xb8\x02\n\x08Response\x12\x12\n\x04code\x18\x01 \x01(\x03R\x04code\x12\x12\n\x04size\x18\x02 \x01(\x03R\x04size\x12T\n\x07headers\x18\x03 \x03(\x0b2:.google.rpc.context.AttributeContext.Response.HeadersEntryR\x07headers\x12.\n\x04time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x04time\x12B\n\x0fbackend_latency\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationR\x0ebackendLatency\x1a:\n\x0cHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01\x1a\x98\x05\n\x08Resource\x12\x18\n\x07service\x18\x01 \x01(\tR\x07service\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x12Q\n\x06labels\x18\x04 \x03(\x0b29.google.rpc.context.AttributeContext.Resource.LabelsEntryR\x06labels\x12\x10\n\x03uid\x18\x05 \x01(\tR\x03uid\x12`\n\x0bannotations\x18\x06 \x03(\x0b2>.google.rpc.context.AttributeContext.Resource.AnnotationsEntryR\x0bannotations\x12!\n\x0cdisplay_name\x18\x07 \x01(\tR\x0bdisplayName\x12;\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\nupdateTime\x12;\n\x0bdelete_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampR\ndeleteTime\x12\x12\n\x04etag\x18\x0b \x01(\tR\x04etag\x12\x1a\n\x08location\x18\x0c \x01(\tR\x08location\x1a9\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01\x1a>\n\x10AnnotationsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01B\x8b\x01\n\x16com.google.rpc.contextB\x15AttributeContextProtoP\x01ZUgoogle.golang.org/genproto/googleapis/rpc/context/attribute_context;attribute_context\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.rpc.context.attribute_context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.rpc.contextB\x15AttributeContextProtoP\x01ZUgoogle.golang.org/genproto/googleapis/rpc/context/attribute_context;attribute_context\xf8\x01\x01'
    _globals['_ATTRIBUTECONTEXT_PEER_LABELSENTRY']._loaded_options = None
    _globals['_ATTRIBUTECONTEXT_PEER_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ATTRIBUTECONTEXT_REQUEST_HEADERSENTRY']._loaded_options = None
    _globals['_ATTRIBUTECONTEXT_REQUEST_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_ATTRIBUTECONTEXT_RESPONSE_HEADERSENTRY']._loaded_options = None
    _globals['_ATTRIBUTECONTEXT_RESPONSE_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_ATTRIBUTECONTEXT_RESOURCE_LABELSENTRY']._loaded_options = None
    _globals['_ATTRIBUTECONTEXT_RESOURCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ATTRIBUTECONTEXT_RESOURCE_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_ATTRIBUTECONTEXT_RESOURCE_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_ATTRIBUTECONTEXT']._serialized_start = 189
    _globals['_ATTRIBUTECONTEXT']._serialized_end = 2750
    _globals['_ATTRIBUTECONTEXT_PEER']._serialized_start = 757
    _globals['_ATTRIBUTECONTEXT_PEER']._serialized_end = 1000
    _globals['_ATTRIBUTECONTEXT_PEER_LABELSENTRY']._serialized_start = 943
    _globals['_ATTRIBUTECONTEXT_PEER_LABELSENTRY']._serialized_end = 1000
    _globals['_ATTRIBUTECONTEXT_API']._serialized_start = 1002
    _globals['_ATTRIBUTECONTEXT_API']._serialized_end = 1117
    _globals['_ATTRIBUTECONTEXT_AUTH']._serialized_start = 1120
    _globals['_ATTRIBUTECONTEXT_AUTH']._serialized_end = 1302
    _globals['_ATTRIBUTECONTEXT_REQUEST']._serialized_start = 1305
    _globals['_ATTRIBUTECONTEXT_REQUEST']._serialized_end = 1768
    _globals['_ATTRIBUTECONTEXT_REQUEST_HEADERSENTRY']._serialized_start = 1710
    _globals['_ATTRIBUTECONTEXT_REQUEST_HEADERSENTRY']._serialized_end = 1768
    _globals['_ATTRIBUTECONTEXT_RESPONSE']._serialized_start = 1771
    _globals['_ATTRIBUTECONTEXT_RESPONSE']._serialized_end = 2083
    _globals['_ATTRIBUTECONTEXT_RESPONSE_HEADERSENTRY']._serialized_start = 1710
    _globals['_ATTRIBUTECONTEXT_RESPONSE_HEADERSENTRY']._serialized_end = 1768
    _globals['_ATTRIBUTECONTEXT_RESOURCE']._serialized_start = 2086
    _globals['_ATTRIBUTECONTEXT_RESOURCE']._serialized_end = 2750
    _globals['_ATTRIBUTECONTEXT_RESOURCE_LABELSENTRY']._serialized_start = 943
    _globals['_ATTRIBUTECONTEXT_RESOURCE_LABELSENTRY']._serialized_end = 1000
    _globals['_ATTRIBUTECONTEXT_RESOURCE_ANNOTATIONSENTRY']._serialized_start = 2688
    _globals['_ATTRIBUTECONTEXT_RESOURCE_ANNOTATIONSENTRY']._serialized_end = 2750