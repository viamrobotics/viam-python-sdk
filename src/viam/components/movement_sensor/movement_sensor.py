import abc
import sys
from dataclasses import dataclass
from typing import Any, Dict, Final, Mapping, Optional, Tuple

from typing_extensions import Self

from viam.components.component_base import ComponentBase
from viam.proto.component.movementsensor import GetAccuracyResponse, GetPropertiesResponse
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype
from viam.utils import SensorReading

from . import GeoPoint, Orientation, Vector3

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


class MovementSensor(ComponentBase):
    """MovementSensor reports information about the robot's direction, position and speed.

    This acts as an abstract base class for any sensors that can provide data regarding the robot's direction, position, and speed.
    This cannot be used on its own. If the ``__init__()`` function is overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "movement_sensor"
    )

    Accuracy: "TypeAlias" = GetAccuracyResponse

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
    async def get_accuracy(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Accuracy:
        """Get the accuracy of the various sensors

        Returns:
            MovementSensor.Accuracy: The accuracies of the movement sensor
        """
        ...

    async def get_readings(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, SensorReading]:
        """Obtain the measurements/data specific to this sensor.
        If a sensor is not configured to have a measurement or fails to read a piece of data, it will not appear in the readings dictionary.

        Returns:
            Mapping[str, Any]: The readings for the MovementSensor. Can be of any type.

        """
        ...
