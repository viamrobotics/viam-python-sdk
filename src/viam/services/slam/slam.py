import abc
from datetime import datetime
from typing import Final, List, Optional

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype

from ..service_base import ServiceBase
from . import Pose


class SLAM(ServiceBase):
    """
    SLAM represents a SLAM service.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "slam")

    @abc.abstractmethod
    async def get_internal_state(self, *, timeout: Optional[float]) -> List[bytes]:
        """Get the internal state of the SLAM algorithm required to continue mapping/localization.

        Returns:
            List[GetInternalStateResponse]: Chunks of the internal state of the SLAM algorithm

        """
        ...

    @abc.abstractmethod
    async def get_point_cloud_map(self, *, timeout: Optional[float]) -> List[bytes]:
        """
        Get the point cloud map.

        Returns:
            List[GetPointCloudMapResponse]: Complete pointcloud in standard PCD format. Chunks of the PointCloud, concatenating all
                GetPointCloudMapResponse.point_cloud_pcd_chunk values
        """
        ...

    @abc.abstractmethod
    async def get_latest_map_info(self, *, timeout: Optional[float]) -> datetime:
        """
        Get the timestamp of the last update to the point cloud SLAM map.

        Returns:
            datetime: The timestamp of the last update.
        """
        ...

    @abc.abstractmethod
    async def get_position(self, *, timeout: Optional[float]) -> Pose:
        """
        Get current position of the specified component in the SLAM Map.

        Returns:
            Pose: The current position of the specified component
        """
        ...
