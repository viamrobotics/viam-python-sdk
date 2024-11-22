"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 2, '', 'app/v1/billing.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14app/v1/billing.proto\x12\x0bviam.app.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\x8e\x02\n\x0eInvoiceSummary\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12=\n\x0cinvoice_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0binvoiceDate\x12%\n\x0einvoice_amount\x18\x03 \x01(\x01R\rinvoiceAmount\x12\x16\n\x06status\x18\x04 \x01(\tR\x06status\x125\n\x08due_date\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07dueDate\x127\n\tpaid_date\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\x08paidDate"S\n\x11PaymentMethodCard\x12\x14\n\x05brand\x18\x01 \x01(\tR\x05brand\x12(\n\x10last_four_digits\x18\x02 \x01(\tR\x0elastFourDigits"4\n\x1bGetCurrentMonthUsageRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"`\n\tUsageCost\x12?\n\rresource_type\x18\x01 \x01(\x0e2\x1a.viam.app.v1.UsageCostTypeR\x0cresourceType\x12\x12\n\x04cost\x18\x02 \x01(\x01R\x04cost"\xc6\x01\n\x1aResourceUsageCostsBySource\x128\n\x0bsource_type\x18\x01 \x01(\x0e2\x17.viam.app.v1.SourceTypeR\nsourceType\x12Q\n\x14resource_usage_costs\x18\x02 \x01(\x0b2\x1f.viam.app.v1.ResourceUsageCostsR\x12resourceUsageCosts\x12\x1b\n\ttier_name\x18\x03 \x01(\tR\x08tierName"\xcf\x01\n\x12ResourceUsageCosts\x127\n\x0busage_costs\x18\x01 \x03(\x0b2\x16.viam.app.v1.UsageCostR\nusageCosts\x12\x1a\n\x08discount\x18\x02 \x01(\x01R\x08discount\x12.\n\x13total_with_discount\x18\x03 \x01(\x01R\x11totalWithDiscount\x124\n\x16total_without_discount\x18\x04 \x01(\x01R\x14totalWithoutDiscount"\xcd\x07\n\x1cGetCurrentMonthUsageResponse\x129\n\nstart_date\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\tstartDate\x125\n\x08end_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07endDate\x12k\n\x1eresource_usage_costs_by_source\x18\x0e \x03(\x0b2\'.viam.app.v1.ResourceUsageCostsBySourceR\x1aresourceUsageCostsBySource\x12\x1a\n\x08subtotal\x18\x0f \x01(\x01R\x08subtotal\x12;\n\x18cloud_storage_usage_cost\x18\x03 \x01(\x01B\x02\x18\x01R\x15cloudStorageUsageCost\x127\n\x16data_upload_usage_cost\x18\x04 \x01(\x01B\x02\x18\x01R\x13dataUploadUsageCost\x125\n\x15data_egres_usage_cost\x18\x05 \x01(\x01B\x02\x18\x01R\x12dataEgresUsageCost\x12=\n\x19remote_control_usage_cost\x18\x06 \x01(\x01B\x02\x18\x01R\x16remoteControlUsageCost\x12A\n\x1bstandard_compute_usage_cost\x18\x07 \x01(\x01B\x02\x18\x01R\x18standardComputeUsageCost\x12+\n\x0fdiscount_amount\x18\x08 \x01(\x01B\x02\x18\x01R\x0ediscountAmount\x12=\n\x19total_usage_with_discount\x18\t \x01(\x01B\x02\x18\x01R\x16totalUsageWithDiscount\x12C\n\x1ctotal_usage_without_discount\x18\n \x01(\x01B\x02\x18\x01R\x19totalUsageWithoutDiscount\x127\n\x16per_machine_usage_cost\x18\x0b \x01(\x01B\x02\x18\x01R\x13perMachineUsageCost\x12Q\n$binary_data_cloud_storage_usage_cost\x18\x0c \x01(\x01B\x02\x18\x01R\x1fbinaryDataCloudStorageUsageCost\x12F\n\x1eother_cloud_storage_usage_cost\x18\r \x01(\x01B\x02\x18\x01R\x1aotherCloudStorageUsageCost"8\n\x1fGetOrgBillingInformationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\xfc\x01\n GetOrgBillingInformationResponse\x122\n\x04type\x18\x01 \x01(\x0e2\x1e.viam.app.v1.PaymentMethodTypeR\x04type\x12#\n\rbilling_email\x18\x02 \x01(\tR\x0cbillingEmail\x12;\n\x06method\x18\x03 \x01(\x0b2\x1e.viam.app.v1.PaymentMethodCardH\x00R\x06method\x88\x01\x01\x12&\n\x0cbilling_tier\x18\x04 \x01(\tH\x01R\x0bbillingTier\x88\x01\x01B\t\n\x07_methodB\x0f\n\r_billing_tier"2\n\x19GetInvoicesSummaryRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\x86\x01\n\x1aGetInvoicesSummaryResponse\x12/\n\x13outstanding_balance\x18\x01 \x01(\x01R\x12outstandingBalance\x127\n\x08invoices\x18\x02 \x03(\x0b2\x1b.viam.app.v1.InvoiceSummaryR\x08invoices"=\n\x14GetInvoicePdfRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId"-\n\x15GetInvoicePdfResponse\x12\x14\n\x05chunk\x18\x01 \x01(\x0cR\x05chunk"z\n\x1fSendPaymentRequiredEmailRequest\x12&\n\x0fcustomer_org_id\x18\x01 \x01(\tR\rcustomerOrgId\x12/\n\x14billing_owner_org_id\x18\x02 \x01(\tR\x11billingOwnerOrgId""\n SendPaymentRequiredEmailResponse*V\n\x11PaymentMethodType\x12#\n\x1fPAYMENT_METHOD_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18PAYMENT_METHOD_TYPE_CARD\x10\x01*\xd8\x02\n\rUsageCostType\x12\x1f\n\x1bUSAGE_COST_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bUSAGE_COST_TYPE_DATA_UPLOAD\x10\x01\x12\x1f\n\x1bUSAGE_COST_TYPE_DATA_EGRESS\x10\x02\x12"\n\x1eUSAGE_COST_TYPE_REMOTE_CONTROL\x10\x03\x12$\n USAGE_COST_TYPE_STANDARD_COMPUTE\x10\x04\x12!\n\x1dUSAGE_COST_TYPE_CLOUD_STORAGE\x10\x05\x12-\n)USAGE_COST_TYPE_BINARY_DATA_CLOUD_STORAGE\x10\x06\x12\'\n#USAGE_COST_TYPE_OTHER_CLOUD_STORAGE\x10\x07\x12\x1f\n\x1bUSAGE_COST_TYPE_PER_MACHINE\x10\x08*X\n\nSourceType\x12\x1b\n\x17SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSOURCE_TYPE_ORG\x10\x01\x12\x18\n\x14SOURCE_TYPE_FRAGMENT\x10\x022\xb0\x04\n\x0eBillingService\x12k\n\x14GetCurrentMonthUsage\x12(.viam.app.v1.GetCurrentMonthUsageRequest\x1a).viam.app.v1.GetCurrentMonthUsageResponse\x12w\n\x18GetOrgBillingInformation\x12,.viam.app.v1.GetOrgBillingInformationRequest\x1a-.viam.app.v1.GetOrgBillingInformationResponse\x12e\n\x12GetInvoicesSummary\x12&.viam.app.v1.GetInvoicesSummaryRequest\x1a\'.viam.app.v1.GetInvoicesSummaryResponse\x12X\n\rGetInvoicePdf\x12!.viam.app.v1.GetInvoicePdfRequest\x1a".viam.app.v1.GetInvoicePdfResponse0\x01\x12w\n\x18SendPaymentRequiredEmail\x12,.viam.app.v1.SendPaymentRequiredEmailRequest\x1a-.viam.app.v1.SendPaymentRequiredEmailResponseB\x18Z\x16go.viam.com/api/app/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.v1.billing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x16go.viam.com/api/app/v1'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['cloud_storage_usage_cost']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['cloud_storage_usage_cost']._serialized_options = b'\x18\x01'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['data_upload_usage_cost']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['data_upload_usage_cost']._serialized_options = b'\x18\x01'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['data_egres_usage_cost']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['data_egres_usage_cost']._serialized_options = b'\x18\x01'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['remote_control_usage_cost']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['remote_control_usage_cost']._serialized_options = b'\x18\x01'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['standard_compute_usage_cost']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['standard_compute_usage_cost']._serialized_options = b'\x18\x01'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['discount_amount']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['discount_amount']._serialized_options = b'\x18\x01'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['total_usage_with_discount']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['total_usage_with_discount']._serialized_options = b'\x18\x01'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['total_usage_without_discount']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['total_usage_without_discount']._serialized_options = b'\x18\x01'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['per_machine_usage_cost']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['per_machine_usage_cost']._serialized_options = b'\x18\x01'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['binary_data_cloud_storage_usage_cost']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['binary_data_cloud_storage_usage_cost']._serialized_options = b'\x18\x01'
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['other_cloud_storage_usage_cost']._loaded_options = None
    _globals['_GETCURRENTMONTHUSAGERESPONSE'].fields_by_name['other_cloud_storage_usage_cost']._serialized_options = b'\x18\x01'
    _globals['_PAYMENTMETHODTYPE']._serialized_start = 2739
    _globals['_PAYMENTMETHODTYPE']._serialized_end = 2825
    _globals['_USAGECOSTTYPE']._serialized_start = 2828
    _globals['_USAGECOSTTYPE']._serialized_end = 3172
    _globals['_SOURCETYPE']._serialized_start = 3174
    _globals['_SOURCETYPE']._serialized_end = 3262
    _globals['_INVOICESUMMARY']._serialized_start = 71
    _globals['_INVOICESUMMARY']._serialized_end = 341
    _globals['_PAYMENTMETHODCARD']._serialized_start = 343
    _globals['_PAYMENTMETHODCARD']._serialized_end = 426
    _globals['_GETCURRENTMONTHUSAGEREQUEST']._serialized_start = 428
    _globals['_GETCURRENTMONTHUSAGEREQUEST']._serialized_end = 480
    _globals['_USAGECOST']._serialized_start = 482
    _globals['_USAGECOST']._serialized_end = 578
    _globals['_RESOURCEUSAGECOSTSBYSOURCE']._serialized_start = 581
    _globals['_RESOURCEUSAGECOSTSBYSOURCE']._serialized_end = 779
    _globals['_RESOURCEUSAGECOSTS']._serialized_start = 782
    _globals['_RESOURCEUSAGECOSTS']._serialized_end = 989
    _globals['_GETCURRENTMONTHUSAGERESPONSE']._serialized_start = 992
    _globals['_GETCURRENTMONTHUSAGERESPONSE']._serialized_end = 1965
    _globals['_GETORGBILLINGINFORMATIONREQUEST']._serialized_start = 1967
    _globals['_GETORGBILLINGINFORMATIONREQUEST']._serialized_end = 2023
    _globals['_GETORGBILLINGINFORMATIONRESPONSE']._serialized_start = 2026
    _globals['_GETORGBILLINGINFORMATIONRESPONSE']._serialized_end = 2278
    _globals['_GETINVOICESSUMMARYREQUEST']._serialized_start = 2280
    _globals['_GETINVOICESSUMMARYREQUEST']._serialized_end = 2330
    _globals['_GETINVOICESSUMMARYRESPONSE']._serialized_start = 2333
    _globals['_GETINVOICESSUMMARYRESPONSE']._serialized_end = 2467
    _globals['_GETINVOICEPDFREQUEST']._serialized_start = 2469
    _globals['_GETINVOICEPDFREQUEST']._serialized_end = 2530
    _globals['_GETINVOICEPDFRESPONSE']._serialized_start = 2532
    _globals['_GETINVOICEPDFRESPONSE']._serialized_end = 2577
    _globals['_SENDPAYMENTREQUIREDEMAILREQUEST']._serialized_start = 2579
    _globals['_SENDPAYMENTREQUIREDEMAILREQUEST']._serialized_end = 2701
    _globals['_SENDPAYMENTREQUIREDEMAILRESPONSE']._serialized_start = 2703
    _globals['_SENDPAYMENTREQUIREDEMAILRESPONSE']._serialized_end = 2737
    _globals['_BILLINGSERVICE']._serialized_start = 3265
    _globals['_BILLINGSERVICE']._serialized_end = 3825