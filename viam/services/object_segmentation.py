from typing import Any, Dict, List, Tuple

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel
from viam.proto.api.common import PointCloudObject
from viam.proto.api.service.objectsegmentation import (
    GetObjectPointCloudsRequest, GetObjectPointCloudsResponse,
    GetSegmenterParametersRequest, GetSegmenterParametersResponse,
    GetSegmentersRequest, GetSegmentersResponse, ObjectSegmentationServiceStub)
from viam.components.types import CameraMimeType


class ObjectSegmentationClient:
    """
    Object Segmentation is a viam service that identifies objects from a given dataset and describes their geometry.
    """

    def __init__(self, channel: Channel):
        self.client = ObjectSegmentationServiceStub(channel)

    async def get_segmenters(self) -> List[str]:
        """
        Get the list of segmenters in the registry

        Returns:
            List[str]: The segmenters
        """
        request = GetSegmentersRequest()
        response: GetSegmentersResponse = \
            await self.client.GetSegmenters(request)
        return list(response.segmenters)

    async def get_segmenter_parameters(
        self,
        segmenter_name: str
    ) -> List[Tuple[str, str]]:
        """
        Get the parameter fields needed for the given segmenter.

        Args:
            segmenter_name (str): The name of the segmenter

        Returns:
            List[Tuple[str, str]]: A list of parameters for the segmenter.
                The first item in the tuple is the name of the parameter.
                The second item in the tuple is the type of the parameter.
        """
        request = GetSegmenterParametersRequest(segmenter_name=segmenter_name)
        response: GetSegmenterParametersResponse = \
            await self.client.GetSegmenterParameters(request)
        return [(x.name, x.type) for x in response.parameters]

    async def get_object_point_clouds(
        self,
        camera_name: str,
        segmenter_name: str,
        parameters: Dict[str, Any]
    ) -> List[PointCloudObject]:
        """
        Get all the found objects in a pointcloud from a camera of the
        underlying robot, as well as the 3-vector center of each of the
        found objects.

        Args:
            camera_name (str): The name of the camera
            segmenter_name (str): The name of the segmenter
            parameters (Dict[str, Any]): The parameters for the pointcloud

        Returns:
            List[PointCloudObject]: The pointclouds
        """
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
