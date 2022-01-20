# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/redis/v1/cloud_redis.proto
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
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/redis/v1/cloud_redis.proto\x12\x15google.cloud.redis.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\":\n\x08NodeInfo\x12\x14\n\x02id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x02id\x12\x18\n\x04zone\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x04zone\"\xa8\x0f\n\x08Instance\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12\x43\n\x06labels\x18\x03 \x03(\x0b\x32+.google.cloud.redis.v1.Instance.LabelsEntryR\x06labels\x12%\n\x0blocation_id\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01R\nlocationId\x12<\n\x17\x61lternative_location_id\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01R\x15\x61lternativeLocationId\x12)\n\rredis_version\x18\x07 \x01(\tB\x04\xe2\x41\x01\x01R\x0credisVersion\x12\x30\n\x11reserved_ip_range\x18\t \x01(\tB\x04\xe2\x41\x01\x01R\x0freservedIpRange\x12\x18\n\x04host\x18\n \x01(\tB\x04\xe2\x41\x01\x03R\x04host\x12\x18\n\x04port\x18\x0b \x01(\x05\x42\x04\xe2\x41\x01\x03R\x04port\x12\x34\n\x13\x63urrent_location_id\x18\x0c \x01(\tB\x04\xe2\x41\x01\x03R\x11\x63urrentLocationId\x12\x41\n\x0b\x63reate_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x05state\x18\x0e \x01(\x0e\x32%.google.cloud.redis.v1.Instance.StateB\x04\xe2\x41\x01\x03R\x05state\x12+\n\x0estatus_message\x18\x0f \x01(\tB\x04\xe2\x41\x01\x03R\rstatusMessage\x12\\\n\rredis_configs\x18\x10 \x03(\x0b\x32\x31.google.cloud.redis.v1.Instance.RedisConfigsEntryB\x04\xe2\x41\x01\x01R\x0credisConfigs\x12>\n\x04tier\x18\x11 \x01(\x0e\x32$.google.cloud.redis.v1.Instance.TierB\x04\xe2\x41\x01\x02R\x04tier\x12*\n\x0ememory_size_gb\x18\x12 \x01(\x05\x42\x04\xe2\x41\x01\x02R\x0cmemorySizeGb\x12\x33\n\x12\x61uthorized_network\x18\x14 \x01(\tB\x04\xe2\x41\x01\x01R\x11\x61uthorizedNetwork\x12>\n\x18persistence_iam_identity\x18\x15 \x01(\tB\x04\xe2\x41\x01\x03R\x16persistenceIamIdentity\x12T\n\x0c\x63onnect_mode\x18\x16 \x01(\x0e\x32+.google.cloud.redis.v1.Instance.ConnectModeB\x04\xe2\x41\x01\x01R\x0b\x63onnectMode\x12)\n\rreplica_count\x18\x1f \x01(\x05\x42\x04\xe2\x41\x01\x01R\x0creplicaCount\x12;\n\x05nodes\x18  \x03(\x0b\x32\x1f.google.cloud.redis.v1.NodeInfoB\x04\xe2\x41\x01\x03R\x05nodes\x12)\n\rread_endpoint\x18! \x01(\tB\x04\xe2\x41\x01\x03R\x0creadEndpoint\x12\x32\n\x12read_endpoint_port\x18\" \x01(\x05\x42\x04\xe2\x41\x01\x03R\x10readEndpointPort\x12\x64\n\x12read_replicas_mode\x18# \x01(\x0e\x32\x30.google.cloud.redis.v1.Instance.ReadReplicasModeB\x04\xe2\x41\x01\x01R\x10readReplicasMode\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a?\n\x11RedisConfigsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x94\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\x12\r\n\tREPAIRING\x10\x05\x12\x0f\n\x0bMAINTENANCE\x10\x06\x12\r\n\tIMPORTING\x10\x08\x12\x10\n\x0c\x46\x41ILING_OVER\x10\t\"8\n\x04Tier\x12\x14\n\x10TIER_UNSPECIFIED\x10\x00\x12\t\n\x05\x42\x41SIC\x10\x01\x12\x0f\n\x0bSTANDARD_HA\x10\x03\"[\n\x0b\x43onnectMode\x12\x1c\n\x18\x43ONNECT_MODE_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x44IRECT_PEERING\x10\x01\x12\x1a\n\x16PRIVATE_SERVICE_ACCESS\x10\x02\"m\n\x10ReadReplicasMode\x12\"\n\x1eREAD_REPLICAS_MODE_UNSPECIFIED\x10\x00\x12\x1a\n\x16READ_REPLICAS_DISABLED\x10\x01\x12\x19\n\x15READ_REPLICAS_ENABLED\x10\x02:`\xea\x41]\n\x1dredis.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}\"\x96\x01\n\x14ListInstancesRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\xa0\x01\n\x15ListInstancesResponse\x12=\n\tinstances\x18\x01 \x03(\x0b\x32\x1f.google.cloud.redis.v1.InstanceR\tinstances\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12 \n\x0bunreachable\x18\x03 \x03(\tR\x0bunreachable\"P\n\x12GetInstanceRequest\x12:\n\x04name\x18\x01 \x01(\tB&\xe2\x41\x01\x02\xfa\x41\x1f\n\x1dredis.googleapis.com/InstanceR\x04name\"\xc5\x01\n\x15\x43reateInstanceRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12%\n\x0binstance_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\ninstanceId\x12\x41\n\x08instance\x18\x03 \x01(\x0b\x32\x1f.google.cloud.redis.v1.InstanceB\x04\xe2\x41\x01\x02R\x08instance\"\x9d\x01\n\x15UpdateInstanceRequest\x12\x41\n\x0bupdate_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\x12\x41\n\x08instance\x18\x02 \x01(\x0b\x32\x1f.google.cloud.redis.v1.InstanceB\x04\xe2\x41\x01\x02R\x08instance\"\x7f\n\x16UpgradeInstanceRequest\x12:\n\x04name\x18\x01 \x01(\tB&\xe2\x41\x01\x02\xfa\x41\x1f\n\x1dredis.googleapis.com/InstanceR\x04name\x12)\n\rredis_version\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0credisVersion\"S\n\x15\x44\x65leteInstanceRequest\x12:\n\x04name\x18\x01 \x01(\tB&\xe2\x41\x01\x02\xfa\x41\x1f\n\x1dredis.googleapis.com/InstanceR\x04name\"#\n\tGcsSource\x12\x16\n\x03uri\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x03uri\"Z\n\x0bInputConfig\x12\x41\n\ngcs_source\x18\x01 \x01(\x0b\x32 .google.cloud.redis.v1.GcsSourceH\x00R\tgcsSourceB\x08\n\x06source\"~\n\x15ImportInstanceRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12K\n\x0cinput_config\x18\x03 \x01(\x0b\x32\".google.cloud.redis.v1.InputConfigB\x04\xe2\x41\x01\x02R\x0binputConfig\"(\n\x0eGcsDestination\x12\x16\n\x03uri\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x03uri\"o\n\x0cOutputConfig\x12P\n\x0fgcs_destination\x18\x01 \x01(\x0b\x32%.google.cloud.redis.v1.GcsDestinationH\x00R\x0egcsDestinationB\r\n\x0b\x64\x65stination\"\x81\x01\n\x15\x45xportInstanceRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12N\n\routput_config\x18\x03 \x01(\x0b\x32#.google.cloud.redis.v1.OutputConfigB\x04\xe2\x41\x01\x02R\x0coutputConfig\"\xb8\x02\n\x17\x46\x61iloverInstanceRequest\x12:\n\x04name\x18\x01 \x01(\tB&\xe2\x41\x01\x02\xfa\x41\x1f\n\x1dredis.googleapis.com/InstanceR\x04name\x12y\n\x14\x64\x61ta_protection_mode\x18\x02 \x01(\x0e\x32\x41.google.cloud.redis.v1.FailoverInstanceRequest.DataProtectionModeB\x04\xe2\x41\x01\x01R\x12\x64\x61taProtectionMode\"f\n\x12\x44\x61taProtectionMode\x12$\n DATA_PROTECTION_MODE_UNSPECIFIED\x10\x00\x12\x15\n\x11LIMITED_DATA_LOSS\x10\x01\x12\x13\n\x0f\x46ORCE_DATA_LOSS\x10\x02\"\xa4\x02\n\x11OperationMetadata\x12;\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x16\n\x06target\x18\x03 \x01(\tR\x06target\x12\x12\n\x04verb\x18\x04 \x01(\tR\x04verb\x12#\n\rstatus_detail\x18\x05 \x01(\tR\x0cstatusDetail\x12)\n\x10\x63\x61ncel_requested\x18\x06 \x01(\x08R\x0f\x63\x61ncelRequested\x12\x1f\n\x0b\x61pi_version\x18\x07 \x01(\tR\napiVersion\"\xe6\x01\n\x10LocationMetadata\x12j\n\x0f\x61vailable_zones\x18\x01 \x03(\x0b\x32;.google.cloud.redis.v1.LocationMetadata.AvailableZonesEntryB\x04\xe2\x41\x01\x03R\x0e\x61vailableZones\x1a\x66\n\x13\x41vailableZonesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32#.google.cloud.redis.v1.ZoneMetadataR\x05value:\x02\x38\x01\"\x0e\n\x0cZoneMetadata2\xb3\x11\n\nCloudRedis\x12\xaa\x01\n\rListInstances\x12+.google.cloud.redis.v1.ListInstancesRequest\x1a,.google.cloud.redis.v1.ListInstancesResponse\">\xda\x41\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances\x12\x97\x01\n\x0bGetInstance\x12).google.cloud.redis.v1.GetInstanceRequest\x1a\x1f.google.cloud.redis.v1.Instance\"<\xda\x41\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}\x12\x89\x02\n\x0e\x43reateInstance\x12,.google.cloud.redis.v1.CreateInstanceRequest\x1a\x1d.google.longrunning.Operation\"\xa9\x01\xca\x41I\n\x1egoogle.cloud.redis.v1.Instance\x12\'google.cloud.redis.v1.OperationMetadata\xda\x41\x1bparent,instance_id,instance\x82\xd3\xe4\x93\x02\x39\"-/v1/{parent=projects/*/locations/*}/instances:\x08instance\x12\x8b\x02\n\x0eUpdateInstance\x12,.google.cloud.redis.v1.UpdateInstanceRequest\x1a\x1d.google.longrunning.Operation\"\xab\x01\xca\x41I\n\x1egoogle.cloud.redis.v1.Instance\x12\'google.cloud.redis.v1.OperationMetadata\xda\x41\x14update_mask,instance\x82\xd3\xe4\x93\x02\x42\x32\x36/v1/{instance.name=projects/*/locations/*/instances/*}:\x08instance\x12\x83\x02\n\x0fUpgradeInstance\x12-.google.cloud.redis.v1.UpgradeInstanceRequest\x1a\x1d.google.longrunning.Operation\"\xa1\x01\xca\x41I\n\x1egoogle.cloud.redis.v1.Instance\x12\'google.cloud.redis.v1.OperationMetadata\xda\x41\x12name,redis_version\x82\xd3\xe4\x93\x02:\"5/v1/{name=projects/*/locations/*/instances/*}:upgrade:\x01*\x12\xff\x01\n\x0eImportInstance\x12,.google.cloud.redis.v1.ImportInstanceRequest\x1a\x1d.google.longrunning.Operation\"\x9f\x01\xca\x41I\n\x1egoogle.cloud.redis.v1.Instance\x12\'google.cloud.redis.v1.OperationMetadata\xda\x41\x11name,input_config\x82\xd3\xe4\x93\x02\x39\"4/v1/{name=projects/*/locations/*/instances/*}:import:\x01*\x12\x80\x02\n\x0e\x45xportInstance\x12,.google.cloud.redis.v1.ExportInstanceRequest\x1a\x1d.google.longrunning.Operation\"\xa0\x01\xca\x41I\n\x1egoogle.cloud.redis.v1.Instance\x12\'google.cloud.redis.v1.OperationMetadata\xda\x41\x12name,output_config\x82\xd3\xe4\x93\x02\x39\"4/v1/{name=projects/*/locations/*/instances/*}:export:\x01*\x12\x8d\x02\n\x10\x46\x61iloverInstance\x12..google.cloud.redis.v1.FailoverInstanceRequest\x1a\x1d.google.longrunning.Operation\"\xa9\x01\xca\x41I\n\x1egoogle.cloud.redis.v1.Instance\x12\'google.cloud.redis.v1.OperationMetadata\xda\x41\x19name,data_protection_mode\x82\xd3\xe4\x93\x02;\"6/v1/{name=projects/*/locations/*/instances/*}:failover:\x01*\x12\xde\x01\n\x0e\x44\x65leteInstance\x12,.google.cloud.redis.v1.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation\"\x7f\xca\x41@\n\x15google.protobuf.Empty\x12\'google.cloud.redis.v1.OperationMetadata\xda\x41\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}\x1aH\xca\x41\x14redis.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformBs\n\x19\x63om.google.cloud.redis.v1B\x18\x43loudRedisServiceV1ProtoP\x01Z:google.golang.org/genproto/googleapis/cloud/redis/v1;redisb\x06proto3')



