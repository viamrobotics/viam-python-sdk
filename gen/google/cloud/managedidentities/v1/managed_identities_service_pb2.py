# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/managedidentities/v1/managed_identities_service.proto
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
from google.cloud.managedidentities.v1 import resource_pb2 as google_dot_cloud_dot_managedidentities_dot_v1_dot_resource__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/cloud/managedidentities/v1/managed_identities_service.proto\x12!google.cloud.managedidentities.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x30google/cloud/managedidentities/v1/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa8\x02\n\nOpMetadata\x12\x41\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12;\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x07\x65ndTime\x12\x1c\n\x06target\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x06target\x12\x18\n\x04verb\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03R\x04verb\x12;\n\x16requested_cancellation\x18\x05 \x01(\x08\x42\x04\xe2\x41\x01\x03R\x15requestedCancellation\x12%\n\x0b\x61pi_version\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03R\napiVersion\"\xda\x01\n\x1e\x43reateMicrosoftAdDomainRequest\x12H\n\x06parent\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\x12\'managedidentities.googleapis.com/DomainR\x06parent\x12%\n\x0b\x64omain_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\ndomainName\x12G\n\x06\x64omain\x18\x03 \x01(\x0b\x32).google.cloud.managedidentities.v1.DomainB\x04\xe2\x41\x01\x02R\x06\x64omain\"a\n\x19ResetAdminPasswordRequest\x12\x44\n\x04name\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\n\'managedidentities.googleapis.com/DomainR\x04name\"8\n\x1aResetAdminPasswordResponse\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password\"\xe5\x01\n\x12ListDomainsRequest\x12H\n\x06parent\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\x12\'managedidentities.googleapis.com/DomainR\x06parent\x12!\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\x12\x1c\n\x06\x66ilter\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01R\x06\x66ilter\x12\x1f\n\x08order_by\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01R\x07orderBy\"\xa4\x01\n\x13ListDomainsResponse\x12\x43\n\x07\x64omains\x18\x01 \x03(\x0b\x32).google.cloud.managedidentities.v1.DomainR\x07\x64omains\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12 \n\x0bunreachable\x18\x03 \x03(\tR\x0bunreachable\"X\n\x10GetDomainRequest\x12\x44\n\x04name\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\n\'managedidentities.googleapis.com/DomainR\x04name\"\xa1\x01\n\x13UpdateDomainRequest\x12\x41\n\x0bupdate_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\x12G\n\x06\x64omain\x18\x02 \x01(\x0b\x32).google.cloud.managedidentities.v1.DomainB\x04\xe2\x41\x01\x02R\x06\x64omain\"[\n\x13\x44\x65leteDomainRequest\x12\x44\n\x04name\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\n\'managedidentities.googleapis.com/DomainR\x04name\"\xa0\x01\n\x12\x41ttachTrustRequest\x12\x44\n\x04name\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\n\'managedidentities.googleapis.com/DomainR\x04name\x12\x44\n\x05trust\x18\x02 \x01(\x0b\x32(.google.cloud.managedidentities.v1.TrustB\x04\xe2\x41\x01\x02R\x05trust\"\xd0\x01\n\x17ReconfigureTrustRequest\x12\x44\n\x04name\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\n\'managedidentities.googleapis.com/DomainR\x04name\x12\x32\n\x12target_domain_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x10targetDomainName\x12;\n\x17target_dns_ip_addresses\x18\x03 \x03(\tB\x04\xe2\x41\x01\x02R\x14targetDnsIpAddresses\"\xa0\x01\n\x12\x44\x65tachTrustRequest\x12\x44\n\x04name\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\n\'managedidentities.googleapis.com/DomainR\x04name\x12\x44\n\x05trust\x18\x02 \x01(\x0b\x32(.google.cloud.managedidentities.v1.TrustB\x04\xe2\x41\x01\x02R\x05trust\"\xa2\x01\n\x14ValidateTrustRequest\x12\x44\n\x04name\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\n\'managedidentities.googleapis.com/DomainR\x04name\x12\x44\n\x05trust\x18\x02 \x01(\x0b\x32(.google.cloud.managedidentities.v1.TrustB\x04\xe2\x41\x01\x02R\x05trust2\xf2\x11\n\x18ManagedIdentitiesService\x12\xf0\x01\n\x17\x43reateMicrosoftAdDomain\x12\x41.google.cloud.managedidentities.v1.CreateMicrosoftAdDomainRequest\x1a\x1d.google.longrunning.Operation\"s\xca\x41\x14\n\x06\x44omain\x12\nOpMetadata\xda\x41\x19parent,domain_name,domain\x82\xd3\xe4\x93\x02:\"0/v1/{parent=projects/*/locations/global}/domains:\x06\x64omain\x12\xe8\x01\n\x12ResetAdminPassword\x12<.google.cloud.managedidentities.v1.ResetAdminPasswordRequest\x1a=.google.cloud.managedidentities.v1.ResetAdminPasswordResponse\"U\xda\x41\x04name\x82\xd3\xe4\x93\x02H\"C/v1/{name=projects/*/locations/global/domains/*}:resetAdminPassword:\x01*\x12\xbf\x01\n\x0bListDomains\x12\x35.google.cloud.managedidentities.v1.ListDomainsRequest\x1a\x36.google.cloud.managedidentities.v1.ListDomainsResponse\"A\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x32\x12\x30/v1/{parent=projects/*/locations/global}/domains\x12\xac\x01\n\tGetDomain\x12\x33.google.cloud.managedidentities.v1.GetDomainRequest\x1a).google.cloud.managedidentities.v1.Domain\"?\xda\x41\x04name\x82\xd3\xe4\x93\x02\x32\x12\x30/v1/{name=projects/*/locations/global/domains/*}\x12\xda\x01\n\x0cUpdateDomain\x12\x36.google.cloud.managedidentities.v1.UpdateDomainRequest\x1a\x1d.google.longrunning.Operation\"s\xca\x41\x14\n\x06\x44omain\x12\nOpMetadata\xda\x41\x12\x64omain,update_mask\x82\xd3\xe4\x93\x02\x41\x32\x37/v1/{domain.name=projects/*/locations/global/domains/*}:\x06\x64omain\x12\xcc\x01\n\x0c\x44\x65leteDomain\x12\x36.google.cloud.managedidentities.v1.DeleteDomainRequest\x1a\x1d.google.longrunning.Operation\"e\xca\x41#\n\x15google.protobuf.Empty\x12\nOpMetadata\xda\x41\x04name\x82\xd3\xe4\x93\x02\x32*0/v1/{name=projects/*/locations/global/domains/*}\x12\xd0\x01\n\x0b\x41ttachTrust\x12\x35.google.cloud.managedidentities.v1.AttachTrustRequest\x1a\x1d.google.longrunning.Operation\"k\xca\x41\x14\n\x06\x44omain\x12\nOpMetadata\xda\x41\nname,trust\x82\xd3\xe4\x93\x02\x41\"</v1/{name=projects/*/locations/global/domains/*}:attachTrust:\x01*\x12\x85\x02\n\x10ReconfigureTrust\x12:.google.cloud.managedidentities.v1.ReconfigureTrustRequest\x1a\x1d.google.longrunning.Operation\"\x95\x01\xca\x41\x14\n\x06\x44omain\x12\nOpMetadata\xda\x41/name,target_domain_name,target_dns_ip_addresses\x82\xd3\xe4\x93\x02\x46\"A/v1/{name=projects/*/locations/global/domains/*}:reconfigureTrust:\x01*\x12\xd0\x01\n\x0b\x44\x65tachTrust\x12\x35.google.cloud.managedidentities.v1.DetachTrustRequest\x1a\x1d.google.longrunning.Operation\"k\xca\x41\x14\n\x06\x44omain\x12\nOpMetadata\xda\x41\nname,trust\x82\xd3\xe4\x93\x02\x41\"</v1/{name=projects/*/locations/global/domains/*}:detachTrust:\x01*\x12\xd6\x01\n\rValidateTrust\x12\x37.google.cloud.managedidentities.v1.ValidateTrustRequest\x1a\x1d.google.longrunning.Operation\"m\xca\x41\x14\n\x06\x44omain\x12\nOpMetadata\xda\x41\nname,trust\x82\xd3\xe4\x93\x02\x43\">/v1/{name=projects/*/locations/global/domains/*}:validateTrust:\x01*\x1aT\xca\x41 managedidentities.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x92\x02\n%com.google.cloud.managedidentities.v1B\x1dManagedIdentitiesServiceProtoP\x01ZRgoogle.golang.org/genproto/googleapis/cloud/managedidentities/v1;managedidentities\xa2\x02\x04GCMI\xaa\x02!Google.Cloud.ManagedIdentities.V1\xca\x02!Google\\Cloud\\ManagedIdentities\\V1\xea\x02$Google::Cloud::ManagedIdentities::V1b\x06proto3')



_OPMETADATA = DESCRIPTOR.message_types_by_name['OpMetadata']
_CREATEMICROSOFTADDOMAINREQUEST = DESCRIPTOR.message_types_by_name['CreateMicrosoftAdDomainRequest']
_RESETADMINPASSWORDREQUEST = DESCRIPTOR.message_types_by_name['ResetAdminPasswordRequest']
_RESETADMINPASSWORDRESPONSE = DESCRIPTOR.message_types_by_name['ResetAdminPasswordResponse']
_LISTDOMAINSREQUEST = DESCRIPTOR.message_types_by_name['ListDomainsRequest']
_LISTDOMAINSRESPONSE = DESCRIPTOR.message_types_by_name['ListDomainsResponse']
_GETDOMAINREQUEST = DESCRIPTOR.message_types_by_name['GetDomainRequest']
_UPDATEDOMAINREQUEST = DESCRIPTOR.message_types_by_name['UpdateDomainRequest']
_DELETEDOMAINREQUEST = DESCRIPTOR.message_types_by_name['DeleteDomainRequest']
_ATTACHTRUSTREQUEST = DESCRIPTOR.message_types_by_name['AttachTrustRequest']
_RECONFIGURETRUSTREQUEST = DESCRIPTOR.message_types_by_name['ReconfigureTrustRequest']
_DETACHTRUSTREQUEST = DESCRIPTOR.message_types_by_name['DetachTrustRequest']
_VALIDATETRUSTREQUEST = DESCRIPTOR.message_types_by_name['ValidateTrustRequest']
OpMetadata = _reflection.GeneratedProtocolMessageType('OpMetadata', (_message.Message,), {
  'DESCRIPTOR' : _OPMETADATA,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.OpMetadata)
  })
