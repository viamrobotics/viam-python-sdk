from typing import Any, List
from grpclib.client import Channel
from viam.proto.api.component.sensor import (
    SensorServiceStub,
    GetReadingsRequest, GetReadingsResponse
)
from viam.utils import value_to_primitive

from .sensor import SensorBase


class SensorClient(SensorBase):
    """
    gRPC client for the Sensor component.
    """

    def __init__(self, name: str, channel: Channel):
        self.client = SensorServiceStub(channel)
        super().__init__(name)

    async def get_readings(self) -> List[Any]:
        request = GetReadingsRequest(name=self.name)
        response: GetReadingsResponse = await self.client.GetReadings(request)
        return [value_to_primitive(reading) for reading in response.readings]
