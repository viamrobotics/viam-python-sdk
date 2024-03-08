import abc
from typing import Any, Dict, Final, Mapping, Optional, Tuple

from viam.components.component_base import ComponentBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype
from viam.utils import SensorReading


class PowerSensor(ComponentBase):
    """PowerSensor reports information about voltage, current and power.

    This acts as an abstract base class for any sensors that can provide data regarding voltage, current and/or power.
    This cannot be used on its own. If the ``__init__()`` function is overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.power_sensor import PowerSensor
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "power_sensor"
    )

    @abc.abstractmethod
    async def get_voltage(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Tuple[float, bool]:
        """Get the voltage reading and bool IsAC

        ::

            my_power_sensor = PowerSensor.from_robot(robot=robot, name='my_power_sensor')

            # Get the voltage reading from the power sensor
            voltage, is_ac = await my_power_sensor.get_voltage()
            print("The voltage is", voltage, "V, Is AC:", is_ac)

        Returns:
            Tuple[float, bool]: voltage (volts) and bool IsAC
        """
        ...

    @abc.abstractmethod
    async def get_current(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Tuple[float, bool]:
        """Get the current reading and bool IsAC

        ::

            my_power_sensor = PowerSensor.from_robot(robot=robot, name='my_power_sensor')

            # Get the current reading from the power sensor
            current, is_ac = await my_power_sensor.get_current()
            print("The current is ", current, " A, Is AC: ", is_ac)

        Returns:
            Tuple[float, bool]: current (amperes) and bool IsAC
        """
        ...

    @abc.abstractmethod
    async def get_power(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
        """Get the power reading in watts

        ::

            my_power_sensor = PowerSensor.from_robot(robot=robot, name='my_power_sensor')

            # Get the power reading from the power sensor
            power = await my_power_sensor.get_power()
            print("The power is", power, "Watts")

        Returns:
            float: power in watts
        """
        ...

    async def get_readings(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, SensorReading]:
        """Obtain the measurements/data specific to this sensor.
        If a sensor is not configured to have a measurement or fails to read a piece of data, it will not appear in the readings dictionary.

        ::

            my_power_sensor = PowerSensor.from_robot(robot=robot, name='my_power_sensor')

            # Get the readings provided by the sensor.
            readings = await my_power_sensor.get_readings()

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
