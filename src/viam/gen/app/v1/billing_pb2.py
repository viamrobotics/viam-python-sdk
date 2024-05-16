"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14app/v1/billing.proto\x12\x0bviam.app.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\x8e\x02\n\x0eInvoiceSummary\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12=\n\x0cinvoice_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0binvoiceDate\x12%\n\x0einvoice_amount\x18\x03 \x01(\x01R\rinvoiceAmount\x12\x16\n\x06status\x18\x04 \x01(\tR\x06status\x125\n\x08due_date\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07dueDate\x127\n\tpaid_date\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\x08paidDate"\x8b\x02\n\x15BillableResourceEvent\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12%\n\x0eusage_quantity\x18\x03 \x01(\x01R\rusageQuantity\x12.\n\x13usage_quantity_unit\x18\x04 \x01(\tR\x11usageQuantityUnit\x12\x1d\n\nusage_cost\x18\x05 \x01(\tR\tusageCost\x12;\n\x0boccurred_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\noccurredAt\x12\x1b\n\tuser_name\x18\x07 \x01(\tR\x08userName"\xa7\x02\n\x07Invoice\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12=\n\x0cinvoice_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0binvoiceDate\x12%\n\x0einvoice_amount\x18\x03 \x01(\x01R\rinvoiceAmount\x12\x16\n\x06status\x18\x04 \x01(\tR\x06status\x125\n\x08due_date\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07dueDate\x128\n\x05items\x18\x06 \x03(\x0b2".viam.app.v1.BillableResourceEventR\x05items\x12\x1d\n\nemailed_to\x18\x07 \x01(\tR\temailedTo"S\n\x11PaymentMethodCard\x12\x14\n\x05brand\x18\x01 \x01(\tR\x05brand\x12(\n\x10last_four_digits\x18\x02 \x01(\tR\x0elastFourDigits"4\n\x1bGetCurrentMonthUsageRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\x98\x06\n\x1cGetCurrentMonthUsageResponse\x129\n\nstart_date\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\tstartDate\x125\n\x08end_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07endDate\x127\n\x18cloud_storage_usage_cost\x18\x03 \x01(\x01R\x15cloudStorageUsageCost\x123\n\x16data_upload_usage_cost\x18\x04 \x01(\x01R\x13dataUploadUsageCost\x121\n\x15data_egres_usage_cost\x18\x05 \x01(\x01R\x12dataEgresUsageCost\x129\n\x19remote_control_usage_cost\x18\x06 \x01(\x01R\x16remoteControlUsageCost\x12=\n\x1bstandard_compute_usage_cost\x18\x07 \x01(\x01R\x18standardComputeUsageCost\x12\'\n\x0fdiscount_amount\x18\x08 \x01(\x01R\x0ediscountAmount\x129\n\x19total_usage_with_discount\x18\t \x01(\x01R\x16totalUsageWithDiscount\x12?\n\x1ctotal_usage_without_discount\x18\n \x01(\x01R\x19totalUsageWithoutDiscount\x123\n\x16per_machine_usage_cost\x18\x0b \x01(\x01R\x13perMachineUsageCost\x12M\n$binary_data_cloud_storage_usage_cost\x18\x0c \x01(\x01R\x1fbinaryDataCloudStorageUsageCost\x12B\n\x1eother_cloud_storage_usage_cost\x18\r \x01(\x01R\x1aotherCloudStorageUsageCost"8\n\x1fGetOrgBillingInformationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\xfc\x01\n GetOrgBillingInformationResponse\x122\n\x04type\x18\x01 \x01(\x0e2\x1e.viam.app.v1.PaymentMethodTypeR\x04type\x12#\n\rbilling_email\x18\x02 \x01(\tR\x0cbillingEmail\x12;\n\x06method\x18\x03 \x01(\x0b2\x1e.viam.app.v1.PaymentMethodCardH\x00R\x06method\x88\x01\x01\x12&\n\x0cbilling_tier\x18\x04 \x01(\tH\x01R\x0bbillingTier\x88\x01\x01B\t\n\x07_methodB\x0f\n\r_billing_tier"2\n\x19GetInvoicesSummaryRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\x86\x01\n\x1aGetInvoicesSummaryResponse\x12/\n\x13outstanding_balance\x18\x01 \x01(\x01R\x12outstandingBalance\x127\n\x08invoices\x18\x02 \x03(\x0b2\x1b.viam.app.v1.InvoiceSummaryR\x08invoices"=\n\x14GetInvoicePdfRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId"-\n\x15GetInvoicePdfResponse\x12\x14\n\x05chunk\x18\x01 \x01(\x0cR\x05chunk*V\n\x11PaymentMethodType\x12#\n\x1fPAYMENT_METHOD_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18PAYMENT_METHOD_TYPE_CARD\x10\x012\xb7\x03\n\x0eBillingService\x12k\n\x14GetCurrentMonthUsage\x12(.viam.app.v1.GetCurrentMonthUsageRequest\x1a).viam.app.v1.GetCurrentMonthUsageResponse\x12w\n\x18GetOrgBillingInformation\x12,.viam.app.v1.GetOrgBillingInformationRequest\x1a-.viam.app.v1.GetOrgBillingInformationResponse\x12e\n\x12GetInvoicesSummary\x12&.viam.app.v1.GetInvoicesSummaryRequest\x1a\'.viam.app.v1.GetInvoicesSummaryResponse\x12X\n\rGetInvoicePdf\x12!.viam.app.v1.GetInvoicePdfRequest\x1a".viam.app.v1.GetInvoicePdfResponse0\x01B\x18Z\x16go.viam.com/api/app/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.v1.billing_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x16go.viam.com/api/app/v1'
    _PAYMENTMETHODTYPE._serialized_start = 2457
    _PAYMENTMETHODTYPE._serialized_end = 2543
    _INVOICESUMMARY._serialized_start = 71
    _INVOICESUMMARY._serialized_end = 341
    _BILLABLERESOURCEEVENT._serialized_start = 344
    _BILLABLERESOURCEEVENT._serialized_end = 611
    _INVOICE._serialized_start = 614
    _INVOICE._serialized_end = 909
    _PAYMENTMETHODCARD._serialized_start = 911
    _PAYMENTMETHODCARD._serialized_end = 994
    _GETCURRENTMONTHUSAGEREQUEST._serialized_start = 996
    _GETCURRENTMONTHUSAGEREQUEST._serialized_end = 1048
    _GETCURRENTMONTHUSAGERESPONSE._serialized_start = 1051
    _GETCURRENTMONTHUSAGERESPONSE._serialized_end = 1843
    _GETORGBILLINGINFORMATIONREQUEST._serialized_start = 1845
    _GETORGBILLINGINFORMATIONREQUEST._serialized_end = 1901
    _GETORGBILLINGINFORMATIONRESPONSE._serialized_start = 1904
    _GETORGBILLINGINFORMATIONRESPONSE._serialized_end = 2156
    _GETINVOICESSUMMARYREQUEST._serialized_start = 2158
    _GETINVOICESSUMMARYREQUEST._serialized_end = 2208
    _GETINVOICESSUMMARYRESPONSE._serialized_start = 2211
    _GETINVOICESSUMMARYRESPONSE._serialized_end = 2345
    _GETINVOICEPDFREQUEST._serialized_start = 2347
    _GETINVOICEPDFREQUEST._serialized_end = 2408
    _GETINVOICEPDFRESPONSE._serialized_start = 2410
    _GETINVOICEPDFRESPONSE._serialized_end = 2455
    _BILLINGSERVICE._serialized_start = 2546
    _BILLINGSERVICE._serialized_end = 2985