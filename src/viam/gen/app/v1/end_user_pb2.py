"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15app/v1/end_user.proto\x12\x0bviam.app.v1"\x18\n\x16IsLegalAcceptedRequest"@\n\x17IsLegalAcceptedResponse\x12%\n\x0eaccepted_legal\x18\x01 \x01(\x08R\racceptedLegal"\x14\n\x12AcceptLegalRequest"\x15\n\x13AcceptLegalResponse"\xc7\x01\n\x1eRegisterAuthApplicationRequest\x12)\n\x10application_name\x18\x01 \x01(\tR\x0fapplicationName\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1f\n\x0borigin_uris\x18\x03 \x03(\tR\noriginUris\x12#\n\rredirect_uris\x18\x04 \x03(\tR\x0credirectUris\x12\x1d\n\nlogout_uri\x18\x05 \x01(\tR\tlogoutUri"\x8b\x01\n\x1fRegisterAuthApplicationResponse\x12%\n\x0eapplication_id\x18\x01 \x01(\tR\rapplicationId\x12)\n\x10application_name\x18\x02 \x01(\tR\x0fapplicationName\x12\x16\n\x06secret\x18\x03 \x01(\tR\x06secret"\xec\x01\n\x1cUpdateAuthApplicationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12%\n\x0eapplication_id\x18\x02 \x01(\tR\rapplicationId\x12)\n\x10application_name\x18\x03 \x01(\tR\x0fapplicationName\x12\x1f\n\x0borigin_uris\x18\x04 \x03(\tR\noriginUris\x12#\n\rredirect_uris\x18\x05 \x03(\tR\x0credirectUris\x12\x1d\n\nlogout_uri\x18\x06 \x01(\tR\tlogoutUri"q\n\x1dUpdateAuthApplicationResponse\x12%\n\x0eapplication_id\x18\x01 \x01(\tR\rapplicationId\x12)\n\x10application_name\x18\x02 \x01(\tR\x0fapplicationName2\xa6\x03\n\x0eEndUserService\x12\\\n\x0fIsLegalAccepted\x12#.viam.app.v1.IsLegalAcceptedRequest\x1a$.viam.app.v1.IsLegalAcceptedResponse\x12P\n\x0bAcceptLegal\x12\x1f.viam.app.v1.AcceptLegalRequest\x1a .viam.app.v1.AcceptLegalResponse\x12t\n\x17RegisterAuthApplication\x12+.viam.app.v1.RegisterAuthApplicationRequest\x1a,.viam.app.v1.RegisterAuthApplicationResponse\x12n\n\x15UpdateAuthApplication\x12).viam.app.v1.UpdateAuthApplicationRequest\x1a*.viam.app.v1.UpdateAuthApplicationResponseB\x18Z\x16go.viam.com/api/app/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.v1.end_user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x16go.viam.com/api/app/v1'
    _ISLEGALACCEPTEDREQUEST._serialized_start = 38
    _ISLEGALACCEPTEDREQUEST._serialized_end = 62
    _ISLEGALACCEPTEDRESPONSE._serialized_start = 64
    _ISLEGALACCEPTEDRESPONSE._serialized_end = 128
    _ACCEPTLEGALREQUEST._serialized_start = 130
    _ACCEPTLEGALREQUEST._serialized_end = 150
    _ACCEPTLEGALRESPONSE._serialized_start = 152
    _ACCEPTLEGALRESPONSE._serialized_end = 173
    _REGISTERAUTHAPPLICATIONREQUEST._serialized_start = 176
    _REGISTERAUTHAPPLICATIONREQUEST._serialized_end = 375
    _REGISTERAUTHAPPLICATIONRESPONSE._serialized_start = 378
    _REGISTERAUTHAPPLICATIONRESPONSE._serialized_end = 517
    _UPDATEAUTHAPPLICATIONREQUEST._serialized_start = 520
    _UPDATEAUTHAPPLICATIONREQUEST._serialized_end = 756
    _UPDATEAUTHAPPLICATIONRESPONSE._serialized_start = 758
    _UPDATEAUTHAPPLICATIONRESPONSE._serialized_end = 871
    _ENDUSERSERVICE._serialized_start = 874
    _ENDUSERSERVICE._serialized_end = 1296