_NODEINFO = DESCRIPTOR.message_types_by_name['NodeInfo']
_INSTANCE = DESCRIPTOR.message_types_by_name['Instance']
_INSTANCE_LABELSENTRY = _INSTANCE.nested_types_by_name['LabelsEntry']
_INSTANCE_REDISCONFIGSENTRY = _INSTANCE.nested_types_by_name['RedisConfigsEntry']
_LISTINSTANCESREQUEST = DESCRIPTOR.message_types_by_name['ListInstancesRequest']
_LISTINSTANCESRESPONSE = DESCRIPTOR.message_types_by_name['ListInstancesResponse']
_GETINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['GetInstanceRequest']
_CREATEINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['CreateInstanceRequest']
_UPDATEINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['UpdateInstanceRequest']
_UPGRADEINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['UpgradeInstanceRequest']
_DELETEINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['DeleteInstanceRequest']
_GCSSOURCE = DESCRIPTOR.message_types_by_name['GcsSource']
_INPUTCONFIG = DESCRIPTOR.message_types_by_name['InputConfig']
_IMPORTINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['ImportInstanceRequest']
_GCSDESTINATION = DESCRIPTOR.message_types_by_name['GcsDestination']
_OUTPUTCONFIG = DESCRIPTOR.message_types_by_name['OutputConfig']
_EXPORTINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['ExportInstanceRequest']
_FAILOVERINSTANCEREQUEST = DESCRIPTOR.message_types_by_name['FailoverInstanceRequest']
_OPERATIONMETADATA = DESCRIPTOR.message_types_by_name['OperationMetadata']
_LOCATIONMETADATA = DESCRIPTOR.message_types_by_name['LocationMetadata']
_LOCATIONMETADATA_AVAILABLEZONESENTRY = _LOCATIONMETADATA.nested_types_by_name['AvailableZonesEntry']
_ZONEMETADATA = DESCRIPTOR.message_types_by_name['ZoneMetadata']
_INSTANCE_STATE = _INSTANCE.enum_types_by_name['State']
_INSTANCE_TIER = _INSTANCE.enum_types_by_name['Tier']
_INSTANCE_CONNECTMODE = _INSTANCE.enum_types_by_name['ConnectMode']
_INSTANCE_READREPLICASMODE = _INSTANCE.enum_types_by_name['ReadReplicasMode']
_FAILOVERINSTANCEREQUEST_DATAPROTECTIONMODE = _FAILOVERINSTANCEREQUEST.enum_types_by_name['DataProtectionMode']
NodeInfo = _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _NODEINFO,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.NodeInfo)
  })
