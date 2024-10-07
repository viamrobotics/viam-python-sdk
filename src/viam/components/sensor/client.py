from typing import Any, Dict, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry, GetReadingsRequest, GetReadingsResponse
from viam.proto.component.sensor import SensorServiceStub
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import SensorReading, ValueTypes, dict_to_struct, get_geometries, sensor_readings_value_to_native, struct_to_dict

from .sensor import Sensor


class SensorClient(Sensor, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the Sensor component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = SensorServiceStub(channel)
        super().__init__(name)

    async def get_readings(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, SensorReading]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetReadingsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetReadingsResponse = await self.client.GetReadings(request, timeout=timeout, metadata=md)
        return sensor_readings_value_to_native(response.readings)

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[Geometry]:
        md = kwargs.get("metadata", self.Metadata())
        return await get_geometries(self.client, self.name, extra, timeout, md)
