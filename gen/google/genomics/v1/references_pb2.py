# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/genomics/v1/references.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/genomics/v1/references.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\"\xd9\x01\n\tReference\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06length\x18\x02 \x01(\x03R\x06length\x12 \n\x0bmd5checksum\x18\x03 \x01(\tR\x0bmd5checksum\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x1d\n\nsource_uri\x18\x05 \x01(\tR\tsourceUri\x12+\n\x11source_accessions\x18\x06 \x03(\tR\x10sourceAccessions\x12\"\n\rncbi_taxon_id\x18\x07 \x01(\x05R\x0bncbiTaxonId\"\x98\x02\n\x0cReferenceSet\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12#\n\rreference_ids\x18\x02 \x03(\tR\x0creferenceIds\x12 \n\x0bmd5checksum\x18\x03 \x01(\tR\x0bmd5checksum\x12\"\n\rncbi_taxon_id\x18\x04 \x01(\x05R\x0bncbiTaxonId\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12\x1f\n\x0b\x61ssembly_id\x18\x06 \x01(\tR\nassemblyId\x12\x1d\n\nsource_uri\x18\x07 \x01(\tR\tsourceUri\x12+\n\x11source_accessions\x18\x08 \x03(\tR\x10sourceAccessions\"\xbd\x01\n\x1aSearchReferenceSetsRequest\x12\"\n\x0cmd5checksums\x18\x01 \x03(\tR\x0cmd5checksums\x12\x1e\n\naccessions\x18\x02 \x03(\tR\naccessions\x12\x1f\n\x0b\x61ssembly_id\x18\x03 \x01(\tR\nassemblyId\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x05 \x01(\x05R\x08pageSize\"\x8e\x01\n\x1bSearchReferenceSetsResponse\x12G\n\x0ereference_sets\x18\x01 \x03(\x0b\x32 .google.genomics.v1.ReferenceSetR\rreferenceSets\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"B\n\x16GetReferenceSetRequest\x12(\n\x10reference_set_id\x18\x01 \x01(\tR\x0ereferenceSetId\"\xc3\x01\n\x17SearchReferencesRequest\x12\"\n\x0cmd5checksums\x18\x01 \x03(\tR\x0cmd5checksums\x12\x1e\n\naccessions\x18\x02 \x03(\tR\naccessions\x12(\n\x10reference_set_id\x18\x03 \x01(\tR\x0ereferenceSetId\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x05 \x01(\x05R\x08pageSize\"\x81\x01\n\x18SearchReferencesResponse\x12=\n\nreferences\x18\x01 \x03(\x0b\x32\x1d.google.genomics.v1.ReferenceR\nreferences\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"8\n\x13GetReferenceRequest\x12!\n\x0creference_id\x18\x01 \x01(\tR\x0breferenceId\"\x99\x01\n\x10ListBasesRequest\x12!\n\x0creference_id\x18\x01 \x01(\tR\x0breferenceId\x12\x14\n\x05start\x18\x02 \x01(\x03R\x05start\x12\x10\n\x03\x65nd\x18\x03 \x01(\x03R\x03\x65nd\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x05 \x01(\x05R\x08pageSize\"o\n\x11ListBasesResponse\x12\x16\n\x06offset\x18\x01 \x01(\x03R\x06offset\x12\x1a\n\x08sequence\x18\x02 \x01(\tR\x08sequence\x12&\n\x0fnext_page_token\x18\x03 \x01(\tR\rnextPageToken2\xdb\x05\n\x12ReferenceServiceV1\x12\x9b\x01\n\x13SearchReferenceSets\x12..google.genomics.v1.SearchReferenceSetsRequest\x1a/.google.genomics.v1.SearchReferenceSetsResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/v1/referencesets/search:\x01*\x12\x8d\x01\n\x0fGetReferenceSet\x12*.google.genomics.v1.GetReferenceSetRequest\x1a .google.genomics.v1.ReferenceSet\",\x82\xd3\xe4\x93\x02&\x12$/v1/referencesets/{reference_set_id}\x12\x8f\x01\n\x10SearchReferences\x12+.google.genomics.v1.SearchReferencesRequest\x1a,.google.genomics.v1.SearchReferencesResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v1/references/search:\x01*\x12}\n\x0cGetReference\x12\'.google.genomics.v1.GetReferenceRequest\x1a\x1d.google.genomics.v1.Reference\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/references/{reference_id}\x12\x85\x01\n\tListBases\x12$.google.genomics.v1.ListBasesRequest\x1a%.google.genomics.v1.ListBasesResponse\"+\x82\xd3\xe4\x93\x02%\x12#/v1/references/{reference_id}/basesBj\n\x16\x63om.google.genomics.v1B\x0fReferencesProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01\x62\x06proto3')



_REFERENCE = DESCRIPTOR.message_types_by_name['Reference']
_REFERENCESET = DESCRIPTOR.message_types_by_name['ReferenceSet']
_SEARCHREFERENCESETSREQUEST = DESCRIPTOR.message_types_by_name['SearchReferenceSetsRequest']
_SEARCHREFERENCESETSRESPONSE = DESCRIPTOR.message_types_by_name['SearchReferenceSetsResponse']
_GETREFERENCESETREQUEST = DESCRIPTOR.message_types_by_name['GetReferenceSetRequest']
_SEARCHREFERENCESREQUEST = DESCRIPTOR.message_types_by_name['SearchReferencesRequest']
_SEARCHREFERENCESRESPONSE = DESCRIPTOR.message_types_by_name['SearchReferencesResponse']
_GETREFERENCEREQUEST = DESCRIPTOR.message_types_by_name['GetReferenceRequest']
_LISTBASESREQUEST = DESCRIPTOR.message_types_by_name['ListBasesRequest']
_LISTBASESRESPONSE = DESCRIPTOR.message_types_by_name['ListBasesResponse']
Reference = _reflection.GeneratedProtocolMessageType('Reference', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCE,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.Reference)
  })
