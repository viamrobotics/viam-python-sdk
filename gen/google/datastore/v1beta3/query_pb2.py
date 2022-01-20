# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/datastore/v1beta3/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.datastore.v1beta3 import entity_pb2 as google_dot_datastore_dot_v1beta3_dot_entity__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/datastore/v1beta3/query.proto\x12\x18google.datastore.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a%google/datastore/v1beta3/entity.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto\"\xcd\x01\n\x0c\x45ntityResult\x12\x38\n\x06\x65ntity\x18\x01 \x01(\x0b\x32 .google.datastore.v1beta3.EntityR\x06\x65ntity\x12\x18\n\x07version\x18\x04 \x01(\x03R\x07version\x12\x16\n\x06\x63ursor\x18\x03 \x01(\x0cR\x06\x63ursor\"Q\n\nResultType\x12\x1b\n\x17RESULT_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\x12\x0e\n\nPROJECTION\x10\x02\x12\x0c\n\x08KEY_ONLY\x10\x03\"\xdf\x03\n\x05Query\x12\x44\n\nprojection\x18\x02 \x03(\x0b\x32$.google.datastore.v1beta3.ProjectionR\nprojection\x12<\n\x04kind\x18\x03 \x03(\x0b\x32(.google.datastore.v1beta3.KindExpressionR\x04kind\x12\x38\n\x06\x66ilter\x18\x04 \x01(\x0b\x32 .google.datastore.v1beta3.FilterR\x06\x66ilter\x12=\n\x05order\x18\x05 \x03(\x0b\x32\'.google.datastore.v1beta3.PropertyOrderR\x05order\x12L\n\x0b\x64istinct_on\x18\x06 \x03(\x0b\x32+.google.datastore.v1beta3.PropertyReferenceR\ndistinctOn\x12!\n\x0cstart_cursor\x18\x07 \x01(\x0cR\x0bstartCursor\x12\x1d\n\nend_cursor\x18\x08 \x01(\x0cR\tendCursor\x12\x16\n\x06offset\x18\n \x01(\x05R\x06offset\x12\x31\n\x05limit\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x05limit\"$\n\x0eKindExpression\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"\'\n\x11PropertyReference\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"U\n\nProjection\x12G\n\x08property\x18\x01 \x01(\x0b\x32+.google.datastore.v1beta3.PropertyReferenceR\x08property\"\xf0\x01\n\rPropertyOrder\x12G\n\x08property\x18\x01 \x01(\x0b\x32+.google.datastore.v1beta3.PropertyReferenceR\x08property\x12O\n\tdirection\x18\x02 \x01(\x0e\x32\x31.google.datastore.v1beta3.PropertyOrder.DirectionR\tdirection\"E\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02\"\xc4\x01\n\x06\x46ilter\x12V\n\x10\x63omposite_filter\x18\x01 \x01(\x0b\x32).google.datastore.v1beta3.CompositeFilterH\x00R\x0f\x63ompositeFilter\x12S\n\x0fproperty_filter\x18\x02 \x01(\x0b\x32(.google.datastore.v1beta3.PropertyFilterH\x00R\x0epropertyFilterB\r\n\x0b\x66ilter_type\"\xc0\x01\n\x0f\x43ompositeFilter\x12\x42\n\x02op\x18\x01 \x01(\x0e\x32\x32.google.datastore.v1beta3.CompositeFilter.OperatorR\x02op\x12:\n\x07\x66ilters\x18\x02 \x03(\x0b\x32 .google.datastore.v1beta3.FilterR\x07\x66ilters\"-\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41ND\x10\x01\"\xeb\x02\n\x0ePropertyFilter\x12G\n\x08property\x18\x01 \x01(\x0b\x32+.google.datastore.v1beta3.PropertyReferenceR\x08property\x12\x41\n\x02op\x18\x02 \x01(\x0e\x32\x31.google.datastore.v1beta3.PropertyFilter.OperatorR\x02op\x12\x35\n\x05value\x18\x03 \x01(\x0b\x32\x1f.google.datastore.v1beta3.ValueR\x05value\"\x95\x01\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\r\n\tLESS_THAN\x10\x01\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x04\x12\t\n\x05\x45QUAL\x10\x05\x12\x10\n\x0cHAS_ANCESTOR\x10\x0b\"\xff\x02\n\x08GqlQuery\x12!\n\x0cquery_string\x18\x01 \x01(\tR\x0bqueryString\x12%\n\x0e\x61llow_literals\x18\x02 \x01(\x08R\rallowLiterals\x12\\\n\x0enamed_bindings\x18\x05 \x03(\x0b\x32\x35.google.datastore.v1beta3.GqlQuery.NamedBindingsEntryR\rnamedBindings\x12\\\n\x13positional_bindings\x18\x04 \x03(\x0b\x32+.google.datastore.v1beta3.GqlQueryParameterR\x12positionalBindings\x1am\n\x12NamedBindingsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32+.google.datastore.v1beta3.GqlQueryParameterR\x05value:\x02\x38\x01\"x\n\x11GqlQueryParameter\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32\x1f.google.datastore.v1beta3.ValueH\x00R\x05value\x12\x18\n\x06\x63ursor\x18\x03 \x01(\x0cH\x00R\x06\x63ursorB\x10\n\x0eparameter_type\"\xd6\x04\n\x10QueryResultBatch\x12\'\n\x0fskipped_results\x18\x06 \x01(\x05R\x0eskippedResults\x12%\n\x0eskipped_cursor\x18\x03 \x01(\x0cR\rskippedCursor\x12_\n\x12\x65ntity_result_type\x18\x01 \x01(\x0e\x32\x31.google.datastore.v1beta3.EntityResult.ResultTypeR\x10\x65ntityResultType\x12M\n\x0e\x65ntity_results\x18\x02 \x03(\x0b\x32&.google.datastore.v1beta3.EntityResultR\rentityResults\x12\x1d\n\nend_cursor\x18\x04 \x01(\x0cR\tendCursor\x12]\n\x0cmore_results\x18\x05 \x01(\x0e\x32:.google.datastore.v1beta3.QueryResultBatch.MoreResultsTypeR\x0bmoreResults\x12)\n\x10snapshot_version\x18\x07 \x01(\x03R\x0fsnapshotVersion\"\x98\x01\n\x0fMoreResultsType\x12!\n\x1dMORE_RESULTS_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_FINISHED\x10\x01\x12\x1c\n\x18MORE_RESULTS_AFTER_LIMIT\x10\x02\x12\x1d\n\x19MORE_RESULTS_AFTER_CURSOR\x10\x04\x12\x13\n\x0fNO_MORE_RESULTS\x10\x03\x42\xd5\x01\n\x1c\x63om.google.datastore.v1beta3B\nQueryProtoP\x01ZAgoogle.golang.org/genproto/googleapis/datastore/v1beta3;datastore\xaa\x02\x1eGoogle.Cloud.Datastore.V1Beta3\xca\x02\x1eGoogle\\Cloud\\Datastore\\V1beta3\xea\x02!Google::Cloud::Datastore::V1beta3b\x06proto3')



