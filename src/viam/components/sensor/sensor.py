import abc
from typing import Any, Final, Mapping, Optional

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype
from viam.utils import SensorReading

from ..component_base import ComponentBase


class Sensor(ComponentBase):
    """
    Sensor represents a physical sensing device that can provide measurement readings.

    This acts as an abstract base class for any drivers representing specific
    sensor implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "sensor"
    )

    @abc.abstractmethod
    async def get_readings(
        self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, SensorReading]:
        """
        Obtain the measurements/data specific to this sensor.

        Returns:
            Mapping[str, Any]: The measurements. Can be of any type.
        """
        ...
