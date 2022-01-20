# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/vision/v1p1beta1/web_detection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/vision/v1p1beta1/web_detection.proto\x12\x1dgoogle.cloud.vision.v1p1beta1\x1a\x1cgoogle/api/annotations.proto\"\x86\t\n\x0cWebDetection\x12X\n\x0cweb_entities\x18\x01 \x03(\x0b\x32\x35.google.cloud.vision.v1p1beta1.WebDetection.WebEntityR\x0bwebEntities\x12\x66\n\x14\x66ull_matching_images\x18\x02 \x03(\x0b\x32\x34.google.cloud.vision.v1p1beta1.WebDetection.WebImageR\x12\x66ullMatchingImages\x12l\n\x17partial_matching_images\x18\x03 \x03(\x0b\x32\x34.google.cloud.vision.v1p1beta1.WebDetection.WebImageR\x15partialMatchingImages\x12p\n\x1apages_with_matching_images\x18\x04 \x03(\x0b\x32\x33.google.cloud.vision.v1p1beta1.WebDetection.WebPageR\x17pagesWithMatchingImages\x12l\n\x17visually_similar_images\x18\x06 \x03(\x0b\x32\x34.google.cloud.vision.v1p1beta1.WebDetection.WebImageR\x15visuallySimilarImages\x12`\n\x11\x62\x65st_guess_labels\x18\x08 \x03(\x0b\x32\x34.google.cloud.vision.v1p1beta1.WebDetection.WebLabelR\x0f\x62\x65stGuessLabels\x1a`\n\tWebEntity\x12\x1b\n\tentity_id\x18\x01 \x01(\tR\x08\x65ntityId\x12\x14\n\x05score\x18\x02 \x01(\x02R\x05score\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x1a\x32\n\x08WebImage\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x14\n\x05score\x18\x02 \x01(\x02R\x05score\x1a\xa6\x02\n\x07WebPage\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x14\n\x05score\x18\x02 \x01(\x02R\x05score\x12\x1d\n\npage_title\x18\x03 \x01(\tR\tpageTitle\x12\x66\n\x14\x66ull_matching_images\x18\x04 \x03(\x0b\x32\x34.google.cloud.vision.v1p1beta1.WebDetection.WebImageR\x12\x66ullMatchingImages\x12l\n\x17partial_matching_images\x18\x05 \x03(\x0b\x32\x34.google.cloud.vision.v1p1beta1.WebDetection.WebImageR\x15partialMatchingImages\x1a\x45\n\x08WebLabel\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\x12#\n\rlanguage_code\x18\x02 \x01(\tR\x0clanguageCodeB\x80\x01\n!com.google.cloud.vision.v1p1beta1B\x11WebDetectionProtoP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/vision/v1p1beta1;vision\xf8\x01\x01\x62\x06proto3')



_WEBDETECTION = DESCRIPTOR.message_types_by_name['WebDetection']
_WEBDETECTION_WEBENTITY = _WEBDETECTION.nested_types_by_name['WebEntity']
_WEBDETECTION_WEBIMAGE = _WEBDETECTION.nested_types_by_name['WebImage']
_WEBDETECTION_WEBPAGE = _WEBDETECTION.nested_types_by_name['WebPage']
_WEBDETECTION_WEBLABEL = _WEBDETECTION.nested_types_by_name['WebLabel']
WebDetection = _reflection.GeneratedProtocolMessageType('WebDetection', (_message.Message,), {

  'WebEntity' : _reflection.GeneratedProtocolMessageType('WebEntity', (_message.Message,), {
    'DESCRIPTOR' : _WEBDETECTION_WEBENTITY,
    '__module__' : 'google.cloud.vision.v1p1beta1.web_detection_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p1beta1.WebDetection.WebEntity)
    })
  ,

  'WebImage' : _reflection.GeneratedProtocolMessageType('WebImage', (_message.Message,), {
    'DESCRIPTOR' : _WEBDETECTION_WEBIMAGE,
    '__module__' : 'google.cloud.vision.v1p1beta1.web_detection_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p1beta1.WebDetection.WebImage)
    })
  ,

  'WebPage' : _reflection.GeneratedProtocolMessageType('WebPage', (_message.Message,), {
    'DESCRIPTOR' : _WEBDETECTION_WEBPAGE,
    '__module__' : 'google.cloud.vision.v1p1beta1.web_detection_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p1beta1.WebDetection.WebPage)
    })
  ,

  'WebLabel' : _reflection.GeneratedProtocolMessageType('WebLabel', (_message.Message,), {
    'DESCRIPTOR' : _WEBDETECTION_WEBLABEL,
    '__module__' : 'google.cloud.vision.v1p1beta1.web_detection_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p1beta1.WebDetection.WebLabel)
    })
  ,
  'DESCRIPTOR' : _WEBDETECTION,
  '__module__' : 'google.cloud.vision.v1p1beta1.web_detection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p1beta1.WebDetection)
  })
_sym_db.RegisterMessage(WebDetection)
_sym_db.RegisterMessage(WebDetection.WebEntity)
_sym_db.RegisterMessage(WebDetection.WebImage)
_sym_db.RegisterMessage(WebDetection.WebPage)
_sym_db.RegisterMessage(WebDetection.WebLabel)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.cloud.vision.v1p1beta1B\021WebDetectionProtoP\001ZCgoogle.golang.org/genproto/googleapis/cloud/vision/v1p1beta1;vision\370\001\001'
  _WEBDETECTION._serialized_start=115
  _WEBDETECTION._serialized_end=1273
  _WEBDETECTION_WEBENTITY._serialized_start=757
  _WEBDETECTION_WEBENTITY._serialized_end=853
  _WEBDETECTION_WEBIMAGE._serialized_start=855
  _WEBDETECTION_WEBIMAGE._serialized_end=905
  _WEBDETECTION_WEBPAGE._serialized_start=908
  _WEBDETECTION_WEBPAGE._serialized_end=1202
  _WEBDETECTION_WEBLABEL._serialized_start=1204
  _WEBDETECTION_WEBLABEL._serialized_end=1273
# @@protoc_insertion_point(module_scope)
