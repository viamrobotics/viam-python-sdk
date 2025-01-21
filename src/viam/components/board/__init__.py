from viam.resource.registry import Registry, ResourceRegistration

from .board import Board, Tick, TickStream
from .client import BoardClient
from .service import BoardRPCService

__all__ = ["Board", "Tick", "TickStream"]

Registry.register_api(ResourceRegistration(Board, BoardRPCService, lambda name, channel: BoardClient(name, channel)))
