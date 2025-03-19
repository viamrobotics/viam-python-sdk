import viam.gen.component.button.v1.button_pb2
from viam.resource.registry import Registry, ResourceRegistration

from .client import ButtonClient
from .service import ButtonRPCService
from .button import Button

__all__ = ["Button"]

Registry.register_api(ResourceRegistration(Button, ButtonRPCService, lambda name, channel: ButtonClient(name, channel)))
