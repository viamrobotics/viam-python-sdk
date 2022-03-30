from typing import Dict, List, Tuple

from grpclib.server import Stream
from viam.proto.api.common import PointCloudObject, PoseInFrame, ResourceName
from viam.proto.api.service.framesystem import (Config, ConfigRequest,
                                                ConfigResponse,
                                                FrameSystemServiceBase,
                                                TransformPoseRequest,
                                                TransformPoseResponse)
from viam.proto.api.service.motion import (GetPoseRequest, GetPoseResponse,
                                           MotionServiceBase, MoveRequest,
                                           MoveResponse)
from viam.proto.api.service.objectsegmentation import (
    GetObjectPointCloudsRequest, GetObjectPointCloudsResponse,
    GetSegmenterParametersRequest, GetSegmenterParametersResponse,
    GetSegmentersRequest, GetSegmentersResponse, ObjectSegmentationServiceBase,
    TypedParameter)
from viam.utils import CameraMimeType


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


class MockObjectSegmentationService(ObjectSegmentationServiceBase):

    def __init__(
        self,
        segmenters: List[str],
        parameters: Dict[str, List[Tuple[str, str]]],
        point_clouds: List[PointCloudObject]
    ):
        self.segmenters = segmenters
        self.parameters = parameters
        self.point_clouds = point_clouds

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
            parameters=[TypedParameter(name=_name, type=_type)
                        for _name, _type in params]
        )
        await stream.send_message(response)

    async def GetSegmenters(
        self,
        stream: Stream[GetSegmentersRequest, GetSegmentersResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = GetSegmentersResponse(
            segmenters=self.segmenters
        )
        await stream.send_message(response)
