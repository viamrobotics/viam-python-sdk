# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/admob/v1/admob_resources.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.type import date_pb2 as google_dot_type_dot_date__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/ads/admob/v1/admob_resources.proto\x12\x13google.ads.admob.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x16google/type/date.proto\"\xe0\x01\n\x10PublisherAccount\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0cpublisher_id\x18\x02 \x01(\tR\x0bpublisherId\x12.\n\x13reporting_time_zone\x18\x03 \x01(\tR\x11reportingTimeZone\x12#\n\rcurrency_code\x18\x04 \x01(\tR\x0c\x63urrencyCode:@\xea\x41=\n%admob.googleapis.com/PublisherAccount\x12\x14\x61\x63\x63ounts/{publisher}\"\xd0\n\n\x11NetworkReportSpec\x12=\n\ndate_range\x18\x01 \x01(\x0b\x32\x1e.google.ads.admob.v1.DateRangeR\tdateRange\x12P\n\ndimensions\x18\x02 \x03(\x0e\x32\x30.google.ads.admob.v1.NetworkReportSpec.DimensionR\ndimensions\x12G\n\x07metrics\x18\x03 \x03(\x0e\x32-.google.ads.admob.v1.NetworkReportSpec.MetricR\x07metrics\x12\x63\n\x11\x64imension_filters\x18\x04 \x03(\x0b\x32\x36.google.ads.admob.v1.NetworkReportSpec.DimensionFilterR\x10\x64imensionFilters\x12]\n\x0fsort_conditions\x18\x05 \x03(\x0b\x32\x34.google.ads.admob.v1.NetworkReportSpec.SortConditionR\x0esortConditions\x12^\n\x15localization_settings\x18\x06 \x01(\x0b\x32).google.ads.admob.v1.LocalizationSettingsR\x14localizationSettings\x12&\n\x0fmax_report_rows\x18\x07 \x01(\x05R\rmaxReportRows\x12\x1b\n\ttime_zone\x18\x08 \x01(\tR\x08timeZone\x1a\xb1\x01\n\x0f\x44imensionFilter\x12\x42\n\x0bmatches_any\x18\x02 \x01(\x0b\x32\x1f.google.ads.admob.v1.StringListH\x00R\nmatchesAny\x12N\n\tdimension\x18\x01 \x01(\x0e\x32\x30.google.ads.admob.v1.NetworkReportSpec.DimensionR\tdimensionB\n\n\x08operator\x1a\xeb\x01\n\rSortCondition\x12P\n\tdimension\x18\x01 \x01(\x0e\x32\x30.google.ads.admob.v1.NetworkReportSpec.DimensionH\x00R\tdimension\x12G\n\x06metric\x18\x02 \x01(\x0e\x32-.google.ads.admob.v1.NetworkReportSpec.MetricH\x00R\x06metric\x12\x34\n\x05order\x18\x03 \x01(\x0e\x32\x1e.google.ads.admob.v1.SortOrderR\x05orderB\t\n\x07sort_on\"\x8f\x01\n\tDimension\x12\x19\n\x15\x44IMENSION_UNSPECIFIED\x10\x00\x12\x08\n\x04\x44\x41TE\x10\x01\x12\t\n\x05MONTH\x10\x02\x12\x08\n\x04WEEK\x10\x03\x12\x0b\n\x07\x41\x44_UNIT\x10\x04\x12\x07\n\x03\x41PP\x10\x05\x12\x0b\n\x07\x41\x44_TYPE\x10\x06\x12\x0b\n\x07\x43OUNTRY\x10\x07\x12\n\n\x06\x46ORMAT\x10\x08\x12\x0c\n\x08PLATFORM\x10\t\"\xc3\x01\n\x06Metric\x12\x16\n\x12METRIC_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x41\x44_REQUESTS\x10\x01\x12\n\n\x06\x43LICKS\x10\x02\x12\x16\n\x12\x45STIMATED_EARNINGS\x10\x03\x12\x0f\n\x0bIMPRESSIONS\x10\x04\x12\x12\n\x0eIMPRESSION_CTR\x10\x05\x12\x12\n\x0eIMPRESSION_RPM\x10\x06\x12\x14\n\x10MATCHED_REQUESTS\x10\x07\x12\x0e\n\nMATCH_RATE\x10\x08\x12\r\n\tSHOW_RATE\x10\t\"\xff\n\n\x13MediationReportSpec\x12=\n\ndate_range\x18\x01 \x01(\x0b\x32\x1e.google.ads.admob.v1.DateRangeR\tdateRange\x12R\n\ndimensions\x18\x02 \x03(\x0e\x32\x32.google.ads.admob.v1.MediationReportSpec.DimensionR\ndimensions\x12I\n\x07metrics\x18\x03 \x03(\x0e\x32/.google.ads.admob.v1.MediationReportSpec.MetricR\x07metrics\x12\x65\n\x11\x64imension_filters\x18\x04 \x03(\x0b\x32\x38.google.ads.admob.v1.MediationReportSpec.DimensionFilterR\x10\x64imensionFilters\x12_\n\x0fsort_conditions\x18\x05 \x03(\x0b\x32\x36.google.ads.admob.v1.MediationReportSpec.SortConditionR\x0esortConditions\x12^\n\x15localization_settings\x18\x06 \x01(\x0b\x32).google.ads.admob.v1.LocalizationSettingsR\x14localizationSettings\x12&\n\x0fmax_report_rows\x18\x07 \x01(\x05R\rmaxReportRows\x12\x1b\n\ttime_zone\x18\x08 \x01(\tR\x08timeZone\x1a\xb3\x01\n\x0f\x44imensionFilter\x12\x42\n\x0bmatches_any\x18\x02 \x01(\x0b\x32\x1f.google.ads.admob.v1.StringListH\x00R\nmatchesAny\x12P\n\tdimension\x18\x01 \x01(\x0e\x32\x32.google.ads.admob.v1.MediationReportSpec.DimensionR\tdimensionB\n\n\x08operator\x1a\xef\x01\n\rSortCondition\x12R\n\tdimension\x18\x01 \x01(\x0e\x32\x32.google.ads.admob.v1.MediationReportSpec.DimensionH\x00R\tdimension\x12I\n\x06metric\x18\x02 \x01(\x0e\x32/.google.ads.admob.v1.MediationReportSpec.MetricH\x00R\x06metric\x12\x34\n\x05order\x18\x03 \x01(\x0e\x32\x1e.google.ads.admob.v1.SortOrderR\x05orderB\t\n\x07sort_on\"\xbe\x01\n\tDimension\x12\x19\n\x15\x44IMENSION_UNSPECIFIED\x10\x00\x12\x08\n\x04\x44\x41TE\x10\x01\x12\t\n\x05MONTH\x10\x02\x12\x08\n\x04WEEK\x10\x03\x12\r\n\tAD_SOURCE\x10\x04\x12\x16\n\x12\x41\x44_SOURCE_INSTANCE\x10\x05\x12\x0b\n\x07\x41\x44_UNIT\x10\x06\x12\x07\n\x03\x41PP\x10\x07\x12\x13\n\x0fMEDIATION_GROUP\x10\x0b\x12\x0b\n\x07\x43OUNTRY\x10\x08\x12\n\n\x06\x46ORMAT\x10\t\x12\x0c\n\x08PLATFORM\x10\n\"\xb3\x01\n\x06Metric\x12\x16\n\x12METRIC_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x41\x44_REQUESTS\x10\x01\x12\n\n\x06\x43LICKS\x10\x02\x12\x16\n\x12\x45STIMATED_EARNINGS\x10\x03\x12\x0f\n\x0bIMPRESSIONS\x10\x04\x12\x12\n\x0eIMPRESSION_CTR\x10\x05\x12\x14\n\x10MATCHED_REQUESTS\x10\x06\x12\x0e\n\nMATCH_RATE\x10\x07\x12\x11\n\rOBSERVED_ECPM\x10\x08\"\xf9\x04\n\tReportRow\x12^\n\x10\x64imension_values\x18\x01 \x03(\x0b\x32\x33.google.ads.admob.v1.ReportRow.DimensionValuesEntryR\x0f\x64imensionValues\x12U\n\rmetric_values\x18\x02 \x03(\x0b\x32\x30.google.ads.admob.v1.ReportRow.MetricValuesEntryR\x0cmetricValues\x1aK\n\x0e\x44imensionValue\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12#\n\rdisplay_label\x18\x02 \x01(\tR\x0c\x64isplayLabel\x1a\x87\x01\n\x0bMetricValue\x12%\n\rinteger_value\x18\x01 \x01(\x03H\x00R\x0cintegerValue\x12#\n\x0c\x64ouble_value\x18\x02 \x01(\x01H\x00R\x0b\x64oubleValue\x12#\n\x0cmicros_value\x18\x03 \x01(\x03H\x00R\x0bmicrosValueB\x07\n\x05value\x1aq\n\x14\x44imensionValuesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x43\n\x05value\x18\x02 \x01(\x0b\x32-.google.ads.admob.v1.ReportRow.DimensionValueR\x05value:\x02\x38\x01\x1ak\n\x11MetricValuesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12@\n\x05value\x18\x02 \x01(\x0b\x32*.google.ads.admob.v1.ReportRow.MetricValueR\x05value:\x02\x38\x01\"\xfd\x01\n\rReportWarning\x12;\n\x04type\x18\x01 \x01(\x0e\x32\'.google.ads.admob.v1.ReportWarning.TypeR\x04type\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"\x8c\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\'\n#DATA_BEFORE_ACCOUNT_TIMEZONE_CHANGE\x10\x01\x12\x10\n\x0c\x44\x41TA_DELAYED\x10\x02\x12\t\n\x05OTHER\x10\x03\x12(\n$REPORT_CURRENCY_NOT_ACCOUNT_CURRENCY\x10\x04\"\xdd\x01\n\x0cReportHeader\x12=\n\ndate_range\x18\x01 \x01(\x0b\x32\x1e.google.ads.admob.v1.DateRangeR\tdateRange\x12^\n\x15localization_settings\x18\x02 \x01(\x0b\x32).google.ads.admob.v1.LocalizationSettingsR\x14localizationSettings\x12.\n\x13reporting_time_zone\x18\x03 \x01(\tR\x11reportingTimeZone\"|\n\x0cReportFooter\x12>\n\x08warnings\x18\x01 \x03(\x0b\x32\".google.ads.admob.v1.ReportWarningR\x08warnings\x12,\n\x12matching_row_count\x18\x02 \x01(\x03R\x10matchingRowCount\"k\n\tDateRange\x12\x30\n\nstart_date\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\tstartDate\x12,\n\x08\x65nd_date\x18\x02 \x01(\x0b\x32\x11.google.type.DateR\x07\x65ndDate\"`\n\x14LocalizationSettings\x12#\n\rcurrency_code\x18\x01 \x01(\tR\x0c\x63urrencyCode\x12#\n\rlanguage_code\x18\x02 \x01(\tR\x0clanguageCode\"$\n\nStringList\x12\x16\n\x06values\x18\x01 \x03(\tR\x06values*F\n\tSortOrder\x12\x1a\n\x16SORT_ORDER_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02\x42h\n\x17\x63om.google.ads.admob.v1B\x13\x41\x64MobResourcesProtoZ8google.golang.org/genproto/googleapis/ads/admob/v1;admobb\x06proto3')