_sym_db.RegisterMessage(OpMetadata)

CreateMicrosoftAdDomainRequest = _reflection.GeneratedProtocolMessageType('CreateMicrosoftAdDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMICROSOFTADDOMAINREQUEST,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.CreateMicrosoftAdDomainRequest)
  })
_sym_db.RegisterMessage(CreateMicrosoftAdDomainRequest)

ResetAdminPasswordRequest = _reflection.GeneratedProtocolMessageType('ResetAdminPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETADMINPASSWORDREQUEST,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.ResetAdminPasswordRequest)
  })
_sym_db.RegisterMessage(ResetAdminPasswordRequest)

ResetAdminPasswordResponse = _reflection.GeneratedProtocolMessageType('ResetAdminPasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETADMINPASSWORDRESPONSE,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.ResetAdminPasswordResponse)
  })
_sym_db.RegisterMessage(ResetAdminPasswordResponse)

ListDomainsRequest = _reflection.GeneratedProtocolMessageType('ListDomainsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOMAINSREQUEST,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.ListDomainsRequest)
  })
_sym_db.RegisterMessage(ListDomainsRequest)

ListDomainsResponse = _reflection.GeneratedProtocolMessageType('ListDomainsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOMAINSRESPONSE,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.ListDomainsResponse)
  })
