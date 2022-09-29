import abc
import asyncio
from typing import Any, Mapping, Tuple

from viam.proto.common import GeoPoint, Orientation, Vector3
from viam.proto.component.movementsensor import GetPropertiesResponse

from ..sensor import Sensor


class MovementSensor(Sensor):
    """MovementSensor reports information about the robot's direction, position and speed.

    This acts as an abstract base class for any sensors that can provide data regarding the robot's direction, position, and speed.
    This cannot be used on its own. If the `__init__()` function is overridden, it must call the `super().__init__()` function.
    """

    Properties = GetPropertiesResponse

    @abc.abstractmethod
    async def get_position(self, **kwargs) -> Tuple[GeoPoint, float]:
        """Get the current GeoPoint (latitude, longitude) and altitude (mm)

        Returns:
            Tuple[GeoPoint, float]: The current lat/long, along with the altitude in mm
        """
        ...

    @abc.abstractmethod
    async def get_linear_velocity(self, **kwargs) -> Vector3:
        """Get the current linear velocity as a `Vector3` with x, y, and z axes represented in mm/sec

        Returns:
            Vector3: The linear velocity in mm/sec
        """
        ...

    @abc.abstractmethod
    async def get_angular_velocity(self, **kwargs) -> Vector3:
        """Get the current angular velocity as a `Vector3` with x, y, and z axes represented in radians/sec

        Returns:
            Vector3: The angular velocity in rad/sec
        """
        ...

    @abc.abstractmethod
    async def get_compass_heading(self, **kwargs) -> float:
        """Get the current compass heading in degrees

        Returns:
            float: The compass heading in degrees
        """
        ...

    @abc.abstractmethod
    async def get_orientation(self, **kwargs) -> Orientation:
        """Get the current orientation

        Returns:
            Orientation: The orientation
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, **kwargs) -> Properties:
        """Get the supported properties of this sensor

        Returns:
            Properties: The properties
        """
        ...

    @abc.abstractmethod
    async def get_accuracy(self, **kwargs) -> Mapping[str, float]:
        """Get the accuracy of the various sensors

        Returns:
            Dict[str, float]: The accuracy in mm
        """
        ...

    async def get_readings(self, **kwargs) -> Mapping[str, Any]:
        """Obtain the measurements/data specific to this sensor.

        Returns:
            Mapping[str, Any]: The readings for the MovementSensor:
            {
                position: GeoPoint,
                altitude: float,
                linear_velocity: Vector3,
                angular_velocity: Vector3,
                compass: float,
                orientation: Orientation
            }
        """
        ((pos, alt), lv, av, comp, orient) = await asyncio.gather(
            self.get_position(),
            self.get_linear_velocity(),
            self.get_angular_velocity(),
            self.get_compass_heading(),
            self.get_orientation(),
        )
        return {
            "position": pos,
            "altitude": alt,
            "linear_velocity": lv,
            "angular_velocity": av,
            "compass": comp,
            "orientation": orient,
        }
