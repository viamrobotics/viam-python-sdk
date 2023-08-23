"""
This file registers the MyBase model with the Python SDK.
"""

from viam.components.base import Base
from viam.resource.registry import Registry, ResourceCreatorRegistration
from .my_base import MyBase

Registry.register_resource_creator(Base.SUBTYPE, MyBase.MODEL, ResourceCreatorRegistration(MyBase.new))
