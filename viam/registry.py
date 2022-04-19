from dataclasses import dataclass
from typing import Callable, Coroutine, Dict, Generic, Type, TypeVar, Any
from google.protobuf.struct_pb2 import Struct

from grpclib.client import Channel
from viam.components.component_base import ComponentBase
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError, DuplicateComponentError
from viam.proto.api.service.status import Status

Component = TypeVar('Component', bound=ComponentBase)


async def default_create_status(component: ComponentBase) -> Status:
    return Status(
        name=component.get_resource_name(component.name),
        status=Struct()
    )


@dataclass
class ComponentRegistration(Generic[Component]):
    component_type: Type[Component]
    name: str
    rpc_service: Type[ComponentServiceBase]
    create_rpc_client: Callable[[str, Channel], Component]
    create_status: Callable[[Component], Coroutine[Any, Any, Status]] = default_create_status


class Registry:

    _COMPONENTS: Dict[str, ComponentRegistration] = {}

    @classmethod
    def register(cls, registration: ComponentRegistration):
        if registration.name in cls._COMPONENTS:
            raise DuplicateComponentError(registration.name)
        cls._COMPONENTS[registration.name] = registration

    @classmethod
    def lookup(cls, component_name: str) -> ComponentRegistration:
        try:
            return cls._COMPONENTS[component_name]
        except KeyError:
            raise ComponentNotFoundError('component', component_name)

    @classmethod
    @property
    def REGISTERED_COMPONENTS(cls) -> Dict[str, ComponentRegistration]:
        return {k: v for (k, v) in cls._COMPONENTS.items()}
