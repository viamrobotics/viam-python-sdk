"""
This file registers the Gizmo subtype with the Viam Registry, as well as the specific MyGizmo model.
"""

from viam.components.motor import *  # noqa: F403 Need to import motor so the component registers itself
from viam.resource.registry import Registry, ResourceRegistration

from .api import Gizmo, GizmoClient, GizmoService

Registry.register_api(ResourceRegistration(Gizmo, GizmoService, lambda name, channel: GizmoClient(name, channel)))
