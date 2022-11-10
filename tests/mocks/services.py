import json
from typing import Any, Dict, List, Mapping, Optional, Sequence, Union

from grpclib.server import Stream

from viam.media.video import CameraMimeType
from viam.proto.common import PointCloudObject, PoseInFrame, ResourceName
from viam.proto.service.motion import (
    GetPoseRequest,
    GetPoseResponse,
    MotionServiceBase,
    MoveRequest,
    MoveResponse,
    MoveSingleComponentRequest,
    MoveSingleComponentResponse,
)
from viam.proto.service.sensors import (
    GetReadingsRequest,
    GetReadingsResponse,
    GetSensorsRequest,
    GetSensorsResponse,
    Readings,
    SensorsServiceBase,
)
from viam.proto.service.vision import (
    AddClassifierRequest,
    AddClassifierResponse,
    AddDetectorRequest,
    AddDetectorResponse,
    AddSegmenterRequest,
    AddSegmenterResponse,
    Classification,
    Detection,
    GetClassificationsFromCameraRequest,
    GetClassificationsFromCameraResponse,
    GetClassificationsRequest,
    GetClassificationsResponse,
    GetClassifierNamesRequest,
    GetClassifierNamesResponse,
    GetDetectionsFromCameraRequest,
    GetDetectionsFromCameraResponse,
    GetDetectionsRequest,
    GetDetectionsResponse,
    GetDetectorNamesRequest,
    GetDetectorNamesResponse,
    GetModelParameterSchemaRequest,
    GetModelParameterSchemaResponse,
    GetObjectPointCloudsRequest,
    GetObjectPointCloudsResponse,
    GetSegmenterNamesRequest,
    GetSegmenterNamesResponse,
    RemoveClassifierRequest,
    RemoveClassifierResponse,
    RemoveDetectorRequest,
    RemoveDetectorResponse,
    RemoveSegmenterRequest,
    RemoveSegmenterResponse,
    VisionServiceBase,
)
from viam.utils import struct_to_dict


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
        self.extra: Optional[Mapping[str, Any]] = None
        self.timeout: Optional[float] = None

    async def Move(self, stream: Stream[MoveRequest, MoveResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        success = self.move_responses[name.name]
        response = MoveResponse(success=success)
        await stream.send_message(response)

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


class MockSensorsService(SensorsServiceBase):
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


class MockVisionService(VisionServiceBase):
    def __init__(
        self,
        detectors: List[str],
        detections: List[Detection],
        classifiers: List[str],
        classifications: List[Classification],
        segmenters: List[str],
        point_clouds: List[PointCloudObject],
        model_schema: Mapping[str, Mapping[str, Union[str, int, float, bool, Sequence, Mapping]]],
    ):
        self.detectors = detectors
        self.detections = detections
        self.classifiers = classifiers
        self.classifications = classifications
        self.segmenters = segmenters
        self.point_clouds = point_clouds
        self.model_schema = model_schema
        self.extra: Optional[Mapping[str, Any]] = None
        self.timeout: Optional[float] = None

    async def GetDetectorNames(self, stream: Stream[GetDetectorNamesRequest, GetDetectorNamesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = GetDetectorNamesResponse(detector_names=self.detectors)
        await stream.send_message(response)

    async def AddDetector(self, stream: Stream[AddDetectorRequest, AddDetectorResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        self.detectors.append(request.detector_name)
        await stream.send_message(AddDetectorResponse())

    async def RemoveDetector(self, stream: Stream[RemoveDetectorRequest, RemoveDetectorResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        self.detectors.remove(request.detector_name)
        await stream.send_message(RemoveDetectorResponse())

    async def GetDetectionsFromCamera(self, stream: Stream[GetDetectionsFromCameraRequest, GetDetectionsFromCameraResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = GetDetectionsFromCameraResponse(detections=self.detections)
        await stream.send_message(response)

    async def GetDetections(self, stream: Stream[GetDetectionsRequest, GetDetectionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = GetDetectionsResponse(detections=self.detections)
        await stream.send_message(response)

    async def GetClassifierNames(self, stream: Stream[GetClassifierNamesRequest, GetClassifierNamesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = GetClassifierNamesResponse(classifier_names=self.classifiers)
        await stream.send_message(response)

    async def AddClassifier(self, stream: Stream[AddClassifierRequest, AddClassifierResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        self.classifiers.append(request.classifier_name)
        await stream.send_message(AddClassifierResponse())

    async def RemoveClassifier(self, stream: Stream[RemoveClassifierRequest, RemoveClassifierResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        self.classifiers.remove(request.classifier_name)
        await stream.send_message(RemoveClassifierResponse())

    async def GetClassificationsFromCamera(
        self, stream: Stream[GetClassificationsFromCameraRequest, GetClassificationsFromCameraResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = GetClassificationsFromCameraResponse(classifications=self.classifications)
        await stream.send_message(response)

    async def GetClassifications(self, stream: Stream[GetClassificationsRequest, GetClassificationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = GetClassificationsResponse(classifications=self.classifications)
        await stream.send_message(response)

    async def GetObjectPointClouds(self, stream: Stream[GetObjectPointCloudsRequest, GetObjectPointCloudsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = GetObjectPointCloudsResponse(mime_type=CameraMimeType.PCD.value, objects=self.point_clouds)
        await stream.send_message(response)

    async def GetModelParameterSchema(self, stream: Stream[GetModelParameterSchemaRequest, GetModelParameterSchemaResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        schema = self.model_schema[request.model_type]
        response = GetModelParameterSchemaResponse(model_parameter_schema=json.dumps(schema).encode("utf-8"))
        await stream.send_message(response)

    async def GetSegmenterNames(self, stream: Stream[GetSegmenterNamesRequest, GetSegmenterNamesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = GetSegmenterNamesResponse(segmenter_names=self.segmenters)
        await stream.send_message(response)

    async def AddSegmenter(self, stream: Stream[AddSegmenterRequest, AddSegmenterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        self.segmenters.append(request.segmenter_name)
        await stream.send_message(AddSegmenterResponse())

    async def RemoveSegmenter(self, stream: Stream[RemoveSegmenterRequest, RemoveSegmenterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        self.segmenters.remove(request.segmenter_name)
        await stream.send_message(RemoveSegmenterResponse())
