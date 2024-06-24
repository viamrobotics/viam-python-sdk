from viam.proto.service.motion import UnimplementedMotionServiceBase
from viam.resource.rpc_service_base import ResourceRPCServiceBase

from .motion import Motion


class MotionRPCService(UnimplementedMotionServiceBase, ResourceRPCServiceBase):
    RESOURCE_TYPE = Motion
