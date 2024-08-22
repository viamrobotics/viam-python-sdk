import inspect
import os
from importlib import import_module


def __get_resource_class(resource_type: str, resource_name: str):
    module = import_module(f"viam.{resource_type}s.{resource_name}")
    return getattr(module, "".join(word.capitalize() for word in resource_name.split("_")))


def __generate_method_stubs(module: type) -> str:
    methods = inspect.getmembers(module, predicate=inspect.isfunction)
    stubs = []
    for name, method in methods:
        if name == "__init__" or name == "__subclasshook__":
            continue
        params = inspect.signature(method).parameters
        param_str = ', '.join(f"{value}" for value in params.values())
        stubs.append(f"async def {name}({param_str}):\n        raise NotImplementedError\n")
    return '\n    '.join(stubs)


def generate_main(resource_type: str, resource_name: str, model_name: str, namespace: str, module_name: str) -> None:
    viam_module = __get_resource_class(resource_type, resource_name)
    method_stubs = __generate_method_stubs(viam_module)

    viam_class = "".join(word.capitalize() for word in resource_name.split("_"))

    file_path = os.path.join(os.getcwd(), "src/__main__.py")
    with open(file_path, 'w') as file:
        file.write(f'''import asyncio
from typing import ClassVar, Mapping, Optional, Self, Sequence, Union
from viam.module.module import Module
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.easy_resource import EasyResource
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily
from viam.{resource_type}s.{resource_name} import {viam_class}


class {model_name.capitalize()}({viam_class}, EasyResource):
    """This is your custom {viam_class} {resource_type}.

    All the methods listed are optional.
    You can implement the methods you want and remove the methods you don't need.
    """
    MODEL: ClassVar[Model] = Model(ModelFamily("{namespace}", "{module_name}"), "{model_name}")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        """This method creates a new instance of this vision service.
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

    {method_stubs}


Registry.register_resource_creator({viam_class}.SUBTYPE, {model_name.capitalize()}.MODEL, ResourceCreatorRegistration({model_name.capitalize()}.new, {model_name.capitalize()}.validate_config))


if __name__ == "__main__":
    """This function will run your module and make it available to the machine."""
    asyncio.run(Module.run_from_registry())
''')


if __name__ == "__main__":
    generate_main(
        "{{cookiecutter.__resource_type}}",
        "{{cookiecutter.__resource}}",
        "{{cookiecutter.model_name}}",
        "{{cookiecutter.namespace}}",
        "{{cookiecutter.module_name}}")