_ENTITYRESULT = DESCRIPTOR.message_types_by_name['EntityResult']
_QUERY = DESCRIPTOR.message_types_by_name['Query']
_KINDEXPRESSION = DESCRIPTOR.message_types_by_name['KindExpression']
_PROPERTYREFERENCE = DESCRIPTOR.message_types_by_name['PropertyReference']
_PROJECTION = DESCRIPTOR.message_types_by_name['Projection']
_PROPERTYORDER = DESCRIPTOR.message_types_by_name['PropertyOrder']
_FILTER = DESCRIPTOR.message_types_by_name['Filter']
_COMPOSITEFILTER = DESCRIPTOR.message_types_by_name['CompositeFilter']
_PROPERTYFILTER = DESCRIPTOR.message_types_by_name['PropertyFilter']
_GQLQUERY = DESCRIPTOR.message_types_by_name['GqlQuery']
_GQLQUERY_NAMEDBINDINGSENTRY = _GQLQUERY.nested_types_by_name['NamedBindingsEntry']
_GQLQUERYPARAMETER = DESCRIPTOR.message_types_by_name['GqlQueryParameter']
_QUERYRESULTBATCH = DESCRIPTOR.message_types_by_name['QueryResultBatch']
_ENTITYRESULT_RESULTTYPE = _ENTITYRESULT.enum_types_by_name['ResultType']
_PROPERTYORDER_DIRECTION = _PROPERTYORDER.enum_types_by_name['Direction']
_COMPOSITEFILTER_OPERATOR = _COMPOSITEFILTER.enum_types_by_name['Operator']
_PROPERTYFILTER_OPERATOR = _PROPERTYFILTER.enum_types_by_name['Operator']
_QUERYRESULTBATCH_MORERESULTSTYPE = _QUERYRESULTBATCH.enum_types_by_name['MoreResultsType']
EntityResult = _reflection.GeneratedProtocolMessageType('EntityResult', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYRESULT,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.EntityResult)
  })
_sym_db.RegisterMessage(EntityResult)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.Query)
  })
_sym_db.RegisterMessage(Query)

KindExpression = _reflection.GeneratedProtocolMessageType('KindExpression', (_message.Message,), {
  'DESCRIPTOR' : _KINDEXPRESSION,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.KindExpression)
  })
_sym_db.RegisterMessage(KindExpression)

PropertyReference = _reflection.GeneratedProtocolMessageType('PropertyReference', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTYREFERENCE,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.PropertyReference)
  })
_sym_db.RegisterMessage(PropertyReference)

Projection = _reflection.GeneratedProtocolMessageType('Projection', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTION,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.Projection)
  })
