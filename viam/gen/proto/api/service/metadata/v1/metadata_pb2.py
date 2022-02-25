"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,proto/api/service/metadata/v1/metadata.proto\x12\x1dproto.api.service.metadata.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"\x12\n\x10ResourcesRequest"T\n\x11ResourcesResponse\x12?\n\tresources\x18\x01 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\tresources2\xa4\x01\n\x0fMetadataService\x12\x90\x01\n\tResources\x12/.proto.api.service.metadata.v1.ResourcesRequest\x1a0.proto.api.service.metadata.v1.ResourcesResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/api/v1/service/metadataB[\n*com.viam.rdk.proto.api.service.metadata.v1Z-go.viam.com/rdk/proto/api/service/metadata/v1b\x06proto3')
_RESOURCESREQUEST = DESCRIPTOR.message_types_by_name['ResourcesRequest']
_RESOURCESRESPONSE = DESCRIPTOR.message_types_by_name['ResourcesResponse']
ResourcesRequest = _reflection.GeneratedProtocolMessageType('ResourcesRequest', (_message.Message,), {'DESCRIPTOR': _RESOURCESREQUEST, '__module__': 'proto.api.service.metadata.v1.metadata_pb2'})
_sym_db.RegisterMessage(ResourcesRequest)
ResourcesResponse = _reflection.GeneratedProtocolMessageType('ResourcesResponse', (_message.Message,), {'DESCRIPTOR': _RESOURCESRESPONSE, '__module__': 'proto.api.service.metadata.v1.metadata_pb2'})
_sym_db.RegisterMessage(ResourcesResponse)
_METADATASERVICE = DESCRIPTOR.services_by_name['MetadataService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n*com.viam.rdk.proto.api.service.metadata.v1Z-go.viam.com/rdk/proto/api/service/metadata/v1'
    _METADATASERVICE.methods_by_name['Resources']._options = None
    _METADATASERVICE.methods_by_name['Resources']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/api/v1/service/metadata'
    _RESOURCESREQUEST._serialized_start = 143
    _RESOURCESREQUEST._serialized_end = 161
    _RESOURCESRESPONSE._serialized_start = 163
    _RESOURCESRESPONSE._serialized_end = 247
    _METADATASERVICE._serialized_start = 250
    _METADATASERVICE._serialized_end = 414