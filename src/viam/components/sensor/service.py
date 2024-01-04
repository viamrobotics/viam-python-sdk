from grpclib.server import Stream

from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GetGeometriesRequest,
    GetGeometriesResponse,
    GetReadingsRequest,
    GetReadingsResponse,
)
from viam.proto.component.sensor import SensorServiceBase
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, sensor_readings_native_to_value, struct_to_dict

from .sensor import Sensor


class SensorRPCService(SensorServiceBase, ResourceRPCServiceBase[Sensor]):
    """
    gRPC Service for a generic Sensor
    """

    RESOURCE_TYPE = Sensor

    async def GetReadings(self, stream: Stream[GetReadingsRequest, GetReadingsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        sensor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        readings = await sensor.get_readings(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetReadingsResponse(readings=sensor_readings_native_to_value(readings))
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        sensor = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await sensor.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        sensor = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await sensor.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)
