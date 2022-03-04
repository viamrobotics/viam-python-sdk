from typing import List

from google.protobuf.struct_pb2 import Value
from grpclib.server import Stream

from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.sensor import (
    SensorServiceBase,
    GetReadingsRequest, GetReadingsResponse,
)
from viam.utils import new_value

from .sensor import Sensor


class SensorService(SensorServiceBase, ComponentServiceBase[Sensor]):
    """
    gRPC Service for a generic Sensor
    """

    RESOURCE_TYPE = Sensor

    async def GetReadings(
        self,
        stream: Stream[GetReadingsRequest, GetReadingsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            sensor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        readings = await sensor.get_readings()
        v_readings: List[Value] = []
        for r in readings:
            v = new_value(r)
            v_readings.append(v)
        response = GetReadingsResponse(readings=v_readings)
        await stream.send_message(response)
