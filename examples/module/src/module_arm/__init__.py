"""
This file registers the ModuleArm model with the Python SDK.
"""

from viam.resource.registry import Registry, ResourceCreatorRegistration
from .module_arm import ModuleArm

Registry.register_resource_creator(ModuleArm.SUBTYPE, ModuleArm.MODEL, ResourceCreatorRegistration(ModuleArm.new))
