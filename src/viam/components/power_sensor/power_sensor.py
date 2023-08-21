import abc
import asyncio
from typing import Any, Dict, Final, List, Mapping, Optional, Tuple

from grpclib import GRPCError

from viam.components.component_base import ComponentBase
from viam.errors import MethodNotImplementedError, NotSupportedError
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype


class PowerSensor(ComponentBase):
    """PowerSensor reports information about voltage, current and power.

    This acts as an abstract base class for any sensors that can provide data regarding voltage, current and/or power.
    This cannot be used on its own. If the ``__init__()`` function is overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "power_sensor")

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

    async def get_readings(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Mapping[str, Any]:
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
        (vol, cur, pow) = await asyncio.gather(
            self.get_voltage(extra=extra, timeout=timeout),
            self.get_current(extra=extra, timeout=timeout),
            self.get_power(extra=extra, timeout=timeout),
            return_exceptions=True,
        )

        readings = {}

        # Add returned value to the readings dictionary if value is of expected type; omit if unimplemented.
        def add_reading(name: str, reading, returntype: List) -> None:
            possible_error_types = (NotImplementedError, MethodNotImplementedError, NotSupportedError)
            if type(reading) in returntype:
                if name == "voltage":
                    readings["voltage"] = reading[0]
                    readings["is_ac"] = reading[1]
                elif name == "current":
                    readings["current"] = reading[0]
                    readings["is_ac"] = reading[1]
                else:
                    readings[name] = reading
                return
            elif isinstance(reading, possible_error_types) or (isinstance(reading, GRPCError) and "Unimplemented" in str(reading.message)):
                return
            raise reading

        add_reading("voltage", vol, [tuple])
        add_reading("current", cur, [tuple])
        add_reading("power", pow, [float])

        return readings
