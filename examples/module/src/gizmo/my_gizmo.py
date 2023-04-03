from typing import ClassVar, Mapping, Sequence

from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from ..gizmo.api import Gizmo


class MyGizmo(Gizmo, Reconfigurable):
    """This is the specific implementation of a ``Gizmo`` (defined in api.py).

    It inherits from Gizmo, as well conforms to the ``Reconfigurable`` protocol, which signifies that this component can be reconfigured.
    It also specifies a function ``MyGizmo.new``, which conforms to the ``resource.types.ResourceCreator`` type, which is required
    for all models.
    """

    MODEL: ClassVar[Model] = Model(ModelFamily("acme", "demo"), "mygizmo")
    my_arg: str

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        gizmo = cls(config.name)
        gizmo.my_arg = config.attributes.fields["arg1"].string_value
        return gizmo

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        # Custom validation can be done by specifiying a validate function like this one. Validate functions
        # can raise errors that will be returned to the parent through gRPC. Validate functions can
        # also return a sequence of strings representing the implicit dependencies of the resource.
        if "invalid" in config.attributes.fields:
            raise Exception(f"'invalid' attribute not allowed for model {cls.SUBTYPE}:{cls.MODEL}")
        arg1 = config.attributes.fields["arg1"].string_value
        if arg1 == "":
            raise Exception("A arg1 attribute is required for Gizmo component.")
        motor = [config.attributes.fields["motor"].string_value]
        if motor == [""]:
            raise Exception("A motor is required for Gizmo component.")
        return motor

    async def do_one(self, arg1: str, **kwargs) -> bool:
        return arg1 == self.my_arg

    async def do_one_client_stream(self, arg1: Sequence[str], **kwargs) -> bool:
        if len(arg1) == 0:
            return False
        resp = True
        for arg in arg1:
            resp = resp and arg == self.my_arg
        return resp

    async def do_one_server_stream(self, arg1: str, **kwargs) -> Sequence[bool]:
        return [arg1 == self.my_arg, False, True, False]

    async def do_one_bidi_stream(self, arg1: Sequence[str], **kwargs) -> Sequence[bool]:
        resps = []
        for arg in arg1:
            resps.append(arg == self.my_arg)
        return resps

    async def do_two(self, arg1: bool, **kwargs) -> str:
        return f"arg1={arg1}"

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.my_arg = config.attributes.fields["arg1"].string_value
