# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent/v4beta1/company_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.talent.v4beta1 import common_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_common__pb2
from google.cloud.talent.v4beta1 import company_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_company__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/talent/v4beta1/company_service.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/talent/v4beta1/common.proto\x1a)google/cloud/talent/v4beta1/company.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"\x9a\x01\n\x14\x43reateCompanyRequest\x12<\n\x06parent\x18\x01 \x01(\tB$\xe2\x41\x01\x02\xfa\x41\x1d\x12\x1bjobs.googleapis.com/CompanyR\x06parent\x12\x44\n\x07\x63ompany\x18\x02 \x01(\x0b\x32$.google.cloud.talent.v4beta1.CompanyB\x04\xe2\x41\x01\x02R\x07\x63ompany\"M\n\x11GetCompanyRequest\x12\x38\n\x04name\x18\x01 \x01(\tB$\xe2\x41\x01\x02\xfa\x41\x1d\n\x1bjobs.googleapis.com/CompanyR\x04name\"\x99\x01\n\x14UpdateCompanyRequest\x12\x44\n\x07\x63ompany\x18\x01 \x01(\x0b\x32$.google.cloud.talent.v4beta1.CompanyB\x04\xe2\x41\x01\x02R\x07\x63ompany\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"P\n\x14\x44\x65leteCompanyRequest\x12\x38\n\x04name\x18\x01 \x01(\tB$\xe2\x41\x01\x02\xfa\x41\x1d\n\x1bjobs.googleapis.com/CompanyR\x04name\"\xbc\x01\n\x14ListCompaniesRequest\x12<\n\x06parent\x18\x01 \x01(\tB$\xe2\x41\x01\x02\xfa\x41\x1d\x12\x1bjobs.googleapis.com/CompanyR\x06parent\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12*\n\x11require_open_jobs\x18\x04 \x01(\x08R\x0frequireOpenJobs\"\xce\x01\n\x15ListCompaniesResponse\x12\x42\n\tcompanies\x18\x01 \x03(\x0b\x32$.google.cloud.talent.v4beta1.CompanyR\tcompanies\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12I\n\x08metadata\x18\x03 \x01(\x0b\x32-.google.cloud.talent.v4beta1.ResponseMetadataR\x08metadata2\xd2\t\n\x0e\x43ompanyService\x12\xe3\x01\n\rCreateCompany\x12\x31.google.cloud.talent.v4beta1.CreateCompanyRequest\x1a$.google.cloud.talent.v4beta1.Company\"y\xda\x41\x0eparent,company\x82\xd3\xe4\x93\x02\x62\"0/v4beta1/{parent=projects/*/tenants/*}/companies:\x01*Z+\"&/v4beta1/{parent=projects/*}/companies:\x01*\x12\xcd\x01\n\nGetCompany\x12..google.cloud.talent.v4beta1.GetCompanyRequest\x1a$.google.cloud.talent.v4beta1.Company\"i\xda\x41\x04name\x82\xd3\xe4\x93\x02\\\x12\x30/v4beta1/{name=projects/*/tenants/*/companies/*}Z(\x12&/v4beta1/{name=projects/*/companies/*}\x12\xed\x01\n\rUpdateCompany\x12\x31.google.cloud.talent.v4beta1.UpdateCompanyRequest\x1a$.google.cloud.talent.v4beta1.Company\"\x82\x01\xda\x41\x07\x63ompany\x82\xd3\xe4\x93\x02r28/v4beta1/{company.name=projects/*/tenants/*/companies/*}:\x01*Z32./v4beta1/{company.name=projects/*/companies/*}:\x01*\x12\xc5\x01\n\rDeleteCompany\x12\x31.google.cloud.talent.v4beta1.DeleteCompanyRequest\x1a\x16.google.protobuf.Empty\"i\xda\x41\x04name\x82\xd3\xe4\x93\x02\\*0/v4beta1/{name=projects/*/tenants/*/companies/*}Z(*&/v4beta1/{name=projects/*/companies/*}\x12\xe3\x01\n\rListCompanies\x12\x31.google.cloud.talent.v4beta1.ListCompaniesRequest\x1a\x32.google.cloud.talent.v4beta1.ListCompaniesResponse\"k\xda\x41\x06parent\x82\xd3\xe4\x93\x02\\\x12\x30/v4beta1/{parent=projects/*/tenants/*}/companiesZ(\x12&/v4beta1/{parent=projects/*}/companies\x1al\xca\x41\x13jobs.googleapis.com\xd2\x41Shttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsB\x81\x01\n\x1f\x63om.google.cloud.talent.v4beta1B\x13\x43ompanyServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3')



_CREATECOMPANYREQUEST = DESCRIPTOR.message_types_by_name['CreateCompanyRequest']
_GETCOMPANYREQUEST = DESCRIPTOR.message_types_by_name['GetCompanyRequest']
_UPDATECOMPANYREQUEST = DESCRIPTOR.message_types_by_name['UpdateCompanyRequest']
_DELETECOMPANYREQUEST = DESCRIPTOR.message_types_by_name['DeleteCompanyRequest']
_LISTCOMPANIESREQUEST = DESCRIPTOR.message_types_by_name['ListCompaniesRequest']
_LISTCOMPANIESRESPONSE = DESCRIPTOR.message_types_by_name['ListCompaniesResponse']
CreateCompanyRequest = _reflection.GeneratedProtocolMessageType('CreateCompanyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOMPANYREQUEST,
  '__module__' : 'google.cloud.talent.v4beta1.company_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.CreateCompanyRequest)
  })
_sym_db.RegisterMessage(CreateCompanyRequest)

