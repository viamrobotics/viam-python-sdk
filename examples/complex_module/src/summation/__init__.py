"""
This file registers the Summation subtype with the Viam Registry, as well as the specific MySummation model.
"""

from viam.resource.registry import Registry, ResourceRegistration

from .api import SummationClient, SummationRPCService, SummationService

Registry.register_api(ResourceRegistration(SummationService, SummationRPCService, lambda name, channel: SummationClient(name, channel)))
