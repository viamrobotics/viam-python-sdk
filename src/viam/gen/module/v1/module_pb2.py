"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 2, '', 'module/v1/module.proto')
_sym_db = _symbol_database.Default()
from ...app.v1 import robot_pb2 as app_dot_v1_dot_robot__pb2
from ...robot.v1 import robot_pb2 as robot_dot_v1_dot_robot__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16module/v1/module.proto\x12\x0eviam.module.v1\x1a\x12app/v1/robot.proto\x1a\x14robot/v1/robot.proto"n\n\x12AddResourceRequest\x124\n\x06config\x18\x01 \x01(\x0b2\x1c.viam.app.v1.ComponentConfigR\x06config\x12"\n\x0cdependencies\x18\x02 \x03(\tR\x0cdependencies"\x15\n\x13AddResourceResponse"v\n\x1aReconfigureResourceRequest\x124\n\x06config\x18\x01 \x01(\x0b2\x1c.viam.app.v1.ComponentConfigR\x06config\x12"\n\x0cdependencies\x18\x02 \x03(\tR\x0cdependencies"\x1d\n\x1bReconfigureResourceResponse"+\n\x15RemoveResourceRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x18\n\x16RemoveResourceResponse"h\n\x11HandlerDefinition\x12;\n\x07subtype\x18\x01 \x01(\x0b2!.viam.robot.v1.ResourceRPCSubtypeR\x07subtype\x12\x16\n\x06models\x18\x02 \x03(\tR\x06models"K\n\nHandlerMap\x12=\n\x08handlers\x18\x01 \x03(\x0b2!.viam.module.v1.HandlerDefinitionR\x08handlers"X\n\x0cReadyRequest\x12%\n\x0eparent_address\x18\x01 \x01(\tR\rparentAddress\x12!\n\x0cwebrtc_offer\x18\x02 \x01(\tR\x0bwebrtcOffer"\x86\x01\n\rReadyResponse\x12\x14\n\x05ready\x18\x01 \x01(\x08R\x05ready\x12:\n\nhandlermap\x18\x02 \x01(\x0b2\x1a.viam.module.v1.HandlerMapR\nhandlermap\x12#\n\rwebrtc_answer\x18\x03 \x01(\tR\x0cwebrtcAnswer"M\n\x15ValidateConfigRequest\x124\n\x06config\x18\x01 \x01(\x0b2\x1c.viam.app.v1.ComponentConfigR\x06config"<\n\x16ValidateConfigResponse\x12"\n\x0cdependencies\x18\x01 \x03(\tR\x0cdependencies2\xdf\x03\n\rModuleService\x12V\n\x0bAddResource\x12".viam.module.v1.AddResourceRequest\x1a#.viam.module.v1.AddResourceResponse\x12n\n\x13ReconfigureResource\x12*.viam.module.v1.ReconfigureResourceRequest\x1a+.viam.module.v1.ReconfigureResourceResponse\x12_\n\x0eRemoveResource\x12%.viam.module.v1.RemoveResourceRequest\x1a&.viam.module.v1.RemoveResourceResponse\x12D\n\x05Ready\x12\x1c.viam.module.v1.ReadyRequest\x1a\x1d.viam.module.v1.ReadyResponse\x12_\n\x0eValidateConfig\x12%.viam.module.v1.ValidateConfigRequest\x1a&.viam.module.v1.ValidateConfigResponseB\x1bZ\x19go.viam.com/api/module/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'module.v1.module_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x19go.viam.com/api/module/v1'
    _globals['_ADDRESOURCEREQUEST']._serialized_start = 84
    _globals['_ADDRESOURCEREQUEST']._serialized_end = 194
    _globals['_ADDRESOURCERESPONSE']._serialized_start = 196
    _globals['_ADDRESOURCERESPONSE']._serialized_end = 217
    _globals['_RECONFIGURERESOURCEREQUEST']._serialized_start = 219
    _globals['_RECONFIGURERESOURCEREQUEST']._serialized_end = 337
    _globals['_RECONFIGURERESOURCERESPONSE']._serialized_start = 339
    _globals['_RECONFIGURERESOURCERESPONSE']._serialized_end = 368
    _globals['_REMOVERESOURCEREQUEST']._serialized_start = 370
    _globals['_REMOVERESOURCEREQUEST']._serialized_end = 413
    _globals['_REMOVERESOURCERESPONSE']._serialized_start = 415
    _globals['_REMOVERESOURCERESPONSE']._serialized_end = 439
    _globals['_HANDLERDEFINITION']._serialized_start = 441
    _globals['_HANDLERDEFINITION']._serialized_end = 545
    _globals['_HANDLERMAP']._serialized_start = 547
    _globals['_HANDLERMAP']._serialized_end = 622
    _globals['_READYREQUEST']._serialized_start = 624
    _globals['_READYREQUEST']._serialized_end = 712
    _globals['_READYRESPONSE']._serialized_start = 715
    _globals['_READYRESPONSE']._serialized_end = 849
    _globals['_VALIDATECONFIGREQUEST']._serialized_start = 851
    _globals['_VALIDATECONFIGREQUEST']._serialized_end = 928
    _globals['_VALIDATECONFIGRESPONSE']._serialized_start = 930
    _globals['_VALIDATECONFIGRESPONSE']._serialized_end = 990
    _globals['_MODULESERVICE']._serialized_start = 993
    _globals['_MODULESERVICE']._serialized_end = 1472