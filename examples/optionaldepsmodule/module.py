from typing import ClassVar, Mapping, Sequence, cast

from typing_extensions import Self

from viam.components.generic import Generic
from viam.components.motor import Motor
from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.resource.base import ResourceBase
from viam.proto.common import ResourceName
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily
from viam.utils import struct_to_dict
from viam.module.module import Module
import asyncio


class Foo(Generic, Reconfigurable):
    MODEL: ClassVar[Model] = Model(ModelFamily("acme", "demo"), "foo")

    def __init__(self, name: str):
        super().__init__(name)

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        foo = cls(config.name)
        foo.reconfigure(config, dependencies)
        return foo

    # Validate validates the config and returns a required dependency on
    # `required_motor` and an optional dependency on `optional_motor`.
    @classmethod
    def validate_config(cls, config: ComponentConfig) -> tuple[Sequence[str], Sequence[str]]:
        attributes_dict = struct_to_dict(config.attributes)

        cfg_required_motor: str = cast(str, attributes_dict.get("required_motor"))
        cfg_optional_motor: str = cast(str, attributes_dict.get("optional_motor"))

        required_deps = []
        optional_deps = []

        if cfg_required_motor is None or cfg_required_motor == "":
            raise Exception(f'expected "required_motor" attribute for foo {config}')

        required_deps.append(cfg_required_motor)

        if cfg_optional_motor is not None and cfg_optional_motor != "":
            optional_deps.append(cfg_optional_motor)

        return required_deps, optional_deps

    # Reconfigure with latest dependencies
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        attributes_dict = struct_to_dict(config.attributes)

        cfg_required_motor: str = cast(str, attributes_dict.get("required_motor"))
        cfg_optional_motor: str = cast(str, attributes_dict.get("optional_motor"))

        required_motor = Motor.get_resource_name(cfg_required_motor)
        if required_motor not in dependencies:
            raise Exception(f"could not get required motor {cfg_required_motor} from dependencies")
        else:
            self.required_motor = required_motor

        optional_motor = Motor.get_resource_name(cfg_optional_motor)
        if optional_motor not in dependencies:
            print(f'could not get optional motor {cfg_optional_motor} from dependencies; continuing')
        else:
            self.optional_motor = optional_motor


async def main():
    """This function creates and starts a new module, after adding all desired resource models.
    Resource creators must be registered to the resource registry before the module adds the resource model.
    """

    Registry.register_resource_creator(Generic.API, Foo.MODEL, ResourceCreatorRegistration(Foo.new, Foo.validate_config))

    module = Module.from_args()
    module.add_model_from_registry(Generic.API, Foo.MODEL)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())
