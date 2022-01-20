# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/pubsublite/v1/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/pubsublite/v1/common.proto\x12\x1agoogle.cloud.pubsublite.v1\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\")\n\x0f\x41ttributeValues\x12\x16\n\x06values\x18\x01 \x03(\x0cR\x06values\"\xb7\x02\n\rPubSubMessage\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\x12Y\n\nattributes\x18\x03 \x03(\x0b\x32\x39.google.cloud.pubsublite.v1.PubSubMessage.AttributesEntryR\nattributes\x12\x39\n\nevent_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\teventTime\x1aj\n\x0f\x41ttributesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32+.google.cloud.pubsublite.v1.AttributeValuesR\x05value:\x02\x38\x01\" \n\x06\x43ursor\x12\x16\n\x06offset\x18\x01 \x01(\x03R\x06offset\"\xf1\x01\n\x10SequencedMessage\x12:\n\x06\x63ursor\x18\x01 \x01(\x0b\x32\".google.cloud.pubsublite.v1.CursorR\x06\x63ursor\x12=\n\x0cpublish_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0bpublishTime\x12\x43\n\x07message\x18\x03 \x01(\x0b\x32).google.cloud.pubsublite.v1.PubSubMessageR\x07message\x12\x1d\n\nsize_bytes\x18\x04 \x01(\x03R\tsizeBytes\"\xc2\x01\n\x0bReservation\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12/\n\x13throughput_capacity\x18\x02 \x01(\x03R\x12throughputCapacity:n\xea\x41k\n%pubsublite.googleapis.com/Reservation\x12\x42projects/{project}/locations/{location}/reservations/{reservation}\"\xa2\x07\n\x05Topic\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\\\n\x10partition_config\x18\x02 \x01(\x0b\x32\x31.google.cloud.pubsublite.v1.Topic.PartitionConfigR\x0fpartitionConfig\x12\\\n\x10retention_config\x18\x03 \x01(\x0b\x32\x31.google.cloud.pubsublite.v1.Topic.RetentionConfigR\x0fretentionConfig\x12\x62\n\x12reservation_config\x18\x04 \x01(\x0b\x32\x33.google.cloud.pubsublite.v1.Topic.ReservationConfigR\x11reservationConfig\x1a\x98\x02\n\x0fPartitionConfig\x12\x14\n\x05\x63ount\x18\x01 \x01(\x03R\x05\x63ount\x12\x1a\n\x05scale\x18\x02 \x01(\x05\x42\x02\x18\x01H\x00R\x05scale\x12X\n\x08\x63\x61pacity\x18\x03 \x01(\x0b\x32:.google.cloud.pubsublite.v1.Topic.PartitionConfig.CapacityH\x00R\x08\x63\x61pacity\x1al\n\x08\x43\x61pacity\x12-\n\x13publish_mib_per_sec\x18\x01 \x01(\x05R\x10publishMibPerSec\x12\x31\n\x15subscribe_mib_per_sec\x18\x02 \x01(\x05R\x12subscribeMibPerSecB\x0b\n\tdimension\x1at\n\x0fRetentionConfig\x12.\n\x13per_partition_bytes\x18\x01 \x01(\x03R\x11perPartitionBytes\x12\x31\n\x06period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x06period\x1av\n\x11ReservationConfig\x12\x61\n\x16throughput_reservation\x18\x01 \x01(\tB*\xfa\x41\'\n%pubsublite.googleapis.com/ReservationR\x15throughputReservation:\\\xea\x41Y\n\x1fpubsublite.googleapis.com/Topic\x12\x36projects/{project}/locations/{location}/topics/{topic}\"\xb6\x04\n\x0cSubscription\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12:\n\x05topic\x18\x02 \x01(\tB$\xfa\x41!\n\x1fpubsublite.googleapis.com/TopicR\x05topic\x12`\n\x0f\x64\x65livery_config\x18\x03 \x01(\x0b\x32\x37.google.cloud.pubsublite.v1.Subscription.DeliveryConfigR\x0e\x64\x65liveryConfig\x1a\x80\x02\n\x0e\x44\x65liveryConfig\x12~\n\x14\x64\x65livery_requirement\x18\x03 \x01(\x0e\x32K.google.cloud.pubsublite.v1.Subscription.DeliveryConfig.DeliveryRequirementR\x13\x64\x65liveryRequirement\"n\n\x13\x44\x65liveryRequirement\x12$\n DELIVERY_REQUIREMENT_UNSPECIFIED\x10\x00\x12\x17\n\x13\x44\x45LIVER_IMMEDIATELY\x10\x01\x12\x18\n\x14\x44\x45LIVER_AFTER_STORED\x10\x02:q\xea\x41n\n&pubsublite.googleapis.com/Subscription\x12\x44projects/{project}/locations/{location}/subscriptions/{subscription}\"\x92\x01\n\nTimeTarget\x12?\n\x0cpublish_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\x0bpublishTime\x12;\n\nevent_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\teventTimeB\x06\n\x04timeB\xd5\x01\n!com.google.cloud.pubsublite.protoB\x0b\x43ommonProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/pubsublite/v1;pubsublite\xf8\x01\x01\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1b\x06proto3')