_sym_db.RegisterMessage(NodeInfo)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_LABELSENTRY,
    '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.Instance.LabelsEntry)
    })
  ,

  'RedisConfigsEntry' : _reflection.GeneratedProtocolMessageType('RedisConfigsEntry', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_REDISCONFIGSENTRY,
    '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.Instance.RedisConfigsEntry)
    })
  ,
  'DESCRIPTOR' : _INSTANCE,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.Instance)
  })
_sym_db.RegisterMessage(Instance)
_sym_db.RegisterMessage(Instance.LabelsEntry)
_sym_db.RegisterMessage(Instance.RedisConfigsEntry)

ListInstancesRequest = _reflection.GeneratedProtocolMessageType('ListInstancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINSTANCESREQUEST,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.ListInstancesRequest)
  })
_sym_db.RegisterMessage(ListInstancesRequest)

ListInstancesResponse = _reflection.GeneratedProtocolMessageType('ListInstancesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINSTANCESRESPONSE,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.ListInstancesResponse)
  })
_sym_db.RegisterMessage(ListInstancesResponse)

GetInstanceRequest = _reflection.GeneratedProtocolMessageType('GetInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINSTANCEREQUEST,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.GetInstanceRequest)
  })
_sym_db.RegisterMessage(GetInstanceRequest)

