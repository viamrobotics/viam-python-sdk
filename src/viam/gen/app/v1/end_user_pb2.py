"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'app/v1/end_user.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15app/v1/end_user.proto\x12\x0bviam.app.v1"\x18\n\x16IsLegalAcceptedRequest"@\n\x17IsLegalAcceptedResponse\x12%\n\x0eaccepted_legal\x18\x01 \x01(\x08R\racceptedLegal"\x14\n\x12AcceptLegalRequest"\x15\n\x13AcceptLegalResponse"\xcb\x01\n\x1eRegisterAuthApplicationRequest\x12)\n\x10application_name\x18\x01 \x01(\tR\x0fapplicationName\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1f\n\x0borigin_uris\x18\x03 \x03(\tR\noriginUris\x12#\n\rredirect_uris\x18\x04 \x03(\tR\x0credirectUris\x12\x1d\n\nlogout_uri\x18\x05 \x01(\tR\tlogoutUri:\x02\x18\x01"\x9c\x01\n\x1fRegisterAuthApplicationResponse\x12%\n\x0eapplication_id\x18\x01 \x01(\tR\rapplicationId\x12)\n\x10application_name\x18\x02 \x01(\tR\x0fapplicationName\x12#\n\rclient_secret\x18\x03 \x01(\tR\x0cclientSecret:\x02\x18\x01"\xf0\x01\n\x1cUpdateAuthApplicationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12%\n\x0eapplication_id\x18\x02 \x01(\tR\rapplicationId\x12)\n\x10application_name\x18\x03 \x01(\tR\x0fapplicationName\x12\x1f\n\x0borigin_uris\x18\x04 \x03(\tR\noriginUris\x12#\n\rredirect_uris\x18\x05 \x03(\tR\x0credirectUris\x12\x1d\n\nlogout_uri\x18\x06 \x01(\tR\tlogoutUri:\x02\x18\x01"u\n\x1dUpdateAuthApplicationResponse\x12%\n\x0eapplication_id\x18\x01 \x01(\tR\rapplicationId\x12)\n\x10application_name\x18\x02 \x01(\tR\x0fapplicationName:\x02\x18\x01"]\n\x19GetAuthApplicationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12%\n\x0eapplication_id\x18\x02 \x01(\tR\rapplicationId:\x02\x18\x01"\xfc\x01\n\x1aGetAuthApplicationResponse\x12%\n\x0eapplication_id\x18\x01 \x01(\tR\rapplicationId\x12)\n\x10application_name\x18\x02 \x01(\tR\x0fapplicationName\x12#\n\rclient_secret\x18\x03 \x01(\tR\x0cclientSecret\x12\x1f\n\x0borigin_uris\x18\x04 \x03(\tR\noriginUris\x12#\n\rredirect_uris\x18\x05 \x03(\tR\x0credirectUris\x12\x1d\n\nlogout_uri\x18\x06 \x01(\tR\tlogoutUri:\x02\x18\x012\x9c\x04\n\x0eEndUserService\x12\\\n\x0fIsLegalAccepted\x12#.viam.app.v1.IsLegalAcceptedRequest\x1a$.viam.app.v1.IsLegalAcceptedResponse\x12P\n\x0bAcceptLegal\x12\x1f.viam.app.v1.AcceptLegalRequest\x1a .viam.app.v1.AcceptLegalResponse\x12y\n\x17RegisterAuthApplication\x12+.viam.app.v1.RegisterAuthApplicationRequest\x1a,.viam.app.v1.RegisterAuthApplicationResponse"\x03\x88\x02\x01\x12s\n\x15UpdateAuthApplication\x12).viam.app.v1.UpdateAuthApplicationRequest\x1a*.viam.app.v1.UpdateAuthApplicationResponse"\x03\x88\x02\x01\x12j\n\x12GetAuthApplication\x12&.viam.app.v1.GetAuthApplicationRequest\x1a\'.viam.app.v1.GetAuthApplicationResponse"\x03\x88\x02\x01B\x18Z\x16go.viam.com/api/app/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.v1.end_user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x16go.viam.com/api/app/v1'
    _globals['_REGISTERAUTHAPPLICATIONREQUEST']._loaded_options = None
    _globals['_REGISTERAUTHAPPLICATIONREQUEST']._serialized_options = b'\x18\x01'
    _globals['_REGISTERAUTHAPPLICATIONRESPONSE']._loaded_options = None
    _globals['_REGISTERAUTHAPPLICATIONRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_UPDATEAUTHAPPLICATIONREQUEST']._loaded_options = None
    _globals['_UPDATEAUTHAPPLICATIONREQUEST']._serialized_options = b'\x18\x01'
    _globals['_UPDATEAUTHAPPLICATIONRESPONSE']._loaded_options = None
    _globals['_UPDATEAUTHAPPLICATIONRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_GETAUTHAPPLICATIONREQUEST']._loaded_options = None
    _globals['_GETAUTHAPPLICATIONREQUEST']._serialized_options = b'\x18\x01'
    _globals['_GETAUTHAPPLICATIONRESPONSE']._loaded_options = None
    _globals['_GETAUTHAPPLICATIONRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_ENDUSERSERVICE'].methods_by_name['RegisterAuthApplication']._loaded_options = None
    _globals['_ENDUSERSERVICE'].methods_by_name['RegisterAuthApplication']._serialized_options = b'\x88\x02\x01'
    _globals['_ENDUSERSERVICE'].methods_by_name['UpdateAuthApplication']._loaded_options = None
    _globals['_ENDUSERSERVICE'].methods_by_name['UpdateAuthApplication']._serialized_options = b'\x88\x02\x01'
    _globals['_ENDUSERSERVICE'].methods_by_name['GetAuthApplication']._loaded_options = None
    _globals['_ENDUSERSERVICE'].methods_by_name['GetAuthApplication']._serialized_options = b'\x88\x02\x01'
    _globals['_ISLEGALACCEPTEDREQUEST']._serialized_start = 38
    _globals['_ISLEGALACCEPTEDREQUEST']._serialized_end = 62
    _globals['_ISLEGALACCEPTEDRESPONSE']._serialized_start = 64
    _globals['_ISLEGALACCEPTEDRESPONSE']._serialized_end = 128
    _globals['_ACCEPTLEGALREQUEST']._serialized_start = 130
    _globals['_ACCEPTLEGALREQUEST']._serialized_end = 150
    _globals['_ACCEPTLEGALRESPONSE']._serialized_start = 152
    _globals['_ACCEPTLEGALRESPONSE']._serialized_end = 173
    _globals['_REGISTERAUTHAPPLICATIONREQUEST']._serialized_start = 176
    _globals['_REGISTERAUTHAPPLICATIONREQUEST']._serialized_end = 379
    _globals['_REGISTERAUTHAPPLICATIONRESPONSE']._serialized_start = 382
    _globals['_REGISTERAUTHAPPLICATIONRESPONSE']._serialized_end = 538
    _globals['_UPDATEAUTHAPPLICATIONREQUEST']._serialized_start = 541
    _globals['_UPDATEAUTHAPPLICATIONREQUEST']._serialized_end = 781
    _globals['_UPDATEAUTHAPPLICATIONRESPONSE']._serialized_start = 783
    _globals['_UPDATEAUTHAPPLICATIONRESPONSE']._serialized_end = 900
    _globals['_GETAUTHAPPLICATIONREQUEST']._serialized_start = 902
    _globals['_GETAUTHAPPLICATIONREQUEST']._serialized_end = 995
    _globals['_GETAUTHAPPLICATIONRESPONSE']._serialized_start = 998
    _globals['_GETAUTHAPPLICATIONRESPONSE']._serialized_end = 1250
    _globals['_ENDUSERSERVICE']._serialized_start = 1253
    _globals['_ENDUSERSERVICE']._serialized_end = 1793