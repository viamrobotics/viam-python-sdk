import abc
from typing import Any, Dict, Final, Mapping, Optional, Tuple, TypeAlias

from viam.components.component_base import ComponentBase
from viam.proto.component.powersensor import GetPropertiesResponse
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT
from viam.utils import SensorReading


class PowerSensor(ComponentBase):
    """PowerSensor reports information about voltage, current and power.

    This acts as an abstract base class for any sensors that can provide data regarding voltage, current and/or power.
    This cannot be used on its own. If the ``__init__()`` function is overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.power_sensor import PowerSensor

    For more information, see `Power Sensor component <https://docs.viam.com/reference/apis/components/power-sensor/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "power_sensor"
    )

    Properties: "TypeAlias" = GetPropertiesResponse

    @abc.abstractmethod
    async def get_voltage(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Tuple[float, bool]:
        """Return the voltage reading of a specified device and whether it is AC or DC.

        ::

            my_power_sensor = PowerSensor.from_robot(robot=machine, name='my_power_sensor')

            # Get the voltage reading from the power sensor
            voltage, is_ac = await my_power_sensor.get_voltage()
            print("The voltage is", voltage, "V, Is AC:", is_ac)

        Returns:
            Tuple[float, bool]: A float representing the voltage reading in V. A bool indicating whether the voltage is AC (`true`) or DC
            (`false`).

        For more information, see `Power Sensor component <https://docs.viam.com/reference/apis/components/power-sensor/#getvoltage>`_.
        """
        ...

    @abc.abstractmethod
    async def get_current(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Tuple[float, bool]:
        """Return the current of a specified device and whether it is AC or DC.

        ::

            my_power_sensor = PowerSensor.from_robot(robot=machine, name='my_power_sensor')

            # Get the current reading from the power sensor
            current, is_ac = await my_power_sensor.get_current()
            print("The current is ", current, " A, Is AC: ", is_ac)

        Returns:
            Tuple[float, bool]: A tuple which includes a float representing the current reading in amps, and a bool indicating whether the
            current is AC (`true`) or DC (`false`).

        For more information, see `Power Sensor component <https://docs.viam.com/reference/apis/components/power-sensor/#getcurrent>`_.
        """
        ...

    @abc.abstractmethod
    async def get_power(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
        """Return the power reading in watts.

        ::

            my_power_sensor = PowerSensor.from_robot(robot=machine, name='my_power_sensor')

            # Get the power reading from the power sensor
            power = await my_power_sensor.get_power()
            print("The power is", power, "Watts")

        Returns:
            float: The power reading in watts.

        For more information, see `Power Sensor component <https://docs.viam.com/reference/apis/components/power-sensor/#getpower>`_.
        """
        ...

    async def get_readings(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, SensorReading]:
        """Get the measurements or readings that this power sensor provides. If a sensor is not configured correctly or fails to read a
        piece of data, it will not appear in the readings dictionary.

        ::

            my_power_sensor = PowerSensor.from_robot(robot=machine, name='my_power_sensor')

            # Get the readings provided by the sensor.
            readings = await my_power_sensor.get_readings()

        Returns:
            Mapping[str, Any]: The readings for the PowerSensor. Can be of any type. Includes voltage in volts (float), current in
            amperes (float), is_ac (bool), and power in watts (float).

        For more information, see `Power Sensor component <https://docs.viam.com/reference/apis/components/power-sensor/#getreadings>`_.
        """
        ...

    @abc.abstractmethod
    async def get_battery_percent(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
        """Return the remaining battery charge, from 0 to 100.

        ::

            my_power_sensor = PowerSensor.from_robot(robot=machine, name='my_power_sensor')

            # Get the remaining battery charge from the power sensor
            percent = await my_power_sensor.get_battery_percent()
            print("The battery charge remaining is", percent, "%")

        Returns:
            float: The remaining battery charge, from 0 to 100.

        For more information, see `Power Sensor component
        <https://docs.viam.com/reference/apis/components/power-sensor/#getbatterypercent>`_.
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Properties:
        """Return a dictionary of the optional methods this power sensor supports.

        ::

            my_power_sensor = PowerSensor.from_robot(robot=machine, name='my_power_sensor')

            # Get whether the power sensor supports GetBatteryPercent.
            properties = await my_power_sensor.get_properties()

        Returns:
            PowerSensor.Properties: Map of optional properties to supported status.

        For more information, see `Power Sensor component
        <https://docs.viam.com/reference/apis/components/power-sensor/#getproperties>`_.
        """
        ...
