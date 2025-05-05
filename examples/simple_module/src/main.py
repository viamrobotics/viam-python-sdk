import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional, Sequence

from typing_extensions import Self

from viam.components.sensor import Sensor
from viam.logging import getLogger
from viam.module.module import Module
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily
from viam.utils import SensorReading, ValueTypes

LOGGER = getLogger(__name__)


class MySensor(Sensor):
    # Subclass the Viam Sensor component and implement the required functions
    MODEL: ClassVar[Model] = Model(ModelFamily("viam", "sensor"), "mysensor")

    def __init__(self, name: str):
        super().__init__(name)

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        sensor = cls(config.name)
        sensor.reconfigure(config, dependencies)
        return sensor

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> (Sequence[str], Sequence[str]):
        if "multiplier" in config.attributes.fields:
            if not config.attributes.fields["multiplier"].HasField("number_value"):
                raise Exception("Multiplier must be a float.")
            multiplier = config.attributes.fields["multiplier"].number_value
            if multiplier == 0:
                raise Exception("Multiplier cannot be 0.")
        return [], []

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, SensorReading]:
        return {"signal": 1 * self.multiplier}

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        LOGGER.info(f"received {command=}.")
        return command

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
    """This function creates and starts a new module, after adding all desired resource models.
    Resource creators must be registered to the resource registry before the module adds the resource model.
    """
    Registry.register_resource_creator(Sensor.API, MySensor.MODEL, ResourceCreatorRegistration(MySensor.new, MySensor.validate_config))

    module = Module.from_args()
    module.add_model_from_registry(Sensor.API, MySensor.MODEL)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())
