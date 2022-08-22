from grpclib.server import Stream

from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.sensor import (
    GetReadingsRequest,
    GetReadingsResponse,
    SensorServiceBase,
)
from viam.utils import primitive_to_value

from .sensor import Sensor


class SensorService(SensorServiceBase, ComponentServiceBase[Sensor]):
    """
    gRPC Service for a generic Sensor
    """

    RESOURCE_TYPE = Sensor

    async def GetReadings(self, stream: Stream[GetReadingsRequest, GetReadingsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        readings = await sensor.get_readings()
        response = GetReadingsResponse(readings={key: primitive_to_value(value) for (key, value) in readings.items()})
        await stream.send_message(response)
