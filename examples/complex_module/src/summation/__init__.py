"""
This file registers the Summation subtype with the Viam Registry, as well as the specific MySummation model.
"""

from viam.resource.registry import Registry, ResourceCreatorRegistration, ResourceRegistration

from .api import SummationClient, SummationRPCService, SummationService
from .my_summation import MySummationService

Registry.register_subtype(ResourceRegistration(SummationService, SummationRPCService, lambda name, channel: SummationClient(name, channel)))

Registry.register_resource_creator(SummationService.SUBTYPE, MySummationService.MODEL, ResourceCreatorRegistration(MySummationService.new))
