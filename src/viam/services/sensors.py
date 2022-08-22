from grpclib.client import Channel
from viam.proto.api.service.sensors import (
    SensorsServiceStub,
    GetReadingsRequest,
    GetReadingsResponse,
    GetSensorsRequest,
    GetSensorsResponse,
    Readings,
)
from viam.proto.api.common import ResourceName
from typing import List


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

    async def get_readings(self, sensors: List[ResourceName]) -> List[Readings]:
        """Get the `Readings` from the specific sensors provided

        Args:
            sensors (List[ResourceName]): The `ResourceName`s of the the `Sensor`s to get readings from

        Returns:
            List[Readings]: The `Readings` from the sensors
        """
        request = GetReadingsRequest(sensor_names=sensors)
        response: GetReadingsResponse = await self.client.GetReadings(request)
        return list(response.readings)
