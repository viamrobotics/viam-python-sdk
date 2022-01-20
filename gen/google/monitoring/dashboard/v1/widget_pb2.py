# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/monitoring/dashboard/v1/widget.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.monitoring.dashboard.v1 import alertchart_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_alertchart__pb2
from google.monitoring.dashboard.v1 import scorecard_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_scorecard__pb2
from google.monitoring.dashboard.v1 import text_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_text__pb2
from google.monitoring.dashboard.v1 import xychart_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_xychart__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/monitoring/dashboard/v1/widget.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a/google/monitoring/dashboard/v1/alertchart.proto\x1a.google/monitoring/dashboard/v1/scorecard.proto\x1a)google/monitoring/dashboard/v1/text.proto\x1a,google/monitoring/dashboard/v1/xychart.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xfb\x02\n\x06Widget\x12\x1a\n\x05title\x18\x01 \x01(\tB\x04\xe2\x41\x01\x01R\x05title\x12\x44\n\x08xy_chart\x18\x02 \x01(\x0b\x32\'.google.monitoring.dashboard.v1.XyChartH\x00R\x07xyChart\x12I\n\tscorecard\x18\x03 \x01(\x0b\x32).google.monitoring.dashboard.v1.ScorecardH\x00R\tscorecard\x12:\n\x04text\x18\x04 \x01(\x0b\x32$.google.monitoring.dashboard.v1.TextH\x00R\x04text\x12.\n\x05\x62lank\x18\x05 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x05\x62lank\x12M\n\x0b\x61lert_chart\x18\x07 \x01(\x0b\x32*.google.monitoring.dashboard.v1.AlertChartH\x00R\nalertChartB\t\n\x07\x63ontentB\xf5\x01\n\"com.google.monitoring.dashboard.v1B\x0bWidgetProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')



_WIDGET = DESCRIPTOR.message_types_by_name['Widget']
Widget = _reflection.GeneratedProtocolMessageType('Widget', (_message.Message,), {
  'DESCRIPTOR' : _WIDGET,
  '__module__' : 'google.monitoring.dashboard.v1.widget_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.Widget)
  })
_sym_db.RegisterMessage(Widget)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.monitoring.dashboard.v1B\013WidgetProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\252\002$Google.Cloud.Monitoring.Dashboard.V1\312\002$Google\\Cloud\\Monitoring\\Dashboard\\V1\352\002(Google::Cloud::Monitoring::Dashboard::V1'
  _WIDGET.fields_by_name['title']._options = None
  _WIDGET.fields_by_name['title']._serialized_options = b'\342A\001\001'
  _WIDGET._serialized_start=328
  _WIDGET._serialized_end=707
# @@protoc_insertion_point(module_scope)
