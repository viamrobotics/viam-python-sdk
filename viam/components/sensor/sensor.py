import abc
from typing import Any, List

from ..component_base import ComponentBase


class SensorBase(ComponentBase):
    """
    Abstract sensing device that can provide measurement readings

    If you override the init function,
    you must call the super init function.
    """

    @abc.abstractmethod
    async def get_readings(self) -> List[Any]:
        """
        Obtain the measurements/data specific to this sensor

        Returns:
            List[Dict]: The measurements. Can be of any type
        """
        ...
