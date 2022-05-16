from typing import Dict, List, Tuple

from grpclib.server import Stream
from viam.components.types import CameraMimeType
from viam.components.input import Control, Event, EventType
from viam.proto.api.common import PointCloudObject, PoseInFrame, ResourceName
from viam.proto.api.component.inputcontroller import (
    GetControlsRequest, GetControlsResponse, GetEventsRequest,
    GetEventsResponse, InputControllerServiceBase, StreamEventsRequest,
    StreamEventsResponse, TriggerEventRequest, TriggerEventResponse)
from viam.proto.api.service.framesystem import (Config, ConfigRequest,
                                                ConfigResponse,
                                                FrameSystemServiceBase,
                                                TransformPoseRequest,
                                                TransformPoseResponse)
from viam.proto.api.service.motion import (GetPoseRequest, GetPoseResponse,
                                           MotionServiceBase, MoveRequest,
                                           MoveResponse)
from viam.proto.api.service.vision import (AddDetectorRequest,
                                           AddDetectorResponse, Detection,
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
                                           TypedParameter, VisionServiceBase)


class MockFrameSystemService(FrameSystemServiceBase):

    def __init__(
        self,
        config_response: List[Config],
        transform_response: PoseInFrame
    ):
        self.config_response = config_response
        self.transform_response = transform_response

    async def Config(
        self,
        stream: Stream[ConfigRequest, ConfigResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = ConfigResponse(frame_system_configs=self.config_response)
        await stream.send_message(response)

    async def TransformPose(
        self,
        stream: Stream[TransformPoseRequest, TransformPoseResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = TransformPoseResponse(pose=self.transform_response)
        await stream.send_message(response)


class MockMotionService(MotionServiceBase):

    def __init__(
        self,
        move_responses: Dict[str, bool],
        get_pose_responses: Dict[str, PoseInFrame]
    ):
        self.move_responses = move_responses
        self.get_pose_responses = get_pose_responses

    async def Move(self, stream: Stream[MoveRequest, MoveResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        success = self.move_responses[name.name]
        response = MoveResponse(success=success)
        await stream.send_message(response)

    async def GetPose(
        self,
        stream: Stream[GetPoseRequest, GetPoseResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        pose = self.get_pose_responses[name.name]
        response = GetPoseResponse(pose=pose)
        await stream.send_message(response)


class MockVisionService(VisionServiceBase):

    def __init__(
        self,
        detectors: List[str],
        detections: List[Detection],
        segmenters: List[str],
        parameters: Dict[str, List[Tuple[str, str]]],
        point_clouds: List[PointCloudObject]
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

    async def GetDetections(self, stream: Stream[GetDetectionsRequest, GetDetectionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetDetectionsResponse(detections=self.detections)
        await stream.send_message(response)

    async def GetObjectPointClouds(
        self,
        stream: Stream[GetObjectPointCloudsRequest,
                       GetObjectPointCloudsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetObjectPointCloudsResponse(
            mime_type=CameraMimeType.PCD.value,
            objects=self.point_clouds
        )
        await stream.send_message(response)

    async def GetSegmenterParameters(
        self,
        stream: Stream[GetSegmenterParametersRequest,
                       GetSegmenterParametersResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        params = self.parameters[request.segmenter_name]
        response = GetSegmenterParametersResponse(
            segmenter_parameters=[TypedParameter(name=_name, type=_type)
                                  for _name, _type in params]
        )
        await stream.send_message(response)

    async def GetSegmenterNames(
        self,
        stream: Stream[GetSegmenterNamesRequest, GetSegmenterNamesResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetSegmenterNamesResponse(
            segmenter_names=self.segmenters
        )
        await stream.send_message(response)


class MockInputControllerService(InputControllerServiceBase):

    async def GetControls(self, stream: Stream[GetControlsRequest, GetControlsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetControlsResponse(controls=[
            Control.ABSOLUTE_X,
            Control.ABSOLUTE_Y,
            Control.ABSOLUTE_Z,
            Control.ABSOLUTE_RX,
            Control.ABSOLUTE_RY,
            Control.ABSOLUTE_RZ,
            Control.ABSOLUTE_HAT0_X,
            Control.ABSOLUTE_HAT0_Y,
            Control.BUTTON_SOUTH,
            Control.BUTTON_EAST,
            Control.BUTTON_WEST,
            Control.BUTTON_NORTH,
            Control.BUTTON_LT,
            Control.BUTTON_RT,
            Control.BUTTON_L_THUMB,
            Control.BUTTON_R_THUMB,
            Control.BUTTON_SELECT,
            Control.BUTTON_START,
            Control.BUTTON_MENU,
            Control.BUTTON_RECORD,
            Control.BUTTON_E_STOP,
        ])
        await stream.send_message(response)

    async def GetEvents(self, stream: Stream[GetEventsRequest, GetEventsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None

    async def StreamEvents(self, stream: Stream[StreamEventsRequest, StreamEventsResponse]) -> None:
        return await super().StreamEvents(stream)

    async def TriggerEvent(self, stream: Stream[TriggerEventRequest, TriggerEventResponse]) -> None:
        return await super().TriggerEvent(stream)
