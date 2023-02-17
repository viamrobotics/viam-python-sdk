import asyncio
from typing import Mapping, Sequence

from viam.components.component_base import ComponentBase
from viam.components.resource_manager import ResourceManager
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.proto.module import AddResourceRequest, ReconfigureResourceRequest, RemoveResourceRequest
from viam.resource.registry import Registry
from viam.resource.types import (
    RESOURCE_TYPE_COMPONENT,
    Model,
    Subtype,
    resource_name_from_string,
)
from viam.robot.client import RobotClient
from viam.rpc.dial import DialOptions

from .types import Reconfigurable, Stoppable


class Module:

    parent: RobotClient
    resources: ResourceManager

    def __init__(self, address: str) -> None:
        self.parent = asyncio.run(
            RobotClient.at_address(
                address,
                RobotClient.Options(
                    dial_options=DialOptions(disable_webrtc=True, allow_insecure_with_creds_downgrade=True),
                ),
            )
        )
        self.resources = ResourceManager()

    # def add_model(self, subtype: Subtype, model: Model):
    #     if subtype not in Registry.REGISTERED_RESOURCES():
    #         raise ResourceNotFoundError("component", str(subtype))
    #     Registry.register_component(subtype, model, )

    def _get_dependencies(self, dependencies: Sequence[str]) -> Mapping[ResourceName, ComponentBase]:
        deps: Mapping[ResourceName, ComponentBase] = {}
        for dep in dependencies:
            rn = resource_name_from_string(dep)
            component = self.parent.get_component(rn)
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
            self.resources.register(component)

    def reconfigure_resource(self, request: ReconfigureResourceRequest):
        dependencies = self._get_dependencies(request.dependencies)
        config: ComponentConfig = request.config
        namespace = config.namespace
        type_of = config.type
        subtype = config.api
        name = config.name
        rn = ResourceName(namespace=namespace, type=type_of, subtype=subtype, name=name)
        resource = self.resources.get_component(ComponentBase, rn)
        if isinstance(resource, Reconfigurable):
            resource.reconfigure(config, dependencies)
        else:
            if isinstance(resource, Stoppable):
                resource.stop()
            add_request = AddResourceRequest(config=request.config, dependencies=request.dependencies)
            self.resources.remove_component(rn)
            self.add_resource(add_request)

    def remove_resource(self, request: RemoveResourceRequest):
        rn = resource_name_from_string(request.name)
        resource = self.resources.get_component(ComponentBase, rn)
        if isinstance(resource, Stoppable):
            resource.stop()
        self.resources.remove_component(rn)
