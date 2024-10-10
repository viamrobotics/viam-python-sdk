"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 2, '', 'app/v1/robot.proto')
_sym_db = _symbol_database.Default()
from ...common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ...tagger.v1 import tagger_pb2 as tagger_dot_v1_dot_tagger__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12app/v1/robot.proto\x12\x0bviam.app.v1\x1a\x16common/v1/common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x16tagger/v1/tagger.proto"\xb9\x07\n\x0bRobotConfig\x12.\n\x05cloud\x18\x01 \x01(\x0b2\x18.viam.app.v1.CloudConfigR\x05cloud\x123\n\x07remotes\x18\x02 \x03(\x0b2\x19.viam.app.v1.RemoteConfigR\x07remotes\x12<\n\ncomponents\x18\x03 \x03(\x0b2\x1c.viam.app.v1.ComponentConfigR\ncomponents\x128\n\tprocesses\x18\x04 \x03(\x0b2\x1a.viam.app.v1.ProcessConfigR\tprocesses\x126\n\x08services\x18\x05 \x03(\x0b2\x1a.viam.app.v1.ServiceConfigR\x08services\x129\n\x07network\x18\x06 \x01(\x0b2\x1a.viam.app.v1.NetworkConfigH\x00R\x07network\x88\x01\x01\x120\n\x04auth\x18\x07 \x01(\x0b2\x17.viam.app.v1.AuthConfigH\x01R\x04auth\x88\x01\x01\x12\x19\n\x05debug\x18\x08 \x01(\x08H\x02R\x05debug\x88\x01\x01\x123\n\x07modules\x18\t \x03(\x0b2\x19.viam.app.v1.ModuleConfigR\x07modules\x127\n\x15disable_partial_start\x18\n \x01(\x08H\x03R\x13disablePartialStart\x88\x01\x01\x126\n\x08packages\x18\x0b \x03(\x0b2\x1a.viam.app.v1.PackageConfigR\x08packages\x12\\\n\x19overwrite_fragment_status\x18\x0c \x03(\x0b2 .viam.app.v1.AppValidationStatusR\x17overwriteFragmentStatus\x12,\n\x12enable_web_profile\x18\r \x01(\x08R\x10enableWebProfile\x12/\n\x03log\x18\x0e \x03(\x0b2\x1d.viam.app.v1.LogPatternConfigR\x03log\x12\x1a\n\x08revision\x18\x0f \x01(\tR\x08revision\x12E\n\x0bmaintenance\x18\x10 \x01(\x0b2\x1e.viam.app.v1.MaintenanceConfigH\x04R\x0bmaintenance\x88\x01\x01B\n\n\x08_networkB\x07\n\x05_authB\x08\n\x06_debugB\x18\n\x16_disable_partial_startB\x0e\n\x0c_maintenance"B\n\x10LogPatternConfig\x12\x18\n\x07pattern\x18\x01 \x01(\tR\x07pattern\x12\x14\n\x05level\x18\x02 \x01(\tR\x05level"8\n\x0eLocationSecret\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06secret\x18\x02 \x01(\tR\x06secret"+\n\x13AppValidationStatus\x12\x14\n\x05error\x18\x01 \x01(\tR\x05error"\xbe\x03\n\x0bCloudConfig\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04fqdn\x18\x02 \x01(\tR\x04fqdn\x12\x1d\n\nlocal_fqdn\x18\x03 \x01(\tR\tlocalFqdn\x12\x1d\n\nmanaged_by\x18\x04 \x01(\tR\tmanagedBy\x12+\n\x11signaling_address\x18\x05 \x01(\tR\x10signalingAddress\x12-\n\x12signaling_insecure\x18\x06 \x01(\x08R\x11signalingInsecure\x12+\n\x0flocation_secret\x18\x07 \x01(\tB\x02\x18\x01R\x0elocationSecret\x12\x16\n\x06secret\x18\x08 \x01(\tR\x06secret\x12F\n\x10location_secrets\x18\t \x03(\x0b2\x1b.viam.app.v1.LocationSecretR\x0flocationSecrets\x12$\n\x0eprimary_org_id\x18\n \x01(\tR\x0cprimaryOrgId\x12\x1f\n\x0blocation_id\x18\x0b \x01(\tR\nlocationId\x12\x1d\n\nmachine_id\x18\x0c \x01(\tR\tmachineId"\xbb\x03\n\x0fComponentConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1c\n\tnamespace\x18\x02 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x12\x14\n\x05model\x18\x04 \x01(\tR\x05model\x12(\n\x05frame\x18\x05 \x01(\x0b2\x12.viam.app.v1.FrameR\x05frame\x12\x1d\n\ndepends_on\x18\x06 \x03(\tR\tdependsOn\x12l\n\x0fservice_configs\x18\x07 \x03(\x0b2\'.viam.app.v1.ResourceLevelServiceConfigB\x1a\x9a\x84\x9e\x03\x15json:"service_config"R\x0eserviceConfigs\x127\n\nattributes\x18\x08 \x01(\x0b2\x17.google.protobuf.StructR\nattributes\x12\x10\n\x03api\x18\t \x01(\tR\x03api\x12J\n\x11log_configuration\x18\n \x01(\x0b2\x1d.viam.app.v1.LogConfigurationR\x10logConfiguration"i\n\x1aResourceLevelServiceConfig\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x127\n\nattributes\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\nattributes"\xd4\x02\n\rProcessConfig\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n\x04args\x18\x03 \x03(\tR\x04args\x12\x10\n\x03cwd\x18\x04 \x01(\tR\x03cwd\x12\x19\n\x08one_shot\x18\x05 \x01(\x08R\x07oneShot\x12\x10\n\x03log\x18\x06 \x01(\x08R\x03log\x12\x1f\n\x0bstop_signal\x18\x07 \x01(\x05R\nstopSignal\x12<\n\x0cstop_timeout\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationR\x0bstopTimeout\x125\n\x03env\x18\t \x03(\x0b2#.viam.app.v1.ProcessConfig.EnvEntryR\x03env\x1a6\n\x08EnvEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\x8f\x03\n\rServiceConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1c\n\tnamespace\x18\x02 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x127\n\nattributes\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\nattributes\x12\x1d\n\ndepends_on\x18\x05 \x03(\tR\tdependsOn\x12\x14\n\x05model\x18\x06 \x01(\tR\x05model\x12\x10\n\x03api\x18\t \x01(\tR\x03api\x12l\n\x0fservice_configs\x18\n \x03(\x0b2\'.viam.app.v1.ResourceLevelServiceConfigB\x1a\x9a\x84\x9e\x03\x15json:"service_config"R\x0eserviceConfigs\x12J\n\x11log_configuration\x18\x0b \x01(\x0b2\x1d.viam.app.v1.LogConfigurationR\x10logConfiguration"\xc5\x01\n\rNetworkConfig\x12\x12\n\x04fqdn\x18\x01 \x01(\tR\x04fqdn\x12!\n\x0cbind_address\x18\x02 \x01(\tR\x0bbindAddress\x12"\n\rtls_cert_file\x18\x03 \x01(\tR\x0btlsCertFile\x12 \n\x0ctls_key_file\x18\x04 \x01(\tR\ntlsKeyFile\x127\n\x08sessions\x18\x05 \x01(\x0b2\x1b.viam.app.v1.SessionsConfigR\x08sessions"V\n\x0eSessionsConfig\x12D\n\x10heartbeat_window\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationR\x0fheartbeatWindow"\xe5\x01\n\nAuthConfig\x12:\n\x08handlers\x18\x01 \x03(\x0b2\x1e.viam.app.v1.AuthHandlerConfigR\x08handlers\x12*\n\x11tls_auth_entities\x18\x02 \x03(\tR\x0ftlsAuthEntities\x12V\n\x14external_auth_config\x18\x03 \x01(\x0b2\x1f.viam.app.v1.ExternalAuthConfigH\x00R\x12externalAuthConfig\x88\x01\x01B\x17\n\x15_external_auth_config"7\n\x08JWKSFile\x12+\n\x04json\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x04json"?\n\x12ExternalAuthConfig\x12)\n\x04jwks\x18\x01 \x01(\x0b2\x15.viam.app.v1.JWKSFileR\x04jwks"v\n\x11AuthHandlerConfig\x120\n\x04type\x18\x01 \x01(\x0e2\x1c.viam.app.v1.CredentialsTypeR\x04type\x12/\n\x06config\x18\x05 \x01(\x0b2\x17.google.protobuf.StructR\x06config"\xcd\x01\n\x05Frame\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12:\n\x0btranslation\x18\x02 \x01(\x0b2\x18.viam.app.v1.TranslationR\x0btranslation\x12:\n\x0borientation\x18\x03 \x01(\x0b2\x18.viam.app.v1.OrientationR\x0borientation\x124\n\x08geometry\x18\x04 \x01(\x0b2\x18.viam.common.v1.GeometryR\x08geometry"(\n\x10LogConfiguration\x12\x14\n\x05level\x18\x01 \x01(\tR\x05level"7\n\x0bTranslation\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z"\xd0\x07\n\x0bOrientation\x12O\n\x0eno_orientation\x18\x01 \x01(\x0b2&.viam.app.v1.Orientation.NoOrientationH\x00R\rnoOrientation\x12Z\n\x0evector_radians\x18\x02 \x01(\x0b21.viam.app.v1.Orientation.OrientationVectorRadiansH\x00R\rvectorRadians\x12Z\n\x0evector_degrees\x18\x03 \x01(\x0b21.viam.app.v1.Orientation.OrientationVectorDegreesH\x00R\rvectorDegrees\x12I\n\x0ceuler_angles\x18\x04 \x01(\x0b2$.viam.app.v1.Orientation.EulerAnglesH\x00R\x0beulerAngles\x12F\n\x0baxis_angles\x18\x05 \x01(\x0b2#.viam.app.v1.Orientation.AxisAnglesH\x00R\naxisAngles\x12E\n\nquaternion\x18\x06 \x01(\x0b2#.viam.app.v1.Orientation.QuaternionH\x00R\nquaternion\x1a\x0f\n\rNoOrientation\x1aj\n\x18OrientationVectorRadians\x12$\n\x05theta\x18\x01 \x01(\x01B\x0e\x9a\x84\x9e\x03\tjson:"th"R\x05theta\x12\x0c\n\x01x\x18\x02 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x03 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x04 \x01(\x01R\x01z\x1aj\n\x18OrientationVectorDegrees\x12$\n\x05theta\x18\x01 \x01(\x01B\x0e\x9a\x84\x9e\x03\tjson:"th"R\x05theta\x12\x0c\n\x01x\x18\x02 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x03 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x04 \x01(\x01R\x01z\x1aI\n\x0bEulerAngles\x12\x12\n\x04roll\x18\x01 \x01(\x01R\x04roll\x12\x14\n\x05pitch\x18\x02 \x01(\x01R\x05pitch\x12\x10\n\x03yaw\x18\x03 \x01(\x01R\x03yaw\x1a\\\n\nAxisAngles\x12$\n\x05theta\x18\x01 \x01(\x01B\x0e\x9a\x84\x9e\x03\tjson:"th"R\x05theta\x12\x0c\n\x01x\x18\x02 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x03 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x04 \x01(\x01R\x01z\x1aD\n\nQuaternion\x12\x0c\n\x01w\x18\x01 \x01(\x01R\x01w\x12\x0c\n\x01x\x18\x02 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x03 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x04 \x01(\x01R\x01zB\x06\n\x04type"\xf5\x03\n\x0cRemoteConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07address\x18\x02 \x01(\tR\x07address\x12(\n\x05frame\x18\x03 \x01(\x0b2\x12.viam.app.v1.FrameR\x05frame\x12+\n\x04auth\x18\x04 \x01(\x0b2\x17.viam.app.v1.RemoteAuthR\x04auth\x12\x1d\n\nmanaged_by\x18\x05 \x01(\tR\tmanagedBy\x12\x1a\n\x08insecure\x18\x06 \x01(\x08R\x08insecure\x12U\n\x19connection_check_interval\x18\x07 \x01(\x0b2\x19.google.protobuf.DurationR\x17connectionCheckInterval\x12H\n\x12reconnect_interval\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationR\x11reconnectInterval\x12l\n\x0fservice_configs\x18\t \x03(\x0b2\'.viam.app.v1.ResourceLevelServiceConfigB\x1a\x9a\x84\x9e\x03\x15json:"service_config"R\x0eserviceConfigs\x12\x16\n\x06secret\x18\n \x01(\tR\x06secret"\xc6\x01\n\nRemoteAuth\x12E\n\x0bcredentials\x18\x01 \x01(\x0b2#.viam.app.v1.RemoteAuth.CredentialsR\x0bcredentials\x12\x16\n\x06entity\x18\x02 \x01(\tR\x06entity\x1aY\n\x0bCredentials\x120\n\x04type\x18\x01 \x01(\x0e2\x1c.viam.app.v1.CredentialsTypeR\x04type\x12\x18\n\x07payload\x18\x02 \x01(\tR\x07payload"\xac\x01\n\tAgentInfo\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x0e\n\x02os\x18\x02 \x01(\tR\x02os\x12\x10\n\x03ips\x18\x03 \x03(\tR\x03ips\x12\x18\n\x07version\x18\x04 \x01(\tR\x07version\x12!\n\x0cgit_revision\x18\x05 \x01(\tR\x0bgitRevision\x12\x1f\n\x08platform\x18\x06 \x01(\tH\x00R\x08platform\x88\x01\x01B\x0b\n\t_platform"j\n\rConfigRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12:\n\nagent_info\x18\x02 \x01(\x0b2\x16.viam.app.v1.AgentInfoH\x00R\tagentInfo\x88\x01\x01B\r\n\x0b_agent_info"B\n\x0eConfigResponse\x120\n\x06config\x18\x01 \x01(\x0b2\x18.viam.app.v1.RobotConfigR\x06config"$\n\x12CertificateRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"v\n\x13CertificateResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\'\n\x0ftls_certificate\x18\x02 \x01(\tR\x0etlsCertificate\x12&\n\x0ftls_private_key\x18\x03 \x01(\tR\rtlsPrivateKey"J\n\nLogRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12,\n\x04logs\x18\x02 \x03(\x0b2\x18.viam.common.v1.LogEntryR\x04logs"\r\n\x0bLogResponse"%\n\x13NeedsRestartRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x9a\x01\n\x14NeedsRestartResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12!\n\x0cmust_restart\x18\x02 \x01(\x08R\x0bmustRestart\x12O\n\x16restart_check_interval\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationR\x14restartCheckInterval"\xf3\x02\n\x0cModuleConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x12\x1b\n\tlog_level\x18\x03 \x01(\tR\x08logLevel\x12\x12\n\x04type\x18\x04 \x01(\tR\x04type\x12\x1b\n\tmodule_id\x18\x05 \x01(\tR\x08moduleId\x124\n\x03env\x18\x06 \x03(\x0b2".viam.app.v1.ModuleConfig.EnvEntryR\x03env\x128\n\x06status\x18\x07 \x01(\x0b2 .viam.app.v1.AppValidationStatusR\x06status\x12E\n\x11first_run_timeout\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationR\x0ffirstRunTimeout\x1a6\n\x08EnvEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\xa5\x01\n\rPackageConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07package\x18\x02 \x01(\tR\x07package\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\x12\x12\n\x04type\x18\x04 \x01(\tR\x04type\x128\n\x06status\x18\x05 \x01(\x0b2 .viam.app.v1.AppValidationStatusR\x06status"\x8a\x01\n\x11MaintenanceConfig\x12=\n\x0bsensor_name\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\nsensorName\x126\n\x17maintenance_allowed_key\x18\x02 \x01(\tR\x15maintenanceAllowedKey*\xbf\x01\n\x0fCredentialsType\x12 \n\x1cCREDENTIALS_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19CREDENTIALS_TYPE_INTERNAL\x10\x01\x12\x1c\n\x18CREDENTIALS_TYPE_API_KEY\x10\x02\x12!\n\x1dCREDENTIALS_TYPE_ROBOT_SECRET\x10\x03\x12*\n&CREDENTIALS_TYPE_ROBOT_LOCATION_SECRET\x10\x042\xb2\x02\n\x0cRobotService\x12A\n\x06Config\x12\x1a.viam.app.v1.ConfigRequest\x1a\x1b.viam.app.v1.ConfigResponse\x12P\n\x0bCertificate\x12\x1f.viam.app.v1.CertificateRequest\x1a .viam.app.v1.CertificateResponse\x128\n\x03Log\x12\x17.viam.app.v1.LogRequest\x1a\x18.viam.app.v1.LogResponse\x12S\n\x0cNeedsRestart\x12 .viam.app.v1.NeedsRestartRequest\x1a!.viam.app.v1.NeedsRestartResponseB\x18Z\x16go.viam.com/api/app/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.v1.robot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x16go.viam.com/api/app/v1'
    _globals['_CLOUDCONFIG'].fields_by_name['location_secret']._loaded_options = None
    _globals['_CLOUDCONFIG'].fields_by_name['location_secret']._serialized_options = b'\x18\x01'
    _globals['_COMPONENTCONFIG'].fields_by_name['service_configs']._loaded_options = None
    _globals['_COMPONENTCONFIG'].fields_by_name['service_configs']._serialized_options = b'\x9a\x84\x9e\x03\x15json:"service_config"'
    _globals['_PROCESSCONFIG_ENVENTRY']._loaded_options = None
    _globals['_PROCESSCONFIG_ENVENTRY']._serialized_options = b'8\x01'
    _globals['_SERVICECONFIG'].fields_by_name['service_configs']._loaded_options = None
    _globals['_SERVICECONFIG'].fields_by_name['service_configs']._serialized_options = b'\x9a\x84\x9e\x03\x15json:"service_config"'
    _globals['_ORIENTATION_ORIENTATIONVECTORRADIANS'].fields_by_name['theta']._loaded_options = None
    _globals['_ORIENTATION_ORIENTATIONVECTORRADIANS'].fields_by_name['theta']._serialized_options = b'\x9a\x84\x9e\x03\tjson:"th"'
    _globals['_ORIENTATION_ORIENTATIONVECTORDEGREES'].fields_by_name['theta']._loaded_options = None
    _globals['_ORIENTATION_ORIENTATIONVECTORDEGREES'].fields_by_name['theta']._serialized_options = b'\x9a\x84\x9e\x03\tjson:"th"'
    _globals['_ORIENTATION_AXISANGLES'].fields_by_name['theta']._loaded_options = None
    _globals['_ORIENTATION_AXISANGLES'].fields_by_name['theta']._serialized_options = b'\x9a\x84\x9e\x03\tjson:"th"'
    _globals['_REMOTECONFIG'].fields_by_name['service_configs']._loaded_options = None
    _globals['_REMOTECONFIG'].fields_by_name['service_configs']._serialized_options = b'\x9a\x84\x9e\x03\x15json:"service_config"'
    _globals['_MODULECONFIG_ENVENTRY']._loaded_options = None
    _globals['_MODULECONFIG_ENVENTRY']._serialized_options = b'8\x01'
    _globals['_CREDENTIALSTYPE']._serialized_start = 7252
    _globals['_CREDENTIALSTYPE']._serialized_end = 7443
    _globals['_ROBOTCONFIG']._serialized_start = 146
    _globals['_ROBOTCONFIG']._serialized_end = 1099
    _globals['_LOGPATTERNCONFIG']._serialized_start = 1101
    _globals['_LOGPATTERNCONFIG']._serialized_end = 1167
    _globals['_LOCATIONSECRET']._serialized_start = 1169
    _globals['_LOCATIONSECRET']._serialized_end = 1225
    _globals['_APPVALIDATIONSTATUS']._serialized_start = 1227
    _globals['_APPVALIDATIONSTATUS']._serialized_end = 1270
    _globals['_CLOUDCONFIG']._serialized_start = 1273
    _globals['_CLOUDCONFIG']._serialized_end = 1719
    _globals['_COMPONENTCONFIG']._serialized_start = 1722
    _globals['_COMPONENTCONFIG']._serialized_end = 2165
    _globals['_RESOURCELEVELSERVICECONFIG']._serialized_start = 2167
    _globals['_RESOURCELEVELSERVICECONFIG']._serialized_end = 2272
    _globals['_PROCESSCONFIG']._serialized_start = 2275
    _globals['_PROCESSCONFIG']._serialized_end = 2615
    _globals['_PROCESSCONFIG_ENVENTRY']._serialized_start = 2561
    _globals['_PROCESSCONFIG_ENVENTRY']._serialized_end = 2615
    _globals['_SERVICECONFIG']._serialized_start = 2618
    _globals['_SERVICECONFIG']._serialized_end = 3017
    _globals['_NETWORKCONFIG']._serialized_start = 3020
    _globals['_NETWORKCONFIG']._serialized_end = 3217
    _globals['_SESSIONSCONFIG']._serialized_start = 3219
    _globals['_SESSIONSCONFIG']._serialized_end = 3305
    _globals['_AUTHCONFIG']._serialized_start = 3308
    _globals['_AUTHCONFIG']._serialized_end = 3537
    _globals['_JWKSFILE']._serialized_start = 3539
    _globals['_JWKSFILE']._serialized_end = 3594
    _globals['_EXTERNALAUTHCONFIG']._serialized_start = 3596
    _globals['_EXTERNALAUTHCONFIG']._serialized_end = 3659
    _globals['_AUTHHANDLERCONFIG']._serialized_start = 3661
    _globals['_AUTHHANDLERCONFIG']._serialized_end = 3779
    _globals['_FRAME']._serialized_start = 3782
    _globals['_FRAME']._serialized_end = 3987
    _globals['_LOGCONFIGURATION']._serialized_start = 3989
    _globals['_LOGCONFIGURATION']._serialized_end = 4029
    _globals['_TRANSLATION']._serialized_start = 4031
    _globals['_TRANSLATION']._serialized_end = 4086
    _globals['_ORIENTATION']._serialized_start = 4089
    _globals['_ORIENTATION']._serialized_end = 5065
    _globals['_ORIENTATION_NOORIENTATION']._serialized_start = 4587
    _globals['_ORIENTATION_NOORIENTATION']._serialized_end = 4602
    _globals['_ORIENTATION_ORIENTATIONVECTORRADIANS']._serialized_start = 4604
    _globals['_ORIENTATION_ORIENTATIONVECTORRADIANS']._serialized_end = 4710
    _globals['_ORIENTATION_ORIENTATIONVECTORDEGREES']._serialized_start = 4712
    _globals['_ORIENTATION_ORIENTATIONVECTORDEGREES']._serialized_end = 4818
    _globals['_ORIENTATION_EULERANGLES']._serialized_start = 4820
    _globals['_ORIENTATION_EULERANGLES']._serialized_end = 4893
    _globals['_ORIENTATION_AXISANGLES']._serialized_start = 4895
    _globals['_ORIENTATION_AXISANGLES']._serialized_end = 4987
    _globals['_ORIENTATION_QUATERNION']._serialized_start = 4989
    _globals['_ORIENTATION_QUATERNION']._serialized_end = 5057
    _globals['_REMOTECONFIG']._serialized_start = 5068
    _globals['_REMOTECONFIG']._serialized_end = 5569
    _globals['_REMOTEAUTH']._serialized_start = 5572
    _globals['_REMOTEAUTH']._serialized_end = 5770
    _globals['_REMOTEAUTH_CREDENTIALS']._serialized_start = 5681
    _globals['_REMOTEAUTH_CREDENTIALS']._serialized_end = 5770
    _globals['_AGENTINFO']._serialized_start = 5773
    _globals['_AGENTINFO']._serialized_end = 5945
    _globals['_CONFIGREQUEST']._serialized_start = 5947
    _globals['_CONFIGREQUEST']._serialized_end = 6053
    _globals['_CONFIGRESPONSE']._serialized_start = 6055
    _globals['_CONFIGRESPONSE']._serialized_end = 6121
    _globals['_CERTIFICATEREQUEST']._serialized_start = 6123
    _globals['_CERTIFICATEREQUEST']._serialized_end = 6159
    _globals['_CERTIFICATERESPONSE']._serialized_start = 6161
    _globals['_CERTIFICATERESPONSE']._serialized_end = 6279
    _globals['_LOGREQUEST']._serialized_start = 6281
    _globals['_LOGREQUEST']._serialized_end = 6355
    _globals['_LOGRESPONSE']._serialized_start = 6357
    _globals['_LOGRESPONSE']._serialized_end = 6370
    _globals['_NEEDSRESTARTREQUEST']._serialized_start = 6372
    _globals['_NEEDSRESTARTREQUEST']._serialized_end = 6409
    _globals['_NEEDSRESTARTRESPONSE']._serialized_start = 6412
    _globals['_NEEDSRESTARTRESPONSE']._serialized_end = 6566
    _globals['_MODULECONFIG']._serialized_start = 6569
    _globals['_MODULECONFIG']._serialized_end = 6940
    _globals['_MODULECONFIG_ENVENTRY']._serialized_start = 2561
    _globals['_MODULECONFIG_ENVENTRY']._serialized_end = 2615
    _globals['_PACKAGECONFIG']._serialized_start = 6943
    _globals['_PACKAGECONFIG']._serialized_end = 7108
    _globals['_MAINTENANCECONFIG']._serialized_start = 7111
    _globals['_MAINTENANCECONFIG']._serialized_end = 7249
    _globals['_ROBOTSERVICE']._serialized_start = 7446
    _globals['_ROBOTSERVICE']._serialized_end = 7752