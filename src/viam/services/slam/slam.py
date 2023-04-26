import abc
from typing import Final, List, Optional
from viam.proto.common import Pose
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype
from viam.services.service_base import ServiceBase


class SLAM(ServiceBase):
    """
    SLAM repressents a SLAM service.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "slam")

    @abc.abstractmethod
    async def get_internal_state(self, name: str, *, timeout: Optional[float]) -> List[bytes]:
        """Get the internal state of the SLAM algorithm required to continue mapping/localization

        Args:
            name (str): The name of the SLAM service

        Returns:
            List[GetInternalStateResponse]: Chunks of the internal state of the SLAM algorithm

        """
        ...

    @abc.abstractmethod
    async def get_point_cloud_map(self, name: str, *, timeout: Optional[float]) -> List[bytes]:
        """
        Get the point cloud map

        Args:
            name (str): The name of the SLAM service

        Returns:
            List[GetPointCloudMapResponse]: Complete pointcloud in standard PCD format. Chunks of the PointCloud, concatenating all
                GetPointCloudMapResponse.point_cloud_pcd_chunk values
        """
        ...

    @abc.abstractmethod
    async def get_position(self, name: str, *, timeout: Optional[float]) -> Pose:
        """
        Get current position of the specified component in the SLAM Map

        Args:
            name (str): The name of the SLAM service

        Returns:
            Pose: The current position of the specified component
        """
        ...
