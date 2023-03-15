"""
This file registers the Gizmo subtype with the Viam Registry, as well as the specific MyGizmo model.
"""

from viam.resource.registry import ResourceRegistration, Registry

from .api import Gizmo, GizmoClient, GizmoService
from .my_gizmo import MyGizmo

Registry.register_subtype(ResourceRegistration(Gizmo, GizmoService, lambda name, channel: GizmoClient(name, channel)))

Registry.register_resource_model(Gizmo.SUBTYPE, MyGizmo.MODEL, MyGizmo.new)
