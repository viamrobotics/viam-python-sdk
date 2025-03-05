"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'app/agent/v1/agent.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18app/agent/v1/agent.proto\x12\x11viam.app.agent.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto"\xe4\x02\n\x18DeviceAgentConfigRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x128\n\thost_info\x18\x02 \x01(\x0b2\x1b.viam.app.agent.v1.HostInfoR\x08hostInfo\x12u\n\x12subsystem_versions\x18\x03 \x03(\x0b2B.viam.app.agent.v1.DeviceAgentConfigRequest.SubsystemVersionsEntryB\x02\x18\x01R\x11subsystemVersions\x12A\n\x0cversion_info\x18\x04 \x01(\x0b2\x1e.viam.app.agent.v1.VersionInfoR\x0bversionInfo\x1aD\n\x16SubsystemVersionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\x8c\x06\n\x19DeviceAgentConfigResponse\x12s\n\x11subsystem_configs\x18\x01 \x03(\x0b2B.viam.app.agent.v1.DeviceAgentConfigResponse.SubsystemConfigsEntryB\x02\x18\x01R\x10subsystemConfigs\x12@\n\x0echeck_interval\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\rcheckInterval\x12I\n\x11agent_update_info\x18\x03 \x01(\x0b2\x1d.viam.app.agent.v1.UpdateInfoR\x0fagentUpdateInfo\x12T\n\x17viam_server_update_info\x18\x04 \x01(\x0b2\x1d.viam.app.agent.v1.UpdateInfoR\x14viamServerUpdateInfo\x12D\n\x11advanced_settings\x18\x05 \x01(\x0b2\x17.google.protobuf.StructR\x10advancedSettings\x12L\n\x15network_configuration\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x14networkConfiguration\x12H\n\x13additional_networks\x18\x07 \x01(\x0b2\x17.google.protobuf.StructR\x12additionalNetworks\x12J\n\x14system_configuration\x18\x08 \x01(\x0b2\x17.google.protobuf.StructR\x13systemConfiguration\x1am\n\x15SubsystemConfigsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12>\n\x05value\x18\x02 \x01(\x0b2(.viam.app.agent.v1.DeviceSubsystemConfigR\x05value:\x028\x01"\xd3\x01\n\x15DeviceSubsystemConfig\x12>\n\x0bupdate_info\x18\x01 \x01(\x0b2\x1d.viam.app.agent.v1.UpdateInfoR\nupdateInfo\x12\x18\n\x07disable\x18\x02 \x01(\x08R\x07disable\x12#\n\rforce_restart\x18\x03 \x01(\x08R\x0cforceRestart\x127\n\nattributes\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\nattributes:\x02\x18\x01"\xbf\x01\n\x0bVersionInfo\x12#\n\ragent_running\x18\x01 \x01(\tR\x0cagentRunning\x12\'\n\x0fagent_installed\x18\x02 \x01(\tR\x0eagentInstalled\x12.\n\x13viam_server_running\x18\x03 \x01(\tR\x11viamServerRunning\x122\n\x15viam_server_installed\x18\x04 \x01(\tR\x13viamServerInstalled"R\n\x08HostInfo\x12\x1a\n\x08platform\x18\x01 \x01(\tR\x08platform\x12\x16\n\x06distro\x18\x02 \x01(\tR\x06distro\x12\x12\n\x04tags\x18\x03 \x03(\tR\x04tags"\xa6\x01\n\nUpdateInfo\x12\x1a\n\x08filename\x18\x01 \x01(\tR\x08filename\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\x12\x16\n\x06sha256\x18\x04 \x01(\x0cR\x06sha256\x128\n\x06format\x18\x05 \x01(\x0e2 .viam.app.agent.v1.PackageFormatR\x06format*\x9f\x01\n\rPackageFormat\x12\x1e\n\x1aPACKAGE_FORMAT_UNSPECIFIED\x10\x00\x12\x16\n\x12PACKAGE_FORMAT_RAW\x10\x01\x12\x15\n\x11PACKAGE_FORMAT_XZ\x10\x02\x12\x1d\n\x19PACKAGE_FORMAT_EXECUTABLE\x10\x03\x12 \n\x1cPACKAGE_FORMAT_XZ_EXECUTABLE\x10\x042\x84\x01\n\x12AgentDeviceService\x12n\n\x11DeviceAgentConfig\x12+.viam.app.agent.v1.DeviceAgentConfigRequest\x1a,.viam.app.agent.v1.DeviceAgentConfigResponseB\x1eZ\x1cgo.viam.com/api/app/agent/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.agent.v1.agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1cgo.viam.com/api/app/agent/v1'
    _globals['_DEVICEAGENTCONFIGREQUEST_SUBSYSTEMVERSIONSENTRY']._loaded_options = None
    _globals['_DEVICEAGENTCONFIGREQUEST_SUBSYSTEMVERSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_DEVICEAGENTCONFIGREQUEST'].fields_by_name['subsystem_versions']._loaded_options = None
    _globals['_DEVICEAGENTCONFIGREQUEST'].fields_by_name['subsystem_versions']._serialized_options = b'\x18\x01'
    _globals['_DEVICEAGENTCONFIGRESPONSE_SUBSYSTEMCONFIGSENTRY']._loaded_options = None
    _globals['_DEVICEAGENTCONFIGRESPONSE_SUBSYSTEMCONFIGSENTRY']._serialized_options = b'8\x01'
    _globals['_DEVICEAGENTCONFIGRESPONSE'].fields_by_name['subsystem_configs']._loaded_options = None
    _globals['_DEVICEAGENTCONFIGRESPONSE'].fields_by_name['subsystem_configs']._serialized_options = b'\x18\x01'
    _globals['_DEVICESUBSYSTEMCONFIG']._loaded_options = None
    _globals['_DEVICESUBSYSTEMCONFIG']._serialized_options = b'\x18\x01'
    _globals['_PACKAGEFORMAT']._serialized_start = 1913
    _globals['_PACKAGEFORMAT']._serialized_end = 2072
    _globals['_DEVICEAGENTCONFIGREQUEST']._serialized_start = 110
    _globals['_DEVICEAGENTCONFIGREQUEST']._serialized_end = 466
    _globals['_DEVICEAGENTCONFIGREQUEST_SUBSYSTEMVERSIONSENTRY']._serialized_start = 398
    _globals['_DEVICEAGENTCONFIGREQUEST_SUBSYSTEMVERSIONSENTRY']._serialized_end = 466
    _globals['_DEVICEAGENTCONFIGRESPONSE']._serialized_start = 469
    _globals['_DEVICEAGENTCONFIGRESPONSE']._serialized_end = 1249
    _globals['_DEVICEAGENTCONFIGRESPONSE_SUBSYSTEMCONFIGSENTRY']._serialized_start = 1140
    _globals['_DEVICEAGENTCONFIGRESPONSE_SUBSYSTEMCONFIGSENTRY']._serialized_end = 1249
    _globals['_DEVICESUBSYSTEMCONFIG']._serialized_start = 1252
    _globals['_DEVICESUBSYSTEMCONFIG']._serialized_end = 1463
    _globals['_VERSIONINFO']._serialized_start = 1466
    _globals['_VERSIONINFO']._serialized_end = 1657
    _globals['_HOSTINFO']._serialized_start = 1659
    _globals['_HOSTINFO']._serialized_end = 1741
    _globals['_UPDATEINFO']._serialized_start = 1744
    _globals['_UPDATEINFO']._serialized_end = 1910
    _globals['_AGENTDEVICESERVICE']._serialized_start = 2075
    _globals['_AGENTDEVICESERVICE']._serialized_end = 2207