import abc
from typing import Any, List

from ..component_base import ComponentBase


class Sensor(ComponentBase):
    """
    Sensor represents a physical sensing device that can provide measurement readings.

    This acts as an abstract base class for any drivers representing specific
    sensor implementations. This cannot be used on its own. If the `__init__()` function is
    overriden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def get_readings(self) -> List[Any]:
        """
        Obtain the measurements/data specific to this sensor.

        Returns:
            List[Dict]: The measurements. Can be of any type.
        """
        ...
