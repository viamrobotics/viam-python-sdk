import abc
import sys
from typing import Final, List, Optional

from viam.proto.service.slam import GetPropertiesResponse
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype

from ..service_base import ServiceBase
from . import Pose

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


class SLAM(ServiceBase):
    """
    SLAM represents a SLAM service.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    For more information, see `SLAM service <https://docs.viam.com/services/slam/>`_.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "slam")  # pyright: ignore [reportIncompatibleVariableOverride]

    Properties: "TypeAlias" = GetPropertiesResponse

    @abc.abstractmethod
    async def get_internal_state(self, *, timeout: Optional[float]) -> List[bytes]:
        """
        Get the internal state of the SLAM algorithm required to continue mapping/localization.

        ::

            slam = SLAMClient.from_robot(robot=robot, name="my_slam_service")

            # Get the internal state of the SLAM algorithm required to continue mapping/localization.
            internal_state = await slam.get_internal_state()

        Returns:
            List[GetInternalStateResponse]: Chunks of the internal state of the SLAM algorithm

        For more information, see `SLAM service <https://docs.viam.com/services/slam/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_point_cloud_map(self, return_edited_map: bool = False, *, timeout: Optional[float]) -> List[bytes]:
        """
        Get the point cloud map.

        ::

            slam_svc = SLAMClient.from_robot(robot=robot, name="my_slam_service")

            # Get the point cloud map in standard PCD format.
            pcd_map = await slam_svc.get_point_cloud_map()

        Args:
            return_edited_map (bool): signal to the SLAM service to return an edited map, if the map package contains one and if
                the SLAM service supports the feature

        Returns:
            List[GetPointCloudMapResponse]: Complete pointcloud in standard PCD format. Chunks of the PointCloud, concatenating all
            GetPointCloudMapResponse.point_cloud_pcd_chunk values.

        For more information, see `SLAM service <https://docs.viam.com/services/slam/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_position(self, *, timeout: Optional[float]) -> Pose:
        """
        Get current position of the specified component in the SLAM Map.

        ::

            slam_svc = SLAMClient.from_robot(robot=robot, name="my_slam_service")

            # Get the current position of the specified source component in the SLAM map as a Pose.
            pose = await slam.get_position()

        Returns:
            Pose: The current position of the specified component

        For more information, see `SLAM service <https://docs.viam.com/services/slam/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, *, timeout: Optional[float]) -> Properties:
        """
        Get information regarding the current SLAM session.

        ::

            slam_svc = SLAMClient.from_robot(robot=robot, name="my_slam_service")

            # Get the properties of your current SLAM session.
            slam_properties = await slam_svc.get_properties()

        Returns:
            Properties: The properties of SLAM

        For more information, see `SLAM service <https://docs.viam.com/services/slam/>`_.
        """
        ...
