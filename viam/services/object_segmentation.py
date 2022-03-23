from typing import Any, Dict, List, Tuple

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel
from viam.proto.api.common import PointCloudObject
from viam.proto.api.service.objectsegmentation import (
    GetObjectPointCloudsRequest, GetObjectPointCloudsResponse,
    GetSegmenterParametersRequest, GetSegmenterParametersResponse,
    GetSegmentersRequest, GetSegmentersResponse, ObjectSegmentationServiceStub)
from viam.utils import CameraMimeType


class ObjectSegmentationClient:

    def __init__(self, channel: Channel):
        self.client = ObjectSegmentationServiceStub(channel)

    async def get_segmenters(self) -> List[str]:
        request = GetSegmentersRequest()
        response: GetSegmentersResponse = \
            await self.client.GetSegmenters(request)
        return list(response.segmenters)

    async def get_segmenter_parameters(
        self,
        name: str
    ) -> List[Tuple[str, str]]:
        request = GetSegmenterParametersRequest(segmenter_name=name)
        response: GetSegmenterParametersResponse = \
            await self.client.GetSegmenterParameters(request)
        return [(x.name, x.type) for x in response.parameters]

    async def get_object_point_clouds(
        self,
        camera_name: str,
        segmenter_name: str,
        parameters: Dict[str, Any]
    ) -> List[PointCloudObject]:
        struct = Struct()
        struct.update(parameters)
        request = GetObjectPointCloudsRequest(
            camera_name=camera_name,
            segmenter_name=segmenter_name,
            mime_type=CameraMimeType.PCD.value,
            parameters=struct
        )
        response: GetObjectPointCloudsResponse = \
            await self.client.GetObjectPointClouds(request)
        return list(response.objects)
