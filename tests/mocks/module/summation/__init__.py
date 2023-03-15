from viam.resource.registry import Registry, ResourceRegistration

from .api import SummationClient, SummationRPCService, SummationService
from .my_summation import MySummationService

Registry.register_subtype(ResourceRegistration(SummationService, SummationRPCService, lambda name, channel: SummationClient(name, channel)))

Registry.register_resource_model(SummationService.SUBTYPE, MySummationService.MODEL, MySummationService.new)
