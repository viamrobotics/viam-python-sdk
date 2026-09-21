from .client import FrameSystemClient
from .framesystem import FrameSystem

__all__ = ["FrameSystem", "FrameSystemClient"]

# There is deliberately no Registry.register_api call here. The frame system RPCs are served by viam-server on the robot
# service, so there is no per resource RPC service to register, and $framesystem never appears in ResourceNames for
# RobotClient to build a client from. RobotClient.get_service special cases the name instead.
