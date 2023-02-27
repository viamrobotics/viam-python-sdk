from grpclib.server import Stream

from viam.components.service_base import ComponentServiceBase
from viam.errors import ResourceNotFoundError
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.sensor import (
    GetReadingsRequest,
    GetReadingsResponse,
    SensorServiceBase,
)
from viam.utils import sensor_readings_native_to_value, struct_to_dict, dict_to_struct

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
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        readings = await sensor.get_readings(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetReadingsResponse(readings=sensor_readings_native_to_value(readings))
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        try:
            sensor = self.get_component(request.name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await sensor.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
