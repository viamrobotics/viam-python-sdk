"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15app/v1/end_user.proto\x12\x0bviam.app.v1"\x18\n\x16IsLegalAcceptedRequest"@\n\x17IsLegalAcceptedResponse\x12%\n\x0eaccepted_legal\x18\x01 \x01(\x08R\racceptedLegal"\x14\n\x12AcceptLegalRequest"\x15\n\x13AcceptLegalResponse2\xc0\x01\n\x0eEndUserService\x12\\\n\x0fIsLegalAccepted\x12#.viam.app.v1.IsLegalAcceptedRequest\x1a$.viam.app.v1.IsLegalAcceptedResponse\x12P\n\x0bAcceptLegal\x12\x1f.viam.app.v1.AcceptLegalRequest\x1a .viam.app.v1.AcceptLegalResponseB\x18Z\x16go.viam.com/api/app/v1b\x06proto3')
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
    _ENDUSERSERVICE._serialized_start = 176
    _ENDUSERSERVICE._serialized_end = 368