_ATTRIBUTEVALUES = DESCRIPTOR.message_types_by_name['AttributeValues']
_PUBSUBMESSAGE = DESCRIPTOR.message_types_by_name['PubSubMessage']
_PUBSUBMESSAGE_ATTRIBUTESENTRY = _PUBSUBMESSAGE.nested_types_by_name['AttributesEntry']
_CURSOR = DESCRIPTOR.message_types_by_name['Cursor']
_SEQUENCEDMESSAGE = DESCRIPTOR.message_types_by_name['SequencedMessage']
_RESERVATION = DESCRIPTOR.message_types_by_name['Reservation']
_TOPIC = DESCRIPTOR.message_types_by_name['Topic']
_TOPIC_PARTITIONCONFIG = _TOPIC.nested_types_by_name['PartitionConfig']
_TOPIC_PARTITIONCONFIG_CAPACITY = _TOPIC_PARTITIONCONFIG.nested_types_by_name['Capacity']
_TOPIC_RETENTIONCONFIG = _TOPIC.nested_types_by_name['RetentionConfig']
_TOPIC_RESERVATIONCONFIG = _TOPIC.nested_types_by_name['ReservationConfig']
_SUBSCRIPTION = DESCRIPTOR.message_types_by_name['Subscription']
_SUBSCRIPTION_DELIVERYCONFIG = _SUBSCRIPTION.nested_types_by_name['DeliveryConfig']
_TIMETARGET = DESCRIPTOR.message_types_by_name['TimeTarget']
_SUBSCRIPTION_DELIVERYCONFIG_DELIVERYREQUIREMENT = _SUBSCRIPTION_DELIVERYCONFIG.enum_types_by_name['DeliveryRequirement']
AttributeValues = _reflection.GeneratedProtocolMessageType('AttributeValues', (_message.Message,), {
  'DESCRIPTOR' : _ATTRIBUTEVALUES,
  '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.AttributeValues)
  })
_sym_db.RegisterMessage(AttributeValues)

PubSubMessage = _reflection.GeneratedProtocolMessageType('PubSubMessage', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _PUBSUBMESSAGE_ATTRIBUTESENTRY,
    '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.PubSubMessage.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _PUBSUBMESSAGE,
  '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.PubSubMessage)
  })
_sym_db.RegisterMessage(PubSubMessage)
_sym_db.RegisterMessage(PubSubMessage.AttributesEntry)

Cursor = _reflection.GeneratedProtocolMessageType('Cursor', (_message.Message,), {
  'DESCRIPTOR' : _CURSOR,
  '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.Cursor)
  })
_sym_db.RegisterMessage(Cursor)

SequencedMessage = _reflection.GeneratedProtocolMessageType('SequencedMessage', (_message.Message,), {
  'DESCRIPTOR' : _SEQUENCEDMESSAGE,
  '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.SequencedMessage)
  })
_sym_db.RegisterMessage(SequencedMessage)

Reservation = _reflection.GeneratedProtocolMessageType('Reservation', (_message.Message,), {
  'DESCRIPTOR' : _RESERVATION,
  '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.Reservation)
  })
_sym_db.RegisterMessage(Reservation)

Topic = _reflection.GeneratedProtocolMessageType('Topic', (_message.Message,), {

  'PartitionConfig' : _reflection.GeneratedProtocolMessageType('PartitionConfig', (_message.Message,), {

    'Capacity' : _reflection.GeneratedProtocolMessageType('Capacity', (_message.Message,), {
      'DESCRIPTOR' : _TOPIC_PARTITIONCONFIG_CAPACITY,
      '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.Topic.PartitionConfig.Capacity)
      })
    ,
    'DESCRIPTOR' : _TOPIC_PARTITIONCONFIG,
    '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.Topic.PartitionConfig)
    })
  ,

  'RetentionConfig' : _reflection.GeneratedProtocolMessageType('RetentionConfig', (_message.Message,), {
    'DESCRIPTOR' : _TOPIC_RETENTIONCONFIG,
    '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.Topic.RetentionConfig)
    })
  ,

  'ReservationConfig' : _reflection.GeneratedProtocolMessageType('ReservationConfig', (_message.Message,), {
    'DESCRIPTOR' : _TOPIC_RESERVATIONCONFIG,
    '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.Topic.ReservationConfig)
    })
  ,
  'DESCRIPTOR' : _TOPIC,
  '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.Topic)
  })
_sym_db.RegisterMessage(Topic)
_sym_db.RegisterMessage(Topic.PartitionConfig)
_sym_db.RegisterMessage(Topic.PartitionConfig.Capacity)
_sym_db.RegisterMessage(Topic.RetentionConfig)
_sym_db.RegisterMessage(Topic.ReservationConfig)

