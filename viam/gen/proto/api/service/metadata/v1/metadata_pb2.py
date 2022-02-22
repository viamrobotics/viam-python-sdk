"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,proto/api/service/metadata/v1/metadata.proto\x12\x1dproto.api.service.metadata.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/httpbody.proto"\x12\n\x10ResourcesRequest"\x82\x01\n\x0cResourceName\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12\x1c\n\tnamespace\x18\x02 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x12\x18\n\x07subtype\x18\x04 \x01(\tR\x07subtype\x12\x12\n\x04name\x18\x05 \x01(\tR\x04name"^\n\x11ResourcesResponse\x12I\n\tresources\x18\x01 \x03(\x0b2+.proto.api.service.metadata.v1.ResourceNameR\tresources2\xa4\x01\n\x0fMetadataService\x12\x90\x01\n\tResources\x12/.proto.api.service.metadata.v1.ResourcesRequest\x1a0.proto.api.service.metadata.v1.ResourcesResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/api/v1/service/metadataBI\n!com.viam.rdk.proto.api.service.v1Z$go.viam.com/rdk/proto/api/service/v1b\x06proto3')
_RESOURCESREQUEST = DESCRIPTOR.message_types_by_name['ResourcesRequest']
_RESOURCENAME = DESCRIPTOR.message_types_by_name['ResourceName']
_RESOURCESRESPONSE = DESCRIPTOR.message_types_by_name['ResourcesResponse']
ResourcesRequest = _reflection.GeneratedProtocolMessageType('ResourcesRequest', (_message.Message,), {'DESCRIPTOR': _RESOURCESREQUEST, '__module__': 'proto.api.service.metadata.v1.metadata_pb2'})
_sym_db.RegisterMessage(ResourcesRequest)
ResourceName = _reflection.GeneratedProtocolMessageType('ResourceName', (_message.Message,), {'DESCRIPTOR': _RESOURCENAME, '__module__': 'proto.api.service.metadata.v1.metadata_pb2'})
_sym_db.RegisterMessage(ResourceName)
ResourcesResponse = _reflection.GeneratedProtocolMessageType('ResourcesResponse', (_message.Message,), {'DESCRIPTOR': _RESOURCESRESPONSE, '__module__': 'proto.api.service.metadata.v1.metadata_pb2'})
_sym_db.RegisterMessage(ResourcesResponse)
_METADATASERVICE = DESCRIPTOR.services_by_name['MetadataService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n!com.viam.rdk.proto.api.service.v1Z$go.viam.com/rdk/proto/api/service/v1'
    _METADATASERVICE.methods_by_name['Resources']._options = None
    _METADATASERVICE.methods_by_name['Resources']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/api/v1/service/metadata'
    _RESOURCESREQUEST._serialized_start = 198
    _RESOURCESREQUEST._serialized_end = 216
    _RESOURCENAME._serialized_start = 219
    _RESOURCENAME._serialized_end = 349
    _RESOURCESRESPONSE._serialized_start = 351
    _RESOURCESRESPONSE._serialized_end = 445
    _METADATASERVICE._serialized_start = 448
    _METADATASERVICE._serialized_end = 612