from typing import Any, List, Mapping

from grpclib.client import Channel

from viam.proto.api.common import ResourceName
from viam.proto.api.service.sensors import (
    GetReadingsRequest,
    GetReadingsResponse,
    GetSensorsRequest,
    GetSensorsResponse,
    SensorsServiceStub,
)
from viam.utils import sensor_readings_value_to_native


class SensorsServiceClient:
    """Connect to the SensorService, which centralizes all Sensors in a single place"""

    def __init__(self, channel: Channel):
        self.client = SensorsServiceStub(channel)

    async def get_sensors(self) -> List[ResourceName]:
        """Get the `ResourceName`s of all the `Sensor`s conneted to this Robot

        Returns:
            List[ResourceName]: The list of all Sensors
        """
        request = GetSensorsRequest()
        response: GetSensorsResponse = await self.client.GetSensors(request)
        return list(response.sensor_names)

    async def get_readings(self, sensors: List[ResourceName]) -> Mapping[ResourceName, Mapping[str, Any]]:
        """Get the readings from the specific sensors provided

        Args:
            sensors (List[ResourceName]): The `ResourceName`s of the the `Sensor`s to get readings from

        Returns:
            Mapping[ResourceName, Mapping[str, Any]]: The readings from the sensors, mapped by `ResourceName`
        """
        request = GetReadingsRequest(sensor_names=sensors)
        response: GetReadingsResponse = await self.client.GetReadings(request)
        return {reading.name: sensor_readings_value_to_native(reading.readings) for reading in response.readings}
