import abc
import asyncio
from dataclasses import dataclass
from typing import Any, Dict, Final, List, Mapping, Optional, Tuple

from grpclib import GRPCError
from typing_extensions import Self

from viam.errors import MethodNotImplementedError, NotSupportedError
from viam.proto.component.movementsensor import GetPropertiesResponse
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..sensor import Sensor
from . import GeoPoint, Orientation, Vector3


class MovementSensor(Sensor):
    """MovementSensor reports information about the robot's direction, position and speed.

    This acts as an abstract base class for any sensors that can provide data regarding the robot's direction, position, and speed.
    This cannot be used on its own. If the ``__init__()`` function is overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "movement_sensor")

    @dataclass
    class Properties:
        linear_acceleration_supported: bool
        angular_velocity_supported: bool
        orientation_supported: bool
        position_supported: bool
        compass_heading_supported: bool
        linear_velocity_supported: bool

        @property
        def proto(self) -> GetPropertiesResponse:
            return GetPropertiesResponse(
                linear_acceleration_supported=self.linear_acceleration_supported,
                angular_velocity_supported=self.angular_velocity_supported,
                orientation_supported=self.orientation_supported,
                position_supported=self.position_supported,
                compass_heading_supported=self.compass_heading_supported,
                linear_velocity_supported=self.linear_velocity_supported,
            )

        @classmethod
        def from_proto(cls, proto: GetPropertiesResponse) -> Self:
            return cls(
                linear_acceleration_supported=proto.linear_acceleration_supported,
                angular_velocity_supported=proto.angular_velocity_supported,
                orientation_supported=proto.orientation_supported,
                position_supported=proto.position_supported,
                compass_heading_supported=proto.compass_heading_supported,
                linear_velocity_supported=proto.linear_velocity_supported,
            )

    @abc.abstractmethod
    async def get_position(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Tuple[GeoPoint, float]:
        """Get the current GeoPoint (latitude, longitude) and altitude (m)

        Returns:
            Tuple[GeoPoint, float]: The current lat/long, along with the altitude in m
        """
        ...

    @abc.abstractmethod
    async def get_linear_velocity(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Vector3:
        """Get the current linear velocity as a ``Vector3`` with x, y, and z axes represented in m/sec

        Returns:
            Vector3: The linear velocity in m/sec
        """
        ...

    @abc.abstractmethod
    async def get_angular_velocity(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Vector3:
        """Get the current angular velocity as a ``Vector3`` with x, y, and z axes represented in degrees/sec

        Returns:
            Vector3: The angular velocity in degrees/sec
        """
        ...

    @abc.abstractmethod
    async def get_linear_acceleration(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Vector3:
        """Get the current linear acceleration as a ``Vector3`` with x, y, and z axes represented in m/sec^2

        Returns:
            Vector3: The linear acceleration in m/sec^2
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
            MovementSensor.Properties: The properties
        """
        ...

    @abc.abstractmethod
    async def get_accuracy(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, float]:
        """Get the accuracy of the various sensors

        Returns:
            Dict[str, float]: The accuracy
        """
        ...

    async def get_readings(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Mapping[str, Any]:
        """Obtain the measurements/data specific to this sensor.
        If a sensor is not configured to have a measurement or fails to read a piece of data, it will not appear in the readings dictionary.

        Returns:
            Mapping[str, Any]: The readings for the MovementSensor:
            {
                position: GeoPoint,
                altitude: float,
                linear_velocity: Vector3,
                angular_velocity: Vector3,
                linear_acceleration: Vector3,
                compass: float,
                orientation: Orientation,
            }
        """
        (pos, lv, av, la, comp, orient) = await asyncio.gather(
            self.get_position(extra=extra, timeout=timeout),
            self.get_linear_velocity(extra=extra, timeout=timeout),
            self.get_angular_velocity(extra=extra, timeout=timeout),
            self.get_linear_acceleration(extra=extra, timeout=timeout),
            self.get_compass_heading(extra=extra, timeout=timeout),
            self.get_orientation(extra=extra, timeout=timeout),
            return_exceptions=True,
        )

        readings = {}

        # Add returned value to the readings dictionary if value is of expected type; omit if unimplemented.
        def add_reading(name: str, reading, returntype: List) -> None:
            possible_error_types = (NotImplementedError, MethodNotImplementedError, NotSupportedError)
            if type(reading) in returntype:
                if name == "position":
                    readings["position"] = reading[0]
                    readings["altitude"] = reading[1]
                else:
                    readings[name] = reading
                return
            elif isinstance(reading, possible_error_types) or (isinstance(reading, GRPCError) and "Unimplemented" in str(reading.message)):
                return
            raise reading

        add_reading("position", pos, [tuple])
        add_reading("linear_velocity", lv, [Vector3])
        add_reading("angular_velocity", av, [Vector3])
        add_reading("linear_acceleration", la, [Vector3])
        add_reading("compass", comp, [float, int])
        add_reading("orientation", orient, [Orientation])

        return readings
