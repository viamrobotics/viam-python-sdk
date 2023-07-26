from typing import Any, Dict, List, Mapping, Optional, Union

from google.protobuf.struct_pb2 import Struct
from grpclib.server import Stream
from PIL import Image

from viam.media.video import RawImage
from viam.proto.app.data import (
    AddBoundingBoxToImageByIDRequest,
    AddBoundingBoxToImageByIDResponse,
    AddTagsToBinaryDataByFilterRequest,
    AddTagsToBinaryDataByFilterResponse,
    AddTagsToBinaryDataByIDsRequest,
    AddTagsToBinaryDataByIDsResponse,
    BinaryData,
    BinaryDataByFilterRequest,
    BinaryDataByFilterResponse,
    BinaryDataByIDsRequest,
    BinaryDataByIDsResponse,
    BoundingBoxLabelsByFilterRequest,
    BoundingBoxLabelsByFilterResponse,
    DataServiceBase,
    DeleteBinaryDataByFilterRequest,
    DeleteBinaryDataByFilterResponse,
    DeleteBinaryDataByIDsRequest,
    DeleteBinaryDataByIDsResponse,
    DeleteTabularDataByFilterRequest,
    DeleteTabularDataByFilterResponse,
    RemoveBoundingBoxFromImageByIDRequest,
    RemoveBoundingBoxFromImageByIDResponse,
    RemoveTagsFromBinaryDataByFilterRequest,
    RemoveTagsFromBinaryDataByFilterResponse,
    RemoveTagsFromBinaryDataByIDsRequest,
    RemoveTagsFromBinaryDataByIDsResponse,
    TabularData,
    TabularDataByFilterRequest,
    TabularDataByFilterResponse,
    TagsByFilterRequest,
    TagsByFilterResponse,
)
from viam.proto.app.datasync import (
    DataCaptureUploadRequest,
    DataCaptureUploadResponse,
    DataSyncServiceBase,
    FileUploadRequest,
    FileUploadResponse,
)
from viam.proto.common import DoCommandRequest, DoCommandResponse, GeoObstacle, GeoPoint, PointCloudObject, Pose, PoseInFrame, ResourceName
from viam.proto.service.motion import (
    Constraints,
    GetPoseRequest,
    GetPoseResponse,
    MotionServiceBase,
    MoveOnGlobeRequest,
    MoveOnGlobeResponse,
    MoveOnMapRequest,
    MoveOnMapResponse,
    MoveRequest,
    MoveResponse,
    MoveSingleComponentRequest,
    MoveSingleComponentResponse,
)
from viam.proto.service.navigation import Mode, Waypoint
from viam.proto.service.sensors import (
    GetReadingsRequest,
    GetReadingsResponse,
    GetSensorsRequest,
    GetSensorsResponse,
    Readings,
    SensorsServiceBase,
)
from viam.proto.service.vision import Classification, Detection
from viam.services.mlmodel import File, LabelType, Metadata, MLModel, TensorInfo
from viam.services.navigation import Navigation
from viam.services.slam import SLAM
from viam.services.vision import Vision
from viam.utils import ValueTypes, struct_to_dict