_SORTORDER = DESCRIPTOR.enum_types_by_name['SortOrder']
SortOrder = enum_type_wrapper.EnumTypeWrapper(_SORTORDER)
SORT_ORDER_UNSPECIFIED = 0
ASCENDING = 1
DESCENDING = 2


_PUBLISHERACCOUNT = DESCRIPTOR.message_types_by_name['PublisherAccount']
_NETWORKREPORTSPEC = DESCRIPTOR.message_types_by_name['NetworkReportSpec']
_NETWORKREPORTSPEC_DIMENSIONFILTER = _NETWORKREPORTSPEC.nested_types_by_name['DimensionFilter']
_NETWORKREPORTSPEC_SORTCONDITION = _NETWORKREPORTSPEC.nested_types_by_name['SortCondition']
_MEDIATIONREPORTSPEC = DESCRIPTOR.message_types_by_name['MediationReportSpec']
_MEDIATIONREPORTSPEC_DIMENSIONFILTER = _MEDIATIONREPORTSPEC.nested_types_by_name['DimensionFilter']
_MEDIATIONREPORTSPEC_SORTCONDITION = _MEDIATIONREPORTSPEC.nested_types_by_name['SortCondition']
_REPORTROW = DESCRIPTOR.message_types_by_name['ReportRow']
_REPORTROW_DIMENSIONVALUE = _REPORTROW.nested_types_by_name['DimensionValue']
_REPORTROW_METRICVALUE = _REPORTROW.nested_types_by_name['MetricValue']
_REPORTROW_DIMENSIONVALUESENTRY = _REPORTROW.nested_types_by_name['DimensionValuesEntry']
_REPORTROW_METRICVALUESENTRY = _REPORTROW.nested_types_by_name['MetricValuesEntry']
_REPORTWARNING = DESCRIPTOR.message_types_by_name['ReportWarning']
_REPORTHEADER = DESCRIPTOR.message_types_by_name['ReportHeader']
_REPORTFOOTER = DESCRIPTOR.message_types_by_name['ReportFooter']
_DATERANGE = DESCRIPTOR.message_types_by_name['DateRange']
_LOCALIZATIONSETTINGS = DESCRIPTOR.message_types_by_name['LocalizationSettings']
_STRINGLIST = DESCRIPTOR.message_types_by_name['StringList']
_NETWORKREPORTSPEC_DIMENSION = _NETWORKREPORTSPEC.enum_types_by_name['Dimension']
_NETWORKREPORTSPEC_METRIC = _NETWORKREPORTSPEC.enum_types_by_name['Metric']
_MEDIATIONREPORTSPEC_DIMENSION = _MEDIATIONREPORTSPEC.enum_types_by_name['Dimension']
_MEDIATIONREPORTSPEC_METRIC = _MEDIATIONREPORTSPEC.enum_types_by_name['Metric']
_REPORTWARNING_TYPE = _REPORTWARNING.enum_types_by_name['Type']
PublisherAccount = _reflection.GeneratedProtocolMessageType('PublisherAccount', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHERACCOUNT,
  '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.admob.v1.PublisherAccount)
  })
