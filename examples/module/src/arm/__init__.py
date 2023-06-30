"""
This file registers the MyArm model with the Python SDK.
"""

from viam.components.arm import Arm
from viam.resource.registry import Registry, ResourceCreatorRegistration
from .my_arm import MyArm

Registry.register_resource_creator(Arm.SUBTYPE, MyArm.MODEL, ResourceCreatorRegistration(MyArm.new))
