from typing import Any, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import ResourceName
from viam.proto.service.sensors import (
    GetReadingsRequest,
    GetReadingsResponse,
    GetSensorsRequest,
    GetSensorsResponse,
    SensorsServiceStub,
)
from viam.utils import dict_to_struct, sensor_readings_value_to_native
from viam.services.service_client_base import ServiceClientBase


class SensorsServiceClient(ServiceClientBase):
    """Connect to the SensorService, which centralizes all Sensors in a single place"""

    SERVICE_TYPE = "sensors"

    def __init__(self, name: str, channel: Channel):
        self.client = SensorsServiceStub(channel)
        self.name = name

    async def get_sensors(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None) -> List[ResourceName]:
        """Get the `ResourceName`s of all the `Sensor`s connected to this Robot

        Returns:
            List[ResourceName]: The list of all Sensors
        """
        if extra is None:
            extra = {}
        request = GetSensorsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetSensorsResponse = await self.client.GetSensors(request, timeout=timeout)
        return list(response.sensor_names)

    async def get_readings(
        self, sensors: List[ResourceName], *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> Mapping[ResourceName, Mapping[str, Any]]:
        """Get the readings from the specific sensors provided

        Args:
            sensors (List[ResourceName]): The `ResourceName`s of the the `Sensor`s to get readings from

        Returns:
            Mapping[ResourceName, Mapping[str, Any]]: The readings from the sensors, mapped by `ResourceName`
        """
        if extra is None:
            extra = {}
        request = GetReadingsRequest(name=self.name, sensor_names=sensors, extra=dict_to_struct(extra))
        response: GetReadingsResponse = await self.client.GetReadings(request, timeout=timeout)
        return {reading.name: sensor_readings_value_to_native(reading.readings) for reading in response.readings}
