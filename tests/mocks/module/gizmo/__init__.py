from viam.components.motor import *  # noqa: F403 Need to import motor so the component registers itself
from viam.resource.registry import Registry, ResourceCreatorRegistration, ResourceRegistration

from .api import Gizmo, GizmoClient, GizmoService
from .my_gizmo import MyGizmo

Registry.register_api(ResourceRegistration(Gizmo, GizmoService, lambda name, channel: GizmoClient(name, channel)))

Registry.register_resource_creator(Gizmo.API, MyGizmo.MODEL, ResourceCreatorRegistration(MyGizmo.new, MyGizmo.validate_config))
