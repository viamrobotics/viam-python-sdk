import abc
from typing import Any, Mapping

from ..component_base import ComponentBase


class Sensor(ComponentBase):
    """
    Sensor represents a physical sensing device that can provide measurement readings.

    This acts as an abstract base class for any drivers representing specific
    sensor implementations. This cannot be used on its own. If the `__init__()` function is
    overridden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def get_readings(self, **kwargs) -> Mapping[str, Any]:
        """
        Obtain the measurements/data specific to this sensor.

        Returns:
            Mapping[str, Any]: The measurements. Can be of any type.
        """
        ...
