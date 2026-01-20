"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....app.v1 import robot_pb2 as app_dot_v1_dot_robot__pb2
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$service/discovery/v1/discovery.proto\x12\x19viam.service.discovery.v1\x1a\x12app/v1/robot.proto\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"]\n\x18DiscoverResourcesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"[\n\x19DiscoverResourcesResponse\x12>\n\x0bdiscoveries\x18\x01 \x03(\x0b2\x1c.viam.app.v1.ComponentConfigR\x0bdiscoveries2\xcf\x02\n\x10DiscoveryService\x12\xad\x01\n\x11DiscoverResources\x123.viam.service.discovery.v1.DiscoverResourcesRequest\x1a4.viam.service.discovery.v1.DiscoverResourcesResponse"-\x82\xd3\xe4\x93\x02\'\x12%/viam/api/v1/service/{name}/discovery\x12\x8a\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/discovery/{name}/do_commandBD\n\x1dcom.viam.service.discovery.v1Z#go.viam.com/api/service/discovey/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.discovery.v1.discovery_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1dcom.viam.service.discovery.v1Z#go.viam.com/api/service/discovey/v1'
    _DISCOVERYSERVICE.methods_by_name['DiscoverResources']._options = None
    _DISCOVERYSERVICE.methods_by_name['DiscoverResources']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/viam/api/v1/service/{name}/discovery"
    _DISCOVERYSERVICE.methods_by_name['DoCommand']._options = None
    _DISCOVERYSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/discovery/{name}/do_command'
    _DISCOVERRESOURCESREQUEST._serialized_start = 171
    _DISCOVERRESOURCESREQUEST._serialized_end = 264
    _DISCOVERRESOURCESRESPONSE._serialized_start = 266
    _DISCOVERRESOURCESRESPONSE._serialized_end = 357
    _DISCOVERYSERVICE._serialized_start = 360
    _DISCOVERYSERVICE._serialized_end = 695