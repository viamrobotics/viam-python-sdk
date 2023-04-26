from typing import Final, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, Pose
from viam.proto.service.slam import (
    GetInternalStateRequest,
    GetInternalStateResponse,
    GetPointCloudMapRequest,
    GetPointCloudMapResponse,
    GetPositionRequest,
    GetPositionResponse,
    SLAMServiceStub,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_client_base import ServiceClientBase
from viam.utils import dict_to_struct, struct_to_dict, ValueTypes


class SLAMServiceClient(ServiceClientBase, ReconfigurableResourceRPCClientBase):
    """
    Connect to the SLAMService, which allows the robot to create a map of its surroundings
    and find its location in that map.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "slam")

    def __init__(self, name: str, channel: Channel):
        super().__init__(name, channel)
        self.client = SLAMServiceStub(channel)

    async def get_position(self, name: str, *, timeout: Optional[float] = None) -> Pose:
        """Get current position of the specified component in the SLAM Map

        Args:
            name (str): The name of the SLAM service

        Returns:
            Pose: The current position of the specified component
        """
        request = GetPositionRequest(name=name)
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout)
        return response.pose

    async def get_point_cloud_map(self, name: str, *, timeout: Optional[float] = None) -> List[GetPointCloudMapResponse]:
        """Get the point

        Args:
            name (str): _description_
            timeout (Optional[float], optional): _description_. Defaults to None.

        Returns:
            List[GetPointCloudMapResponse]: Complete pointcloud in standard PCD format. Chunks of the PointCloud, concatenating all
                GetPointCloudMapResponse.point_cloud_pcd_chunk values
        """
        request = GetPointCloudMapRequest(name=name)
        response: List[GetPointCloudMapResponse] = await self.client.GetPointCloudMap(request, timeout=timeout)
        return response

    async def get_internal_state(self, name: str, *, timeout: Optional[float] = None) -> List[GetInternalStateResponse]:
        """_summary_

        Args:
            name (str): The name of the SLAM service

        Returns:
            List[GetInternalStateResponse]: Chunks of the internal state of the SLAM algorithm required to continue mapping/localization

        """
        request = GetInternalStateRequest(name=name)
        response: List[GetInternalStateResponse] = await self.client.GetInternalState(request, timeout=timeout)
        return response

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        """Send/receive arbitrary commands

        Args:
            command (Dict[str, ValueTypes]): The command to execute

        Returns:
            Dict[str, ValueTypes]: Result of the executed command
        """
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
