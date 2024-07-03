import abc
from typing import Final, List, Optional

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype

from ..service_base import ServiceBase
from . import GeoGeometry, GeoPoint, MapType, Mode, Path, Waypoint


class Navigation(ServiceBase):
    """
    Navigation represents a Navigation service.

    This acts as an abstract base class for any drivers representing specific
    navigation service implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    For more information, see `Navigation service <https://docs.viam.com/services/navigation/>`_.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "navigation"
    )

    @abc.abstractmethod
    async def get_paths(self, *, timeout: Optional[float]) -> List[Path]:
        """
        Get each path, the series of geo points the robot plans to travel through
        to get to a destination waypoint, in the machine's motion planning.

        ::

            my_nav = NavigationClient.from_robot(robot=robot, name="my_nav_service")

            # Get a list containing each path stored by the navigation service
            paths = await my_nav.get_paths()

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            List[navigation.Path]: An array comprised of Paths, where each path is either a user-provided destination or
            a Waypoint, along with the corresponding set of geopoints. This outlines the route the machine is expected to take to
            reach the specified destination or Waypoint.

        For more information, see `Navigation service <https://docs.viam.com/services/navigation/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_location(self, *, timeout: Optional[float]) -> GeoPoint:
        """
        Get the current location of the robot in the navigation service.

        ::

            my_nav = NavigationClient.from_robot(robot=robot, name="my_nav_service")

            # Get the current location of the robot in the navigation service
            location = await my_nav.get_location()

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.GeoPoint: The current location of the robot in the navigation service,
            represented in a GeoPoint with latitude and longitude values.

        For more information, see `Navigation service <https://docs.viam.com/services/navigation/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_obstacles(self, *, timeout: Optional[float]) -> List[GeoGeometry]:
        """
        Get an array or list of the obstacles currently in the service's data storage.
        These are objects designated for the robot to avoid when navigating.
        These include all transient obstacles which are discovered by the vision services configured for the navigation service,
        in addition to the obstacles that are configured as a part of the service.

        ::

            my_nav = NavigationClient.from_robot(robot=robot, name="my_nav_service")

            # Get a list containing each obstacle stored by the navigation service
            obstacles = await my_nav.get_obstacles()

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            List[navigation.GeoGeometry]: A list comprised of each GeoGeometry in the service's data storage.
            These are objects designated for the robot to avoid when navigating.

        For more information, see `Navigation service <https://docs.viam.com/services/navigation/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_waypoints(self, *, timeout: Optional[float]) -> List[Waypoint]:
        """
        Get an array of waypoints currently in the service's data storage.
        These are locations designated within a path for the robot to navigate to.

        ::

            my_nav = NavigationClient.from_robot(robot=robot, name="my_nav_service")

            # Get a list containing each waypoint stored by the navigation service
            waypoints = await my_nav.get_waypoints()

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            List[navigation.Waypoint]: An array comprised of each Waypoint in the service's data storage.
            These are locations designated within a path for the robot to navigate to.

        For more information, see `Navigation service <https://docs.viam.com/services/navigation/>`_.
        """
        ...

    @abc.abstractmethod
    async def add_waypoint(self, point: GeoPoint, *, timeout: Optional[float]):
        """
        Add a waypoint to the service's data storage.

        ::

           my_nav = NavigationClient.from_robot(robot=robot, name="my_nav_service")

            # Create a new waypoint with latitude and longitude values of 0 degrees
            location = GeoPoint(latitude=0, longitude=0)


            # Add your waypoint to the service's data storage
            await my_nav.add_waypoint(point=location)

        Args:
            point (navigation.GeoPoint): The current location of the robot in the navigation service,
                represented in a GeoPoint with latitude and longitude values.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        For more information, see `Navigation service <https://docs.viam.com/services/navigation/>`_.
        """
        ...

    @abc.abstractmethod
    async def remove_waypoint(self, id: str, *, timeout: Optional[float]):
        """
        Remove a waypoint from the service's data storage. If the robot is currently navigating to this waypoint,
        the motion will be canceled, and the robot will proceed to the next waypoint.

        ::

            my_nav = NavigationClient.from_robot(robot=robot, name="my_nav_service")

            # Remove the waypoint matching that ObjectID from the service's data storage
            await my_nav.remove_waypoint(waypoint_id)

        Args:
            id (str): The MongoDB ObjectID of the Waypoint to remove from the service's data storage.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        For more information, see `Navigation service <https://docs.viam.com/services/navigation/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_mode(self, *, timeout: Optional[float]) -> Mode.ValueType:
        """
        Get the Mode the service is operating in.

        There are two options for modes: MODE_MANUAL or MODE_WAYPOINT.

            MODE_WAYPOINT: Start to look for added waypoints and begin autonomous navigation.
            MODE_MANUAL: Stop autonomous navigation between waypoints and allow the base to be controlled manually.

        ::

            my_nav = NavigationClient.from_robot(robot=robot, name="my_nav_service")

            # Get the Mode the service is operating in
            await my_nav.get_mode()

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Mode.ValueType: The Mode the service is operating in.

        For more information, see `Navigation service <https://docs.viam.com/services/navigation/>`_.
        """
        ...

    @abc.abstractmethod
    async def set_mode(self, mode: Mode.ValueType, *, timeout: Optional[float]):
        """
        Set the Mode the service is operating in.

        There are two options for modes: MODE_MANUAL or MODE_WAYPOINT.

            MODE_WAYPOINT: Start to look for added waypoints and begin autonomous navigation.
            MODE_MANUAL: Stop autonomous navigation between waypoints and allow the base to be controlled manually.

        ::

            my_nav = NavigationClient.from_robot(robot=robot, name="my_nav_service")

            # Set the Mode the service is operating in to MODE_WAYPOINT and begin navigation
            await my_nav.set_mode(Mode.ValueType.MODE_WAYPOINT)

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.
            mode (navigation.Mode.ValueType): The Mode for the service to operate in.

        For more information, see `Navigation service <https://docs.viam.com/services/navigation/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, *, timeout: Optional[float]) -> MapType.ValueType:
        """
        Get information about the navigation service.

        ::

            my_nav = NavigationClient.from_robot(robot=robot, name="my_nav_service")

            # Get the properties of the current navigation service.
            nav_properties = await my_nav.get_properties()

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            MapType.ValueType: Information about the type of map the service is using.

        For more information, see `Navigation service <https://docs.viam.com/services/navigation/>`_.
        """
        ...