CreateInstanceRequest = _reflection.GeneratedProtocolMessageType('CreateInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEINSTANCEREQUEST,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.CreateInstanceRequest)
  })
_sym_db.RegisterMessage(CreateInstanceRequest)

UpdateInstanceRequest = _reflection.GeneratedProtocolMessageType('UpdateInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEINSTANCEREQUEST,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.UpdateInstanceRequest)
  })
_sym_db.RegisterMessage(UpdateInstanceRequest)

UpgradeInstanceRequest = _reflection.GeneratedProtocolMessageType('UpgradeInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPGRADEINSTANCEREQUEST,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.UpgradeInstanceRequest)
  })
_sym_db.RegisterMessage(UpgradeInstanceRequest)

DeleteInstanceRequest = _reflection.GeneratedProtocolMessageType('DeleteInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEINSTANCEREQUEST,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.DeleteInstanceRequest)
  })
_sym_db.RegisterMessage(DeleteInstanceRequest)

GcsSource = _reflection.GeneratedProtocolMessageType('GcsSource', (_message.Message,), {
  'DESCRIPTOR' : _GCSSOURCE,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.GcsSource)
  })
_sym_db.RegisterMessage(GcsSource)

InputConfig = _reflection.GeneratedProtocolMessageType('InputConfig', (_message.Message,), {
  'DESCRIPTOR' : _INPUTCONFIG,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.InputConfig)
  })