_sym_db.RegisterMessage(Reference)

ReferenceSet = _reflection.GeneratedProtocolMessageType('ReferenceSet', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCESET,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.ReferenceSet)
  })
_sym_db.RegisterMessage(ReferenceSet)

SearchReferenceSetsRequest = _reflection.GeneratedProtocolMessageType('SearchReferenceSetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREFERENCESETSREQUEST,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.SearchReferenceSetsRequest)
  })
_sym_db.RegisterMessage(SearchReferenceSetsRequest)

SearchReferenceSetsResponse = _reflection.GeneratedProtocolMessageType('SearchReferenceSetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREFERENCESETSRESPONSE,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.SearchReferenceSetsResponse)
  })
_sym_db.RegisterMessage(SearchReferenceSetsResponse)

GetReferenceSetRequest = _reflection.GeneratedProtocolMessageType('GetReferenceSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREFERENCESETREQUEST,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.GetReferenceSetRequest)
  })
_sym_db.RegisterMessage(GetReferenceSetRequest)

SearchReferencesRequest = _reflection.GeneratedProtocolMessageType('SearchReferencesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREFERENCESREQUEST,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.SearchReferencesRequest)
  })
_sym_db.RegisterMessage(SearchReferencesRequest)

SearchReferencesResponse = _reflection.GeneratedProtocolMessageType('SearchReferencesResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREFERENCESRESPONSE,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.SearchReferencesResponse)
  })
_sym_db.RegisterMessage(SearchReferencesResponse)

GetReferenceRequest = _reflection.GeneratedProtocolMessageType('GetReferenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREFERENCEREQUEST,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.GetReferenceRequest)
  })
_sym_db.RegisterMessage(GetReferenceRequest)

ListBasesRequest = _reflection.GeneratedProtocolMessageType('ListBasesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBASESREQUEST,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.ListBasesRequest)
  })
_sym_db.RegisterMessage(ListBasesRequest)

ListBasesResponse = _reflection.GeneratedProtocolMessageType('ListBasesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBASESRESPONSE,
  '__module__' : 'google.genomics.v1.references_pb2'
  # @@protoc_insertion_point(class_scope:google.genomics.v1.ListBasesResponse)
  })
_sym_db.RegisterMessage(ListBasesResponse)

_REFERENCESERVICEV1 = DESCRIPTOR.services_by_name['ReferenceServiceV1']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.google.genomics.v1B\017ReferencesProtoP\001Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\370\001\001'
  _REFERENCESERVICEV1.methods_by_name['SearchReferenceSets']._options = None
  _REFERENCESERVICEV1.methods_by_name['SearchReferenceSets']._serialized_options = b'\202\323\344\223\002\035\"\030/v1/referencesets/search:\001*'
  _REFERENCESERVICEV1.methods_by_name['GetReferenceSet']._options = None
  _REFERENCESERVICEV1.methods_by_name['GetReferenceSet']._serialized_options = b'\202\323\344\223\002&\022$/v1/referencesets/{reference_set_id}'
  _REFERENCESERVICEV1.methods_by_name['SearchReferences']._options = None
  _REFERENCESERVICEV1.methods_by_name['SearchReferences']._serialized_options = b'\202\323\344\223\002\032\"\025/v1/references/search:\001*'
  _REFERENCESERVICEV1.methods_by_name['GetReference']._options = None
  _REFERENCESERVICEV1.methods_by_name['GetReference']._serialized_options = b'\202\323\344\223\002\037\022\035/v1/references/{reference_id}'
  _REFERENCESERVICEV1.methods_by_name['ListBases']._options = None
  _REFERENCESERVICEV1.methods_by_name['ListBases']._serialized_options = b'\202\323\344\223\002%\022#/v1/references/{reference_id}/bases'
  _REFERENCE._serialized_start=90
  _REFERENCE._serialized_end=307
  _REFERENCESET._serialized_start=310
  _REFERENCESET._serialized_end=590
  _SEARCHREFERENCESETSREQUEST._serialized_start=593
  _SEARCHREFERENCESETSREQUEST._serialized_end=782
  _SEARCHREFERENCESETSRESPONSE._serialized_start=785
  _SEARCHREFERENCESETSRESPONSE._serialized_end=927
  _GETREFERENCESETREQUEST._serialized_start=929
  _GETREFERENCESETREQUEST._serialized_end=995
  _SEARCHREFERENCESREQUEST._serialized_start=998
  _SEARCHREFERENCESREQUEST._serialized_end=1193
  _SEARCHREFERENCESRESPONSE._serialized_start=1196
  _SEARCHREFERENCESRESPONSE._serialized_end=1325
  _GETREFERENCEREQUEST._serialized_start=1327
  _GETREFERENCEREQUEST._serialized_end=1383
  _LISTBASESREQUEST._serialized_start=1386
  _LISTBASESREQUEST._serialized_end=1539
  _LISTBASESRESPONSE._serialized_start=1541
  _LISTBASESRESPONSE._serialized_end=1652
  _REFERENCESERVICEV1._serialized_start=1655
  _REFERENCESERVICEV1._serialized_end=2386
# @@protoc_insertion_point(module_scope)
