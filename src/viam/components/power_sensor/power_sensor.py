import abc
from typing import Any, Dict, Final, Mapping, Optional, Tuple

from viam.components.component_base import ComponentBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype
from viam.utils import SensorReading


class PowerSensor(ComponentBase):
    """PowerSensor reports information about voltage, current and power.

    This acts as an abstract base class for any sensors that can provide data regarding voltage, current and/or power.
    This cannot be used on its own. If the ``__init__()`` function is overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "power_sensor"
    )

    @abc.abstractmethod
    async def get_voltage(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Tuple[float, bool]:
        """Get the voltage reading and bool IsAC

        Returns:
            Tuple[float, bool]: voltage (volts) and bool IsAC
        """
        ...

    @abc.abstractmethod
    async def get_current(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Tuple[float, bool]:
        """Get the current reading and bool IsAC

        Returns:
            Tuple[float, bool]: current (amperes) and bool IsAC
        """
        ...

    @abc.abstractmethod
    async def get_power(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
        """Get the power reading in watts

        Returns:
            float: power in watts
        """
        ...

    async def get_readings(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, SensorReading]:
        """Obtain the measurements/data specific to this sensor.
        If a sensor is not configured to have a measurement or fails to read a piece of data, it will not appear in the readings dictionary.

        Returns:
            Mapping[str, Any]: The readings for the PowerSensor:
            {
               voltage: float
               current: float
               is_ac: bool
               power: float
            }

        """
        ...
