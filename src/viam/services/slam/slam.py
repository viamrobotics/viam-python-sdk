import abc
from typing import Final, List, Optional, Tuple

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype

from ..service_base import ServiceBase
from . import MappingMode, Pose


class SLAM(ServiceBase):
    """
    SLAM represents a SLAM service.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "slam")  # pyright: ignore [reportIncompatibleVariableOverride]

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
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.
            return_edited_map (bool): signal to the SLAM service to return an edited map, if the map package contains one and if
                the SLAM service supports the feature

        Returns:
            List[GetPointCloudMapResponse]: Complete pointcloud in standard PCD format. Chunks of the PointCloud, concatenating all
                GetPointCloudMapResponse.point_cloud_pcd_chunk values
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
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, *, timeout: Optional[float]) -> Tuple[bool, MappingMode.ValueType]:
        """
        Get information regarding the current SLAM session.

        ::

            slam_svc = SLAMClient.from_robot(robot=robot, name="my_slam_service")

            # Get the properties of your current SLAM session.
            slam_properties = await slam_svc.get_properties()

        Returns:
            Tuple[bool, MappingMode.ValueType]: A tuple of a boolean value representing if the SLAM session is being run in
            the cloud and the mapping mode of said session
        """
        ...
