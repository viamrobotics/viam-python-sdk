import asyncio
from typing import ClassVar, Mapping, Optional, Self, Sequence
from viam.module.module import Module
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.easy_resource import EasyResource
from viam.resource.types import Model, ModelFamily
from viam.{{cookiecutter.__resource_type}}s.{{cookiecutter.__resource}} import {{cookiecutter.__resource.capitalize()}}
from viam.utils import ValueTypes


class {{cookiecutter.model_name}}({{cookiecutter.__resource.capitalize()}}, EasyResource):
    """This is your custom {{cookiecutter.__resource.capitalize()}} {{cookiecutter.__resource_type}}.

    All the methods listed are optional.
    You can implement the methods you want and remove the methods you don't need.
    """

    MODEL: ClassVar[Model] = Model(ModelFamily("{{cookiecutter.namespace}}", "{{cookiecutter.module_name}}"), "{{cookiecutter.model_name}}")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        """
        This method creates a new instance of this vision service.
        The default implementation sets the name from the `config` parameter and then calls `reconfigure`.

        Args:
            config (ComponentConfig): The configuration for this resource
            dependencies (Mapping[ResourceName, ResourceBase]): The dependencies (both implicit and explicit)

        Returns:
            Self: The resource
        """
        return super().new(config, dependencies)

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        """This method allows you to validate the configuration object received from the machine,
        as well as to return any implicit dependencies based on that `config`.

        Args:
            config (ComponentConfig): The configuration for this resource

        Returns:
            Sequence[str]: A list of implicit dependencies
        """
        raise NotImplementedError

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        """This method allows you to dynamically update your service when it receives a new `config` object.

        Args:
            config (ComponentConfig): The new configuration
            dependencies (Mapping[ResourceName, ResourceBase]): Any dependencies (both implicit and explicit)
        """
        return super().reconfigure(config, dependencies)

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs):
        raise NotImplementedError


if __name__ == "__main__":
    """This function will run your module and make it available to the machine."""
    asyncio.run(Module.run_from_registry())
