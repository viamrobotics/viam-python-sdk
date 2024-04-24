import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import app
from ... import robot
from ... import module
from .module_grpc import ModuleServiceBase as _ModuleServiceBase

class UnimplementedModuleServiceBase(_ModuleServiceBase):

    async def AddResource(self, stream: 'grpclib.server.Stream[module.v1.module_pb2.AddResourceRequest, module.v1.module_pb2.AddResourceResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ReconfigureResource(self, stream: 'grpclib.server.Stream[module.v1.module_pb2.ReconfigureResourceRequest, module.v1.module_pb2.ReconfigureResourceResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RemoveResource(self, stream: 'grpclib.server.Stream[module.v1.module_pb2.RemoveResourceRequest, module.v1.module_pb2.RemoveResourceResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Ready(self, stream: 'grpclib.server.Stream[module.v1.module_pb2.ReadyRequest, module.v1.module_pb2.ReadyResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ValidateConfig(self, stream: 'grpclib.server.Stream[module.v1.module_pb2.ValidateConfigRequest, module.v1.module_pb2.ValidateConfigResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)