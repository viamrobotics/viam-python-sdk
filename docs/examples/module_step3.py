# wifi-sensor/src/wifi_sensor_module.py
import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional

from typing_extensions import Self

from viam.components.sensor import Sensor
from viam.logging import getLogger
from viam.module.module import Module
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily
from viam.utils import ValueTypes

LOGGER = getLogger(__name__)


class MySensor(Sensor):
    # Subclass the Viam Sensor component and implement the required functions
    MODEL: ClassVar[Model] = Model(ModelFamily("viam", "sensor"), "linux-wifi")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        sensor = cls(config.name)
        return sensor

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, ValueTypes]:
        with open("/proc/net/wireless") as wifi_stats:
            content = wifi_stats.readlines()
        wifi_signal = [x for x in content[2].split(" ") if x != ""]
        return {"link": wifi_signal[2], "level": wifi_signal[3], "noise": wifi_signal[4]}

    async def close(self):
        # This is a completely optional function to include. This will be called when the resource is removed from the config or the module
        # is shutting down.
        LOGGER.info(f"{self.name} is closed.")


async def main():
    """
    This function creates and starts a new module, after adding all desired resource model.
    Resource creators must be registered to the resource registry before the module adds the resource model.
    """
    Registry.register_resource_creator(Sensor.SUBTYPE, MySensor.MODEL, ResourceCreatorRegistration(MySensor.new))

    module = Module.from_args()
    module.add_model_from_registry(Sensor.SUBTYPE, MySensor.MODEL)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())