_sym_db.RegisterMessage(PublisherAccount)

NetworkReportSpec = _reflection.GeneratedProtocolMessageType('NetworkReportSpec', (_message.Message,), {

  'DimensionFilter' : _reflection.GeneratedProtocolMessageType('DimensionFilter', (_message.Message,), {
    'DESCRIPTOR' : _NETWORKREPORTSPEC_DIMENSIONFILTER,
    '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.admob.v1.NetworkReportSpec.DimensionFilter)
    })
  ,

  'SortCondition' : _reflection.GeneratedProtocolMessageType('SortCondition', (_message.Message,), {
    'DESCRIPTOR' : _NETWORKREPORTSPEC_SORTCONDITION,
    '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.admob.v1.NetworkReportSpec.SortCondition)
    })
  ,
  'DESCRIPTOR' : _NETWORKREPORTSPEC,
  '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.admob.v1.NetworkReportSpec)
  })
_sym_db.RegisterMessage(NetworkReportSpec)
_sym_db.RegisterMessage(NetworkReportSpec.DimensionFilter)
_sym_db.RegisterMessage(NetworkReportSpec.SortCondition)

MediationReportSpec = _reflection.GeneratedProtocolMessageType('MediationReportSpec', (_message.Message,), {

  'DimensionFilter' : _reflection.GeneratedProtocolMessageType('DimensionFilter', (_message.Message,), {
    'DESCRIPTOR' : _MEDIATIONREPORTSPEC_DIMENSIONFILTER,
    '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.admob.v1.MediationReportSpec.DimensionFilter)
    })
  ,

  'SortCondition' : _reflection.GeneratedProtocolMessageType('SortCondition', (_message.Message,), {
    'DESCRIPTOR' : _MEDIATIONREPORTSPEC_SORTCONDITION,
    '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.admob.v1.MediationReportSpec.SortCondition)
    })
  ,
  'DESCRIPTOR' : _MEDIATIONREPORTSPEC,
  '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.admob.v1.MediationReportSpec)
  })
