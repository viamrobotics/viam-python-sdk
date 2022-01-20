# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl/v1/data_items.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.automl.v1 import geometry_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_geometry__pb2
from google.cloud.automl.v1 import io_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_io__pb2
from google.cloud.automl.v1 import text_segment_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_text__segment__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/automl/v1/data_items.proto\x12\x16google.cloud.automl.v1\x1a\x1cgoogle/api/annotations.proto\x1a%google/cloud/automl/v1/geometry.proto\x1a\x1fgoogle/cloud/automl/v1/io.proto\x1a)google/cloud/automl/v1/text_segment.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\"W\n\x05Image\x12!\n\x0bimage_bytes\x18\x01 \x01(\x0cH\x00R\nimageBytes\x12#\n\rthumbnail_uri\x18\x04 \x01(\tR\x0cthumbnailUriB\x06\n\x04\x64\x61ta\"e\n\x0bTextSnippet\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\x12\x1f\n\x0b\x63ontent_uri\x18\x04 \x01(\tR\ncontentUri\"\xff\x01\n\x12\x44ocumentDimensions\x12T\n\x04unit\x18\x01 \x01(\x0e\x32@.google.cloud.automl.v1.DocumentDimensions.DocumentDimensionUnitR\x04unit\x12\x14\n\x05width\x18\x02 \x01(\x02R\x05width\x12\x16\n\x06height\x18\x03 \x01(\x02R\x06height\"e\n\x15\x44ocumentDimensionUnit\x12\'\n#DOCUMENT_DIMENSION_UNIT_UNSPECIFIED\x10\x00\x12\x08\n\x04INCH\x10\x01\x12\x0e\n\nCENTIMETER\x10\x02\x12\t\n\x05POINT\x10\x03\"\xd0\x06\n\x08\x44ocument\x12N\n\x0cinput_config\x18\x01 \x01(\x0b\x32+.google.cloud.automl.v1.DocumentInputConfigR\x0binputConfig\x12H\n\rdocument_text\x18\x02 \x01(\x0b\x32#.google.cloud.automl.v1.TextSnippetR\x0c\x64ocumentText\x12?\n\x06layout\x18\x03 \x03(\x0b\x32\'.google.cloud.automl.v1.Document.LayoutR\x06layout\x12[\n\x13\x64ocument_dimensions\x18\x04 \x01(\x0b\x32*.google.cloud.automl.v1.DocumentDimensionsR\x12\x64ocumentDimensions\x12\x1d\n\npage_count\x18\x05 \x01(\x05R\tpageCount\x1a\xec\x03\n\x06Layout\x12\x46\n\x0ctext_segment\x18\x01 \x01(\x0b\x32#.google.cloud.automl.v1.TextSegmentR\x0btextSegment\x12\x1f\n\x0bpage_number\x18\x02 \x01(\x05R\npageNumber\x12I\n\rbounding_poly\x18\x03 \x01(\x0b\x32$.google.cloud.automl.v1.BoundingPolyR\x0c\x62oundingPoly\x12\x63\n\x11text_segment_type\x18\x04 \x01(\x0e\x32\x37.google.cloud.automl.v1.Document.Layout.TextSegmentTypeR\x0ftextSegmentType\"\xc8\x01\n\x0fTextSegmentType\x12!\n\x1dTEXT_SEGMENT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TOKEN\x10\x01\x12\r\n\tPARAGRAPH\x10\x02\x12\x0e\n\nFORM_FIELD\x10\x03\x12\x13\n\x0f\x46ORM_FIELD_NAME\x10\x04\x12\x17\n\x13\x46ORM_FIELD_CONTENTS\x10\x05\x12\t\n\x05TABLE\x10\x06\x12\x10\n\x0cTABLE_HEADER\x10\x07\x12\r\n\tTABLE_ROW\x10\x08\x12\x0e\n\nTABLE_CELL\x10\t\"\xdc\x01\n\x0e\x45xamplePayload\x12\x35\n\x05image\x18\x01 \x01(\x0b\x32\x1d.google.cloud.automl.v1.ImageH\x00R\x05image\x12H\n\x0ctext_snippet\x18\x02 \x01(\x0b\x32#.google.cloud.automl.v1.TextSnippetH\x00R\x0btextSnippet\x12>\n\x08\x64ocument\x18\x04 \x01(\x0b\x32 .google.cloud.automl.v1.DocumentH\x00R\x08\x64ocumentB\t\n\x07payloadB\xaa\x01\n\x1a\x63om.google.cloud.automl.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')



