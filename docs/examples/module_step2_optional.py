# wifi-sensor/src/wifi_sensor_module.py
import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional, Sequence

from typing_extensions import Self

from viam.components.sensor import Sensor
from viam.logging import getLogger
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily

LOGGER = getLogger(__name__)


class MySensor(Sensor):
    # Subclass the Viam Sensor component and implement the required functions
    MODEL: ClassVar[Model] = Model(ModelFamily("viam", "sensor"), "linux-wifi")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        sensor = cls(config.name)
        sensor.reconfigure(config, dependencies)
        return sensor

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        if "multiplier" in config.attributes.fields:
            if not config.attributes.fields["multiplier"].HasField("number_value"):
                raise Exception("Multiplier must be a float.")
            multiplier = config.attributes.fields["multiplier"].number_value
            if multiplier == 0:
                raise Exception("Multiplier cannot be 0.")
        return []

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        with open("/proc/net/wireless") as wifi_stats:
            content = wifi_stats.readlines()
        result = [x for x in content[2].split(" ") if x != ""]

        wifi_signal = []
        for i in range(2, 5):
            wifi_signal.append(int(result[i]) * self.multiplier)
        return {"link": wifi_signal[0], "level": wifi_signal[1], "noise": wifi_signal[2]}

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        if "multiplier" in config.attributes.fields:
            multiplier = config.attributes.fields["multiplier"].number_value
        else:
            multiplier = 1.0
        self.multiplier = multiplier

    async def close(self):
        # This is a completely optional function to include. This will be called when the resource is removed from the config or the module
        # is shutting down.
        LOGGER.info(f"{self.name} is closed.")


async def main():
    Registry.register_resource_creator(Sensor.SUBTYPE, MySensor.MODEL, ResourceCreatorRegistration(MySensor.new, MySensor.validate_config))


if __name__ == "__main__":
    asyncio.run(main())
