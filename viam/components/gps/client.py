from grpclib.client import Channel
from viam.proto.api.common import GeoPoint
from viam.proto.api.component.gps import (GPSServiceStub, ReadAltitudeRequest,
                                          ReadAltitudeResponse,
                                          ReadLocationRequest,
                                          ReadLocationResponse,
                                          ReadSpeedRequest, ReadSpeedResponse)

from .gps import GPS


class GPSClient(GPS):
    """
    gRPC client for the GPS component.
    """

    def __init__(self, name: str, channel: Channel):
        self.client = GPSServiceStub(channel)
        super().__init__(name)

    async def read_location(self) -> GPS.Point:
        request = ReadLocationRequest(name=self.name)
        response: ReadLocationResponse = \
            await self.client.ReadLocation(request)
        coordinate: GeoPoint = response.coordinate
        return GPS.Point(coordinate.latitude, coordinate.longitude)

    async def read_altitude(self) -> float:
        request = ReadAltitudeRequest(name=self.name)
        response: ReadAltitudeResponse = \
            await self.client.ReadAltitude(request)
        return response.altitude_meters

    async def read_speed(self) -> float:
        request = ReadSpeedRequest(name=self.name)
        response: ReadSpeedResponse = await self.client.ReadSpeed(request)
        return response.speed_mm_per_sec