_sym_db.RegisterMessage(MediationReportSpec)
_sym_db.RegisterMessage(MediationReportSpec.DimensionFilter)
_sym_db.RegisterMessage(MediationReportSpec.SortCondition)

ReportRow = _reflection.GeneratedProtocolMessageType('ReportRow', (_message.Message,), {

  'DimensionValue' : _reflection.GeneratedProtocolMessageType('DimensionValue', (_message.Message,), {
    'DESCRIPTOR' : _REPORTROW_DIMENSIONVALUE,
    '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.admob.v1.ReportRow.DimensionValue)
    })
  ,

  'MetricValue' : _reflection.GeneratedProtocolMessageType('MetricValue', (_message.Message,), {
    'DESCRIPTOR' : _REPORTROW_METRICVALUE,
    '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.admob.v1.ReportRow.MetricValue)
    })
  ,

  'DimensionValuesEntry' : _reflection.GeneratedProtocolMessageType('DimensionValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _REPORTROW_DIMENSIONVALUESENTRY,
    '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.admob.v1.ReportRow.DimensionValuesEntry)
    })
  ,

  'MetricValuesEntry' : _reflection.GeneratedProtocolMessageType('MetricValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _REPORTROW_METRICVALUESENTRY,
    '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.admob.v1.ReportRow.MetricValuesEntry)
    })
  ,
  'DESCRIPTOR' : _REPORTROW,
  '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.admob.v1.ReportRow)
  })
