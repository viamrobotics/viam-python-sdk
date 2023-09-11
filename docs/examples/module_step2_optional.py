# wifi-sensor/src/wifi_sensor_module.py
import asyncio
from typing import Any, ClassVar, Dict, List, Mapping, Optional, Sequence
from typing_extensions import Self

from viam.components.sensor import Geometry, Sensor
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily


class MySensor(Sensor):
    # Subclass the Viam Sensor component and implement the required functions
    MODEL: ClassVar[Model] = Model(ModelFamily("acme", "wifi_sensor"), "linux")
    multiplier: float

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        sensor = cls(config.name)
        return sensor

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        if "multiplier" in config.attributes.fields:
            if not isinstance(config.attributes.fields["multiplier"], float):
                raise Exception("Multiplier must be a float.")
            cls.multiplier = config.attributes.fields["multiplier"].number_value
            if cls.multiplier == 0:
                raise Exception("Multiplier cannot be 0.")
        else:
            cls.multiplier = 1.0
        return []

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        with open("/proc/net/wireless") as wifi_stats:
            content = wifi_stats.readlines()
        result = [x for x in content[2].split(" ") if x != ""]

        wifi_signal = []
        for i in range(2, 5):
            wifi_signal.append(int(result[i]) * self.multiplier)
        return {"link": wifi_signal[0], "level": wifi_signal[1], "noise": wifi_signal[2]}

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        raise NotImplementedError

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.multiplier = config.attributes.fields["multiplier"].number_value


async def main():
    Registry.register_resource_creator(Sensor.SUBTYPE, MySensor.MODEL, ResourceCreatorRegistration(MySensor.new, MySensor.validate_config))


if __name__ == "__main__":
    asyncio.run(main())
