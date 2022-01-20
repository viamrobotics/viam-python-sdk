# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/genomics/v1/readgroup.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"google/genomics/v1/readgroup.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xca\x06\n\tReadGroup\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\ndataset_id\x18\x02 \x01(\tR\tdatasetId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x1b\n\tsample_id\x18\x05 \x01(\tR\x08sampleId\x12H\n\nexperiment\x18\x06 \x01(\x0b\x32(.google.genomics.v1.ReadGroup.ExperimentR\nexperiment\x12\x32\n\x15predicted_insert_size\x18\x07 \x01(\x05R\x13predictedInsertSize\x12\x41\n\x08programs\x18\n \x03(\x0b\x32%.google.genomics.v1.ReadGroup.ProgramR\x08programs\x12(\n\x10reference_set_id\x18\x0b \x01(\tR\x0ereferenceSetId\x12;\n\x04info\x18\x0c \x03(\x0b\x32\'.google.genomics.v1.ReadGroup.InfoEntryR\x04info\x1a\xa8\x01\n\nExperiment\x12\x1d\n\nlibrary_id\x18\x01 \x01(\tR\tlibraryId\x12#\n\rplatform_unit\x18\x02 \x01(\tR\x0cplatformUnit\x12+\n\x11sequencing_center\x18\x03 \x01(\tR\x10sequencingCenter\x12)\n\x10instrument_model\x18\x04 \x01(\tR\x0finstrumentModel\x1a\x92\x01\n\x07Program\x12!\n\x0c\x63ommand_line\x18\x01 \x01(\tR\x0b\x63ommandLine\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12&\n\x0fprev_program_id\x18\x04 \x01(\tR\rprevProgramId\x12\x18\n\x07version\x18\x05 \x01(\tR\x07version\x1aS\n\tInfoEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValueR\x05value:\x02\x38\x01\x42i\n\x16\x63om.google.genomics.v1B\x0eReadGroupProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01\x62\x06proto3')



_READGROUP = DESCRIPTOR.message_types_by_name['ReadGroup']
_READGROUP_EXPERIMENT = _READGROUP.nested_types_by_name['Experiment']
_READGROUP_PROGRAM = _READGROUP.nested_types_by_name['Program']
_READGROUP_INFOENTRY = _READGROUP.nested_types_by_name['InfoEntry']
ReadGroup = _reflection.GeneratedProtocolMessageType('ReadGroup', (_message.Message,), {

  'Experiment' : _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), {
    'DESCRIPTOR' : _READGROUP_EXPERIMENT,
    '__module__' : 'google.genomics.v1.readgroup_pb2'
    # @@protoc_insertion_point(class_scope:google.genomics.v1.ReadGroup.Experiment)
    })
  ,

  'Program' : _reflection.GeneratedProtocolMessageType('Program', (_message.Message,), {
    'DESCRIPTOR' : _READGROUP_PROGRAM,
    '__module__' : 'google.genomics.v1.readgroup_pb2'
    # @@protoc_insertion_point(class_scope:google.genomics.v1.ReadGroup.Program)
    })
  ,

  'InfoEntry' : _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), {
    'DESCRIPTOR' : _READGROUP_INFOENTRY,
    '__module__' : 'google.genomics.v1.readgroup_pb2'
    # @@protoc_insertion_point(class_scope:google.genomics.v1.ReadGroup.InfoEntry)
    })
  ,
  'DESCRIPTOR' : _READGROUP,
  '__module__' : 'google.genomics.v1.readgroup_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.ReadGroup)
  })
_sym_db.RegisterMessage(ReadGroup)
_sym_db.RegisterMessage(ReadGroup.Experiment)
_sym_db.RegisterMessage(ReadGroup.Program)
_sym_db.RegisterMessage(ReadGroup.InfoEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.google.genomics.v1B\016ReadGroupProtoP\001Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\370\001\001'
  _READGROUP_INFOENTRY._options = None
  _READGROUP_INFOENTRY._serialized_options = b'8\001'
  _READGROUP._serialized_start=119
  _READGROUP._serialized_end=961
  _READGROUP_EXPERIMENT._serialized_start=559
  _READGROUP_EXPERIMENT._serialized_end=727
  _READGROUP_PROGRAM._serialized_start=730
  _READGROUP_PROGRAM._serialized_end=876
  _READGROUP_INFOENTRY._serialized_start=878
  _READGROUP_INFOENTRY._serialized_end=961
# @@protoc_insertion_point(module_scope)
