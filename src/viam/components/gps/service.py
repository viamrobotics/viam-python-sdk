from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.common import GeoPoint
from viam.proto.api.component.gps import (GPSServiceBase, ReadAltitudeRequest,
                                          ReadAltitudeResponse,
                                          ReadLocationRequest,
                                          ReadLocationResponse,
                                          ReadSpeedRequest, ReadSpeedResponse)

from .gps import GPS


class GPSService(GPSServiceBase, ComponentServiceBase[GPS]):
    """
    gRPC Service for a GPS
    """

    RESOURCE_TYPE = GPS

    async def ReadLocation(
        self,
        stream: Stream[ReadLocationRequest, ReadLocationResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gps = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        loc = await gps.read_location()
        point = GeoPoint(latitude=loc.lat, longitude=loc.lng)
        response = ReadLocationResponse(coordinate=point)
        await stream.send_message(response)

    async def ReadAltitude(
        self,
        stream: Stream[ReadAltitudeRequest, ReadAltitudeResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gps = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        alt = await gps.read_altitude()
        response = ReadAltitudeResponse(altitude_meters=alt)
        await stream.send_message(response)

    async def ReadSpeed(
        self,
        stream: Stream[ReadSpeedRequest, ReadSpeedResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gps = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        speed = await gps.read_speed()
        response = ReadSpeedResponse(speed_mm_per_sec=speed)
        await stream.send_message(response)
