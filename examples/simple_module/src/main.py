import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional, Sequence

from typing_extensions import Self

from viam.components.sensor import Sensor
from viam.module.module import Module
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily
from viam.utils import ValueTypes


class MySensor(Sensor):
    # Subclass the Viam Sensor component and implement the required functions
    MODEL: ClassVar[Model] = Model(ModelFamily("viam", "sensor"), "mysensor")
    multiplier: float

    def __init__(self, name: str):
        super().__init__(name)

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
        return [""]

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        return {"signal": 1 * self.multiplier}

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return command

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.multiplier = config.attributes.fields["multiplier"].number_value


async def main():
    """This function creates and starts a new module, after adding all desired resource models.
    Resource creators must be registered to the resource registry before the module adds the resource model.
    """
    Registry.register_resource_creator(Sensor.SUBTYPE, MySensor.MODEL, ResourceCreatorRegistration(MySensor.new, MySensor.validate_config))

    module = Module.from_args()
    module.add_model_from_registry(Sensor.SUBTYPE, MySensor.MODEL)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())