class MockVision(Vision):
    def __init__(
        self,
        name: str,
        detectors: List[str],
        detections: List[Detection],
        classifiers: List[str],
        classifications: List[Classification],
        segmenters: List[str],
        point_clouds: List[PointCloudObject],
    ):
        self.detectors = detectors
        self.detections = detections
        self.classifiers = classifiers
        self.classifications = classifications
        self.segmenters = segmenters
        self.point_clouds = point_clouds
        self.extra: Optional[Mapping[str, Any]] = None
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_detections_from_camera(
        self, camera_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[Detection]:
        self.extra = extra
        self.timeout = timeout
        return self.detections

    async def get_detections(
        self, image: Union[Image.Image, RawImage], *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[Detection]:
        self.extra = extra
        self.timeout = timeout
        return self.detections

    async def get_classifications_from_camera(
        self, camera_name: str, count: int, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[Classification]:
        self.extra = extra
        self.timeout = timeout
        return self.classifications

    async def get_classifications(
        self, image: Union[Image.Image, RawImage], count: int, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[Classification]:
        self.extra = extra
        self.timeout = timeout
        return self.classifications

    async def get_object_point_clouds(
        self, camera_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[PointCloudObject]:
        self.extra = extra
        self.timeout = timeout
        return self.point_clouds

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        self.timeout = timeout
        return {"cmd": command}


class MockMLModel(MLModel):
    INPUT_DATA: Dict = {"image": [10, 10, 255, 0, 0, 255, 255, 0, 100]}
    OUTPUT_DATA = {
        "n_detections": [3],
        "confidence_scores": [[0.9084375, 0.7359375, 0.33984375]],
        "labels": [[0, 0, 4]],
        "locations": [[[0.1, 0.4, 0.22, 0.4], [0.02, 0.22, 0.77, 0.90], [0.40, 0.50, 0.40, 0.50]]],
    }
    META_INPUTS = [TensorInfo(name="image", description="i0", data_type="uint8", shape=[300, 200])]
    META_OUTPUTS = [
        TensorInfo(name="n_detections", description="o0", data_type="int32", shape=[1]),
        TensorInfo(name="confidence_scores", description="o1", data_type="float32", shape=[3, 1]),
        TensorInfo(
            name="labels",
            description="o2",
            data_type="int32",
            shape=[3, 1],
            associated_files=[
                File(
                    name="category_labels.txt",
                    description="these labels represent types of plants",
                    label_type=LabelType.LABEL_TYPE_TENSOR_VALUE,
                )
            ],
        ),
        TensorInfo(name="locations", description="o3", data_type="float32", shape=[4, 3, 1]),
    ]
    META = Metadata(name="fake_detector", type="object_detector", description="desc", input_info=META_INPUTS, output_info=META_OUTPUTS)

    def __init__(self, name: str):
        self.timeout: Optional[float] = None

        super().__init__(name)

    async def infer(self, input_data: Dict[str, ValueTypes], *, timeout: Optional[float] = None) -> Dict[str, ValueTypes]:
        self.timeout = timeout
        return self.OUTPUT_DATA

    async def metadata(self, *, timeout: Optional[float] = None) -> Metadata:
        self.timeout = timeout
        return self.META


class MockMotion(MotionServiceBase):
    def __init__(
        self,
        move_responses: Dict[str, bool],
        move_single_component_responses: Dict[str, bool],
        get_pose_responses: Dict[str, PoseInFrame],
    ):
        self.move_responses = move_responses
        self.move_single_component_responses = move_single_component_responses
        self.get_pose_responses = get_pose_responses
        self.constraints: Optional[Constraints] = None
        self.extra: Optional[Mapping[str, Any]] = None
        self.timeout: Optional[float] = None

    async def Move(self, stream: Stream[MoveRequest, MoveResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        self.constraints = request.constraints
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        success = self.move_responses[name.name]
        response = MoveResponse(success=success)
        await stream.send_message(response)

    async def MoveOnMap(self, stream: Stream[MoveOnMapRequest, MoveOnMapResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.component_name = request.component_name
        self.destination = request.destination
        self.slam_service = request.slam_service_name
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        await stream.send_message(MoveOnMapResponse(success=True))

    async def MoveOnGlobe(self, stream: Stream[MoveOnGlobeRequest, MoveOnGlobeResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.component_name = request.component_name
        self.destination = request.destination
        self.movement_sensor = request.movement_sensor_name
        self.obstacles = request.obstacles
        self.heading = request.heading
        self.linear_meters_per_sec = request.linear_meters_per_sec
        self.angular_deg_per_sec = request.angular_deg_per_sec
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        await stream.send_message(MoveOnGlobeResponse(success=True))

    async def MoveSingleComponent(self, stream: Stream[MoveSingleComponentRequest, MoveSingleComponentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        success = self.move_single_component_responses[name.name]
        response = MoveSingleComponentResponse(success=success)
        await stream.send_message(response)

    async def GetPose(self, stream: Stream[GetPoseRequest, GetPoseResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        pose = self.get_pose_responses[name.name]
        response = GetPoseResponse(pose=pose)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        await stream.send_message(DoCommandResponse(result=request.command))


class MockSensors(SensorsServiceBase):
    def __init__(self, sensors: List[ResourceName], readings: List[Readings]):
        self.sensors = sensors
        self.readings = readings
        self.extra: Optional[Mapping[str, Any]] = None
        self.timeout: Optional[float] = None

    async def GetSensors(self, stream: Stream[GetSensorsRequest, GetSensorsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = GetSensorsResponse(sensor_names=self.sensors)
        await stream.send_message(response)

    async def GetReadings(self, stream: Stream[GetReadingsRequest, GetReadingsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        self.sensors_for_readings: List[ResourceName] = list(request.sensor_names)
        response = GetReadingsResponse(readings=self.readings)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        await stream.send_message(DoCommandResponse(result=request.command))


class MockSLAM(SLAM):
    INTERNAL_STATE_CHUNKS = [bytes(5), bytes(2)]
    POINT_CLOUD_PCD_CHUNKS = [bytes(3), bytes(2)]
    POSITION = Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20)

    def __init__(self, name: str):
        self.name = name
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_internal_state(self, *, timeout: Optional[float] = None) -> List[bytes]:
        self.timeout = timeout
        return self.INTERNAL_STATE_CHUNKS

    async def get_point_cloud_map(self, *, timeout: Optional[float] = None) -> List[bytes]:
        self.timeout = timeout
        return self.POINT_CLOUD_PCD_CHUNKS

    async def get_position(self, *, timeout: Optional[float] = None) -> Pose:
        self.timeout = timeout
        return self.POSITION

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockNavigation(Navigation):
    LOCATION = GeoPoint(latitude=100.0, longitude=150.0)
    OBSTACLES = [GeoObstacle(location=GeoPoint(latitude=200.0, longitude=250.0))]
    WAYPOINTS = [Waypoint(location=GeoPoint(latitude=300.0, longitude=350.0))]

    def __init__(self, name: str):
        self.name = name
        self.add_waypoints: list[GeoPoint] = []
        self.remove_waypoints: list[str] = []
        self.mode = Mode.MODE_UNSPECIFIED
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_location(self, *, timeout: Optional[float] = None) -> GeoPoint:
        self.timeout = timeout
        return self.LOCATION

    async def get_obstacles(self, *, timeout: Optional[float] = None) -> List[GeoObstacle]:
        self.timeout = timeout
        return self.OBSTACLES

    async def get_waypoints(self, *, timeout: Optional[float] = None) -> List[Waypoint]:
        self.timeout = timeout
        return self.WAYPOINTS

    async def add_waypoint(self, point: GeoPoint, *, timeout: Optional[float] = None):
        self.timeout = timeout
        self.add_waypoints.append(point)

    async def remove_waypoint(self, id: str, *, timeout: Optional[float] = None):
        self.timeout = timeout
        self.remove_waypoints.append(id)

    async def get_mode(self, *, timeout: Optional[float] = None) -> Mode.ValueType:
        self.timeout = timeout
        return self.mode

    async def set_mode(self, mode: Mode.ValueType, *, timeout: Optional[float] = None):
        self.timeout = timeout
        self.mode = mode

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockData(DataServiceBase):
    def __init__(
        self,
        tabular_response: List[Mapping[str, Any]],
        binary_response: List[bytes],
        delete_remove_response: int,
        tags_response: List[str],
        bbox_labels_response: List[str],
    ):
        self.tabular_response = tabular_response
        self.binary_response = binary_response
        self.delete_remove_response = delete_remove_response
        self.tags_response = tags_response
        self.bbox_labels_response = bbox_labels_response
        self.was_tabular_data_requested = False
        self.was_binary_data_requested = False

    async def TabularDataByFilter(self, stream: Stream[TabularDataByFilterRequest, TabularDataByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        if self.was_tabular_data_requested:
            await stream.send_message(TabularDataByFilterResponse(data=None))
            return
        self.filter = request.data_request.filter
        n = len(self.tabular_response)
        tabular_response_structs = [None] * n
        for i in range(n):
            s = Struct()
            s.update(self.tabular_response[i])
            tabular_response_structs[i] = s
        await stream.send_message(TabularDataByFilterResponse(data=[TabularData(data=struct) for struct in tabular_response_structs]))
        self.was_tabular_data_requested = True

    async def BinaryDataByFilter(self, stream: Stream[BinaryDataByFilterRequest, BinaryDataByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        if self.was_binary_data_requested:
            await stream.send_message(BinaryDataByFilterResponse())
            return
        self.filter = request.data_request.filter
        await stream.send_message(BinaryDataByFilterResponse(data=[BinaryData(binary=binary_data) for binary_data in self.binary_response]))
        self.was_binary_data_requested = True

    async def BinaryDataByIDs(self, stream: Stream[BinaryDataByIDsRequest, BinaryDataByIDsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.binary_ids = request.binary_ids
        await stream.send_message(BinaryDataByIDsResponse(data=[BinaryData(binary=binary_data) for binary_data in self.binary_response]))

    async def DeleteTabularDataByFilter(self, stream: Stream[DeleteTabularDataByFilterRequest, DeleteTabularDataByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        await stream.send_message(DeleteTabularDataByFilterResponse(deleted_count=self.delete_remove_response))

    async def DeleteBinaryDataByFilter(self, stream: Stream[DeleteBinaryDataByFilterRequest, DeleteBinaryDataByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        await stream.send_message(DeleteBinaryDataByFilterResponse(deleted_count=self.delete_remove_response))

    async def DeleteBinaryDataByIDs(self, stream: Stream[DeleteBinaryDataByIDsRequest, DeleteBinaryDataByIDsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.binary_ids = request.binary_ids
        await stream.send_message(DeleteBinaryDataByIDsResponse(deleted_count=self.delete_remove_response))

    async def AddTagsToBinaryDataByIDs(self, stream: Stream[AddTagsToBinaryDataByIDsRequest, AddTagsToBinaryDataByIDsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.binary_ids = request.binary_ids
        self.tags = request.tags
        await stream.send_message(AddTagsToBinaryDataByIDsResponse())

    async def AddTagsToBinaryDataByFilter(
        self, stream: Stream[AddTagsToBinaryDataByFilterRequest, AddTagsToBinaryDataByFilterResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        self.tags = request.tags
        await stream.send_message(AddTagsToBinaryDataByFilterResponse())

    async def RemoveTagsFromBinaryDataByIDs(
        self, stream: Stream[RemoveTagsFromBinaryDataByIDsRequest, RemoveTagsFromBinaryDataByIDsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.binary_ids = request.binary_ids
        self.tags = request.tags
        await stream.send_message(RemoveTagsFromBinaryDataByIDsResponse(deleted_count=self.delete_remove_response))

    async def RemoveTagsFromBinaryDataByFilter(
        self, stream: Stream[RemoveTagsFromBinaryDataByFilterRequest, RemoveTagsFromBinaryDataByFilterResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        self.tags = request.tags
        await stream.send_message(RemoveTagsFromBinaryDataByFilterResponse(deleted_count=len(request.tags)))

    async def TagsByFilter(self, stream: Stream[TagsByFilterRequest, TagsByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        await stream.send_message(TagsByFilterResponse(tags=self.tags_response))

    async def AddBoundingBoxToImageByID(self, stream: Stream[AddBoundingBoxToImageByIDRequest, AddBoundingBoxToImageByIDResponse]) -> None:
        pass

    async def RemoveBoundingBoxFromImageByID(
        self, stream: Stream[RemoveBoundingBoxFromImageByIDRequest, RemoveBoundingBoxFromImageByIDResponse]
    ) -> None:
        pass

    async def BoundingBoxLabelsByFilter(self, stream: Stream[BoundingBoxLabelsByFilterRequest, BoundingBoxLabelsByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        await stream.send_message(BoundingBoxLabelsByFilterResponse(labels=self.bbox_labels_response))


class MockDataSync(DataSyncServiceBase):
    async def DataCaptureUpload(self, stream: Stream[DataCaptureUploadRequest, DataCaptureUploadResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.metadata = request.metadata
        self.sensor_contents = request.sensor_contents
        await stream.send_message(DataCaptureUploadResponse())

    async def FileUpload(self, stream: Stream[FileUploadRequest, FileUploadResponse]) -> None:
        request_metadata = await stream.recv_message()
        assert request_metadata is not None
        self.metadata = request_metadata.metadata
        request_file_contents = await stream.recv_message()
        assert request_file_contents is not None
        self.binary_data = request_file_contents.file_contents.data
        await stream.send_message(FileUploadResponse())


class MockLocation(AppServiceBase):
    async def GetUserIDByEmail(self, stream: Stream[GetUserIDByEmailRequest, GetUserIDByEmailResponse]) -> None:
        pass

    async def CreateOrganization(self, stream: Stream[CreateOrganizationRequest, CreateOrganizationResponse]) -> None:
        pass

    async def ListOrganizations(self, stream: Stream[ListOrganizationsRequest, ListOrganizationsResponse]) -> None:
        pass

    async def ListOrganizationsByUser(self, stream: Stream[ListOrganizationsByUserRequest, ListOrganizationsByUserResponse]) -> None:
        pass

    async def GetOrganization(self, stream: Stream[GetOrganizationRequest, GetOrganizationResponse]) -> None:
        pass

    async def GetOrganizationNamespaceAvailability(
        self,
        stream: Stream[GetOrganizationNamespaceAvailabilityRequest, GetOrganizationNamespaceAvailabilityResponse]
    ) -> None:
        pass

    async def UpdateOrganization(self, stream: Stream[UpdateOrganizationRequest, UpdateOrganizationResponse]) -> None:
        pass

    async def DeleteOrganization(self, stream: Stream[DeleteOrganizationRequest, DeleteOrganizationResponse]) -> None:
        pass

    async def ListOrganizationMembers(self, stream: Stream[ListOrganizationMembersRequest, ListOrganizationMembersResponse]) -> None:
        pass

    async def CreateOrganizationInvite(self, stream: Stream[CreateOrganizationInviteRequest, CreateOrganizationInviteResponse]) -> None:
        pass

    async def UpdateOrganizationInviteAuthorizations(
        self,
        stream: Stream[UpdateOrganizationInviteAuthorizationsRequest, UpdateOrganizationInviteAuthorizationsResponse]
    ) -> None:
        pass

    async def DeleteOrganizationMember(self, stream: Stream[DeleteOrganizationMemberRequest, DeleteOrganizationMemberResponse]) -> None:
        pass

    async def DeleteOrganizationInvite(self, stream: Stream[DeleteOrganizationInviteRequest, DeleteOrganizationInviteResponse]) -> None:
        pass

    async def ResendOrganizationInvite(self, stream: Stream[ResendOrganizationInviteRequest, ResendOrganizationInviteResponse]) -> None:
        pass

    async def CreateLocation(self, stream: Stream[CreateLocationRequest, CreateLocationResponse]) -> None:
        raise NotImplementedError()

    async def GetLocation(self, stream: Stream[GetLocationRequest, GetLocationResponse]) -> None:
        raise NotImplementedError()

    async def UpdateLocation(self, stream: Stream[UpdateLocationRequest, UpdateLocationResponse]) -> None:
        raise NotImplementedError()

    async def DeleteLocation(self, stream: Stream[DeleteLocationRequest, DeleteLocationResponse]) -> None:
        raise NotImplementedError()

    async def ListLocations(self, stream: Stream[ListLocationsRequest, ListLocationsResponse]) -> None:
        raise NotImplementedError()

    async def ShareLocation(self, stream: Stream[ShareLocationRequest, ShareLocationResponse]) -> None:
        raise NotImplementedError()

    async def UnshareLocation(self, stream: Stream[UnshareLocationRequest, UnshareLocationResponse]) -> None:
        raise NotImplementedError()

    async def LocationAuth(self, stream: Stream[LocationAuthRequest, LocationAuthResponse]) -> None:
        pass

    async def CreateLocationSecret(self, stream: Stream[CreateLocationSecretRequest, CreateLocationSecretResponse]) -> None:
        pass

    async def DeleteLocationSecret(self, stream: Stream[DeleteLocationSecretRequest, DeleteLocationSecretResponse]) -> None:
        pass

    async def GetRobot(self, stream: Stream[GetRobotRequest, GetRobotResponse]) -> None:
        raise NotImplementedError()

    async def GetRoverRentalRobots(self, stream: Stream[GetRoverRentalRobotsRequest, GetRoverRentalRobotsResponse]) -> None:
        pass

    async def GetRobotParts(self, stream: Stream[GetRobotPartsRequest, GetRobotPartsResponse]) -> None:
        raise NotImplementedError()

    async def GetRobotPart(self, stream: Stream[GetRobotPartRequest, GetRobotPartResponse]) -> None:
        raise NotImplementedError()

    async def GetRobotPartLogs(self, stream: Stream[GetRobotPartLogsRequest, GetRobotPartLogsResponse]) -> None:
        raise NotImplementedError()

    async def TailRobotPartLogs(self, stream: Stream[TailRobotPartLogsRequest, TailRobotPartLogsResponse]) -> None:
        pass

    async def GetRobotPartHistory(self, stream: Stream[GetRobotPartHistoryRequest, GetRobotPartHistoryResponse]) -> None:
        pass

    async def UpdateRobotPart(self, stream: Stream[UpdateRobotPartRequest, UpdateRobotPartResponse]) -> None:
        raise NotImplementedError()

    async def NewRobotPart(self, stream: Stream[NewRobotPartRequest, NewRobotPartResponse]) -> None:
        raise NotImplementedError()

    async def DeleteRobotPart(self, stream: Stream[DeleteRobotPartRequest, DeleteRobotPartResponse]) -> None:
        raise NotImplementedError()

    async def MarkPartAsMain(self, stream: Stream[MarkPartAsMainRequest, MarkPartAsMainResponse]) -> None:
        pass

    async def MarkPartForRestart(self, stream: Stream[MarkPartForRestartRequest, MarkPartForRestartResponse]) -> None:
        raise NotImplementedError()

    async def CreateRobotPartSecret(self, stream: Stream[CreateRobotPartSecretRequest, CreateRobotPartSecretResponse]) -> None:
        pass

    async def DeleteRobotPartSecret(self, stream: Stream[DeleteRobotPartSecretRequest, DeleteRobotPartSecretResponse]) -> None:
        pass

    async def ListRobots(self, stream: Stream[ListRobotsRequest, ListRobotsResponse]) -> None:
        raise NotImplementedError()

    async def NewRobot(self, stream: Stream[NewRobotRequest, NewRobotResponse]) -> None:
        raise NotImplementedError()

    async def UpdateRobot(self, stream: Stream[UpdateRobotRequest, UpdateRobotResponse]) -> None:
        raise NotImplementedError()

    async def DeleteRobot(self, stream: Stream[DeleteRobotRequest, DeleteRobotResponse]) -> None:
        raise NotImplementedError()

    async def ListFragments(self, stream: Stream[ListFragmentsRequest, ListFragmentsResponse]) -> None:
        raise NotImplementedError()

    async def GetFragment(self, stream: Stream[GetFragmentRequest, GetFragmentResponse]) -> None:
        raise NotImplementedError()

    async def CreateFragment(self, stream: Stream[CreateFragmentRequest, CreateFragmentResponse]) -> None:
        pass

    async def UpdateFragment(self, stream: Stream[UpdateFragmentRequest, UpdateFragmentResponse]) -> None:
        pass

    async def DeleteFragment(self, stream: Stream[DeleteFragmentRequest, DeleteFragmentResponse]) -> None:
        pass

    async def AddRole(self, stream: Stream[AddRoleRequest, AddRoleResponse]) -> None:
        pass

    async def RemoveRole(self, stream: Stream[RemoveRoleRequest, RemoveRoleResponse]) -> None:
        pass

    async def ListAuthorizations(self, stream: Stream[ListAuthorizationsRequest, ListAuthorizationsResponse]) -> None:
        pass

    async def CheckPermissions(self, stream: Stream[CheckPermissionsRequest, CheckPermissionsResponse]) -> None:
        pass

    async def CreateModule(self, stream: Stream[CreateModuleRequest, CreateModuleResponse]) -> None:
        pass

    async def UpdateModule(self, stream: Stream[UpdateModuleRequest, UpdateModuleResponse]) -> None:
        pass

    async def UploadModuleFile(self, stream: Stream[UploadModuleFileRequest, UploadModuleFileResponse]) -> None:
        pass

    async def GetModule(self, stream: Stream[GetModuleRequest, GetModuleResponse]) -> None:
        pass

    async def ListModules(self, stream: Stream[ListModulesRequest, ListModulesResponse]) -> None:
        pass