GetCompanyRequest = _reflection.GeneratedProtocolMessageType('GetCompanyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCOMPANYREQUEST,
  '__module__' : 'google.cloud.talent.v4beta1.company_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.GetCompanyRequest)
  })
_sym_db.RegisterMessage(GetCompanyRequest)

UpdateCompanyRequest = _reflection.GeneratedProtocolMessageType('UpdateCompanyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOMPANYREQUEST,
  '__module__' : 'google.cloud.talent.v4beta1.company_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.UpdateCompanyRequest)
  })
_sym_db.RegisterMessage(UpdateCompanyRequest)

DeleteCompanyRequest = _reflection.GeneratedProtocolMessageType('DeleteCompanyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECOMPANYREQUEST,
  '__module__' : 'google.cloud.talent.v4beta1.company_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.DeleteCompanyRequest)
  })
_sym_db.RegisterMessage(DeleteCompanyRequest)

ListCompaniesRequest = _reflection.GeneratedProtocolMessageType('ListCompaniesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOMPANIESREQUEST,
  '__module__' : 'google.cloud.talent.v4beta1.company_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.ListCompaniesRequest)
  })
_sym_db.RegisterMessage(ListCompaniesRequest)

ListCompaniesResponse = _reflection.GeneratedProtocolMessageType('ListCompaniesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOMPANIESRESPONSE,
  '__module__' : 'google.cloud.talent.v4beta1.company_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.ListCompaniesResponse)
  })
_sym_db.RegisterMessage(ListCompaniesResponse)

_COMPANYSERVICE = DESCRIPTOR.services_by_name['CompanyService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.google.cloud.talent.v4beta1B\023CompanyServiceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS'
  _CREATECOMPANYREQUEST.fields_by_name['parent']._options = None
  _CREATECOMPANYREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\035\022\033jobs.googleapis.com/Company'
  _CREATECOMPANYREQUEST.fields_by_name['company']._options = None
  _CREATECOMPANYREQUEST.fields_by_name['company']._serialized_options = b'\342A\001\002'
  _GETCOMPANYREQUEST.fields_by_name['name']._options = None
  _GETCOMPANYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\035\n\033jobs.googleapis.com/Company'
  _UPDATECOMPANYREQUEST.fields_by_name['company']._options = None
  _UPDATECOMPANYREQUEST.fields_by_name['company']._serialized_options = b'\342A\001\002'
  _DELETECOMPANYREQUEST.fields_by_name['name']._options = None
  _DELETECOMPANYREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\035\n\033jobs.googleapis.com/Company'
  _LISTCOMPANIESREQUEST.fields_by_name['parent']._options = None
  _LISTCOMPANIESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\035\022\033jobs.googleapis.com/Company'
  _COMPANYSERVICE._options = None
  _COMPANYSERVICE._serialized_options = b'\312A\023jobs.googleapis.com\322AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs'
  _COMPANYSERVICE.methods_by_name['CreateCompany']._options = None
  _COMPANYSERVICE.methods_by_name['CreateCompany']._serialized_options = b'\332A\016parent,company\202\323\344\223\002b\"0/v4beta1/{parent=projects/*/tenants/*}/companies:\001*Z+\"&/v4beta1/{parent=projects/*}/companies:\001*'
  _COMPANYSERVICE.methods_by_name['GetCompany']._options = None
  _COMPANYSERVICE.methods_by_name['GetCompany']._serialized_options = b'\332A\004name\202\323\344\223\002\\\0220/v4beta1/{name=projects/*/tenants/*/companies/*}Z(\022&/v4beta1/{name=projects/*/companies/*}'
  _COMPANYSERVICE.methods_by_name['UpdateCompany']._options = None
  _COMPANYSERVICE.methods_by_name['UpdateCompany']._serialized_options = b'\332A\007company\202\323\344\223\002r28/v4beta1/{company.name=projects/*/tenants/*/companies/*}:\001*Z32./v4beta1/{company.name=projects/*/companies/*}:\001*'
  _COMPANYSERVICE.methods_by_name['DeleteCompany']._options = None
  _COMPANYSERVICE.methods_by_name['DeleteCompany']._serialized_options = b'\332A\004name\202\323\344\223\002\\*0/v4beta1/{name=projects/*/tenants/*/companies/*}Z(*&/v4beta1/{name=projects/*/companies/*}'
  _COMPANYSERVICE.methods_by_name['ListCompanies']._options = None
  _COMPANYSERVICE.methods_by_name['ListCompanies']._serialized_options = b'\332A\006parent\202\323\344\223\002\\\0220/v4beta1/{parent=projects/*/tenants/*}/companiesZ(\022&/v4beta1/{parent=projects/*}/companies'
  _CREATECOMPANYREQUEST._serialized_start=346
  _CREATECOMPANYREQUEST._serialized_end=500
  _GETCOMPANYREQUEST._serialized_start=502
  _GETCOMPANYREQUEST._serialized_end=579
  _UPDATECOMPANYREQUEST._serialized_start=582
  _UPDATECOMPANYREQUEST._serialized_end=735
  _DELETECOMPANYREQUEST._serialized_start=737
  _DELETECOMPANYREQUEST._serialized_end=817
  _LISTCOMPANIESREQUEST._serialized_start=820
  _LISTCOMPANIESREQUEST._serialized_end=1008
  _LISTCOMPANIESRESPONSE._serialized_start=1011
  _LISTCOMPANIESRESPONSE._serialized_end=1217
  _COMPANYSERVICE._serialized_start=1220
  _COMPANYSERVICE._serialized_end=2454
# @@protoc_insertion_point(module_scope)