_sym_db.RegisterMessage(ListDomainsResponse)

GetDomainRequest = _reflection.GeneratedProtocolMessageType('GetDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDOMAINREQUEST,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.GetDomainRequest)
  })
_sym_db.RegisterMessage(GetDomainRequest)

UpdateDomainRequest = _reflection.GeneratedProtocolMessageType('UpdateDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDOMAINREQUEST,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.UpdateDomainRequest)
  })
_sym_db.RegisterMessage(UpdateDomainRequest)

DeleteDomainRequest = _reflection.GeneratedProtocolMessageType('DeleteDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDOMAINREQUEST,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.DeleteDomainRequest)
  })
_sym_db.RegisterMessage(DeleteDomainRequest)

AttachTrustRequest = _reflection.GeneratedProtocolMessageType('AttachTrustRequest', (_message.Message,), {
  'DESCRIPTOR' : _ATTACHTRUSTREQUEST,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.AttachTrustRequest)
  })
_sym_db.RegisterMessage(AttachTrustRequest)

ReconfigureTrustRequest = _reflection.GeneratedProtocolMessageType('ReconfigureTrustRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECONFIGURETRUSTREQUEST,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.ReconfigureTrustRequest)
  })
_sym_db.RegisterMessage(ReconfigureTrustRequest)

