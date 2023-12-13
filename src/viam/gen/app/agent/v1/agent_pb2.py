"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....tagger.v1 import tagger_pb2 as tagger_dot_v1_dot_tagger__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18app/agent/v1/agent.proto\x12\x11viam.app.agent.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x16tagger/v1/tagger.proto"\'\n\x15GetAgentConfigRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"^\n\x16GetAgentConfigResponse\x12D\n\x0cagent_config\x18\x01 \x01(\x0b2!.viam.app.agent.v1.AppAgentConfigR\x0bagentConfig"p\n\x18UpdateAgentConfigRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12D\n\x0cagent_config\x18\x02 \x01(\x0b2!.viam.app.agent.v1.AppAgentConfigR\x0bagentConfig"a\n\x19UpdateAgentConfigResponse\x12D\n\x0cagent_config\x18\x01 \x01(\x0b2!.viam.app.agent.v1.AppAgentConfigR\x0bagentConfig"\x9b\x02\n\x0eAppAgentConfig\x12\x9c\x01\n\x11subsystem_configs\x18\x01 \x03(\x0b27.viam.app.agent.v1.AppAgentConfig.SubsystemConfigsEntryB6\x9a\x84\x9e\x031bson:"subsystem_configs" json:"subsystem_configs"R\x10subsystemConfigs\x1aj\n\x15SubsystemConfigsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12;\n\x05value\x18\x02 \x01(\x0b2%.viam.app.agent.v1.AppSubsystemConfigR\x05value:\x028\x01"\xe0\x02\n\x12AppSubsystemConfig\x12[\n\x0frelease_channel\x18\x01 \x01(\tB2\x9a\x84\x9e\x03-bson:"release_channel" json:"release_channel"R\x0ereleaseChannel\x12K\n\x0bpin_version\x18\x02 \x01(\tB*\x9a\x84\x9e\x03%bson:"pin_version" json:"pin_version"R\npinVersion\x12;\n\x07pin_url\x18\x03 \x01(\tB"\x9a\x84\x9e\x03\x1dbson:"pin_url" json:"pin_url"R\x06pinUrl\x12c\n\x11disable_subsystem\x18\x04 \x01(\x08B6\x9a\x84\x9e\x031bson:"disable_subsystem" json:"disable_subsystem"R\x10disableSubsystem"\x9d\x02\n\x18DeviceAgentConfigRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x128\n\thost_info\x18\x02 \x01(\x0b2\x1b.viam.app.agent.v1.HostInfoR\x08hostInfo\x12q\n\x12subsystem_versions\x18\x03 \x03(\x0b2B.viam.app.agent.v1.DeviceAgentConfigRequest.SubsystemVersionsEntryR\x11subsystemVersions\x1aD\n\x16SubsystemVersionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\xbd\x02\n\x19DeviceAgentConfigResponse\x12o\n\x11subsystem_configs\x18\x01 \x03(\x0b2B.viam.app.agent.v1.DeviceAgentConfigResponse.SubsystemConfigsEntryR\x10subsystemConfigs\x12@\n\x0echeck_interval\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\rcheckInterval\x1am\n\x15SubsystemConfigsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12>\n\x05value\x18\x02 \x01(\x0b2(.viam.app.agent.v1.DeviceSubsystemConfigR\x05value:\x028\x01"\x9f\x01\n\x15DeviceSubsystemConfig\x12G\n\x0bupdate_info\x18\x01 \x01(\x0b2&.viam.app.agent.v1.SubsystemUpdateInfoR\nupdateInfo\x12\x18\n\x07disable\x18\x02 \x01(\x08R\x07disable\x12#\n\rforce_restart\x18\x03 \x01(\x08R\x0cforceRestart"R\n\x08HostInfo\x12\x1a\n\x08platform\x18\x01 \x01(\tR\x08platform\x12\x16\n\x06distro\x18\x02 \x01(\tR\x06distro\x12\x12\n\x04tags\x18\x03 \x03(\tR\x04tags"\xaf\x01\n\x13SubsystemUpdateInfo\x12\x1a\n\x08filename\x18\x01 \x01(\tR\x08filename\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\x12\x16\n\x06sha256\x18\x04 \x01(\x0cR\x06sha256\x128\n\x06format\x18\x05 \x01(\x0e2 .viam.app.agent.v1.PackageFormatR\x06format*\x9f\x01\n\rPackageFormat\x12\x1e\n\x1aPACKAGE_FORMAT_UNSPECIFIED\x10\x00\x12\x16\n\x12PACKAGE_FORMAT_RAW\x10\x01\x12\x15\n\x11PACKAGE_FORMAT_XZ\x10\x02\x12\x1d\n\x19PACKAGE_FORMAT_EXECUTABLE\x10\x03\x12 \n\x1cPACKAGE_FORMAT_XZ_EXECUTABLE\x10\x042\xe8\x01\n\x0fAgentAppService\x12e\n\x0eGetAgentConfig\x12(.viam.app.agent.v1.GetAgentConfigRequest\x1a).viam.app.agent.v1.GetAgentConfigResponse\x12n\n\x11UpdateAgentConfig\x12+.viam.app.agent.v1.UpdateAgentConfigRequest\x1a,.viam.app.agent.v1.UpdateAgentConfigResponse2\x84\x01\n\x12AgentDeviceService\x12n\n\x11DeviceAgentConfig\x12+.viam.app.agent.v1.DeviceAgentConfigRequest\x1a,.viam.app.agent.v1.DeviceAgentConfigResponseB\x1eZ\x1cgo.viam.com/api/app/agent/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.agent.v1.agent_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1cgo.viam.com/api/app/agent/v1'
    _APPAGENTCONFIG_SUBSYSTEMCONFIGSENTRY._options = None
    _APPAGENTCONFIG_SUBSYSTEMCONFIGSENTRY._serialized_options = b'8\x01'
    _APPAGENTCONFIG.fields_by_name['subsystem_configs']._options = None
    _APPAGENTCONFIG.fields_by_name['subsystem_configs']._serialized_options = b'\x9a\x84\x9e\x031bson:"subsystem_configs" json:"subsystem_configs"'
    _APPSUBSYSTEMCONFIG.fields_by_name['release_channel']._options = None
    _APPSUBSYSTEMCONFIG.fields_by_name['release_channel']._serialized_options = b'\x9a\x84\x9e\x03-bson:"release_channel" json:"release_channel"'
    _APPSUBSYSTEMCONFIG.fields_by_name['pin_version']._options = None
    _APPSUBSYSTEMCONFIG.fields_by_name['pin_version']._serialized_options = b'\x9a\x84\x9e\x03%bson:"pin_version" json:"pin_version"'
    _APPSUBSYSTEMCONFIG.fields_by_name['pin_url']._options = None
    _APPSUBSYSTEMCONFIG.fields_by_name['pin_url']._serialized_options = b'\x9a\x84\x9e\x03\x1dbson:"pin_url" json:"pin_url"'
    _APPSUBSYSTEMCONFIG.fields_by_name['disable_subsystem']._options = None
    _APPSUBSYSTEMCONFIG.fields_by_name['disable_subsystem']._serialized_options = b'\x9a\x84\x9e\x031bson:"disable_subsystem" json:"disable_subsystem"'
    _DEVICEAGENTCONFIGREQUEST_SUBSYSTEMVERSIONSENTRY._options = None
    _DEVICEAGENTCONFIGREQUEST_SUBSYSTEMVERSIONSENTRY._serialized_options = b'8\x01'
    _DEVICEAGENTCONFIGRESPONSE_SUBSYSTEMCONFIGSENTRY._options = None
    _DEVICEAGENTCONFIGRESPONSE_SUBSYSTEMCONFIGSENTRY._serialized_options = b'8\x01'
    _PACKAGEFORMAT._serialized_start = 2127
    _PACKAGEFORMAT._serialized_end = 2286
    _GETAGENTCONFIGREQUEST._serialized_start = 103
    _GETAGENTCONFIGREQUEST._serialized_end = 142
    _GETAGENTCONFIGRESPONSE._serialized_start = 144
    _GETAGENTCONFIGRESPONSE._serialized_end = 238
    _UPDATEAGENTCONFIGREQUEST._serialized_start = 240
    _UPDATEAGENTCONFIGREQUEST._serialized_end = 352
    _UPDATEAGENTCONFIGRESPONSE._serialized_start = 354
    _UPDATEAGENTCONFIGRESPONSE._serialized_end = 451
    _APPAGENTCONFIG._serialized_start = 454
    _APPAGENTCONFIG._serialized_end = 737
    _APPAGENTCONFIG_SUBSYSTEMCONFIGSENTRY._serialized_start = 631
    _APPAGENTCONFIG_SUBSYSTEMCONFIGSENTRY._serialized_end = 737
    _APPSUBSYSTEMCONFIG._serialized_start = 740
    _APPSUBSYSTEMCONFIG._serialized_end = 1092
    _DEVICEAGENTCONFIGREQUEST._serialized_start = 1095
    _DEVICEAGENTCONFIGREQUEST._serialized_end = 1380
    _DEVICEAGENTCONFIGREQUEST_SUBSYSTEMVERSIONSENTRY._serialized_start = 1312
    _DEVICEAGENTCONFIGREQUEST_SUBSYSTEMVERSIONSENTRY._serialized_end = 1380
    _DEVICEAGENTCONFIGRESPONSE._serialized_start = 1383
    _DEVICEAGENTCONFIGRESPONSE._serialized_end = 1700
    _DEVICEAGENTCONFIGRESPONSE_SUBSYSTEMCONFIGSENTRY._serialized_start = 1591
    _DEVICEAGENTCONFIGRESPONSE_SUBSYSTEMCONFIGSENTRY._serialized_end = 1700
    _DEVICESUBSYSTEMCONFIG._serialized_start = 1703
    _DEVICESUBSYSTEMCONFIG._serialized_end = 1862
    _HOSTINFO._serialized_start = 1864
    _HOSTINFO._serialized_end = 1946
    _SUBSYSTEMUPDATEINFO._serialized_start = 1949
    _SUBSYSTEMUPDATEINFO._serialized_end = 2124
    _AGENTAPPSERVICE._serialized_start = 2289
    _AGENTAPPSERVICE._serialized_end = 2521
    _AGENTDEVICESERVICE._serialized_start = 2524
    _AGENTDEVICESERVICE._serialized_end = 2656