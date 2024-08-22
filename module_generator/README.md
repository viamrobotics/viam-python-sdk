# Module Generator Template

> DISCLAIMER: This is the Python module template for what will eventually be a CLI module generator. It is very much a work in progress, and significant changes will follow. Using this is **NOT** recommended until it is ready.

## How to Use

1. Install cookiecutter: `pipx install cookiecutter`. If pipx is not an option, use `python -m pip install --user cookiecutter`.
2. Call the template: `python3 module_generator/cookiecutter-template`.
3. Fill out the prompts given (see below).
4. The necessary files for the created module will be generated in a new directory `module_generator/<MODULE_NAME>`.

NOTE: The imports in `module_generator/<MODULE_NAME>/src/__main__.py` may have to be adjusted. More details below in the example.

## Prompts

To create a module, the generator needs the user to fill out information about the module. The prompts can be seen in `cookiecutter-template/cookiecutter.json`. The public prompts that a user directly affects are as follows:

- `module_name` (str): Set the name of the module.
- `language` (int): Specify the language for the module being created. Currently, the options are (1) Python.
- `namespace` (str): Set the name of the namespace or organization ID in which the module is being created.
- `resource` (int): Select a resource from a numbered list to be added to the module.
- `model_name` (str): Set the name of the model of the resource.
- `initialize_workflow` (bool): Initialize a workflow for building the module and other cloud build info.

## Template Structure

When a module is created using the template, there are a couple of different files created or populated. Some files to note:

- `.viam-gen-info` saves the user inputs, the module creation time, and the generator version.
- `meta.json` saves the `module_name`, `visibility` (default to public), `language`, `generator_version`, `model`, `api`, and `entrypoint` (default to `run.sh`) into a json file.
- `src/__main__.py` contains all the functions available to the resource.

---

## Module Creation Example

Create a Python module named `rover` in the namespace `test`. Add a vision service model `vizz`. Do not initialize a github workflow.

```python
% python3 cookiecutter-template
  [1/6] module_name (MyModule): rover
  [2/6] Select language
    1 - python
    Choose from [1] (1): 1
  [3/6] namespace (ns): test
  [4/6] Select resource
    1 - arm component
    2 - base component
    3 - motor component
    4 - vision service
    Choose from [1/2/3/4] (1): 4
  [5/6] model_name (model): vizz
  [6/6] initialize_workflow (n): n
```

### Generated Files

`module_generator/rover/.viam-gen-info`

```json
{
  "module_name": "rover",
  "language": "python",
  "namespace": "test",
  "resource": "vision service",
  "model_name": "vizz",
  "generator_version": "0.14.0",
  "generated_on": "2024-08-21 11:50:11"
}
```

`module_generator/rover/meta.json`

```json
{
  "module_name": "rover",
  "visibility": "public",
  "language": "python",
  "generator": "0.14.0",
  "models": [
    {
      "api": "rdk:service:vision",
      "model": "test:rover:vizz"
    }
  ],
  "entrypoint": "run.sh"
}
```

`module_generator/rover/README.md`

```
# rover Module

This module implements the Vision API in the `test:rover:vizz` model.

More information on the Vision Service can be found here: https://python.viam.dev/autoapi/viam/services/vision/index.html.

```

`module_generator/rover/src/__main__.py`

This is the raw file right after generation. This newly created file has some missing imports, which will be fixed below.

```python
import asyncio
from typing import ClassVar, Mapping, Optional, Self, Sequence, Union
from viam.module.module import Module
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.easy_resource import EasyResource
from viam.resource.types import Model, ModelFamily
from viam.services.vision import Vision


class Vizz(Vision, EasyResource):
    """This is your custom Vision service.

    All the methods listed are optional.
    You can implement the methods you want and remove the methods you don't need.
    """
    MODEL: ClassVar[Model] = Model(ModelFamily("test", "rover"), "vizz")

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

    async def capture_all_from_camera(self, camera_name: str, return_image: bool = False, return_classifications: bool = False, return_detections: bool = False, return_object_point_clouds: bool = False, extra: Optional[Mapping[str, Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, NoneType]]] = None, timeout: Optional[float] = None):
        raise NotImplementedError

    async def close(self):
        raise NotImplementedError

    async def do_command(self, command: Mapping[str, Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, NoneType]], timeout: Optional[float] = None, **kwargs):
        raise NotImplementedError

    async def get_classifications(self, image: viam.media.video.ViamImage, count: int, extra: Optional[Mapping[str, Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, NoneType]]] = None, timeout: Optional[float] = None):
        raise NotImplementedError

    async def get_classifications_from_camera(self, camera_name: str, count: int, extra: Optional[Mapping[str, Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, NoneType]]] = None, timeout: Optional[float] = None):
        raise NotImplementedError

    async def get_detections(self, image: viam.media.video.ViamImage, extra: Optional[Mapping[str, Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, NoneType]]] = None, timeout: Optional[float] = None):
        raise NotImplementedError

    async def get_detections_from_camera(self, camera_name: str, extra: Optional[Mapping[str, Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, NoneType]]] = None, timeout: Optional[float] = None):
        raise NotImplementedError

    async def get_object_point_clouds(self, camera_name: str, extra: Optional[Mapping[str, Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, NoneType]]] = None, timeout: Optional[float] = None):
        raise NotImplementedError

    async def get_operation(self, kwargs: Mapping[str, Any]):
        raise NotImplementedError

    async def get_properties(self, extra: Optional[Mapping[str, Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, NoneType]]] = None, timeout: Optional[float] = None):
        raise NotImplementedError


if __name__ == "__main__":
    """This function will run your module and make it available to the machine."""
    asyncio.run(Module.run_from_registry())
```

The types `NoneType`, `Any`, `List`, `SupportsBytes`, and `SupportsFloat` are missing in the above file.

There are some missing Viam types as well. For example, `get_classifications()` has a parameter `get_classifications(self, image: viam.media.video.ViamImage, ...)`.

Add all the imports so that they now include `NoneType`, `Any`, `List`, `SupportsBytes`, `SupportsFloat`, and `ViamImage`. Change the function so that the parameter is now `get_classifications(self, image: ViamImage, ...)`.

```python
from types import NoneType
from typing import Any, ClassVar, List, Mapping, Optional, Self, Sequence, SupportsBytes, SupportsFloat, Union
from viam.media.video import ViamImage

class Vizz(Vision, EasyResource):
    ...

    async def get_classifications(self, image: ViamImage, count: int, extra: Optional[Mapping[str, Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, NoneType]]] = None, timeout: Optional[float] = None):
        raise NotImplementedError

    ...

    async def get_detections(self, image: ViamImage, extra: Optional[Mapping[str, Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, NoneType]]] = None, timeout: Optional[float] = None):
        raise NotImplementedError

    ...
```
