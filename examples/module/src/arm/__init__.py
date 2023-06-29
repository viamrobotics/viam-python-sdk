"""
This file registers the ModuleArm model with the Python SDK.
"""

from viam.resource.registry import Registry, ResourceCreatorRegistration
from .my_arm import MyArm

Registry.register_resource_creator(MyArm.SUBTYPE, MyArm.MODEL, ResourceCreatorRegistration(MyArm.new))
