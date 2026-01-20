"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!app/cloudslam/v1/cloud_slam.proto\x12\x15viam.app.cloudslam.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa2\x04\n\x1aStartMappingSessionRequest\x12!\n\x0cslam_version\x18\x01 \x01(\tR\x0bslamVersion\x12.\n\x13viam_server_version\x18\x02 \x01(\tR\x11viamServerVersion\x12\x19\n\x08map_name\x18\x03 \x01(\tR\x07mapName\x12\'\n\x0forganization_id\x18\x04 \x01(\tR\x0eorganizationId\x12\x1f\n\x0blocation_id\x18\x05 \x01(\tR\nlocationId\x12\x19\n\x08robot_id\x18\x06 \x01(\tR\x07robotId\x12Q\n\x10capture_interval\x18\x07 \x01(\x0b2&.viam.app.cloudslam.v1.CaptureIntervalR\x0fcaptureInterval\x12;\n\x07sensors\x18\x08 \x03(\x0b2!.viam.app.cloudslam.v1.SensorInfoR\x07sensors\x128\n\x0bslam_config\x18\n \x01(\x0b2\x17.google.protobuf.StructR\nslamConfig\x120\n\x14existing_map_version\x18\x0b \x01(\tR\x12existingMapVersion\x125\n\x06module\x18\x0c \x01(\x0b2\x1d.viam.app.cloudslam.v1.ModuleR\x06module"S\n\x06Module\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1b\n\tmodule_id\x18\x03 \x01(\tR\x08moduleId\x12\x18\n\x07version\x18\x04 \x01(\tR\x07version"\x80\x01\n\nSensorInfo\x122\n\x15source_component_name\x18\x01 \x01(\tR\x13sourceComponentName\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12*\n\x11data_frequency_hz\x18\x03 \x01(\tR\x0fdataFrequencyHz"\x83\x01\n\x0fCaptureInterval\x129\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\tstartTime\x125\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07endTime"<\n\x1bStartMappingSessionResponse\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId"D\n\'GetActiveMappingSessionsForRobotRequest\x12\x19\n\x08robot_id\x18\x01 \x01(\tR\x07robotId"I\n(GetActiveMappingSessionsForRobotResponse\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId"C\n"GetMappingSessionPointCloudRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId"h\n#GetMappingSessionPointCloudResponse\x12\x17\n\x07map_url\x18\x01 \x01(\tR\x06mapUrl\x12(\n\x04pose\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose"f\n\x1aListMappingSessionsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId"_\n\x1bListMappingSessionsResponse\x12@\n\x07session\x18\x01 \x03(\x0b2&.viam.app.cloudslam.v1.MappingMetadataR\x07session":\n\x19StopMappingSessionRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId"U\n\x1aStopMappingSessionResponse\x12\x1d\n\npackage_id\x18\x01 \x01(\tR\tpackageId\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version"E\n$GetMappingSessionMetadataByIDRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId"z\n%GetMappingSessionMetadataByIDResponse\x12Q\n\x10session_metadata\x18\x01 \x01(\x0b2&.viam.app.cloudslam.v1.MappingMetadataR\x0fsessionMetadata"\xb5\x05\n\x0fMappingMetadata\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId\x12\x19\n\x08robot_id\x18\x03 \x01(\tR\x07robotId\x12L\n\x14time_start_submitted\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x12timeStartSubmitted\x12V\n\x1atime_cloud_run_job_started\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x16timeCloudRunJobStarted\x12H\n\x12time_end_submitted\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\x10timeEndSubmitted\x12R\n\x18time_cloud_run_job_ended\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampR\x14timeCloudRunJobEnded\x12?\n\nend_status\x18\x08 \x01(\x0e2 .viam.app.cloudslam.v1.EndStatusR\tendStatus\x12\'\n\x10cloud_run_job_id\x18\t \x01(\tR\rcloudRunJobId\x12.\n\x13viam_server_version\x18\n \x01(\tR\x11viamServerVersion\x12\x19\n\x08map_name\x18\x0b \x01(\tR\x07mapName\x12!\n\x0cslam_version\x18\x0c \x01(\tR\x0bslamVersion\x12\x16\n\x06config\x18\r \x01(\tR\x06config\x12\x1b\n\terror_msg\x18\x0e \x01(\tR\x08errorMsg*l\n\tEndStatus\x12\x1a\n\x16END_STATUS_UNSPECIFIED\x10\x00\x12\x16\n\x12END_STATUS_SUCCESS\x10\x01\x12\x16\n\x12END_STATUS_TIMEOUT\x10\x02\x12\x13\n\x0fEND_STATUS_FAIL\x10\x032\xe3\x06\n\x10CloudSLAMService\x12|\n\x13StartMappingSession\x121.viam.app.cloudslam.v1.StartMappingSessionRequest\x1a2.viam.app.cloudslam.v1.StartMappingSessionResponse\x12\xa3\x01\n GetActiveMappingSessionsForRobot\x12>.viam.app.cloudslam.v1.GetActiveMappingSessionsForRobotRequest\x1a?.viam.app.cloudslam.v1.GetActiveMappingSessionsForRobotResponse\x12\x94\x01\n\x1bGetMappingSessionPointCloud\x129.viam.app.cloudslam.v1.GetMappingSessionPointCloudRequest\x1a:.viam.app.cloudslam.v1.GetMappingSessionPointCloudResponse\x12|\n\x13ListMappingSessions\x121.viam.app.cloudslam.v1.ListMappingSessionsRequest\x1a2.viam.app.cloudslam.v1.ListMappingSessionsResponse\x12y\n\x12StopMappingSession\x120.viam.app.cloudslam.v1.StopMappingSessionRequest\x1a1.viam.app.cloudslam.v1.StopMappingSessionResponse\x12\x9a\x01\n\x1dGetMappingSessionMetadataByID\x12;.viam.app.cloudslam.v1.GetMappingSessionMetadataByIDRequest\x1a<.viam.app.cloudslam.v1.GetMappingSessionMetadataByIDResponseB"Z go.viam.com/api/app/cloudslam/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.cloudslam.v1.cloud_slam_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z go.viam.com/api/app/cloudslam/v1'
    _ENDSTATUS._serialized_start = 2667
    _ENDSTATUS._serialized_end = 2775
    _STARTMAPPINGSESSIONREQUEST._serialized_start = 148
    _STARTMAPPINGSESSIONREQUEST._serialized_end = 694
    _MODULE._serialized_start = 696
    _MODULE._serialized_end = 779
    _SENSORINFO._serialized_start = 782
    _SENSORINFO._serialized_end = 910
    _CAPTUREINTERVAL._serialized_start = 913
    _CAPTUREINTERVAL._serialized_end = 1044
    _STARTMAPPINGSESSIONRESPONSE._serialized_start = 1046
    _STARTMAPPINGSESSIONRESPONSE._serialized_end = 1106
    _GETACTIVEMAPPINGSESSIONSFORROBOTREQUEST._serialized_start = 1108
    _GETACTIVEMAPPINGSESSIONSFORROBOTREQUEST._serialized_end = 1176
    _GETACTIVEMAPPINGSESSIONSFORROBOTRESPONSE._serialized_start = 1178
    _GETACTIVEMAPPINGSESSIONSFORROBOTRESPONSE._serialized_end = 1251
    _GETMAPPINGSESSIONPOINTCLOUDREQUEST._serialized_start = 1253
    _GETMAPPINGSESSIONPOINTCLOUDREQUEST._serialized_end = 1320
    _GETMAPPINGSESSIONPOINTCLOUDRESPONSE._serialized_start = 1322
    _GETMAPPINGSESSIONPOINTCLOUDRESPONSE._serialized_end = 1426
    _LISTMAPPINGSESSIONSREQUEST._serialized_start = 1428
    _LISTMAPPINGSESSIONSREQUEST._serialized_end = 1530
    _LISTMAPPINGSESSIONSRESPONSE._serialized_start = 1532
    _LISTMAPPINGSESSIONSRESPONSE._serialized_end = 1627
    _STOPMAPPINGSESSIONREQUEST._serialized_start = 1629
    _STOPMAPPINGSESSIONREQUEST._serialized_end = 1687
    _STOPMAPPINGSESSIONRESPONSE._serialized_start = 1689
    _STOPMAPPINGSESSIONRESPONSE._serialized_end = 1774
    _GETMAPPINGSESSIONMETADATABYIDREQUEST._serialized_start = 1776
    _GETMAPPINGSESSIONMETADATABYIDREQUEST._serialized_end = 1845
    _GETMAPPINGSESSIONMETADATABYIDRESPONSE._serialized_start = 1847
    _GETMAPPINGSESSIONMETADATABYIDRESPONSE._serialized_end = 1969
    _MAPPINGMETADATA._serialized_start = 1972
    _MAPPINGMETADATA._serialized_end = 2665
    _CLOUDSLAMSERVICE._serialized_start = 2778
    _CLOUDSLAMSERVICE._serialized_end = 3645