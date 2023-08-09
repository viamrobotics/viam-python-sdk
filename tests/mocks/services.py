from typing import Any, Dict, List, Mapping, Optional, Union
from datetime import datetime

from grpclib.server import Stream
from PIL import Image

from viam.media.video import RawImage
from viam.proto.app import (
    AppServiceBase,
    GetUserIDByEmailRequest,
    GetUserIDByEmailResponse,
    CreateOrganizationRequest,
    CreateOrganizationResponse,
    OrganizationMember,
    OrganizationInvite,
    RobotPartHistoryEntry,
    ListOrganizationsRequest,
    ListOrganizationsResponse,
    ListOrganizationsByUserRequest,
    Authorization,
    ListOrganizationsByUserResponse,
    GetOrganizationRequest,
    LocationAuth,
    GetOrganizationResponse,
    GetOrganizationNamespaceAvailabilityRequest,
    GetOrganizationNamespaceAvailabilityResponse,
    UpdateOrganizationRequest,
    UpdateOrganizationResponse,
    DeleteOrganizationRequest,
    DeleteOrganizationResponse,
    ListOrganizationMembersRequest,
    ListOrganizationMembersResponse,
    CreateOrganizationInviteRequest,
    CreateOrganizationInviteResponse,
    UpdateOrganizationInviteAuthorizationsRequest,
    UpdateOrganizationInviteAuthorizationsResponse,
    DeleteOrganizationMemberRequest,
    DeleteOrganizationMemberResponse,
    DeleteOrganizationInviteRequest,
    Module,
    DeleteOrganizationInviteResponse,
    ResendOrganizationInviteRequest,
    ResendOrganizationInviteResponse,
    CreateLocationRequest,
    CreateLocationResponse,
    GetLocationRequest,
    GetLocationResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    DeleteLocationRequest,
    DeleteLocationResponse,
    ListLocationsRequest,
    ListLocationsResponse,
    ShareLocationRequest,
    ShareLocationResponse,
    UnshareLocationRequest,
    UnshareLocationResponse,
    LocationAuthRequest,
    LocationAuthResponse,
    CreateLocationSecretRequest,
    CreateLocationSecretResponse,
    DeleteLocationSecretRequest,
    DeleteLocationSecretResponse,
    GetRobotRequest,
    GetRobotResponse,
    GetRoverRentalRobotsRequest,
    GetRoverRentalRobotsResponse,
    GetRobotPartsRequest,
    GetRobotPartsResponse,
    GetRobotPartRequest,
    GetRobotPartResponse,
    GetRobotPartLogsRequest,
    GetRobotPartLogsResponse,
    TailRobotPartLogsRequest,
    TailRobotPartLogsResponse,
    GetRobotPartHistoryRequest,
    GetRobotPartHistoryResponse,
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    NewRobotPartRequest,
    NewRobotPartResponse,
    DeleteRobotPartRequest,
    DeleteRobotPartResponse,
    MarkPartAsMainRequest,
    MarkPartAsMainResponse,
    MarkPartForRestartRequest,
    MarkPartForRestartResponse,
    CreateRobotPartSecretRequest,
    CreateRobotPartSecretResponse,
    DeleteRobotPartSecretRequest,
    DeleteRobotPartSecretResponse,
    ListRobotsRequest,
    ListRobotsResponse,
    NewRobotRequest,
    NewRobotResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
    DeleteRobotRequest,
    DeleteRobotResponse,
    ListFragmentsRequest,
    ListFragmentsResponse,
    GetFragmentRequest,
    GetFragmentResponse,
    CreateFragmentRequest,
    CreateFragmentResponse,
    UpdateFragmentRequest,
    UpdateFragmentResponse,
    DeleteFragmentRequest,
    DeleteFragmentResponse,
    AddRoleRequest,
    AddRoleResponse,
    Fragment,
    RemoveRoleRequest,
    RemoveRoleResponse,
    ListAuthorizationsRequest,
    ListAuthorizationsResponse,
    CheckPermissionsRequest,
    CheckPermissionsResponse,
    CreateModuleRequest,
    CreateModuleResponse,
    UpdateModuleRequest,
    UpdateModuleResponse,
    UploadModuleFileRequest,
    UploadModuleFileResponse,
    GetModuleRequest,
    GetModuleResponse,
    ListModulesRequest,
    ListModulesResponse,
    Location,
    Organization,
    Robot,
    RobotPart,
    LogEntry,
)
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
from viam.app.data_client import DataClient
from viam.services.mlmodel import File, LabelType, Metadata, MLModel, TensorInfo
from viam.services.navigation import Navigation
from viam.services.slam import SLAM
from viam.services.vision import Vision
from viam.utils import ValueTypes, datetime_to_timestamp, dict_to_struct, struct_to_dict


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
    LAST_UPDATE = datetime(2023, 3, 12, 3, 24, 34, 29)

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

    async def get_latest_map_info(self, *, timeout: Optional[float] = None) -> datetime:
        self.timeout = timeout
        return self.LAST_UPDATE

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
        tabular_response: List[DataClient.TabularData],
        binary_response: List[DataClient.BinaryData],
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
        tabular_response_structs = []
        tabular_metadata = [data.metadata for data in self.tabular_response]
        for idx, tabular_data in enumerate(self.tabular_response):
            tabular_response_structs.append(
                TabularData(
                    data=dict_to_struct(tabular_data.data),
                    metadata_index=idx,
                    time_requested=datetime_to_timestamp(tabular_data.time_requested),
                    time_received=datetime_to_timestamp(tabular_data.time_received),
                )
            )
        await stream.send_message(TabularDataByFilterResponse(data=tabular_response_structs, metadata=tabular_metadata))
        self.was_tabular_data_requested = True

    async def BinaryDataByFilter(self, stream: Stream[BinaryDataByFilterRequest, BinaryDataByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        if self.was_binary_data_requested:
            await stream.send_message(BinaryDataByFilterResponse())
            return
        self.filter = request.data_request.filter
        await stream.send_message(
            BinaryDataByFilterResponse(data=[BinaryData(binary=data.data, metadata=data.metadata) for data in self.binary_response])
        )
        self.was_binary_data_requested = True

    async def BinaryDataByIDs(self, stream: Stream[BinaryDataByIDsRequest, BinaryDataByIDsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.binary_ids = request.binary_ids
        await stream.send_message(
            BinaryDataByIDsResponse(data=[BinaryData(binary=data.data, metadata=data.metadata) for data in self.binary_response])
        )

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
        raise NotImplementedError()

    async def RemoveBoundingBoxFromImageByID(
        self, stream: Stream[RemoveBoundingBoxFromImageByIDRequest, RemoveBoundingBoxFromImageByIDResponse]
    ) -> None:
        raise NotImplementedError()

    async def BoundingBoxLabelsByFilter(self, stream: Stream[BoundingBoxLabelsByFilterRequest, BoundingBoxLabelsByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        await stream.send_message(BoundingBoxLabelsByFilterResponse(labels=self.bbox_labels_response))


class MockDataSync(DataSyncServiceBase):
    def __init__(self, file_upload_response: str):
        self.file_upload_response = file_upload_response

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
        await stream.send_message(FileUploadResponse(file_id=self.file_upload_response))


class MockApp(AppServiceBase):
    def __init__(
        self,
        organizations: List[Organization],
        location: Location,
        robot: Robot,
        robot_part: RobotPart,
        log_entry: LogEntry,
        id: str,
        fragment: Fragment,
        available: bool,
        location_auth: LocationAuth,
        robot_part_history: List[RobotPartHistoryEntry],
        authorizations: List[Authorization],
        url: str,
        module: Module,
        members: List[OrganizationMember],
        invite: OrganizationInvite
    ):
        self.organizations = organizations
        self.location = location
        self.robot = robot
        self.robot_part = robot_part
        self.log_entry = log_entry
        self.id = id
        self.fragment = fragment
        self.available = available
        self.location_auth = location_auth
        self.robot_part_history = robot_part_history
        self.authorizations = authorizations
        self.url = url
        self.module = module
        self.members = members
        self.invite = invite

    async def GetUserIDByEmail(self, stream: Stream[GetUserIDByEmailRequest, GetUserIDByEmailResponse]) -> None:
        raise NotImplementedError()

    async def CreateOrganization(self, stream: Stream[CreateOrganizationRequest, CreateOrganizationResponse]) -> None:
        raise NotImplementedError()

    async def ListOrganizations(self, stream: Stream[ListOrganizationsRequest, ListOrganizationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListOrganizationsResponse(organizations=self.organizations))

    async def ListOrganizationsByUser(self, stream: Stream[ListOrganizationsByUserRequest, ListOrganizationsByUserResponse]) -> None:
        raise NotImplementedError()

    async def GetOrganization(self, stream: Stream[GetOrganizationRequest, GetOrganizationResponse]) -> None:
        raise NotImplementedError()

    async def GetOrganizationNamespaceAvailability(
        self, stream: Stream[GetOrganizationNamespaceAvailabilityRequest, GetOrganizationNamespaceAvailabilityResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.namespace = request.public_namespace
        await stream.send_message(GetOrganizationNamespaceAvailabilityResponse(available=self.available))

    async def UpdateOrganization(self, stream: Stream[UpdateOrganizationRequest, UpdateOrganizationResponse]) -> None:
        raise NotImplementedError()

    async def DeleteOrganization(self, stream: Stream[DeleteOrganizationRequest, DeleteOrganizationResponse]) -> None:
        raise NotImplementedError()

    async def ListOrganizationMembers(self, stream: Stream[ListOrganizationMembersRequest, ListOrganizationMembersResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListOrganizationMembersResponse(members=self.members, invites=[self.invite]))

    async def CreateOrganizationInvite(self, stream: Stream[CreateOrganizationInviteRequest, CreateOrganizationInviteResponse]) -> None:
        raise NotImplementedError()

    async def UpdateOrganizationInviteAuthorizations(
        self, stream: Stream[UpdateOrganizationInviteAuthorizationsRequest, UpdateOrganizationInviteAuthorizationsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.email = request.email
        self.add_authorizations = request.add_authorizations
        self.remove_authorizations = request.remove_authorizations
        await stream.send_message(UpdateOrganizationInviteAuthorizationsResponse(invite=self.invite))

    async def DeleteOrganizationMember(self, stream: Stream[DeleteOrganizationMemberRequest, DeleteOrganizationMemberResponse]) -> None:
        raise NotImplementedError()

    async def DeleteOrganizationInvite(self, stream: Stream[DeleteOrganizationInviteRequest, DeleteOrganizationInviteResponse]) -> None:
        raise NotImplementedError()

    async def ResendOrganizationInvite(self, stream: Stream[ResendOrganizationInviteRequest, ResendOrganizationInviteResponse]) -> None:
        raise NotImplementedError()

    async def CreateLocation(self, stream: Stream[CreateLocationRequest, CreateLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        self.parent_location_id = request.parent_location_id
        await stream.send_message(CreateLocationResponse(location=self.location))

    async def GetLocation(self, stream: Stream[GetLocationRequest, GetLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        await stream.send_message(GetLocationResponse(location=self.location))

    async def UpdateLocation(self, stream: Stream[UpdateLocationRequest, UpdateLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        self.name = request.name
        self.parent_location_id = request.parent_location_id
        await stream.send_message(UpdateLocationResponse(location=self.location))

    async def DeleteLocation(self, stream: Stream[DeleteLocationRequest, DeleteLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        await stream.send_message(DeleteLocationResponse())

    async def ListLocations(self, stream: Stream[ListLocationsRequest, ListLocationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListLocationsResponse(locations=[self.location]))

    async def ShareLocation(self, stream: Stream[ShareLocationRequest, ShareLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.organization_id = request.organization_id
        self.location_id = request.location_id
        await stream.send_message(ShareLocationResponse())

    async def UnshareLocation(self, stream: Stream[UnshareLocationRequest, UnshareLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.organization_id = request.organization_id
        self.location_id = request.location_id
        await stream.send_message(UnshareLocationResponse())

    async def LocationAuth(self, stream: Stream[LocationAuthRequest, LocationAuthResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        await stream.send_message(LocationAuthResponse(auth=self.location_auth))

    async def CreateLocationSecret(self, stream: Stream[CreateLocationSecretRequest, CreateLocationSecretResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        await stream.send_message(CreateLocationSecretResponse(auth=self.location_auth))

    async def DeleteLocationSecret(self, stream: Stream[DeleteLocationSecretRequest, DeleteLocationSecretResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        self.secret_id = request.secret_id
        await stream.send_message(DeleteLocationSecretResponse())

    async def GetRobot(self, stream: Stream[GetRobotRequest, GetRobotResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_id = request.id
        await stream.send_message(GetRobotResponse(robot=self.robot))

    async def GetRoverRentalRobots(self, stream: Stream[GetRoverRentalRobotsRequest, GetRoverRentalRobotsResponse]) -> None:
        raise NotImplementedError()

    async def GetRobotParts(self, stream: Stream[GetRobotPartsRequest, GetRobotPartsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_id = request.robot_id
        await stream.send_message(GetRobotPartsResponse(parts=[self.robot_part]))

    async def GetRobotPart(self, stream: Stream[GetRobotPartRequest, GetRobotPartResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.id
        await stream.send_message(GetRobotPartResponse(part=self.robot_part))

    async def GetRobotPartLogs(self, stream: Stream[GetRobotPartLogsRequest, GetRobotPartLogsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.id
        self.filter = request.filter
        self.errors_only = request.errors_only
        await stream.send_message(GetRobotPartLogsResponse(logs=[self.log_entry]))

    async def TailRobotPartLogs(self, stream: Stream[TailRobotPartLogsRequest, TailRobotPartLogsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.id
        self.errors_only = request.errors_only
        self.filter = request.filter
        await stream.send_message(TailRobotPartLogsResponse(logs=[]))

    async def GetRobotPartHistory(self, stream: Stream[GetRobotPartHistoryRequest, GetRobotPartHistoryResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.id
        await stream.send_message(GetRobotPartHistoryResponse(history=self.robot_part_history))

    async def UpdateRobotPart(self, stream: Stream[UpdateRobotPartRequest, UpdateRobotPartResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.id
        self.name = request.name
        self.robot_config = request.robot_config
        await stream.send_message(UpdateRobotPartResponse(part=self.robot_part))

    async def NewRobotPart(self, stream: Stream[NewRobotPartRequest, NewRobotPartResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_id = request.robot_id
        self.part_name = request.part_name
        await stream.send_message(NewRobotPartResponse(part_id=self.id))

    async def DeleteRobotPart(self, stream: Stream[DeleteRobotPartRequest, DeleteRobotPartResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.part_id
        await stream.send_message(DeleteRobotPartResponse())

    async def MarkPartAsMain(self, stream: Stream[MarkPartAsMainRequest, MarkPartAsMainResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.part_id
        await stream.send_message(MarkPartAsMainResponse())

    async def MarkPartForRestart(self, stream: Stream[MarkPartForRestartRequest, MarkPartForRestartResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.part_id
        await stream.send_message(MarkPartForRestartResponse())

    async def CreateRobotPartSecret(self, stream: Stream[CreateRobotPartSecretRequest, CreateRobotPartSecretResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.part_id
        await stream.send_message(CreateRobotPartSecretResponse(part=self.robot_part))

    async def DeleteRobotPartSecret(self, stream: Stream[DeleteRobotPartSecretRequest, DeleteRobotPartSecretResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.part_id
        self.secret_id = request.secret_id
        await stream.send_message(DeleteRobotPartSecretResponse())

    async def ListRobots(self, stream: Stream[ListRobotsRequest, ListRobotsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        await stream.send_message(ListRobotsResponse(robots=[self.robot]))

    async def NewRobot(self, stream: Stream[NewRobotRequest, NewRobotResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        self.location_id = request.location
        await stream.send_message(NewRobotResponse(id=self.id))

    async def UpdateRobot(self, stream: Stream[UpdateRobotRequest, UpdateRobotResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_id = request.id
        self.name = request.name
        self.location_id = request.location
        await stream.send_message(UpdateRobotResponse(robot=self.robot))

    async def DeleteRobot(self, stream: Stream[DeleteRobotRequest, DeleteRobotResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_id = request.id
        await stream.send_message(DeleteRobotResponse())

    async def ListFragments(self, stream: Stream[ListFragmentsRequest, ListFragmentsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.show_public = request.show_public
        await stream.send_message(ListFragmentsResponse(fragments=[self.fragment]))

    async def GetFragment(self, stream: Stream[GetFragmentRequest, GetFragmentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.fragment_id = request.id
        await stream.send_message(GetFragmentResponse(fragment=self.fragment))

    async def CreateFragment(self, stream: Stream[CreateFragmentRequest, CreateFragmentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        await stream.send_message(CreateFragmentResponse(fragment=self.fragment))

    async def UpdateFragment(self, stream: Stream[UpdateFragmentRequest, UpdateFragmentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.fragment_id = request.id
        self.name = request.name
        self.public = request.public
        await stream.send_message(UpdateFragmentResponse(fragment=self.fragment))

    async def DeleteFragment(self, stream: Stream[DeleteFragmentRequest, DeleteFragmentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.fragment_id = request.id
        await stream.send_message(DeleteFragmentResponse())

    async def AddRole(self, stream: Stream[AddRoleRequest, AddRoleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.identity_id = request.authorization.identity_id
        self.role = request.authorization.authorization_id.split("_")[-1]
        self.resource_type = request.authorization.resource_type
        self.resource_id = request.authorization.resource_id
        await stream.send_message(AddRoleResponse())

    async def RemoveRole(self, stream: Stream[RemoveRoleRequest, RemoveRoleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.identity_id = request.authorization.identity_id
        self.role = request.authorization.authorization_id.split("_")[-1]
        self.resource_type = request.authorization.resource_type
        self.resource_id = request.authorization.resource_id
        await stream.send_message(RemoveRoleResponse())

    async def ListAuthorizations(self, stream: Stream[ListAuthorizationsRequest, ListAuthorizationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.resource_ids = request.resource_ids
        await stream.send_message(ListAuthorizationsResponse(authorizations=self.authorizations))

    async def CheckPermissions(self, stream: Stream[CheckPermissionsRequest, CheckPermissionsResponse]) -> None:
        raise NotImplementedError()

    async def CreateModule(self, stream: Stream[CreateModuleRequest, CreateModuleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        await stream.send_message(CreateModuleResponse(module_id=self.id, url=self.url))

    async def UpdateModule(self, stream: Stream[UpdateModuleRequest, UpdateModuleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.module_id = request.module_id
        self.url = request.url
        self.description = request.description
        self.models = request.models
        self.entrypoint = request.entrypoint
        self.organization_id = request.organization_id
        self.visibility = request.visibility
        await stream.send_message(UpdateModuleResponse(url=self.url))

    async def UploadModuleFile(self, stream: Stream[UploadModuleFileRequest, UploadModuleFileResponse]) -> None:
        request_file_info = await stream.recv_message()
        assert request_file_info is not None
        self.module_file_info = request_file_info.module_file_info
        request_file = await stream.recv_message()
        assert request_file is not None
        self.file = request_file.file
        await stream.send_message(UploadModuleFileResponse(url=self.id))

    async def GetModule(self, stream: Stream[GetModuleRequest, GetModuleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.module_id = request.module_id
        await stream.send_message(GetModuleResponse(module=self.module))

    async def ListModules(self, stream: Stream[ListModulesRequest, ListModulesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListModulesResponse(modules=[self.module]))