_sym_db.RegisterMessage(InputConfig)

ImportInstanceRequest = _reflection.GeneratedProtocolMessageType('ImportInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTINSTANCEREQUEST,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.ImportInstanceRequest)
  })
_sym_db.RegisterMessage(ImportInstanceRequest)

GcsDestination = _reflection.GeneratedProtocolMessageType('GcsDestination', (_message.Message,), {
  'DESCRIPTOR' : _GCSDESTINATION,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.GcsDestination)
  })
_sym_db.RegisterMessage(GcsDestination)

OutputConfig = _reflection.GeneratedProtocolMessageType('OutputConfig', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTCONFIG,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.OutputConfig)
  })
_sym_db.RegisterMessage(OutputConfig)

ExportInstanceRequest = _reflection.GeneratedProtocolMessageType('ExportInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTINSTANCEREQUEST,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.ExportInstanceRequest)
  })
_sym_db.RegisterMessage(ExportInstanceRequest)

FailoverInstanceRequest = _reflection.GeneratedProtocolMessageType('FailoverInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _FAILOVERINSTANCEREQUEST,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.FailoverInstanceRequest)
  })
_sym_db.RegisterMessage(FailoverInstanceRequest)

OperationMetadata = _reflection.GeneratedProtocolMessageType('OperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONMETADATA,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.OperationMetadata)
  })
_sym_db.RegisterMessage(OperationMetadata)

LocationMetadata = _reflection.GeneratedProtocolMessageType('LocationMetadata', (_message.Message,), {

  'AvailableZonesEntry' : _reflection.GeneratedProtocolMessageType('AvailableZonesEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOCATIONMETADATA_AVAILABLEZONESENTRY,
    '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.LocationMetadata.AvailableZonesEntry)
    })
  ,
  'DESCRIPTOR' : _LOCATIONMETADATA,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.LocationMetadata)
  })
_sym_db.RegisterMessage(LocationMetadata)
_sym_db.RegisterMessage(LocationMetadata.AvailableZonesEntry)

ZoneMetadata = _reflection.GeneratedProtocolMessageType('ZoneMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ZONEMETADATA,
  '__module__' : 'google.cloud.redis.v1.cloud_redis_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.redis.v1.ZoneMetadata)
  })
_sym_db.RegisterMessage(ZoneMetadata)

