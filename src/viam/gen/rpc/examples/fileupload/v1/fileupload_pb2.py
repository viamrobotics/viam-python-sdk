"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1proto/rpc/examples/fileupload/v1/fileupload.proto\x12 proto.rpc.examples.fileupload.v1"R\n\x11UploadFileRequest\x12\x14\n\x04name\x18\x01 \x01(\tH\x00R\x04name\x12\x1f\n\nchunk_data\x18\x02 \x01(\x0cH\x00R\tchunkDataB\x06\n\x04data"<\n\x12UploadFileResponse\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04size\x18\x02 \x01(\x03R\x04size2\x92\x01\n\x11FileUploadService\x12}\n\nUploadFile\x123.proto.rpc.examples.fileupload.v1.UploadFileRequest\x1a4.proto.rpc.examples.fileupload.v1.UploadFileResponse"\x00(\x010\x01B4Z2go.viam.com/utils/proto/rpc/examples/fileupload/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.rpc.examples.fileupload.v1.fileupload_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2go.viam.com/utils/proto/rpc/examples/fileupload/v1'
    _UPLOADFILEREQUEST._serialized_start = 87
    _UPLOADFILEREQUEST._serialized_end = 169
    _UPLOADFILERESPONSE._serialized_start = 171
    _UPLOADFILERESPONSE._serialized_end = 231
    _FILEUPLOADSERVICE._serialized_start = 234
    _FILEUPLOADSERVICE._serialized_end = 380