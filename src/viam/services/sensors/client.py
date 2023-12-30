from typing import Any, Final, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, ResourceName
from viam.proto.service.sensors import GetReadingsRequest, GetReadingsResponse, GetSensorsRequest, GetSensorsResponse, SensorsServiceStub
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_client_base import ServiceClientBase
from viam.utils import SensorReading, ValueTypes, dict_to_struct, sensor_readings_value_to_native, struct_to_dict


class SensorsClient(ServiceClientBase, ReconfigurableResourceRPCClientBase):
    """Connect to the SensorService, which centralizes all Sensors in a single place"""

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "sensors"
    )
    client: SensorsServiceStub

    def __init__(self, name: str, channel: Channel):
        super().__init__(name, channel)
        self.client = SensorsServiceStub(channel)

    async def get_sensors(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None) -> List[ResourceName]:
        """Get the ``ResourceName`` of all the ``Sensor`` resources connected to this Robot

        Returns:
            List[viam.proto.common.ResourceName]: The list of all Sensors
        """
        if extra is None:
            extra = {}
        request = GetSensorsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetSensorsResponse = await self.client.GetSensors(request, timeout=timeout)
        return list(response.sensor_names)

    async def get_readings(
        self, sensors: List[ResourceName], *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> Mapping[ResourceName, Mapping[str, SensorReading]]:
        """Get the readings from the specific sensors provided

        Args:
            sensors (List[viam.proto.common.ResourceName]): The ``ResourceName`` of the the ``Sensor`` resources to get readings from

        Returns:
            Mapping[viam.proto.common.ResourceName, Mapping[str, Any]]: The readings from the sensors, mapped by ``ResourceName``
        """
        if extra is None:
            extra = {}
        request = GetReadingsRequest(name=self.name, sensor_names=sensors, extra=dict_to_struct(extra))
        response: GetReadingsResponse = await self.client.GetReadings(request, timeout=timeout)
        return {reading.name: sensor_readings_value_to_native(reading.readings) for reading in response.readings}

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **__) -> Mapping[str, ValueTypes]:
        """Send/receive arbitrary commands

        Args:
            command (Dict[str, ValueTypes]): The command to execute

        Returns:
            Dict[str, ValueTypes]: Result of the executed command
        """
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
