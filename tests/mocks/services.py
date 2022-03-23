from typing import Dict, List, Tuple

from grpclib.server import Stream
from viam.proto.api.common import PointCloudObject
from viam.proto.api.service.objectsegmentation import (
    GetObjectPointCloudsRequest, GetObjectPointCloudsResponse,
    GetSegmenterParametersRequest, GetSegmenterParametersResponse,
    GetSegmentersRequest, GetSegmentersResponse, ObjectSegmentationServiceBase,
    TypedParameter)
from viam.utils import CameraMimeType


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
