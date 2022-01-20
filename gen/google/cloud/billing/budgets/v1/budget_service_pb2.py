# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/billing/budgets/v1/budget_service.proto
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
from google.cloud.billing.budgets.v1 import budget_model_pb2 as google_dot_cloud_dot_billing_dot_budgets_dot_v1_dot_budget__model__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/billing/budgets/v1/budget_service.proto\x12\x1fgoogle.cloud.billing.budgets.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x32google/cloud/billing/budgets/v1/budget_model.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"\xa3\x01\n\x13\x43reateBudgetRequest\x12\x45\n\x06parent\x18\x01 \x01(\tB-\xe2\x41\x01\x02\xfa\x41&\x12$billingbudgets.googleapis.com/BudgetR\x06parent\x12\x45\n\x06\x62udget\x18\x02 \x01(\x0b\x32\'.google.cloud.billing.budgets.v1.BudgetB\x04\xe2\x41\x01\x02R\x06\x62udget\"\x9f\x01\n\x13UpdateBudgetRequest\x12\x45\n\x06\x62udget\x18\x01 \x01(\x0b\x32\'.google.cloud.billing.budgets.v1.BudgetB\x04\xe2\x41\x01\x02R\x06\x62udget\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01R\nupdateMask\"U\n\x10GetBudgetRequest\x12\x41\n\x04name\x18\x01 \x01(\tB-\xe2\x41\x01\x02\xfa\x41&\n$billingbudgets.googleapis.com/BudgetR\x04name\"\xa3\x01\n\x12ListBudgetsRequest\x12\x45\n\x06parent\x18\x01 \x01(\tB-\xe2\x41\x01\x02\xfa\x41&\x12$billingbudgets.googleapis.com/BudgetR\x06parent\x12!\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\"\x80\x01\n\x13ListBudgetsResponse\x12\x41\n\x07\x62udgets\x18\x01 \x03(\x0b\x32\'.google.cloud.billing.budgets.v1.BudgetR\x07\x62udgets\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"X\n\x13\x44\x65leteBudgetRequest\x12\x41\n\x04name\x18\x01 \x01(\tB-\xe2\x41\x01\x02\xfa\x41&\n$billingbudgets.googleapis.com/BudgetR\x04name2\xf7\x07\n\rBudgetService\x12\xb5\x01\n\x0c\x43reateBudget\x12\x34.google.cloud.billing.budgets.v1.CreateBudgetRequest\x1a\'.google.cloud.billing.budgets.v1.Budget\"F\xda\x41\rparent,budget\x82\xd3\xe4\x93\x02\x30\"&/v1/{parent=billingAccounts/*}/budgets:\x06\x62udget\x12\xc1\x01\n\x0cUpdateBudget\x12\x34.google.cloud.billing.budgets.v1.UpdateBudgetRequest\x1a\'.google.cloud.billing.budgets.v1.Budget\"R\xda\x41\x12\x62udget,update_mask\x82\xd3\xe4\x93\x02\x37\x32-/v1/{budget.name=billingAccounts/*/budgets/*}:\x06\x62udget\x12\x9e\x01\n\tGetBudget\x12\x31.google.cloud.billing.budgets.v1.GetBudgetRequest\x1a\'.google.cloud.billing.budgets.v1.Budget\"5\xda\x41\x04name\x82\xd3\xe4\x93\x02(\x12&/v1/{name=billingAccounts/*/budgets/*}\x12\xb1\x01\n\x0bListBudgets\x12\x33.google.cloud.billing.budgets.v1.ListBudgetsRequest\x1a\x34.google.cloud.billing.budgets.v1.ListBudgetsResponse\"7\xda\x41\x06parent\x82\xd3\xe4\x93\x02(\x12&/v1/{parent=billingAccounts/*}/budgets\x12\x93\x01\n\x0c\x44\x65leteBudget\x12\x34.google.cloud.billing.budgets.v1.DeleteBudgetRequest\x1a\x16.google.protobuf.Empty\"5\xda\x41\x04name\x82\xd3\xe4\x93\x02(*&/v1/{name=billingAccounts/*/budgets/*}\x1a\x7f\xca\x41\x1d\x62illingbudgets.googleapis.com\xd2\x41\\https://www.googleapis.com/auth/cloud-billing,https://www.googleapis.com/auth/cloud-platformB\x83\x01\n#com.google.cloud.billing.budgets.v1B\x12\x42udgetServiceProtoP\x01ZFgoogle.golang.org/genproto/googleapis/cloud/billing/budgets/v1;budgetsb\x06proto3')



_CREATEBUDGETREQUEST = DESCRIPTOR.message_types_by_name['CreateBudgetRequest']
_UPDATEBUDGETREQUEST = DESCRIPTOR.message_types_by_name['UpdateBudgetRequest']
_GETBUDGETREQUEST = DESCRIPTOR.message_types_by_name['GetBudgetRequest']
_LISTBUDGETSREQUEST = DESCRIPTOR.message_types_by_name['ListBudgetsRequest']
_LISTBUDGETSRESPONSE = DESCRIPTOR.message_types_by_name['ListBudgetsResponse']
_DELETEBUDGETREQUEST = DESCRIPTOR.message_types_by_name['DeleteBudgetRequest']
CreateBudgetRequest = _reflection.GeneratedProtocolMessageType('CreateBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBUDGETREQUEST,
  '__module__' : 'google.cloud.billing.budgets.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1.CreateBudgetRequest)
  })
_sym_db.RegisterMessage(CreateBudgetRequest)

