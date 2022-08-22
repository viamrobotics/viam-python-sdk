from typing import Dict, List, Tuple

from grpclib.server import Stream

from viam.components.types import CameraMimeType
from viam.proto.api.common import PointCloudObject, PoseInFrame, ResourceName
from viam.proto.api.service.motion import (
    GetPoseRequest,
    GetPoseResponse,
    MotionServiceBase,
    MoveRequest,
    MoveResponse,
    MoveSingleComponentRequest,
    MoveSingleComponentResponse,
)
from viam.proto.api.service.sensors import (
    GetReadingsRequest,
    GetReadingsResponse,
    GetSensorsRequest,
    GetSensorsResponse,
    Readings,
    SensorsServiceBase,
)
from viam.proto.api.service.vision import (
    AddDetectorRequest,
    AddDetectorResponse,
    Detection,
    GetDetectionsFromCameraRequest,
    GetDetectionsFromCameraResponse,
    GetDetectionsRequest,
    GetDetectionsResponse,
    GetDetectorNamesRequest,
    GetDetectorNamesResponse,
    GetObjectPointCloudsRequest,
    GetObjectPointCloudsResponse,
    GetSegmenterNamesRequest,
    GetSegmenterNamesResponse,
    GetSegmenterParametersRequest,
    GetSegmenterParametersResponse,
    TypedParameter,
    VisionServiceBase,
)


class MockMotionService(MotionServiceBase):
    def __init__(
        self,
        move_responses: Dict[str, bool],
        move_single_component_responses: Dict[str, bool],
        get_pose_responses: Dict[str, PoseInFrame],
    ):
        self.move_responses = move_responses
        self.move_single_component_responses = move_single_component_responses
        self.get_pose_responses = get_pose_responses

    async def Move(self, stream: Stream[MoveRequest, MoveResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        success = self.move_responses[name.name]
        response = MoveResponse(success=success)
        await stream.send_message(response)

    async def MoveSingleComponent(self, stream: Stream[MoveSingleComponentRequest, MoveSingleComponentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        success = self.move_single_component_responses[name.name]
        response = MoveSingleComponentResponse(success=success)
        await stream.send_message(response)

    async def GetPose(self, stream: Stream[GetPoseRequest, GetPoseResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        pose = self.get_pose_responses[name.name]
        response = GetPoseResponse(pose=pose)
        await stream.send_message(response)


class MockSensorsService(SensorsServiceBase):
    def __init__(self, sensors: List[ResourceName], readings: List[Readings]):
        self.sensors = sensors
        self.readings = readings

    async def GetSensors(self, stream: Stream[GetSensorsRequest, GetSensorsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetSensorsResponse(sensor_names=self.sensors)
        await stream.send_message(response)

    async def GetReadings(self, stream: Stream[GetReadingsRequest, GetReadingsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.sensors_for_readings: List[ResourceName] = list(request.sensor_names)
        response = GetReadingsResponse(readings=self.readings)
        await stream.send_message(response)


class MockVisionService(VisionServiceBase):
    def __init__(
        self,
        detectors: List[str],
        detections: List[Detection],
        segmenters: List[str],
        parameters: Dict[str, List[Tuple[str, str]]],
        point_clouds: List[PointCloudObject],
    ):
        self.detectors = detectors
        self.detections = detections
        self.segmenters = segmenters
        self.parameters = parameters
        self.point_clouds = point_clouds

    async def GetDetectorNames(self, stream: Stream[GetDetectorNamesRequest, GetDetectorNamesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetDetectorNamesResponse(detector_names=self.detectors)
        await stream.send_message(response)

    async def AddDetector(self, stream: Stream[AddDetectorRequest, AddDetectorResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.detectors.append(request.detector_name)
        await stream.send_message(AddDetectorResponse())

    async def GetDetectionsFromCamera(self, stream: Stream[GetDetectionsFromCameraRequest, GetDetectionsFromCameraResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetDetectionsFromCameraResponse(detections=self.detections)
        await stream.send_message(response)

    async def GetDetections(self, stream: Stream[GetDetectionsRequest, GetDetectionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetDetectionsResponse(detections=self.detections)
        await stream.send_message(response)

    async def GetObjectPointClouds(self, stream: Stream[GetObjectPointCloudsRequest, GetObjectPointCloudsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetObjectPointCloudsResponse(mime_type=CameraMimeType.PCD.value, objects=self.point_clouds)
        await stream.send_message(response)

    async def GetSegmenterParameters(self, stream: Stream[GetSegmenterParametersRequest, GetSegmenterParametersResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        params = self.parameters[request.segmenter_name]
        response = GetSegmenterParametersResponse(segmenter_parameters=[TypedParameter(name=_name, type=_type) for _name, _type in params])
        await stream.send_message(response)

    async def GetSegmenterNames(self, stream: Stream[GetSegmenterNamesRequest, GetSegmenterNamesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetSegmenterNamesResponse(segmenter_names=self.segmenters)
        await stream.send_message(response)