Subscription = _reflection.GeneratedProtocolMessageType('Subscription', (_message.Message,), {

  'DeliveryConfig' : _reflection.GeneratedProtocolMessageType('DeliveryConfig', (_message.Message,), {
    'DESCRIPTOR' : _SUBSCRIPTION_DELIVERYCONFIG,
    '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.Subscription.DeliveryConfig)
    })
  ,
  'DESCRIPTOR' : _SUBSCRIPTION,
  '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.Subscription)
  })
_sym_db.RegisterMessage(Subscription)
_sym_db.RegisterMessage(Subscription.DeliveryConfig)

TimeTarget = _reflection.GeneratedProtocolMessageType('TimeTarget', (_message.Message,), {
  'DESCRIPTOR' : _TIMETARGET,
  '__module__' : 'google.cloud.pubsublite.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.TimeTarget)
  })
_sym_db.RegisterMessage(TimeTarget)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.cloud.pubsublite.protoB\013CommonProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/pubsublite/v1;pubsublite\370\001\001\252\002\032Google.Cloud.PubSubLite.V1\312\002\032Google\\Cloud\\PubSubLite\\V1\352\002\035Google::Cloud::PubSubLite::V1'
  _PUBSUBMESSAGE_ATTRIBUTESENTRY._options = None
  _PUBSUBMESSAGE_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _RESERVATION._options = None
  _RESERVATION._serialized_options = b'\352Ak\n%pubsublite.googleapis.com/Reservation\022Bprojects/{project}/locations/{location}/reservations/{reservation}'
  _TOPIC_PARTITIONCONFIG.fields_by_name['scale']._options = None
  _TOPIC_PARTITIONCONFIG.fields_by_name['scale']._serialized_options = b'\030\001'
  _TOPIC_RESERVATIONCONFIG.fields_by_name['throughput_reservation']._options = None
  _TOPIC_RESERVATIONCONFIG.fields_by_name['throughput_reservation']._serialized_options = b'\372A\'\n%pubsublite.googleapis.com/Reservation'
  _TOPIC._options = None
  _TOPIC._serialized_options = b'\352AY\n\037pubsublite.googleapis.com/Topic\0226projects/{project}/locations/{location}/topics/{topic}'
  _SUBSCRIPTION.fields_by_name['topic']._options = None
  _SUBSCRIPTION.fields_by_name['topic']._serialized_options = b'\372A!\n\037pubsublite.googleapis.com/Topic'
  _SUBSCRIPTION._options = None
  _SUBSCRIPTION._serialized_options = b'\352An\n&pubsublite.googleapis.com/Subscription\022Dprojects/{project}/locations/{location}/subscriptions/{subscription}'
  _ATTRIBUTEVALUES._serialized_start=193
  _ATTRIBUTEVALUES._serialized_end=234
  _PUBSUBMESSAGE._serialized_start=237
  _PUBSUBMESSAGE._serialized_end=548
  _PUBSUBMESSAGE_ATTRIBUTESENTRY._serialized_start=442
  _PUBSUBMESSAGE_ATTRIBUTESENTRY._serialized_end=548
  _CURSOR._serialized_start=550
  _CURSOR._serialized_end=582
  _SEQUENCEDMESSAGE._serialized_start=585
  _SEQUENCEDMESSAGE._serialized_end=826
  _RESERVATION._serialized_start=829
  _RESERVATION._serialized_end=1023
  _TOPIC._serialized_start=1026
  _TOPIC._serialized_end=1956
  _TOPIC_PARTITIONCONFIG._serialized_start=1344
  _TOPIC_PARTITIONCONFIG._serialized_end=1624
  _TOPIC_PARTITIONCONFIG_CAPACITY._serialized_start=1503
  _TOPIC_PARTITIONCONFIG_CAPACITY._serialized_end=1611
  _TOPIC_RETENTIONCONFIG._serialized_start=1626
  _TOPIC_RETENTIONCONFIG._serialized_end=1742
  _TOPIC_RESERVATIONCONFIG._serialized_start=1744
  _TOPIC_RESERVATIONCONFIG._serialized_end=1862
  _SUBSCRIPTION._serialized_start=1959
  _SUBSCRIPTION._serialized_end=2525
  _SUBSCRIPTION_DELIVERYCONFIG._serialized_start=2154
  _SUBSCRIPTION_DELIVERYCONFIG._serialized_end=2410
  _SUBSCRIPTION_DELIVERYCONFIG_DELIVERYREQUIREMENT._serialized_start=2300
  _SUBSCRIPTION_DELIVERYCONFIG_DELIVERYREQUIREMENT._serialized_end=2410
  _TIMETARGET._serialized_start=2528
  _TIMETARGET._serialized_end=2674
# @@protoc_insertion_point(module_scope)