_sym_db.RegisterMessage(ReportRow)
_sym_db.RegisterMessage(ReportRow.DimensionValue)
_sym_db.RegisterMessage(ReportRow.MetricValue)
_sym_db.RegisterMessage(ReportRow.DimensionValuesEntry)
_sym_db.RegisterMessage(ReportRow.MetricValuesEntry)

ReportWarning = _reflection.GeneratedProtocolMessageType('ReportWarning', (_message.Message,), {
  'DESCRIPTOR' : _REPORTWARNING,
  '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.admob.v1.ReportWarning)
  })
_sym_db.RegisterMessage(ReportWarning)

ReportHeader = _reflection.GeneratedProtocolMessageType('ReportHeader', (_message.Message,), {
  'DESCRIPTOR' : _REPORTHEADER,
  '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.admob.v1.ReportHeader)
  })
_sym_db.RegisterMessage(ReportHeader)

ReportFooter = _reflection.GeneratedProtocolMessageType('ReportFooter', (_message.Message,), {
  'DESCRIPTOR' : _REPORTFOOTER,
  '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.admob.v1.ReportFooter)
  })
_sym_db.RegisterMessage(ReportFooter)

DateRange = _reflection.GeneratedProtocolMessageType('DateRange', (_message.Message,), {
  'DESCRIPTOR' : _DATERANGE,
  '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.admob.v1.DateRange)
  })
_sym_db.RegisterMessage(DateRange)

LocalizationSettings = _reflection.GeneratedProtocolMessageType('LocalizationSettings', (_message.Message,), {
  'DESCRIPTOR' : _LOCALIZATIONSETTINGS,
  '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.admob.v1.LocalizationSettings)
  })
_sym_db.RegisterMessage(LocalizationSettings)

StringList = _reflection.GeneratedProtocolMessageType('StringList', (_message.Message,), {
  'DESCRIPTOR' : _STRINGLIST,
  '__module__' : 'google.ads.admob.v1.admob_resources_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.admob.v1.StringList)
  })