_CLOUDREDIS = DESCRIPTOR.services_by_name['CloudRedis']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.google.cloud.redis.v1B\030CloudRedisServiceV1ProtoP\001Z:google.golang.org/genproto/googleapis/cloud/redis/v1;redis'
  _NODEINFO.fields_by_name['id']._options = None
  _NODEINFO.fields_by_name['id']._serialized_options = b'\342A\001\003'
  _NODEINFO.fields_by_name['zone']._options = None
  _NODEINFO.fields_by_name['zone']._serialized_options = b'\342A\001\003'
  _INSTANCE_LABELSENTRY._options = None
  _INSTANCE_LABELSENTRY._serialized_options = b'8\001'
  _INSTANCE_REDISCONFIGSENTRY._options = None
  _INSTANCE_REDISCONFIGSENTRY._serialized_options = b'8\001'
  _INSTANCE.fields_by_name['name']._options = None
  _INSTANCE.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _INSTANCE.fields_by_name['location_id']._options = None
  _INSTANCE.fields_by_name['location_id']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['alternative_location_id']._options = None
  _INSTANCE.fields_by_name['alternative_location_id']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['redis_version']._options = None
  _INSTANCE.fields_by_name['redis_version']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['reserved_ip_range']._options = None
  _INSTANCE.fields_by_name['reserved_ip_range']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['host']._options = None
  _INSTANCE.fields_by_name['host']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['port']._options = None
  _INSTANCE.fields_by_name['port']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['current_location_id']._options = None
  _INSTANCE.fields_by_name['current_location_id']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['create_time']._options = None
  _INSTANCE.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['state']._options = None
  _INSTANCE.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['status_message']._options = None
  _INSTANCE.fields_by_name['status_message']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['redis_configs']._options = None
  _INSTANCE.fields_by_name['redis_configs']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['tier']._options = None
  _INSTANCE.fields_by_name['tier']._serialized_options = b'\342A\001\002'
  _INSTANCE.fields_by_name['memory_size_gb']._options = None
  _INSTANCE.fields_by_name['memory_size_gb']._serialized_options = b'\342A\001\002'
  _INSTANCE.fields_by_name['authorized_network']._options = None
  _INSTANCE.fields_by_name['authorized_network']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['persistence_iam_identity']._options = None
  _INSTANCE.fields_by_name['persistence_iam_identity']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['connect_mode']._options = None
  _INSTANCE.fields_by_name['connect_mode']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['replica_count']._options = None
  _INSTANCE.fields_by_name['replica_count']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['nodes']._options = None
  _INSTANCE.fields_by_name['nodes']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['read_endpoint']._options = None
  _INSTANCE.fields_by_name['read_endpoint']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['read_endpoint_port']._options = None
  _INSTANCE.fields_by_name['read_endpoint_port']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['read_replicas_mode']._options = None
  _INSTANCE.fields_by_name['read_replicas_mode']._serialized_options = b'\342A\001\001'
  _INSTANCE._options = None
  _INSTANCE._serialized_options = b'\352A]\n\035redis.googleapis.com/Instance\022<projects/{project}/locations/{location}/instances/{instance}'
  _LISTINSTANCESREQUEST.fields_by_name['parent']._options = None
  _LISTINSTANCESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _GETINSTANCEREQUEST.fields_by_name['name']._options = None
  _GETINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\037\n\035redis.googleapis.com/Instance'
  _CREATEINSTANCEREQUEST.fields_by_name['parent']._options = None
  _CREATEINSTANCEREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\n!locations.googleapis.com/Location'
  _CREATEINSTANCEREQUEST.fields_by_name['instance_id']._options = None
  _CREATEINSTANCEREQUEST.fields_by_name['instance_id']._serialized_options = b'\342A\001\002'
  _CREATEINSTANCEREQUEST.fields_by_name['instance']._options = None
  _CREATEINSTANCEREQUEST.fields_by_name['instance']._serialized_options = b'\342A\001\002'
  _UPDATEINSTANCEREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEINSTANCEREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _UPDATEINSTANCEREQUEST.fields_by_name['instance']._options = None
  _UPDATEINSTANCEREQUEST.fields_by_name['instance']._serialized_options = b'\342A\001\002'
  _UPGRADEINSTANCEREQUEST.fields_by_name['name']._options = None
  _UPGRADEINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\037\n\035redis.googleapis.com/Instance'
  _UPGRADEINSTANCEREQUEST.fields_by_name['redis_version']._options = None
  _UPGRADEINSTANCEREQUEST.fields_by_name['redis_version']._serialized_options = b'\342A\001\002'
  _DELETEINSTANCEREQUEST.fields_by_name['name']._options = None
  _DELETEINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\037\n\035redis.googleapis.com/Instance'
  _GCSSOURCE.fields_by_name['uri']._options = None
  _GCSSOURCE.fields_by_name['uri']._serialized_options = b'\342A\001\002'
  _IMPORTINSTANCEREQUEST.fields_by_name['name']._options = None
  _IMPORTINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _IMPORTINSTANCEREQUEST.fields_by_name['input_config']._options = None
  _IMPORTINSTANCEREQUEST.fields_by_name['input_config']._serialized_options = b'\342A\001\002'
  _GCSDESTINATION.fields_by_name['uri']._options = None
  _GCSDESTINATION.fields_by_name['uri']._serialized_options = b'\342A\001\002'
  _EXPORTINSTANCEREQUEST.fields_by_name['name']._options = None
  _EXPORTINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _EXPORTINSTANCEREQUEST.fields_by_name['output_config']._options = None
  _EXPORTINSTANCEREQUEST.fields_by_name['output_config']._serialized_options = b'\342A\001\002'
  _FAILOVERINSTANCEREQUEST.fields_by_name['name']._options = None
  _FAILOVERINSTANCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\037\n\035redis.googleapis.com/Instance'
  _FAILOVERINSTANCEREQUEST.fields_by_name['data_protection_mode']._options = None
  _FAILOVERINSTANCEREQUEST.fields_by_name['data_protection_mode']._serialized_options = b'\342A\001\001'
  _LOCATIONMETADATA_AVAILABLEZONESENTRY._options = None
  _LOCATIONMETADATA_AVAILABLEZONESENTRY._serialized_options = b'8\001'
  _LOCATIONMETADATA.fields_by_name['available_zones']._options = None
  _LOCATIONMETADATA.fields_by_name['available_zones']._serialized_options = b'\342A\001\003'
  _CLOUDREDIS._options = None
  _CLOUDREDIS._serialized_options = b'\312A\024redis.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _CLOUDREDIS.methods_by_name['ListInstances']._options = None
  _CLOUDREDIS.methods_by_name['ListInstances']._serialized_options = b'\332A\006parent\202\323\344\223\002/\022-/v1/{parent=projects/*/locations/*}/instances'
  _CLOUDREDIS.methods_by_name['GetInstance']._options = None
  _CLOUDREDIS.methods_by_name['GetInstance']._serialized_options = b'\332A\004name\202\323\344\223\002/\022-/v1/{name=projects/*/locations/*/instances/*}'
  _CLOUDREDIS.methods_by_name['CreateInstance']._options = None
  _CLOUDREDIS.methods_by_name['CreateInstance']._serialized_options = b'\312AI\n\036google.cloud.redis.v1.Instance\022\'google.cloud.redis.v1.OperationMetadata\332A\033parent,instance_id,instance\202\323\344\223\0029\"-/v1/{parent=projects/*/locations/*}/instances:\010instance'
  _CLOUDREDIS.methods_by_name['UpdateInstance']._options = None
  _CLOUDREDIS.methods_by_name['UpdateInstance']._serialized_options = b'\312AI\n\036google.cloud.redis.v1.Instance\022\'google.cloud.redis.v1.OperationMetadata\332A\024update_mask,instance\202\323\344\223\002B26/v1/{instance.name=projects/*/locations/*/instances/*}:\010instance'
  _CLOUDREDIS.methods_by_name['UpgradeInstance']._options = None
  _CLOUDREDIS.methods_by_name['UpgradeInstance']._serialized_options = b'\312AI\n\036google.cloud.redis.v1.Instance\022\'google.cloud.redis.v1.OperationMetadata\332A\022name,redis_version\202\323\344\223\002:\"5/v1/{name=projects/*/locations/*/instances/*}:upgrade:\001*'
  _CLOUDREDIS.methods_by_name['ImportInstance']._options = None
  _CLOUDREDIS.methods_by_name['ImportInstance']._serialized_options = b'\312AI\n\036google.cloud.redis.v1.Instance\022\'google.cloud.redis.v1.OperationMetadata\332A\021name,input_config\202\323\344\223\0029\"4/v1/{name=projects/*/locations/*/instances/*}:import:\001*'
  _CLOUDREDIS.methods_by_name['ExportInstance']._options = None
  _CLOUDREDIS.methods_by_name['ExportInstance']._serialized_options = b'\312AI\n\036google.cloud.redis.v1.Instance\022\'google.cloud.redis.v1.OperationMetadata\332A\022name,output_config\202\323\344\223\0029\"4/v1/{name=projects/*/locations/*/instances/*}:export:\001*'
  _CLOUDREDIS.methods_by_name['FailoverInstance']._options = None
  _CLOUDREDIS.methods_by_name['FailoverInstance']._serialized_options = b'\312AI\n\036google.cloud.redis.v1.Instance\022\'google.cloud.redis.v1.OperationMetadata\332A\031name,data_protection_mode\202\323\344\223\002;\"6/v1/{name=projects/*/locations/*/instances/*}:failover:\001*'
  _CLOUDREDIS.methods_by_name['DeleteInstance']._options = None
  _CLOUDREDIS.methods_by_name['DeleteInstance']._serialized_options = b'\312A@\n\025google.protobuf.Empty\022\'google.cloud.redis.v1.OperationMetadata\332A\004name\202\323\344\223\002/*-/v1/{name=projects/*/locations/*/instances/*}'
  _NODEINFO._serialized_start=285
  _NODEINFO._serialized_end=343
  _INSTANCE._serialized_start=346
  _INSTANCE._serialized_end=2306
  _INSTANCE_LABELSENTRY._serialized_start=1673
  _INSTANCE_LABELSENTRY._serialized_end=1730
  _INSTANCE_REDISCONFIGSENTRY._serialized_start=1732
  _INSTANCE_REDISCONFIGSENTRY._serialized_end=1795
  _INSTANCE_STATE._serialized_start=1798
  _INSTANCE_STATE._serialized_end=1946
  _INSTANCE_TIER._serialized_start=1948
  _INSTANCE_TIER._serialized_end=2004
  _INSTANCE_CONNECTMODE._serialized_start=2006
  _INSTANCE_CONNECTMODE._serialized_end=2097
  _INSTANCE_READREPLICASMODE._serialized_start=2099
  _INSTANCE_READREPLICASMODE._serialized_end=2208
  _LISTINSTANCESREQUEST._serialized_start=2309
  _LISTINSTANCESREQUEST._serialized_end=2459
  _LISTINSTANCESRESPONSE._serialized_start=2462
  _LISTINSTANCESRESPONSE._serialized_end=2622
  _GETINSTANCEREQUEST._serialized_start=2624
  _GETINSTANCEREQUEST._serialized_end=2704
  _CREATEINSTANCEREQUEST._serialized_start=2707
  _CREATEINSTANCEREQUEST._serialized_end=2904
  _UPDATEINSTANCEREQUEST._serialized_start=2907
  _UPDATEINSTANCEREQUEST._serialized_end=3064
  _UPGRADEINSTANCEREQUEST._serialized_start=3066
  _UPGRADEINSTANCEREQUEST._serialized_end=3193
  _DELETEINSTANCEREQUEST._serialized_start=3195
  _DELETEINSTANCEREQUEST._serialized_end=3278
  _GCSSOURCE._serialized_start=3280
  _GCSSOURCE._serialized_end=3315
  _INPUTCONFIG._serialized_start=3317
  _INPUTCONFIG._serialized_end=3407
  _IMPORTINSTANCEREQUEST._serialized_start=3409
  _IMPORTINSTANCEREQUEST._serialized_end=3535
  _GCSDESTINATION._serialized_start=3537
  _GCSDESTINATION._serialized_end=3577
  _OUTPUTCONFIG._serialized_start=3579
  _OUTPUTCONFIG._serialized_end=3690
  _EXPORTINSTANCEREQUEST._serialized_start=3693
  _EXPORTINSTANCEREQUEST._serialized_end=3822
  _FAILOVERINSTANCEREQUEST._serialized_start=3825
  _FAILOVERINSTANCEREQUEST._serialized_end=4137
  _FAILOVERINSTANCEREQUEST_DATAPROTECTIONMODE._serialized_start=4035
  _FAILOVERINSTANCEREQUEST_DATAPROTECTIONMODE._serialized_end=4137
  _OPERATIONMETADATA._serialized_start=4140
  _OPERATIONMETADATA._serialized_end=4432
  _LOCATIONMETADATA._serialized_start=4435
  _LOCATIONMETADATA._serialized_end=4665
  _LOCATIONMETADATA_AVAILABLEZONESENTRY._serialized_start=4563
  _LOCATIONMETADATA_AVAILABLEZONESENTRY._serialized_end=4665
  _ZONEMETADATA._serialized_start=4667
  _ZONEMETADATA._serialized_end=4681
  _CLOUDREDIS._serialized_start=4684
  _CLOUDREDIS._serialized_end=6911
# @@protoc_insertion_point(module_scope)
