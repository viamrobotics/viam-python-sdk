from typing import Any, Dict, List

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.api.component.sensor import (GetReadingsRequest,
                                             GetReadingsResponse,
                                             SensorServiceStub)
from viam.utils import value_to_primitive

from .sensor import Sensor


class SensorClient(Sensor):
    """
    gRPC client for the Sensor component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = SensorServiceStub(channel)
        super().__init__(name)

    async def get_readings(self) -> List[Any]:
        request = GetReadingsRequest(name=self.name)
        response: GetReadingsResponse = await self.client.GetReadings(request)
        return [value_to_primitive(reading) for reading in response.readings]

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