_sym_db.RegisterMessage(StringList)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.google.ads.admob.v1B\023AdMobResourcesProtoZ8google.golang.org/genproto/googleapis/ads/admob/v1;admob'
  _PUBLISHERACCOUNT._options = None
  _PUBLISHERACCOUNT._serialized_options = b'\352A=\n%admob.googleapis.com/PublisherAccount\022\024accounts/{publisher}'
  _REPORTROW_DIMENSIONVALUESENTRY._options = None
  _REPORTROW_DIMENSIONVALUESENTRY._serialized_options = b'8\001'
  _REPORTROW_METRICVALUESENTRY._options = None
  _REPORTROW_METRICVALUESENTRY._serialized_options = b'8\001'
  _SORTORDER._serialized_start=4637
  _SORTORDER._serialized_end=4707
  _PUBLISHERACCOUNT._serialized_start=151
  _PUBLISHERACCOUNT._serialized_end=375
  _NETWORKREPORTSPEC._serialized_start=378
  _NETWORKREPORTSPEC._serialized_end=1738
  _NETWORKREPORTSPEC_DIMENSIONFILTER._serialized_start=979
  _NETWORKREPORTSPEC_DIMENSIONFILTER._serialized_end=1156
  _NETWORKREPORTSPEC_SORTCONDITION._serialized_start=1159
  _NETWORKREPORTSPEC_SORTCONDITION._serialized_end=1394
  _NETWORKREPORTSPEC_DIMENSION._serialized_start=1397
  _NETWORKREPORTSPEC_DIMENSION._serialized_end=1540
  _NETWORKREPORTSPEC_METRIC._serialized_start=1543
  _NETWORKREPORTSPEC_METRIC._serialized_end=1738
  _MEDIATIONREPORTSPEC._serialized_start=1741
  _MEDIATIONREPORTSPEC._serialized_end=3148
  _MEDIATIONREPORTSPEC_DIMENSIONFILTER._serialized_start=2352
  _MEDIATIONREPORTSPEC_DIMENSIONFILTER._serialized_end=2531
  _MEDIATIONREPORTSPEC_SORTCONDITION._serialized_start=2534
  _MEDIATIONREPORTSPEC_SORTCONDITION._serialized_end=2773
  _MEDIATIONREPORTSPEC_DIMENSION._serialized_start=2776
  _MEDIATIONREPORTSPEC_DIMENSION._serialized_end=2966
  _MEDIATIONREPORTSPEC_METRIC._serialized_start=2969
  _MEDIATIONREPORTSPEC_METRIC._serialized_end=3148
  _REPORTROW._serialized_start=3151
  _REPORTROW._serialized_end=3784
  _REPORTROW_DIMENSIONVALUE._serialized_start=3347
  _REPORTROW_DIMENSIONVALUE._serialized_end=3422
  _REPORTROW_METRICVALUE._serialized_start=3425
  _REPORTROW_METRICVALUE._serialized_end=3560
  _REPORTROW_DIMENSIONVALUESENTRY._serialized_start=3562
  _REPORTROW_DIMENSIONVALUESENTRY._serialized_end=3675
  _REPORTROW_METRICVALUESENTRY._serialized_start=3677
  _REPORTROW_METRICVALUESENTRY._serialized_end=3784
  _REPORTWARNING._serialized_start=3787
  _REPORTWARNING._serialized_end=4040
  _REPORTWARNING_TYPE._serialized_start=3900
  _REPORTWARNING_TYPE._serialized_end=4040
  _REPORTHEADER._serialized_start=4043
  _REPORTHEADER._serialized_end=4264
  _REPORTFOOTER._serialized_start=4266
  _REPORTFOOTER._serialized_end=4390
  _DATERANGE._serialized_start=4392
  _DATERANGE._serialized_end=4499
  _LOCALIZATIONSETTINGS._serialized_start=4501
  _LOCALIZATIONSETTINGS._serialized_end=4597
  _STRINGLIST._serialized_start=4599
  _STRINGLIST._serialized_end=4635
# @@protoc_insertion_point(module_scope)
