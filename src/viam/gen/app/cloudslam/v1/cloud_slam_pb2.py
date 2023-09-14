"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!app/cloudslam/v1/cloud_slam.proto\x12\x15viam.app.cloudslam.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc6\x02\n\x1aStartMappingSessionRequest\x128\n\x0bslam_config\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\nslamConfig\x12!\n\x0cslam_version\x18\x02 \x01(\tR\x0bslamVersion\x12\x19\n\x08map_name\x18\x03 \x01(\tR\x07mapName\x12\'\n\x0forganization_id\x18\x04 \x01(\tR\x0eorganizationId\x12\x1f\n\x0blocation_id\x18\x05 \x01(\tR\nlocationId\x12\x19\n\x08robot_id\x18\x06 \x01(\tR\x07robotId\x12.\n\x13viam_server_version\x18\x07 \x01(\tR\x11viamServerVersion\x12\x1b\n\tis_online\x18\x08 \x01(\x08R\x08isOnline"<\n\x1bStartMappingSessionResponse\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId"D\n\'GetActiveMappingSessionsForRobotRequest\x12\x19\n\x08robot_id\x18\x01 \x01(\tR\x07robotId"I\n(GetActiveMappingSessionsForRobotResponse\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId"C\n"GetMappingSessionPointCloudRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId"h\n#GetMappingSessionPointCloudResponse\x12\x17\n\x07map_url\x18\x01 \x01(\tR\x06mapUrl\x12(\n\x04pose\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose"f\n\x1aListMappingSessionsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId"_\n\x1bListMappingSessionsResponse\x12@\n\x07session\x18\x01 \x03(\x0b2&.viam.app.cloudslam.v1.MappingMetadataR\x07session":\n\x19StopMappingSessionRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId"U\n\x1aStopMappingSessionResponse\x12\x1d\n\npackage_id\x18\x01 \x01(\tR\tpackageId\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version"E\n$GetMappingSessionMetadataByIDRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId"z\n%GetMappingSessionMetadataByIDResponse\x12Q\n\x10session_metadata\x18\x01 \x01(\x0b2&.viam.app.cloudslam.v1.MappingMetadataR\x0fsessionMetadata"\xd8\x01\n\'UpdateMappingSessionMetadataByIDRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId\x12\x1d\n\nend_status\x18\x02 \x01(\tR\tendStatus\x12R\n\x18time_cloud_run_job_ended\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\x14timeCloudRunJobEnded\x12\x1b\n\terror_msg\x18\x04 \x01(\tR\x08errorMsg"*\n(UpdateMappingSessionMetadataByIDResponse"\x93\x05\n\x0fMappingMetadata\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId\x12\x19\n\x08robot_id\x18\x03 \x01(\tR\x07robotId\x12L\n\x14time_start_submitted\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x12timeStartSubmitted\x12V\n\x1atime_cloud_run_job_started\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x16timeCloudRunJobStarted\x12H\n\x12time_end_submitted\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\x10timeEndSubmitted\x12R\n\x18time_cloud_run_job_ended\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampR\x14timeCloudRunJobEnded\x12\x1d\n\nend_status\x18\x08 \x01(\tR\tendStatus\x12\'\n\x10cloud_run_job_id\x18\t \x01(\tR\rcloudRunJobId\x12.\n\x13viam_server_version\x18\n \x01(\tR\x11viamServerVersion\x12\x19\n\x08map_name\x18\x0b \x01(\tR\x07mapName\x12!\n\x0cslam_version\x18\x0c \x01(\tR\x0bslamVersion\x12\x16\n\x06config\x18\r \x01(\tR\x06config\x12\x1b\n\terror_msg\x18\x0e \x01(\tR\x08errorMsg2\x89\x08\n\x10CloudSLAMService\x12|\n\x13StartMappingSession\x121.viam.app.cloudslam.v1.StartMappingSessionRequest\x1a2.viam.app.cloudslam.v1.StartMappingSessionResponse\x12\xa3\x01\n GetActiveMappingSessionsForRobot\x12>.viam.app.cloudslam.v1.GetActiveMappingSessionsForRobotRequest\x1a?.viam.app.cloudslam.v1.GetActiveMappingSessionsForRobotResponse\x12\x94\x01\n\x1bGetMappingSessionPointCloud\x129.viam.app.cloudslam.v1.GetMappingSessionPointCloudRequest\x1a:.viam.app.cloudslam.v1.GetMappingSessionPointCloudResponse\x12|\n\x13ListMappingSessions\x121.viam.app.cloudslam.v1.ListMappingSessionsRequest\x1a2.viam.app.cloudslam.v1.ListMappingSessionsResponse\x12y\n\x12StopMappingSession\x120.viam.app.cloudslam.v1.StopMappingSessionRequest\x1a1.viam.app.cloudslam.v1.StopMappingSessionResponse\x12\x9a\x01\n\x1dGetMappingSessionMetadataByID\x12;.viam.app.cloudslam.v1.GetMappingSessionMetadataByIDRequest\x1a<.viam.app.cloudslam.v1.GetMappingSessionMetadataByIDResponse\x12\xa3\x01\n UpdateMappingSessionMetadataByID\x12>.viam.app.cloudslam.v1.UpdateMappingSessionMetadataByIDRequest\x1a?.viam.app.cloudslam.v1.UpdateMappingSessionMetadataByIDResponseB"Z go.viam.com/api/app/cloudslam/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.cloudslam.v1.cloud_slam_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z go.viam.com/api/app/cloudslam/v1'
    _STARTMAPPINGSESSIONREQUEST._serialized_start = 148
    _STARTMAPPINGSESSIONREQUEST._serialized_end = 474
    _STARTMAPPINGSESSIONRESPONSE._serialized_start = 476
    _STARTMAPPINGSESSIONRESPONSE._serialized_end = 536
    _GETACTIVEMAPPINGSESSIONSFORROBOTREQUEST._serialized_start = 538
    _GETACTIVEMAPPINGSESSIONSFORROBOTREQUEST._serialized_end = 606
    _GETACTIVEMAPPINGSESSIONSFORROBOTRESPONSE._serialized_start = 608
    _GETACTIVEMAPPINGSESSIONSFORROBOTRESPONSE._serialized_end = 681
    _GETMAPPINGSESSIONPOINTCLOUDREQUEST._serialized_start = 683
    _GETMAPPINGSESSIONPOINTCLOUDREQUEST._serialized_end = 750
    _GETMAPPINGSESSIONPOINTCLOUDRESPONSE._serialized_start = 752
    _GETMAPPINGSESSIONPOINTCLOUDRESPONSE._serialized_end = 856
    _LISTMAPPINGSESSIONSREQUEST._serialized_start = 858
    _LISTMAPPINGSESSIONSREQUEST._serialized_end = 960
    _LISTMAPPINGSESSIONSRESPONSE._serialized_start = 962
    _LISTMAPPINGSESSIONSRESPONSE._serialized_end = 1057
    _STOPMAPPINGSESSIONREQUEST._serialized_start = 1059
    _STOPMAPPINGSESSIONREQUEST._serialized_end = 1117
    _STOPMAPPINGSESSIONRESPONSE._serialized_start = 1119
    _STOPMAPPINGSESSIONRESPONSE._serialized_end = 1204
    _GETMAPPINGSESSIONMETADATABYIDREQUEST._serialized_start = 1206
    _GETMAPPINGSESSIONMETADATABYIDREQUEST._serialized_end = 1275
    _GETMAPPINGSESSIONMETADATABYIDRESPONSE._serialized_start = 1277
    _GETMAPPINGSESSIONMETADATABYIDRESPONSE._serialized_end = 1399
    _UPDATEMAPPINGSESSIONMETADATABYIDREQUEST._serialized_start = 1402
    _UPDATEMAPPINGSESSIONMETADATABYIDREQUEST._serialized_end = 1618
    _UPDATEMAPPINGSESSIONMETADATABYIDRESPONSE._serialized_start = 1620
    _UPDATEMAPPINGSESSIONMETADATABYIDRESPONSE._serialized_end = 1662
    _MAPPINGMETADATA._serialized_start = 1665
    _MAPPINGMETADATA._serialized_end = 2324
    _CLOUDSLAMSERVICE._serialized_start = 2327
    _CLOUDSLAMSERVICE._serialized_end = 3360