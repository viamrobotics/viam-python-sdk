import viam.gen.component.switch.v1.switch_pb2
from viam.resource.registry import Registry, ResourceRegistration

from .client import SwitchClient
from .service import SwitchRPCService
from .switch import Switch

__all__ = ["Switch"]

Registry.register_api(ResourceRegistration(Switch, SwitchRPCService, lambda name, channel: SwitchClient(name, channel)))
