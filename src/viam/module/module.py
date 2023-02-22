import asyncio
from typing import List, Mapping, Optional, Sequence, Tuple

from grpclib.utils import _service_name

from viam.components.component_base import ComponentBase

# from viam.components.resource_manager import ResourceManager
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.proto.module import (
    AddResourceRequest,
    HandlerDefinition,
    HandlerMap,
    ReadyRequest,
    ReadyResponse,
    ReconfigureResourceRequest,
    RemoveResourceRequest,
)
from viam.proto.robot import ResourceRPCSubtype
from viam.resource.registry import Registry
from viam.resource.types import (
    RESOURCE_TYPE_COMPONENT,
    Model,
    Subtype,
    resource_name_from_string,
)
from viam.robot.client import RobotClient
from viam.rpc.dial import DialOptions
from viam.rpc.server import Server

from .types import Reconfigurable, Stoppable


class Module:

    _address: str
    _parent_address: Optional[str] = None
    parent: Optional[RobotClient] = None
    # resources: ResourceManager
    server: Server
    _ready: bool

    def __init__(self, address: str) -> None:
        self._address = address
        # self.resources = ResourceManager()
        self.server = Server(components=[])

    def _connect_to_parent(self):
        if self.parent is None:
            if self._parent_address is None:
                raise TypeError("Parent address not found")
            self.parent = asyncio.run(
                RobotClient.at_address(
                    self._parent_address,
                    RobotClient.Options(
                        dial_options=DialOptions(disable_webrtc=True, allow_insecure_with_creds_downgrade=True),
                    ),
                )
            )

    def _get_component(self, name: ResourceName) -> ComponentBase:
        self._connect_to_parent()
        assert self.parent is not None
        asyncio.run(self.parent.refresh())
        return self.parent.get_component(name)

    # def add_model(self, subtype: Subtype, model: Model):
    #     if subtype not in Registry.REGISTERED_RESOURCES():
    #         raise ResourceNotFoundError("component", str(subtype))
    #     Registry.register_component(subtype, model, )

    def _get_dependencies(self, dependencies: Sequence[str]) -> Mapping[ResourceName, ComponentBase]:
        deps: Mapping[ResourceName, ComponentBase] = {}
        for dep in dependencies:
            rn = resource_name_from_string(dep)
            component = self._get_component(rn)
            deps[rn] = component
        return deps

    def add_resource(self, request: AddResourceRequest):
        dependencies = self._get_dependencies(request.dependencies)
        config: ComponentConfig = request.config
        namespace = config.namespace
        type_of = config.type
        subtype = config.api
        model = config.model
        if type_of == RESOURCE_TYPE_COMPONENT:
            creator = Registry.lookup_component(Subtype(namespace, type_of, subtype), Model.from_string(model, ignore_errors=True))
            component = creator(dependencies, config)
            self.server.register(component)
            # self.resources.register(component)

    def reconfigure_resource(self, request: ReconfigureResourceRequest):
        dependencies = self._get_dependencies(request.dependencies)
        config: ComponentConfig = request.config
        namespace = config.namespace
        type_of = config.type
        subtype = config.api
        name = config.name
        rn = ResourceName(namespace=namespace, type=type_of, subtype=subtype, name=name)
        # resource = self.resources.get_component(ComponentBase, rn)
        resource = self.server.get_component(ComponentBase, rn)
        if isinstance(resource, Reconfigurable):
            resource.reconfigure(config, dependencies)
        else:
            if isinstance(resource, Stoppable):
                resource.stop()
            add_request = AddResourceRequest(config=request.config, dependencies=request.dependencies)
            # self.resources.remove_component(rn)
            self.server.remove_component(rn)
            self.add_resource(add_request)

    def remove_resource(self, request: RemoveResourceRequest):
        rn = resource_name_from_string(request.name)
        # resource = self.resources.get_component(ComponentBase, rn)
        resource = self.server.get_component(ComponentBase, rn)
        if isinstance(resource, Stoppable):
            resource.stop()
        # self.resources.remove_component(rn)
        self.server.remove_component(rn)

    def ready(self, request: ReadyRequest) -> ReadyResponse:
        self._parent_address = request.parent_address

        svcname_to_models: Mapping[Tuple[str, Subtype], List[Model]] = {}
        for subtype_model_str in Registry.REGISTERED_COMPONENTS().keys():
            subtype_str, model_str = subtype_model_str.split("/")
            subtype = Subtype.from_string(subtype_str)
            model = Model.from_string(model_str)

            registration = Registry.lookup_subtype(subtype)
            service = registration.rpc_service(self.server)
            service_name = _service_name(service)

            models = svcname_to_models.get((service_name, subtype), [])
            models.append(model)
            svcname_to_models[(service_name, subtype)] = models

        handlers: List[HandlerDefinition] = []
        for key, value in svcname_to_models.items():
            svc_name, subtype = key
            rpc_subtype = ResourceRPCSubtype(
                subtype=ResourceName(
                    namespace=subtype.namespace,
                    type=subtype.resource_type,
                    subtype=subtype.resource_subtype,
                    name="",
                ),
                proto_service=svc_name,
            )
            handler_def = HandlerDefinition(subtype=rpc_subtype, models=[str(model) for model in value])
            handlers.append(handler_def)

        return ReadyResponse(ready=self._ready, handlermap=HandlerMap(handlers=handlers))
