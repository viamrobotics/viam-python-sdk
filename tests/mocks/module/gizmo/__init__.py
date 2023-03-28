from viam.components.motor import *
from viam.resource.registry import Registry, ResourceRegistration

from .api import Gizmo, GizmoClient, GizmoService
from .my_gizmo import MyGizmo

Registry.register_subtype(ResourceRegistration(Gizmo, GizmoService, lambda name, channel: GizmoClient(name, channel)))

Registry.register_resource_creator(Gizmo.SUBTYPE, MyGizmo.MODEL, MyGizmo.new)
Registry.register_resource_validator(Gizmo.SUBTYPE, MyGizmo.MODEL, MyGizmo.validate_config)
