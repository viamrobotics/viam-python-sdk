from typing import Any, List, Mapping

from grpclib.client import Channel

from viam.proto.api.common import GeoPoint, Orientation, ResourceName, Vector3
from viam.proto.api.service.sensors import (
    GetReadingsRequest,
    GetReadingsResponse,
    GetSensorsRequest,
    GetSensorsResponse,
    SensorsServiceStub,
)
from viam.utils import value_to_primitive


class SensorsServiceClient:
    """Connect to the SensorService, which centralizes all Sensors in a single place"""

    def __init__(self, channel: Channel):
        self.client = SensorsServiceStub(channel)

    def _dict_to_proto(self, value: Mapping[str, Any]) -> Any:
        kind = value.get("_type", "")
        if kind == "angular_velocity":
            return Vector3(x=value["x"], y=value["y"], z=value["z"])
        if kind == "vector3":
            return Vector3(x=value["x"], y=value["y"], z=value["z"])
        if kind == "geopoint":
            return GeoPoint(latitude=value["lat"], longitude=value["lng"])
        if kind == "orientation_vector_degrees":
            return Orientation(o_x=value["ox"], o_y=value["oy"], o_z=value["oz"], theta=value["theta"])
        return value

    async def get_sensors(self) -> List[ResourceName]:
        """Get the `ResourceName`s of all the `Sensor`s conneted to this Robot

        Returns:
            List[ResourceName]: The list of all Sensors
        """
        request = GetSensorsRequest()
        response: GetSensorsResponse = await self.client.GetSensors(request)
        return list(response.sensor_names)

    async def get_readings(self, sensors: List[ResourceName]) -> Mapping[ResourceName, Mapping[str, Any]]:
        """Get the readings from the specific sensors provided

        Args:
            sensors (List[ResourceName]): The `ResourceName`s of the the `Sensor`s to get readings from

        Returns:
            Mapping[ResourceName, Mapping[str, Any]]: The readings from the sensors, mapped by `ResourceName`
        """
        request = GetReadingsRequest(sensor_names=sensors)
        response: GetReadingsResponse = await self.client.GetReadings(request)
        return {
            reading.name: {
                key: (
                    self._dict_to_proto(value_to_primitive(value))
                    if isinstance(value_to_primitive(value), Mapping)
                    else value_to_primitive(value)
                )
                for (key, value) in reading.readings.items()
            }
            for reading in response.readings
        }