DetachTrustRequest = _reflection.GeneratedProtocolMessageType('DetachTrustRequest', (_message.Message,), {
  'DESCRIPTOR' : _DETACHTRUSTREQUEST,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.DetachTrustRequest)
  })
_sym_db.RegisterMessage(DetachTrustRequest)

ValidateTrustRequest = _reflection.GeneratedProtocolMessageType('ValidateTrustRequest', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATETRUSTREQUEST,
  '__module__' : 'google.cloud.managedidentities.v1.managed_identities_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.managedidentities.v1.ValidateTrustRequest)
  })
_sym_db.RegisterMessage(ValidateTrustRequest)

_MANAGEDIDENTITIESSERVICE = DESCRIPTOR.services_by_name['ManagedIdentitiesService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.cloud.managedidentities.v1B\035ManagedIdentitiesServiceProtoP\001ZRgoogle.golang.org/genproto/googleapis/cloud/managedidentities/v1;managedidentities\242\002\004GCMI\252\002!Google.Cloud.ManagedIdentities.V1\312\002!Google\\Cloud\\ManagedIdentities\\V1\352\002$Google::Cloud::ManagedIdentities::V1'
  _OPMETADATA.fields_by_name['create_time']._options = None
  _OPMETADATA.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _OPMETADATA.fields_by_name['end_time']._options = None
  _OPMETADATA.fields_by_name['end_time']._serialized_options = b'\342A\001\003'
  _OPMETADATA.fields_by_name['target']._options = None
  _OPMETADATA.fields_by_name['target']._serialized_options = b'\342A\001\003'
  _OPMETADATA.fields_by_name['verb']._options = None
  _OPMETADATA.fields_by_name['verb']._serialized_options = b'\342A\001\003'
  _OPMETADATA.fields_by_name['requested_cancellation']._options = None
  _OPMETADATA.fields_by_name['requested_cancellation']._serialized_options = b'\342A\001\003'
  _OPMETADATA.fields_by_name['api_version']._options = None
  _OPMETADATA.fields_by_name['api_version']._serialized_options = b'\342A\001\003'
  _CREATEMICROSOFTADDOMAINREQUEST.fields_by_name['parent']._options = None
  _CREATEMICROSOFTADDOMAINREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A)\022\'managedidentities.googleapis.com/Domain'
  _CREATEMICROSOFTADDOMAINREQUEST.fields_by_name['domain_name']._options = None
  _CREATEMICROSOFTADDOMAINREQUEST.fields_by_name['domain_name']._serialized_options = b'\342A\001\002'
  _CREATEMICROSOFTADDOMAINREQUEST.fields_by_name['domain']._options = None
  _CREATEMICROSOFTADDOMAINREQUEST.fields_by_name['domain']._serialized_options = b'\342A\001\002'
  _RESETADMINPASSWORDREQUEST.fields_by_name['name']._options = None
  _RESETADMINPASSWORDREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A)\n\'managedidentities.googleapis.com/Domain'
  _LISTDOMAINSREQUEST.fields_by_name['parent']._options = None
  _LISTDOMAINSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A)\022\'managedidentities.googleapis.com/Domain'
  _LISTDOMAINSREQUEST.fields_by_name['page_size']._options = None
  _LISTDOMAINSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTDOMAINSREQUEST.fields_by_name['page_token']._options = None
  _LISTDOMAINSREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTDOMAINSREQUEST.fields_by_name['filter']._options = None
  _LISTDOMAINSREQUEST.fields_by_name['filter']._serialized_options = b'\342A\001\001'
  _LISTDOMAINSREQUEST.fields_by_name['order_by']._options = None
  _LISTDOMAINSREQUEST.fields_by_name['order_by']._serialized_options = b'\342A\001\001'
  _GETDOMAINREQUEST.fields_by_name['name']._options = None
  _GETDOMAINREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A)\n\'managedidentities.googleapis.com/Domain'
  _UPDATEDOMAINREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEDOMAINREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _UPDATEDOMAINREQUEST.fields_by_name['domain']._options = None
  _UPDATEDOMAINREQUEST.fields_by_name['domain']._serialized_options = b'\342A\001\002'
  _DELETEDOMAINREQUEST.fields_by_name['name']._options = None
  _DELETEDOMAINREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A)\n\'managedidentities.googleapis.com/Domain'
  _ATTACHTRUSTREQUEST.fields_by_name['name']._options = None
  _ATTACHTRUSTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A)\n\'managedidentities.googleapis.com/Domain'
  _ATTACHTRUSTREQUEST.fields_by_name['trust']._options = None
  _ATTACHTRUSTREQUEST.fields_by_name['trust']._serialized_options = b'\342A\001\002'
  _RECONFIGURETRUSTREQUEST.fields_by_name['name']._options = None
  _RECONFIGURETRUSTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A)\n\'managedidentities.googleapis.com/Domain'
  _RECONFIGURETRUSTREQUEST.fields_by_name['target_domain_name']._options = None
  _RECONFIGURETRUSTREQUEST.fields_by_name['target_domain_name']._serialized_options = b'\342A\001\002'
  _RECONFIGURETRUSTREQUEST.fields_by_name['target_dns_ip_addresses']._options = None
  _RECONFIGURETRUSTREQUEST.fields_by_name['target_dns_ip_addresses']._serialized_options = b'\342A\001\002'
  _DETACHTRUSTREQUEST.fields_by_name['name']._options = None
  _DETACHTRUSTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A)\n\'managedidentities.googleapis.com/Domain'
  _DETACHTRUSTREQUEST.fields_by_name['trust']._options = None
  _DETACHTRUSTREQUEST.fields_by_name['trust']._serialized_options = b'\342A\001\002'
  _VALIDATETRUSTREQUEST.fields_by_name['name']._options = None
  _VALIDATETRUSTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A)\n\'managedidentities.googleapis.com/Domain'
  _VALIDATETRUSTREQUEST.fields_by_name['trust']._options = None
  _VALIDATETRUSTREQUEST.fields_by_name['trust']._serialized_options = b'\342A\001\002'
  _MANAGEDIDENTITIESSERVICE._options = None
  _MANAGEDIDENTITIESSERVICE._serialized_options = b'\312A managedidentities.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _MANAGEDIDENTITIESSERVICE.methods_by_name['CreateMicrosoftAdDomain']._options = None
  _MANAGEDIDENTITIESSERVICE.methods_by_name['CreateMicrosoftAdDomain']._serialized_options = b'\312A\024\n\006Domain\022\nOpMetadata\332A\031parent,domain_name,domain\202\323\344\223\002:\"0/v1/{parent=projects/*/locations/global}/domains:\006domain'
  _MANAGEDIDENTITIESSERVICE.methods_by_name['ResetAdminPassword']._options = None
  _MANAGEDIDENTITIESSERVICE.methods_by_name['ResetAdminPassword']._serialized_options = b'\332A\004name\202\323\344\223\002H\"C/v1/{name=projects/*/locations/global/domains/*}:resetAdminPassword:\001*'
  _MANAGEDIDENTITIESSERVICE.methods_by_name['ListDomains']._options = None
  _MANAGEDIDENTITIESSERVICE.methods_by_name['ListDomains']._serialized_options = b'\332A\006parent\202\323\344\223\0022\0220/v1/{parent=projects/*/locations/global}/domains'
  _MANAGEDIDENTITIESSERVICE.methods_by_name['GetDomain']._options = None
  _MANAGEDIDENTITIESSERVICE.methods_by_name['GetDomain']._serialized_options = b'\332A\004name\202\323\344\223\0022\0220/v1/{name=projects/*/locations/global/domains/*}'
  _MANAGEDIDENTITIESSERVICE.methods_by_name['UpdateDomain']._options = None
  _MANAGEDIDENTITIESSERVICE.methods_by_name['UpdateDomain']._serialized_options = b'\312A\024\n\006Domain\022\nOpMetadata\332A\022domain,update_mask\202\323\344\223\002A27/v1/{domain.name=projects/*/locations/global/domains/*}:\006domain'
  _MANAGEDIDENTITIESSERVICE.methods_by_name['DeleteDomain']._options = None
  _MANAGEDIDENTITIESSERVICE.methods_by_name['DeleteDomain']._serialized_options = b'\312A#\n\025google.protobuf.Empty\022\nOpMetadata\332A\004name\202\323\344\223\0022*0/v1/{name=projects/*/locations/global/domains/*}'
  _MANAGEDIDENTITIESSERVICE.methods_by_name['AttachTrust']._options = None
  _MANAGEDIDENTITIESSERVICE.methods_by_name['AttachTrust']._serialized_options = b'\312A\024\n\006Domain\022\nOpMetadata\332A\nname,trust\202\323\344\223\002A\"</v1/{name=projects/*/locations/global/domains/*}:attachTrust:\001*'
  _MANAGEDIDENTITIESSERVICE.methods_by_name['ReconfigureTrust']._options = None
  _MANAGEDIDENTITIESSERVICE.methods_by_name['ReconfigureTrust']._serialized_options = b'\312A\024\n\006Domain\022\nOpMetadata\332A/name,target_domain_name,target_dns_ip_addresses\202\323\344\223\002F\"A/v1/{name=projects/*/locations/global/domains/*}:reconfigureTrust:\001*'
  _MANAGEDIDENTITIESSERVICE.methods_by_name['DetachTrust']._options = None
  _MANAGEDIDENTITIESSERVICE.methods_by_name['DetachTrust']._serialized_options = b'\312A\024\n\006Domain\022\nOpMetadata\332A\nname,trust\202\323\344\223\002A\"</v1/{name=projects/*/locations/global/domains/*}:detachTrust:\001*'
  _MANAGEDIDENTITIESSERVICE.methods_by_name['ValidateTrust']._options = None
  _MANAGEDIDENTITIESSERVICE.methods_by_name['ValidateTrust']._serialized_options = b'\312A\024\n\006Domain\022\nOpMetadata\332A\nname,trust\202\323\344\223\002C\">/v1/{name=projects/*/locations/global/domains/*}:validateTrust:\001*'
  _OPMETADATA._serialized_start=375
  _OPMETADATA._serialized_end=671
  _CREATEMICROSOFTADDOMAINREQUEST._serialized_start=674
  _CREATEMICROSOFTADDOMAINREQUEST._serialized_end=892
  _RESETADMINPASSWORDREQUEST._serialized_start=894
  _RESETADMINPASSWORDREQUEST._serialized_end=991
  _RESETADMINPASSWORDRESPONSE._serialized_start=993
  _RESETADMINPASSWORDRESPONSE._serialized_end=1049
  _LISTDOMAINSREQUEST._serialized_start=1052
  _LISTDOMAINSREQUEST._serialized_end=1281
  _LISTDOMAINSRESPONSE._serialized_start=1284
  _LISTDOMAINSRESPONSE._serialized_end=1448
  _GETDOMAINREQUEST._serialized_start=1450
  _GETDOMAINREQUEST._serialized_end=1538
  _UPDATEDOMAINREQUEST._serialized_start=1541
  _UPDATEDOMAINREQUEST._serialized_end=1702
  _DELETEDOMAINREQUEST._serialized_start=1704
  _DELETEDOMAINREQUEST._serialized_end=1795
  _ATTACHTRUSTREQUEST._serialized_start=1798
  _ATTACHTRUSTREQUEST._serialized_end=1958
  _RECONFIGURETRUSTREQUEST._serialized_start=1961
  _RECONFIGURETRUSTREQUEST._serialized_end=2169
  _DETACHTRUSTREQUEST._serialized_start=2172
  _DETACHTRUSTREQUEST._serialized_end=2332
  _VALIDATETRUSTREQUEST._serialized_start=2335
  _VALIDATETRUSTREQUEST._serialized_end=2497
  _MANAGEDIDENTITIESSERVICE._serialized_start=2500
  _MANAGEDIDENTITIESSERVICE._serialized_end=4790
# @@protoc_insertion_point(module_scope)
