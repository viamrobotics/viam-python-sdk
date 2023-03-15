from typing import ClassVar, Mapping, Sequence

from typing_extensions import Self

from viam.components.component_base import ComponentBase
from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from ..gizmo.api import Gizmo


class MyGizmo(Gizmo, Reconfigurable):
    MODEL: ClassVar[Model] = Model(ModelFamily("acme", "demo"), "mygizmo")
    my_arg: str

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        gizmo = cls(config.name)
        gizmo.my_arg = config.attributes.fields["arg1"].string_value
        return gizmo

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

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ComponentBase]):
        self.my_arg = config.attributes.fields["arg1"].string_value