_sym_db.RegisterMessage(Projection)

PropertyOrder = _reflection.GeneratedProtocolMessageType('PropertyOrder', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTYORDER,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.PropertyOrder)
  })
_sym_db.RegisterMessage(PropertyOrder)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
  'DESCRIPTOR' : _FILTER,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.Filter)
  })
_sym_db.RegisterMessage(Filter)

CompositeFilter = _reflection.GeneratedProtocolMessageType('CompositeFilter', (_message.Message,), {
  'DESCRIPTOR' : _COMPOSITEFILTER,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.CompositeFilter)
  })
_sym_db.RegisterMessage(CompositeFilter)

PropertyFilter = _reflection.GeneratedProtocolMessageType('PropertyFilter', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTYFILTER,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.PropertyFilter)
  })
_sym_db.RegisterMessage(PropertyFilter)

GqlQuery = _reflection.GeneratedProtocolMessageType('GqlQuery', (_message.Message,), {

  'NamedBindingsEntry' : _reflection.GeneratedProtocolMessageType('NamedBindingsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GQLQUERY_NAMEDBINDINGSENTRY,
    '__module__' : 'google.datastore.v1beta3.query_pb2'
    # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.GqlQuery.NamedBindingsEntry)
    })
  ,
  'DESCRIPTOR' : _GQLQUERY,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.GqlQuery)
  })
_sym_db.RegisterMessage(GqlQuery)
_sym_db.RegisterMessage(GqlQuery.NamedBindingsEntry)

GqlQueryParameter = _reflection.GeneratedProtocolMessageType('GqlQueryParameter', (_message.Message,), {
  'DESCRIPTOR' : _GQLQUERYPARAMETER,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.GqlQueryParameter)
  })
_sym_db.RegisterMessage(GqlQueryParameter)

QueryResultBatch = _reflection.GeneratedProtocolMessageType('QueryResultBatch', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESULTBATCH,
  '__module__' : 'google.datastore.v1beta3.query_pb2'
  # @@protoc_insertion_point(class_scope:google.datastore.v1beta3.QueryResultBatch)
  })
_sym_db.RegisterMessage(QueryResultBatch)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.google.datastore.v1beta3B\nQueryProtoP\001ZAgoogle.golang.org/genproto/googleapis/datastore/v1beta3;datastore\252\002\036Google.Cloud.Datastore.V1Beta3\312\002\036Google\\Cloud\\Datastore\\V1beta3\352\002!Google::Cloud::Datastore::V1beta3'
  _GQLQUERY_NAMEDBINDINGSENTRY._options = None
  _GQLQUERY_NAMEDBINDINGSENTRY._serialized_options = b'8\001'
  _ENTITYRESULT._serialized_start=194
  _ENTITYRESULT._serialized_end=399
  _ENTITYRESULT_RESULTTYPE._serialized_start=318
  _ENTITYRESULT_RESULTTYPE._serialized_end=399
  _QUERY._serialized_start=402
  _QUERY._serialized_end=881
  _KINDEXPRESSION._serialized_start=883
  _KINDEXPRESSION._serialized_end=919
  _PROPERTYREFERENCE._serialized_start=921
  _PROPERTYREFERENCE._serialized_end=960
  _PROJECTION._serialized_start=962
  _PROJECTION._serialized_end=1047
  _PROPERTYORDER._serialized_start=1050
  _PROPERTYORDER._serialized_end=1290
  _PROPERTYORDER_DIRECTION._serialized_start=1221
  _PROPERTYORDER_DIRECTION._serialized_end=1290
  _FILTER._serialized_start=1293
  _FILTER._serialized_end=1489
  _COMPOSITEFILTER._serialized_start=1492
  _COMPOSITEFILTER._serialized_end=1684
  _COMPOSITEFILTER_OPERATOR._serialized_start=1639
  _COMPOSITEFILTER_OPERATOR._serialized_end=1684
  _PROPERTYFILTER._serialized_start=1687
  _PROPERTYFILTER._serialized_end=2050
  _PROPERTYFILTER_OPERATOR._serialized_start=1901
  _PROPERTYFILTER_OPERATOR._serialized_end=2050
  _GQLQUERY._serialized_start=2053
  _GQLQUERY._serialized_end=2436
  _GQLQUERY_NAMEDBINDINGSENTRY._serialized_start=2327
  _GQLQUERY_NAMEDBINDINGSENTRY._serialized_end=2436
  _GQLQUERYPARAMETER._serialized_start=2438
  _GQLQUERYPARAMETER._serialized_end=2558
  _QUERYRESULTBATCH._serialized_start=2561
  _QUERYRESULTBATCH._serialized_end=3159
  _QUERYRESULTBATCH_MORERESULTSTYPE._serialized_start=3007
  _QUERYRESULTBATCH_MORERESULTSTYPE._serialized_end=3159
# @@protoc_insertion_point(module_scope)
