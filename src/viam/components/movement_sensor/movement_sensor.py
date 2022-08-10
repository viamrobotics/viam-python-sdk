import abc
from typing import Mapping, Tuple

from viam.proto.api.common import GeoPoint, Orientation, Vector3
from viam.proto.api.component.movementsensor import GetPropertiesResponse

from ..component_base import ComponentBase


class MovementSensor(ComponentBase):
    """MovementSensor reports information about the robot's direction, position and speed.

    This acts as an abstract base class for any sensors that can provide data regarding the robot's direction, position, and speed.
    This cannot be used on its own. If the `__init__()` function is overriden, it must call the `super().__init__()` function.
    """

    Properties = GetPropertiesResponse

    @abc.abstractmethod
    async def get_position(self) -> Tuple[GeoPoint, float]:
        """Get the current GeoPoint (latitude, longitude) and altitude (mm)

        Returns:
            Tuple[GeoPoint, float]: The current lat/long, along with the altitude in mm
        """
        ...

    @abc.abstractmethod
    async def get_linear_velocity(self) -> Vector3:
        """Get the current linear velocity as a `Vector3` with x, y, and z axes represented in mm/sec

        Returns:
            Vector3: The linear velocity in mm/sec
        """
        ...

    @abc.abstractmethod
    async def get_angular_velocity(self) -> Vector3:
        """Get the current angular velocity as a `Vector3` with x, y, and z axes represented in radians/sec

        Returns:
            Vector3: The angular velocity in rad/sec
        """
        ...

    @abc.abstractmethod
    async def get_compass_heading(self) -> float:
        """Get the current compass heading in degrees

        Returns:
            float: The compass heading in degrees
        """
        ...

    @abc.abstractmethod
    async def get_orientation(self) -> Orientation:
        """Get the current orientation

        Returns:
            Orientation: The orientation
        """
        ...

    @abc.abstractmethod
    async def get_properties(self) -> Properties:
        """Get the supported properties of this sensor

        Returns:
            Properties: The properties
        """
        ...

    @abc.abstractmethod
    async def get_accuracy(self) -> Mapping[str, float]:
        """Get the accuracy of the various sensors

        Returns:
            Dict[str, float]: The accuracy in mm
        """
        ...
