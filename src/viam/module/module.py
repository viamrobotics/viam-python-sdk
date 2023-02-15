from typing import Mapping

from viam.components.component_base import ComponentBase
from viam.proto.common import ResourceName
from viam.proto.module import AddResourceRequest
from viam.resource.types import Model, Subtype, resource_name_from_string
from viam.resource.registry import Registry, ComponentRegistration
from viam.robot.client import RobotClient


class Module:

    parent: RobotClient

    def add_model(self, subtype: Subtype, model: Model):
        if not subtype in Registry.REGISTERED_RESOURCES():
            regitration = ComponentRegistration()
            Registry.register_subtype()

    async def add_resource(self, request: AddResourceRequest):
        dependencies: Mapping[ResourceName, ComponentBase] = {}
        for dep in request.dependencies:
            rn = resource_name_from_string(dep)
            component = self.parent.get_component(rn)
            dependencies[rn] = component
