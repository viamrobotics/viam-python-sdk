import abc
from typing import Any, Dict, Final, Mapping, Optional, Tuple

from grpclib import GRPCError
from viam.proto.common import GeoPoint, Orientation, Vector3
from viam.proto.component.movementsensor import GetPropertiesResponse
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..sensor import Sensor


class MovementSensor(Sensor):
    """MovementSensor reports information about the robot's direction, position and speed.

    This acts as an abstract base class for any sensors that can provide data regarding the robot's direction, position, and speed.
    This cannot be used on its own. If the ``__init__()`` function is overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "movement_sensor")

    Properties = GetPropertiesResponse

    @abc.abstractmethod
    async def get_position(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Tuple[GeoPoint, float]:
        """Get the current GeoPoint (latitude, longitude) and altitude (mm)

        Returns:
            Tuple[GeoPoint, float]: The current lat/long, along with the altitude in mm
        """
        ...

    @abc.abstractmethod
    async def get_linear_velocity(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Vector3:
        """Get the current linear velocity as a ``Vector3`` with x, y, and z axes represented in mm/sec

        Returns:
            Vector3: The linear velocity in mm/sec
        """
        ...

    @abc.abstractmethod
    async def get_angular_velocity(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Vector3:
        """Get the current angular velocity as a ``Vector3`` with x, y, and z axes represented in radians/sec

        Returns:
            Vector3: The angular velocity in rad/sec
        """
        ...

    @abc.abstractmethod
    async def get_linear_acceleration(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Vector3:
        """Get the current linear acceleration as a ``Vector3`` with x, y, and z axes represented in mm/sec^2

        Returns:
            Vector3: The linear acceleration in mm/sec^2
        """
        ...

    @abc.abstractmethod
    async def get_compass_heading(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
        """Get the current compass heading in degrees

        Returns:
            float: The compass heading in degrees
        """
        ...

    @abc.abstractmethod
    async def get_orientation(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Orientation:
        """Get the current orientation

        Returns:
            Orientation: The orientation
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Properties:
        """Get the supported properties of this sensor

        Returns:
            Properties: The properties
        """
        ...

    @abc.abstractmethod
    async def get_accuracy(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, float]:
        """Get the accuracy of the various sensors

        Returns:
            Dict[str, float]: The accuracy in mm
        """
        ...

    async def get_readings(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Mapping[str, Any]:
        """Obtain the measurements/data specific to this sensor.
        If a sensor is not configured to have a measurement or piece of data, it will be missing from the return dictionary.
        An ERROR log will still appear stating that the measurement/data was Unimplemented.

        Returns:
            Mapping[str, Any]: The readings for the MovementSensor:
            {
                position: GeoPoint,
                altitude: float,
                linear_velocity: Vector3,
                angular_velocity: Vector3,
                linear_acceleration: Vector3
                compass: float,
                orientation: Orientation
            }
        """
        functions = {
            "position": self.get_position,
            "linear_velocity": self.get_linear_velocity,
            "angular_velocity": self.get_angular_velocity,
            "linear_acceleration": self.get_linear_acceleration,
            "compass": self.get_compass_heading,
            "orientation": self.get_orientation,
        }
        readings = {}
        for property, function in functions.items():
            try:
                if property == "position":
                    readings["position"], readings["altitude"] = await function(extra=extra, timeout=timeout)
                else:
                    readings[property] = await function(extra=extra, timeout=timeout)
            except GRPCError:
                pass
        return readings