UpdateBudgetRequest = _reflection.GeneratedProtocolMessageType('UpdateBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBUDGETREQUEST,
  '__module__' : 'google.cloud.billing.budgets.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1.UpdateBudgetRequest)
  })
_sym_db.RegisterMessage(UpdateBudgetRequest)

GetBudgetRequest = _reflection.GeneratedProtocolMessageType('GetBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBUDGETREQUEST,
  '__module__' : 'google.cloud.billing.budgets.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1.GetBudgetRequest)
  })
_sym_db.RegisterMessage(GetBudgetRequest)

ListBudgetsRequest = _reflection.GeneratedProtocolMessageType('ListBudgetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBUDGETSREQUEST,
  '__module__' : 'google.cloud.billing.budgets.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1.ListBudgetsRequest)
  })
_sym_db.RegisterMessage(ListBudgetsRequest)

ListBudgetsResponse = _reflection.GeneratedProtocolMessageType('ListBudgetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBUDGETSRESPONSE,
  '__module__' : 'google.cloud.billing.budgets.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1.ListBudgetsResponse)
  })
_sym_db.RegisterMessage(ListBudgetsResponse)

DeleteBudgetRequest = _reflection.GeneratedProtocolMessageType('DeleteBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBUDGETREQUEST,
  '__module__' : 'google.cloud.billing.budgets.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.billing.budgets.v1.DeleteBudgetRequest)
  })
_sym_db.RegisterMessage(DeleteBudgetRequest)

_BUDGETSERVICE = DESCRIPTOR.services_by_name['BudgetService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.billing.budgets.v1B\022BudgetServiceProtoP\001ZFgoogle.golang.org/genproto/googleapis/cloud/billing/budgets/v1;budgets'
  _CREATEBUDGETREQUEST.fields_by_name['parent']._options = None
  _CREATEBUDGETREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A&\022$billingbudgets.googleapis.com/Budget'
  _CREATEBUDGETREQUEST.fields_by_name['budget']._options = None
  _CREATEBUDGETREQUEST.fields_by_name['budget']._serialized_options = b'\342A\001\002'
  _UPDATEBUDGETREQUEST.fields_by_name['budget']._options = None
  _UPDATEBUDGETREQUEST.fields_by_name['budget']._serialized_options = b'\342A\001\002'
  _UPDATEBUDGETREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEBUDGETREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\001'
  _GETBUDGETREQUEST.fields_by_name['name']._options = None
  _GETBUDGETREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A&\n$billingbudgets.googleapis.com/Budget'
  _LISTBUDGETSREQUEST.fields_by_name['parent']._options = None
  _LISTBUDGETSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A&\022$billingbudgets.googleapis.com/Budget'
  _LISTBUDGETSREQUEST.fields_by_name['page_size']._options = None
  _LISTBUDGETSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTBUDGETSREQUEST.fields_by_name['page_token']._options = None
  _LISTBUDGETSREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _DELETEBUDGETREQUEST.fields_by_name['name']._options = None
  _DELETEBUDGETREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A&\n$billingbudgets.googleapis.com/Budget'
  _BUDGETSERVICE._options = None
  _BUDGETSERVICE._serialized_options = b'\312A\035billingbudgets.googleapis.com\322A\\https://www.googleapis.com/auth/cloud-billing,https://www.googleapis.com/auth/cloud-platform'
  _BUDGETSERVICE.methods_by_name['CreateBudget']._options = None
  _BUDGETSERVICE.methods_by_name['CreateBudget']._serialized_options = b'\332A\rparent,budget\202\323\344\223\0020\"&/v1/{parent=billingAccounts/*}/budgets:\006budget'
  _BUDGETSERVICE.methods_by_name['UpdateBudget']._options = None
  _BUDGETSERVICE.methods_by_name['UpdateBudget']._serialized_options = b'\332A\022budget,update_mask\202\323\344\223\00272-/v1/{budget.name=billingAccounts/*/budgets/*}:\006budget'
  _BUDGETSERVICE.methods_by_name['GetBudget']._options = None
  _BUDGETSERVICE.methods_by_name['GetBudget']._serialized_options = b'\332A\004name\202\323\344\223\002(\022&/v1/{name=billingAccounts/*/budgets/*}'
  _BUDGETSERVICE.methods_by_name['ListBudgets']._options = None
  _BUDGETSERVICE.methods_by_name['ListBudgets']._serialized_options = b'\332A\006parent\202\323\344\223\002(\022&/v1/{parent=billingAccounts/*}/budgets'
  _BUDGETSERVICE.methods_by_name['DeleteBudget']._options = None
  _BUDGETSERVICE.methods_by_name['DeleteBudget']._serialized_options = b'\332A\004name\202\323\344\223\002(*&/v1/{name=billingAccounts/*/budgets/*}'
  _CREATEBUDGETREQUEST._serialized_start=320
  _CREATEBUDGETREQUEST._serialized_end=483
  _UPDATEBUDGETREQUEST._serialized_start=486
  _UPDATEBUDGETREQUEST._serialized_end=645
  _GETBUDGETREQUEST._serialized_start=647
  _GETBUDGETREQUEST._serialized_end=732
  _LISTBUDGETSREQUEST._serialized_start=735
  _LISTBUDGETSREQUEST._serialized_end=898
  _LISTBUDGETSRESPONSE._serialized_start=901
  _LISTBUDGETSRESPONSE._serialized_end=1029
  _DELETEBUDGETREQUEST._serialized_start=1031
  _DELETEBUDGETREQUEST._serialized_end=1119
  _BUDGETSERVICE._serialized_start=1122
  _BUDGETSERVICE._serialized_end=2137
# @@protoc_insertion_point(module_scope)
