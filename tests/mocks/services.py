from typing import Any, Dict, List, Mapping, Optional, Union

from grpclib.server import Stream
from PIL import Image

from viam.media.video import RawImage
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
