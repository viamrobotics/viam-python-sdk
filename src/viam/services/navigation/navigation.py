import abc
from typing import Any, Dict, Final, List, Optional

from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE

from ..service_base import ServiceBase
from . import (
    GetCostmapResponse,
    Location,
    Plan,
    Position,
    Properties,
    Route,
    Status,
    Waypoint,
    Zone,
)


class Navigation(ServiceBase):
    """
    Navigation represents a Navigation service.

    This acts as an abstract base class for any drivers representing specific
    navigation service implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    For more information, see `Navigation service <https://docs.viam.com/dev/reference/apis/services/navigation/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "navigation"
    )

    @abc.abstractmethod
    async def add_location(
        self,
        location_name: str,
        position: Optional[Position] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Location:
        """
        Save a named Location on the active map.

        Args:
            location_name (str): The name of the location to save.
            position (Optional[navigation.Position]): The position to save. Omit to use the robot's current position.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Location: The saved location.
        """
        ...

    @abc.abstractmethod
    async def get_location(
        self, location_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Location:
        """
        Get a previously saved Location by name.

        Args:
            location_name (str): The name of the location to retrieve.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Location: The requested location.
        """
        ...

    @abc.abstractmethod
    async def list_locations(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[Location]:
        """
        List all previously saved Locations.

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            List[navigation.Location]: All saved locations.
        """
        ...

    @abc.abstractmethod
    async def update_location(
        self,
        location_name: str,
        position: Optional[Position] = None,
        new_name: Optional[str] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Location:
        """
        Update a previously saved Location.

        Args:
            location_name (str): The name of the location to update.
            position (Optional[navigation.Position]): The new position. Omit to leave the position unchanged.
            new_name (Optional[str]): The new name for the location. Omit to leave the name unchanged.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Location: The updated location.
        """
        ...

    @abc.abstractmethod
    async def delete_location(
        self, location_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> None:
        """
        Delete a previously saved Location.

        Args:
            location_name (str): The name of the location to delete.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.
        """
        ...

    @abc.abstractmethod
    async def add_route(
        self,
        route_name: str,
        waypoints: Optional[List[Waypoint]] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Route:
        """
        Save a named Route, an ordered list of waypoints.

        Args:
            route_name (str): The name of the route to save.
            waypoints (Optional[List[navigation.Waypoint]]): The ordered waypoints that make up the route.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Route: The saved route.
        """
        ...

    @abc.abstractmethod
    async def get_route(
        self, route_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Route:
        """
        Get a previously saved Route by name.

        Args:
            route_name (str): The name of the route to retrieve.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Route: The requested route.
        """
        ...

    @abc.abstractmethod
    async def list_routes(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[Route]:
        """
        List all previously saved Routes.

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            List[navigation.Route]: All saved routes.
        """
        ...

    @abc.abstractmethod
    async def update_route(
        self,
        route_name: str,
        new_name: Optional[str] = None,
        waypoints: Optional[List[Waypoint]] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Route:
        """
        Update a previously saved Route.

        Args:
            route_name (str): The name of the route to update.
            new_name (Optional[str]): The new name for the route. Omit to leave the name unchanged.
            waypoints (Optional[List[navigation.Waypoint]]): The new ordered waypoints. Omit to leave the waypoints unchanged;
                pass an empty list to clear them.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Route: The updated route.
        """
        ...

    @abc.abstractmethod
    async def delete_route(
        self, route_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> None:
        """
        Delete a previously saved Route.

        Args:
            route_name (str): The name of the route to delete.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.
        """
        ...

    @abc.abstractmethod
    async def add_zone(
        self,
        zone_name: str,
        type: str,
        geometry: Dict[str, Any],
        max_speed: Optional[float] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Zone:
        """
        Save a named Zone, a region on the active map.

        Args:
            zone_name (str): The name of the zone to save.
            type (str): The type of zone, either "keepout" or "speed_limit".
            geometry (Dict[str, Any]): The shape of the zone (circle, box, or polygon).
            max_speed (Optional[float]): Max speed in meters/sec; required when type is "speed_limit".
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Zone: The saved zone.
        """
        ...

    @abc.abstractmethod
    async def get_zone(self, zone_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Zone:
        """
        Get a previously saved Zone by name.

        Args:
            zone_name (str): The name of the zone to retrieve.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Zone: The requested zone.
        """
        ...

    @abc.abstractmethod
    async def list_zones(
        self, type: Optional[str] = None, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> List[Zone]:
        """
        List all previously saved Zones.

        Args:
            type (Optional[str]): Filter by zone type, either "keepout" or "speed_limit".
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            List[navigation.Zone]: All saved zones matching the filter, if provided.
        """
        ...

    @abc.abstractmethod
    async def update_zone(
        self,
        zone_name: str,
        type: Optional[str] = None,
        geometry: Optional[Dict[str, Any]] = None,
        max_speed: Optional[float] = None,
        new_name: Optional[str] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Zone:
        """
        Update a previously saved Zone.

        Args:
            zone_name (str): The name of the zone to update.
            type (Optional[str]): The new zone type. Omit to leave unchanged.
            geometry (Optional[Dict[str, Any]]): The new shape of the zone. Omit to leave unchanged.
            max_speed (Optional[float]): The new max speed in meters/sec. Omit to leave unchanged.
            new_name (Optional[str]): The new name for the zone. Omit to leave the name unchanged.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Zone: The updated zone.
        """
        ...

    @abc.abstractmethod
    async def delete_zone(
        self, zone_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> None:
        """
        Delete a previously saved Zone.

        Args:
            zone_name (str): The name of the zone to delete.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.
        """
        ...

    @abc.abstractmethod
    async def navigate_to_location(
        self, location_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Status:
        """
        Start navigating to a previously saved Location.

        Args:
            location_name (str): The name of the location to navigate to.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Status: The resulting navigation status.
        """
        ...

    @abc.abstractmethod
    async def navigate_to_point(
        self, destination: Position, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Status:
        """
        Start navigating to a destination Position.

        Args:
            destination (navigation.Position): The destination to navigate to.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Status: The resulting navigation status.
        """
        ...

    @abc.abstractmethod
    async def navigate_route(
        self,
        route_name: Optional[str] = None,
        waypoints: Optional[List[Waypoint]] = None,
        start_index: int = 0,
        start_nearest: bool = False,
        loop: bool = False,
        wait: bool = False,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Status:
        """
        Start navigating a Route, either a previously saved one or an inline list of waypoints.

        Args:
            route_name (Optional[str]): The name of a previously saved route.
            waypoints (Optional[List[navigation.Waypoint]]): An inline list of waypoints.
            start_index (int): The index of the waypoint to start at.
            start_nearest (bool): Start at the waypoint nearest to the robot's current position, overriding start_index.
            loop (bool): Loop the route indefinitely.
            wait (bool): With loop, only return once the robot has stopped.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Status: The resulting navigation status.
        """
        ...

    @abc.abstractmethod
    async def plan_to_point(
        self,
        destination: Position,
        start: Optional[Position] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Plan:
        """
        Preview a path to a destination Position without moving the robot.

        Args:
            destination (navigation.Position): The destination to plan to.
            start (Optional[navigation.Position]): The position to plan from. Defaults to the robot's current position.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Plan: The planned path.
        """
        ...

    @abc.abstractmethod
    async def plan_to_location(
        self,
        location_name: str,
        start: Optional[Position] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Plan:
        """
        Preview a path to a previously saved Location without moving the robot.

        Args:
            location_name (str): The name of the location to plan to.
            start (Optional[navigation.Position]): The position to plan from. Defaults to the robot's current position.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Plan: The planned path.
        """
        ...

    @abc.abstractmethod
    async def execute_plan(
        self, plan: Plan, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Status:
        """
        Start navigating a previously previewed Plan.

        Args:
            plan (navigation.Plan): The plan to execute, as returned by ``plan_to_point`` or ``plan_to_location``.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Status: The resulting navigation status.
        """
        ...

    @abc.abstractmethod
    async def go_to_location(
        self,
        location_name: str,
        wait: Optional[bool] = None,
        linear_m_per_sec: Optional[float] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Status:
        """
        Drive directly to a previously saved Location, without planning around zones or obstacles.

        Args:
            location_name (str): The name of the location to drive to.
            wait (Optional[bool]): Whether to wait until the robot has arrived. Defaults to true.
            linear_m_per_sec (Optional[float]): The linear speed to drive at.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Status: The resulting navigation status.
        """
        ...

    @abc.abstractmethod
    async def go_to_point(
        self,
        destination: Position,
        wait: Optional[bool] = None,
        linear_m_per_sec: Optional[float] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Status:
        """
        Drive directly to a destination Position, without planning around zones or obstacles.

        Args:
            destination (navigation.Position): The destination to drive to.
            wait (Optional[bool]): Whether to wait until the robot has arrived. Defaults to true.
            linear_m_per_sec (Optional[float]): The linear speed to drive at.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Status: The resulting navigation status.
        """
        ...

    @abc.abstractmethod
    async def suspend(
        self, reason: str = "", *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Status:
        """
        Suspend the current goal, holding position until ``resume`` is called.

        Args:
            reason (str): The reason for suspending, reported on the suspended goal.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Status: The resulting navigation status.
        """
        ...

    @abc.abstractmethod
    async def resume(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Status:
        """
        Resume a previously suspended goal.

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Status: The resulting navigation status.
        """
        ...

    @abc.abstractmethod
    async def cancel(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Status:
        """
        Cancel the current goal.

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Status: The resulting navigation status.
        """
        ...

    @abc.abstractmethod
    async def get_position(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Position:
        """
        Get the current position of the robot in the navigation service.

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Position: The current position of the robot.
        """
        ...

    @abc.abstractmethod
    async def get_navigation_status(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Status:
        """
        Get the current navigation state of the robot.

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Status: The current navigation status.
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Properties:
        """
        Get information about the navigation service that does not change while the service is running.

        Args:
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.Properties: Information about the navigation service.
        """
        ...

    @abc.abstractmethod
    async def get_costmap(
        self,
        layer: str = "",
        stride: int = 0,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> GetCostmapResponse:
        """
        Get a costmap describing the obstacles known to the navigation service.

        Args:
            layer (str): Which costmap layer to retrieve, one of "auto", "local", or "global". Defaults to "auto".
            stride (int): Downsample factor. Defaults to 2.
            timeout (Optional[float]): An option to set how long to wait (in seconds)
                before calling a time-out and closing the underlying RPC call.

        Returns:
            navigation.GetCostmapResponse: The requested costmap.
        """
        ...
