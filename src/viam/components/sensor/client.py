from typing import Any, Dict, Mapping

from grpclib.client import Channel

from viam.components.generic.client import do_command
from viam.proto.component.sensor import (
    GetReadingsRequest,
    GetReadingsResponse,
    SensorServiceStub,
)
from viam.utils import sensor_readings_value_to_native

from .sensor import Sensor


class SensorClient(Sensor):
    """
    gRPC client for the Sensor component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = SensorServiceStub(channel)
        super().__init__(name)

    async def get_readings(self) -> Mapping[str, Any]:
        request = GetReadingsRequest(name=self.name)
        response: GetReadingsResponse = await self.client.GetReadings(request)
        return sensor_readings_value_to_native(response.readings)

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
