import abc

from collections import namedtuple
from typing import Tuple
from viam.components.component_base import ComponentBase


class GPS(ComponentBase):
    """
    GPS represents a GPS unit that can report latitude/longitude, altitude, and speed measurements.

    This acts as an abstract base class for any drivers representing specific 
    GPS implementations. This cannot be used on its own. If the `__init__()` function is
    overriden, it must call the `super().__init__()` function.
    """

    Point = namedtuple('Point', ['lat', 'lng'])

    @abc.abstractmethod
    async def read_location(self) -> Point:
        """
        Get the current latitude and longitude.

        Returns:
            Point: The current lat/long.
        """
        ...

    @abc.abstractmethod
    async def read_altitude(self) -> float:
        """
        Get the current altitude.

        Returns:
            float: The current altitude in meters.
        """
        ...

    @abc.abstractmethod
    async def read_speed(self) -> float:
        """
        Get the current ground speed in millimeters per second.

        Returns:
            float: The speed in mm/sec.
        """
        ...


class LocalGPS(GPS):
    """
    LocalGPS represents a GPS that can report accuracy,
    satellites, and valid measurements in addition to the standard
    GPS measurements of latitude/longitude, altitude, and speed.
    """

    @abc.abstractmethod
    async def read_accuracy(self) -> Tuple[float, float]:
        """
        Get the horizontal and vertical position error in meters.

        Returns:
            Tuple[float, float]: Horizontal and vertical position errors,
                in meters.
        """
        ...

    @abc.abstractmethod
    async def read_satellites(self) -> Tuple[int, int]:
        """
        Get the number of satellites used for the location fix and the total satellites in view.

        Returns:
            Tuple[int, int]: The number of satellites used for the location fix
                and the total number of satellites in view.
        """
        ...

    @abc.abstractmethod
    async def read_valid(self) -> bool:
        """
        Get whether or not the GPS had a valid location fix for the most recent dataset.

        Returns:
            bool: If the location fix is valid.
        """
        ...
