"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16tagger/v1/tagger.proto\x12\ttagger.v1\x1a google/protobuf/descriptor.proto:3\n\x04tags\x12\x1d.google.protobuf.FieldOptions\x18\xc3\xe03 \x01(\tR\x04tags:>\n\noneof_tags\x12\x1d.google.protobuf.OneofOptions\x18\xc3\xe03 \x01(\tR\toneofTagsB4Z2github.com/srikrsna/protoc-gen-gotag/tagger;taggerb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tagger.v1.tagger_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(tags)
    google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(oneof_tags)
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/srikrsna/protoc-gen-gotag/tagger;tagger'