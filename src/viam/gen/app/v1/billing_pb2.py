"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'app/v1/billing.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14app/v1/billing.proto\x12\x0bviam.app.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\x8e\x02\n\x0eInvoiceSummary\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12=\n\x0cinvoice_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0binvoiceDate\x12%\n\x0einvoice_amount\x18\x03 \x01(\x01R\rinvoiceAmount\x12\x16\n\x06status\x18\x04 \x01(\tR\x06status\x125\n\x08due_date\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07dueDate\x127\n\tpaid_date\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\x08paidDate"S\n\x11PaymentMethodCard\x12\x14\n\x05brand\x18\x01 \x01(\tR\x05brand\x12(\n\x10last_four_digits\x18\x02 \x01(\tR\x0elastFourDigits"v\n\x10VerificationInfo\x12!\n\x0carrival_date\x18\x01 \x01(\x03R\x0barrivalDate\x12?\n\x1chosted_verification_page_url\x18\x02 \x01(\tR\x19hostedVerificationPageUrl"\xb0\x02\n\x1aPaymentMethodUSBankAccount\x12\x1b\n\tbank_name\x18\x01 \x01(\tR\x08bankName\x12D\n\x1flast_four_digits_account_number\x18\x02 \x01(\tR\x1blastFourDigitsAccountNumber\x12%\n\x0erouting_number\x18\x03 \x01(\tR\rroutingNumber\x12!\n\x0caccount_type\x18\x04 \x01(\tR\x0baccountType\x12O\n\x11verification_info\x18\x05 \x01(\x0b2\x1d.viam.app.v1.VerificationInfoH\x00R\x10verificationInfo\x88\x01\x01B\x14\n\x12_verification_info"4\n\x1bGetCurrentMonthUsageRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"`\n\tUsageCost\x12?\n\rresource_type\x18\x01 \x01(\x0e2\x1a.viam.app.v1.UsageCostTypeR\x0cresourceType\x12\x12\n\x04cost\x18\x02 \x01(\x01R\x04cost"\xc6\x01\n\x1aResourceUsageCostsBySource\x128\n\x0bsource_type\x18\x01 \x01(\x0e2\x17.viam.app.v1.SourceTypeR\nsourceType\x12Q\n\x14resource_usage_costs\x18\x02 \x01(\x0b2\x1f.viam.app.v1.ResourceUsageCostsR\x12resourceUsageCosts\x12\x1b\n\ttier_name\x18\x03 \x01(\tR\x08tierName"\xcf\x01\n\x12ResourceUsageCosts\x127\n\x0busage_costs\x18\x01 \x03(\x0b2\x16.viam.app.v1.UsageCostR\nusageCosts\x12\x1a\n\x08discount\x18\x02 \x01(\x01R\x08discount\x12.\n\x13total_with_discount\x18\x03 \x01(\x01R\x11totalWithDiscount\x124\n\x16total_without_discount\x18\x04 \x01(\x01R\x14totalWithoutDiscount"\xcd\x07\n\x1cGetCurrentMonthUsageResponse\x129\n\nstart_date\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\tstartDate\x125\n\x08end_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07endDate\x12k\n\x1eresource_usage_costs_by_source\x18\x0e \x03(\x0b2\'.viam.app.v1.ResourceUsageCostsBySourceR\x1aresourceUsageCostsBySource\x12\x1a\n\x08subtotal\x18\x0f \x01(\x01R\x08subtotal\x12;\n\x18cloud_storage_usage_cost\x18\x03 \x01(\x01B\x02\x18\x01R\x15cloudStorageUsageCost\x127\n\x16data_upload_usage_cost\x18\x04 \x01(\x01B\x02\x18\x01R\x13dataUploadUsageCost\x125\n\x15data_egres_usage_cost\x18\x05 \x01(\x01B\x02\x18\x01R\x12dataEgresUsageCost\x12=\n\x19remote_control_usage_cost\x18\x06 \x01(\x01B\x02\x18\x01R\x16remoteControlUsageCost\x12A\n\x1bstandard_compute_usage_cost\x18\x07 \x01(\x01B\x02\x18\x01R\x18standardComputeUsageCost\x12+\n\x0fdiscount_amount\x18\x08 \x01(\x01B\x02\x18\x01R\x0ediscountAmount\x12=\n\x19total_usage_with_discount\x18\t \x01(\x01B\x02\x18\x01R\x16totalUsageWithDiscount\x12C\n\x1ctotal_usage_without_discount\x18\n \x01(\x01B\x02\x18\x01R\x19totalUsageWithoutDiscount\x127\n\x16per_machine_usage_cost\x18\x0b \x01(\x01B\x02\x18\x01R\x13perMachineUsageCost\x12Q\n$binary_data_cloud_storage_usage_cost\x18\x0c \x01(\x01B\x02\x18\x01R\x1fbinaryDataCloudStorageUsageCost\x12F\n\x1eother_cloud_storage_usage_cost\x18\r \x01(\x01B\x02\x18\x01R\x1aotherCloudStorageUsageCost"8\n\x1fGetOrgBillingInformationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\xfa\x02\n GetOrgBillingInformationResponse\x122\n\x04type\x18\x01 \x01(\x0e2\x1e.viam.app.v1.PaymentMethodTypeR\x04type\x12#\n\rbilling_email\x18\x02 \x01(\tR\x0cbillingEmail\x12;\n\x06method\x18\x03 \x01(\x0b2\x1e.viam.app.v1.PaymentMethodCardH\x00R\x06method\x88\x01\x01\x12&\n\x0cbilling_tier\x18\x04 \x01(\tH\x01R\x0bbillingTier\x88\x01\x01\x12a\n\x16method_us_bank_account\x18\x05 \x01(\x0b2\'.viam.app.v1.PaymentMethodUSBankAccountH\x02R\x13methodUsBankAccount\x88\x01\x01B\t\n\x07_methodB\x0f\n\r_billing_tierB\x19\n\x17_method_us_bank_account"2\n\x19GetInvoicesSummaryRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\x86\x01\n\x1aGetInvoicesSummaryResponse\x12/\n\x13outstanding_balance\x18\x01 \x01(\x01R\x12outstandingBalance\x127\n\x08invoices\x18\x02 \x03(\x0b2\x1b.viam.app.v1.InvoiceSummaryR\x08invoices"=\n\x14GetInvoicePdfRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId"-\n\x15GetInvoicePdfResponse\x12\x14\n\x05chunk\x18\x01 \x01(\x0cR\x05chunk"z\n\x1fSendPaymentRequiredEmailRequest\x12&\n\x0fcustomer_org_id\x18\x01 \x01(\tR\rcustomerOrgId\x12/\n\x14billing_owner_org_id\x18\x02 \x01(\tR\x11billingOwnerOrgId""\n SendPaymentRequiredEmailResponse"!\n\x1fGetAvailableBillingTiersRequest"8\n GetAvailableBillingTiersResponse\x12\x14\n\x05tiers\x18\x01 \x03(\tR\x05tiers"r\n$UpdateOrganizationBillingTierRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12!\n\x0cbilling_tier\x18\x02 \x01(\tR\x0bbillingTier"\'\n%UpdateOrganizationBillingTierResponse"\x93\x02\n(CreateInvoiceAndChargeImmediatelyRequest\x12\'\n\x10org_id_to_charge\x18\x01 \x01(\tR\rorgIdToCharge\x12\x16\n\x06amount\x18\x02 \x01(\x01R\x06amount\x12%\n\x0bdescription\x18\x03 \x01(\tH\x00R\x0bdescription\x88\x01\x01\x122\n\x13org_id_for_branding\x18\x04 \x01(\tH\x01R\x10orgIdForBranding\x88\x01\x01\x12#\n\rdisable_email\x18\x05 \x01(\x08R\x0cdisableEmailB\x0e\n\x0c_descriptionB\x16\n\x14_org_id_for_branding"J\n)CreateInvoiceAndChargeImmediatelyResponse\x12\x1d\n\ninvoice_id\x18\x01 \x01(\tR\tinvoiceId*}\n\x11PaymentMethodType\x12#\n\x1fPAYMENT_METHOD_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18PAYMENT_METHOD_TYPE_CARD\x10\x01\x12%\n!PAYMENT_METHOD_TYPE_USBANKACCOUNT\x10\x02*\x84\t\n\rUsageCostType\x12\x1f\n\x1bUSAGE_COST_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1bUSAGE_COST_TYPE_DATA_UPLOAD\x10\x01\x1a\x02\x08\x01\x12#\n\x1bUSAGE_COST_TYPE_DATA_EGRESS\x10\x02\x1a\x02\x08\x01\x12"\n\x1eUSAGE_COST_TYPE_REMOTE_CONTROL\x10\x03\x12$\n USAGE_COST_TYPE_STANDARD_COMPUTE\x10\x04\x12%\n\x1dUSAGE_COST_TYPE_CLOUD_STORAGE\x10\x05\x1a\x02\x08\x01\x12-\n)USAGE_COST_TYPE_BINARY_DATA_CLOUD_STORAGE\x10\x06\x12+\n#USAGE_COST_TYPE_OTHER_CLOUD_STORAGE\x10\x07\x1a\x02\x08\x01\x12\x1f\n\x1bUSAGE_COST_TYPE_PER_MACHINE\x10\x08\x12(\n$USAGE_COST_TYPE_TRIGGER_NOTIFICATION\x10\t\x12.\n*USAGE_COST_TYPE_TABULAR_DATA_CLOUD_STORAGE\x10\n\x120\n,USAGE_COST_TYPE_CONFIG_HISTORY_CLOUD_STORAGE\x10\x0b\x12&\n"USAGE_COST_TYPE_LOGS_CLOUD_STORAGE\x10\x0c\x12/\n+USAGE_COST_TYPE_TRAINING_LOGS_CLOUD_STORAGE\x10\r\x12*\n&USAGE_COST_TYPE_PACKAGES_CLOUD_STORAGE\x10\x0e\x12&\n"USAGE_COST_TYPE_BINARY_DATA_UPLOAD\x10\x0f\x12\'\n#USAGE_COST_TYPE_TABULAR_DATA_UPLOAD\x10\x10\x12\x1f\n\x1bUSAGE_COST_TYPE_LOGS_UPLOAD\x10\x11\x12&\n"USAGE_COST_TYPE_BINARY_DATA_EGRESS\x10\x12\x12\'\n#USAGE_COST_TYPE_TABULAR_DATA_EGRESS\x10\x13\x12\x1f\n\x1bUSAGE_COST_TYPE_LOGS_EGRESS\x10\x14\x12(\n$USAGE_COST_TYPE_TRAINING_LOGS_EGRESS\x10\x15\x127\n3USAGE_COST_TYPE_TABULAR_DATA_DATABASE_CLOUD_STORAGE\x10\x16\x121\n-USAGE_COST_TYPE_TABULAR_DATA_DATABASE_COMPUTE\x10\x17\x123\n/USAGE_COST_TYPE_BINARY_DATA_CROSS_REGION_EGRESS\x10\x18\x12/\n+USAGE_COST_TYPE_PIPELINE_SINK_CLOUD_STORAGE\x10\x19\x12)\n%USAGE_COST_TYPE_PIPELINE_SINK_COMPUTE\x10\x1a*X\n\nSourceType\x12\x1b\n\x17SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSOURCE_TYPE_ORG\x10\x01\x12\x18\n\x14SOURCE_TYPE_FRAGMENT\x10\x022\xc7\x07\n\x0eBillingService\x12k\n\x14GetCurrentMonthUsage\x12(.viam.app.v1.GetCurrentMonthUsageRequest\x1a).viam.app.v1.GetCurrentMonthUsageResponse\x12w\n\x18GetOrgBillingInformation\x12,.viam.app.v1.GetOrgBillingInformationRequest\x1a-.viam.app.v1.GetOrgBillingInformationResponse\x12e\n\x12GetInvoicesSummary\x12&.viam.app.v1.GetInvoicesSummaryRequest\x1a\'.viam.app.v1.GetInvoicesSummaryResponse\x12X\n\rGetInvoicePdf\x12!.viam.app.v1.GetInvoicePdfRequest\x1a".viam.app.v1.GetInvoicePdfResponse0\x01\x12w\n\x18SendPaymentRequiredEmail\x12,.viam.app.v1.SendPaymentRequiredEmailRequest\x1a-.viam.app.v1.SendPaymentRequiredEmailResponse\x12w\n\x18GetAvailableBillingTiers\x12,.viam.app.v1.GetAvailableBillingTiersRequest\x1a-.viam.app.v1.GetAvailableBillingTiersResponse\x12\x86\x01\n\x1dUpdateOrganizationBillingTier\x121.viam.app.v1.UpdateOrganizationBillingTierRequest\x1a2.viam.app.v1.UpdateOrganizationBillingTierResponse\x12\x92\x01\n!CreateInvoiceAndChargeImmediately\x125.viam.app.v1.CreateInvoiceAndChargeImmediatelyRequest\x1a6.viam.app.v1.CreateInvoiceAndChargeImmediatelyResponseB\x18Z\x16go.viam.com/api/app/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.v1.billing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x16go.viam.com/api/app/v1'
    _globals['_USAGECOSTTYPE'].values_by_name['USAGE_COST_TYPE_DATA_UPLOAD']._loaded_options = None
    _globals['_USAGECOSTTYPE'].values_by_name['USAGE_COST_TYPE_DATA_UPLOAD']._serialized_options = b'\x08\x01'
    _globals['_USAGECOSTTYPE'].values_by_name['USAGE_COST_TYPE_DATA_EGRESS']._loaded_options = None
    _globals['_USAGECOSTTYPE'].values_by_name['USAGE_COST_TYPE_DATA_EGRESS']._serialized_options = b'\x08\x01'
    _globals['_USAGECOSTTYPE'].values_by_name['USAGE_COST_TYPE_CLOUD_STORAGE']._loaded_options = None
    _globals['_USAGECOSTTYPE'].values_by_name['USAGE_COST_TYPE_CLOUD_STORAGE']._serialized_options = b'\x08\x01'
    _globals['_USAGECOSTTYPE'].values_by_name['USAGE_COST_TYPE_OTHER_CLOUD_STORAGE']._loaded_options = None
    _globals['_USAGECOSTTYPE'].values_by_name['USAGE_COST_TYPE_OTHER_CLOUD_STORAGE']._serialized_options = b'\x08\x01'
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
    _globals['_PAYMENTMETHODTYPE']._serialized_start = 3896
    _globals['_PAYMENTMETHODTYPE']._serialized_end = 4021
    _globals['_USAGECOSTTYPE']._serialized_start = 4024
    _globals['_USAGECOSTTYPE']._serialized_end = 5180
    _globals['_SOURCETYPE']._serialized_start = 5182
    _globals['_SOURCETYPE']._serialized_end = 5270
    _globals['_INVOICESUMMARY']._serialized_start = 71
    _globals['_INVOICESUMMARY']._serialized_end = 341
    _globals['_PAYMENTMETHODCARD']._serialized_start = 343
    _globals['_PAYMENTMETHODCARD']._serialized_end = 426
    _globals['_VERIFICATIONINFO']._serialized_start = 428
    _globals['_VERIFICATIONINFO']._serialized_end = 546
    _globals['_PAYMENTMETHODUSBANKACCOUNT']._serialized_start = 549
    _globals['_PAYMENTMETHODUSBANKACCOUNT']._serialized_end = 853
    _globals['_GETCURRENTMONTHUSAGEREQUEST']._serialized_start = 855
    _globals['_GETCURRENTMONTHUSAGEREQUEST']._serialized_end = 907
    _globals['_USAGECOST']._serialized_start = 909
    _globals['_USAGECOST']._serialized_end = 1005
    _globals['_RESOURCEUSAGECOSTSBYSOURCE']._serialized_start = 1008
    _globals['_RESOURCEUSAGECOSTSBYSOURCE']._serialized_end = 1206
    _globals['_RESOURCEUSAGECOSTS']._serialized_start = 1209
    _globals['_RESOURCEUSAGECOSTS']._serialized_end = 1416
    _globals['_GETCURRENTMONTHUSAGERESPONSE']._serialized_start = 1419
    _globals['_GETCURRENTMONTHUSAGERESPONSE']._serialized_end = 2392
    _globals['_GETORGBILLINGINFORMATIONREQUEST']._serialized_start = 2394
    _globals['_GETORGBILLINGINFORMATIONREQUEST']._serialized_end = 2450
    _globals['_GETORGBILLINGINFORMATIONRESPONSE']._serialized_start = 2453
    _globals['_GETORGBILLINGINFORMATIONRESPONSE']._serialized_end = 2831
    _globals['_GETINVOICESSUMMARYREQUEST']._serialized_start = 2833
    _globals['_GETINVOICESSUMMARYREQUEST']._serialized_end = 2883
    _globals['_GETINVOICESSUMMARYRESPONSE']._serialized_start = 2886
    _globals['_GETINVOICESSUMMARYRESPONSE']._serialized_end = 3020
    _globals['_GETINVOICEPDFREQUEST']._serialized_start = 3022
    _globals['_GETINVOICEPDFREQUEST']._serialized_end = 3083
    _globals['_GETINVOICEPDFRESPONSE']._serialized_start = 3085
    _globals['_GETINVOICEPDFRESPONSE']._serialized_end = 3130
    _globals['_SENDPAYMENTREQUIREDEMAILREQUEST']._serialized_start = 3132
    _globals['_SENDPAYMENTREQUIREDEMAILREQUEST']._serialized_end = 3254
    _globals['_SENDPAYMENTREQUIREDEMAILRESPONSE']._serialized_start = 3256
    _globals['_SENDPAYMENTREQUIREDEMAILRESPONSE']._serialized_end = 3290
    _globals['_GETAVAILABLEBILLINGTIERSREQUEST']._serialized_start = 3292
    _globals['_GETAVAILABLEBILLINGTIERSREQUEST']._serialized_end = 3325
    _globals['_GETAVAILABLEBILLINGTIERSRESPONSE']._serialized_start = 3327
    _globals['_GETAVAILABLEBILLINGTIERSRESPONSE']._serialized_end = 3383
    _globals['_UPDATEORGANIZATIONBILLINGTIERREQUEST']._serialized_start = 3385
    _globals['_UPDATEORGANIZATIONBILLINGTIERREQUEST']._serialized_end = 3499
    _globals['_UPDATEORGANIZATIONBILLINGTIERRESPONSE']._serialized_start = 3501
    _globals['_UPDATEORGANIZATIONBILLINGTIERRESPONSE']._serialized_end = 3540
    _globals['_CREATEINVOICEANDCHARGEIMMEDIATELYREQUEST']._serialized_start = 3543
    _globals['_CREATEINVOICEANDCHARGEIMMEDIATELYREQUEST']._serialized_end = 3818
    _globals['_CREATEINVOICEANDCHARGEIMMEDIATELYRESPONSE']._serialized_start = 3820
    _globals['_CREATEINVOICEANDCHARGEIMMEDIATELYRESPONSE']._serialized_end = 3894
    _globals['_BILLINGSERVICE']._serialized_start = 5273
    _globals['_BILLINGSERVICE']._serialized_end = 6240