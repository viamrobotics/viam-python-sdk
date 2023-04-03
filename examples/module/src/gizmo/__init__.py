"""
This file registers the Gizmo subtype with the Viam Registry, as well as the specific MyGizmo model.
"""

from viam.components.motor import *  # noqa: F403 Need to import motor so the component registers itself
from viam.resource.registry import Registry, ResourceCreatorRegistration, ResourceRegistration

from .api import Gizmo, GizmoClient, GizmoService
from .my_gizmo import MyGizmo

Registry.register_subtype(ResourceRegistration(Gizmo, GizmoService, lambda name, channel: GizmoClient(name, channel)))

Registry.register_resource_creator(Gizmo.SUBTYPE, MyGizmo.MODEL, ResourceCreatorRegistration(MyGizmo.new, MyGizmo.validate_config))