_IMAGE = DESCRIPTOR.message_types_by_name['Image']
_TEXTSNIPPET = DESCRIPTOR.message_types_by_name['TextSnippet']
_DOCUMENTDIMENSIONS = DESCRIPTOR.message_types_by_name['DocumentDimensions']
_DOCUMENT = DESCRIPTOR.message_types_by_name['Document']
_DOCUMENT_LAYOUT = _DOCUMENT.nested_types_by_name['Layout']
_EXAMPLEPAYLOAD = DESCRIPTOR.message_types_by_name['ExamplePayload']
_DOCUMENTDIMENSIONS_DOCUMENTDIMENSIONUNIT = _DOCUMENTDIMENSIONS.enum_types_by_name['DocumentDimensionUnit']
_DOCUMENT_LAYOUT_TEXTSEGMENTTYPE = _DOCUMENT_LAYOUT.enum_types_by_name['TextSegmentType']
Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'google.cloud.automl.v1.data_items_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.Image)
  })
_sym_db.RegisterMessage(Image)

TextSnippet = _reflection.GeneratedProtocolMessageType('TextSnippet', (_message.Message,), {
  'DESCRIPTOR' : _TEXTSNIPPET,
  '__module__' : 'google.cloud.automl.v1.data_items_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.TextSnippet)
  })
_sym_db.RegisterMessage(TextSnippet)

DocumentDimensions = _reflection.GeneratedProtocolMessageType('DocumentDimensions', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTDIMENSIONS,
  '__module__' : 'google.cloud.automl.v1.data_items_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.DocumentDimensions)
  })
_sym_db.RegisterMessage(DocumentDimensions)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {

  'Layout' : _reflection.GeneratedProtocolMessageType('Layout', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENT_LAYOUT,
    '__module__' : 'google.cloud.automl.v1.data_items_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.Document.Layout)
    })
  ,
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'google.cloud.automl.v1.data_items_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.Document)
  })
_sym_db.RegisterMessage(Document)
_sym_db.RegisterMessage(Document.Layout)

ExamplePayload = _reflection.GeneratedProtocolMessageType('ExamplePayload', (_message.Message,), {
  'DESCRIPTOR' : _EXAMPLEPAYLOAD,
  '__module__' : 'google.cloud.automl.v1.data_items_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ExamplePayload)
  })
_sym_db.RegisterMessage(ExamplePayload)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.google.cloud.automl.v1P\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoMl\\V1\352\002\031Google::Cloud::AutoML::V1'
  _IMAGE._serialized_start=301
  _IMAGE._serialized_end=388
  _TEXTSNIPPET._serialized_start=390
  _TEXTSNIPPET._serialized_end=491
  _DOCUMENTDIMENSIONS._serialized_start=494
  _DOCUMENTDIMENSIONS._serialized_end=749
  _DOCUMENTDIMENSIONS_DOCUMENTDIMENSIONUNIT._serialized_start=648
  _DOCUMENTDIMENSIONS_DOCUMENTDIMENSIONUNIT._serialized_end=749
  _DOCUMENT._serialized_start=752
  _DOCUMENT._serialized_end=1600
  _DOCUMENT_LAYOUT._serialized_start=1108
  _DOCUMENT_LAYOUT._serialized_end=1600
  _DOCUMENT_LAYOUT_TEXTSEGMENTTYPE._serialized_start=1400
  _DOCUMENT_LAYOUT_TEXTSEGMENTTYPE._serialized_end=1600
  _EXAMPLEPAYLOAD._serialized_start=1603
  _EXAMPLEPAYLOAD._serialized_end=1823
# @@protoc_insertion_point(module_scope)
