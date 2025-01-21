from viam.resource.registry import Registry, ResourceCreatorRegistration, ResourceRegistration

from .api import SummationClient, SummationRPCService, SummationService
from .my_summation import MySummationService

Registry.register_api(ResourceRegistration(SummationService, SummationRPCService, lambda name, channel: SummationClient(name, channel)))

Registry.register_resource_creator(SummationService.SUBTYPE, MySummationService.MODEL, ResourceCreatorRegistration(MySummationService.new))
