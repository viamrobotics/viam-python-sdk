import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import app
from ... import robot
from ... import module

class ModuleServiceBase(abc.ABC):

    @abc.abstractmethod
    async def AddResource(self, stream: 'grpclib.server.Stream[module.v1.module_pb2.AddResourceRequest, module.v1.module_pb2.AddResourceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReconfigureResource(self, stream: 'grpclib.server.Stream[module.v1.module_pb2.ReconfigureResourceRequest, module.v1.module_pb2.ReconfigureResourceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveResource(self, stream: 'grpclib.server.Stream[module.v1.module_pb2.RemoveResourceRequest, module.v1.module_pb2.RemoveResourceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Ready(self, stream: 'grpclib.server.Stream[module.v1.module_pb2.ReadyRequest, module.v1.module_pb2.ReadyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ValidateConfig(self, stream: 'grpclib.server.Stream[module.v1.module_pb2.ValidateConfigRequest, module.v1.module_pb2.ValidateConfigResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.module.v1.ModuleService/AddResource': grpclib.const.Handler(self.AddResource, grpclib.const.Cardinality.UNARY_UNARY, module.v1.module_pb2.AddResourceRequest, module.v1.module_pb2.AddResourceResponse), '/viam.module.v1.ModuleService/ReconfigureResource': grpclib.const.Handler(self.ReconfigureResource, grpclib.const.Cardinality.UNARY_UNARY, module.v1.module_pb2.ReconfigureResourceRequest, module.v1.module_pb2.ReconfigureResourceResponse), '/viam.module.v1.ModuleService/RemoveResource': grpclib.const.Handler(self.RemoveResource, grpclib.const.Cardinality.UNARY_UNARY, module.v1.module_pb2.RemoveResourceRequest, module.v1.module_pb2.RemoveResourceResponse), '/viam.module.v1.ModuleService/Ready': grpclib.const.Handler(self.Ready, grpclib.const.Cardinality.UNARY_UNARY, module.v1.module_pb2.ReadyRequest, module.v1.module_pb2.ReadyResponse), '/viam.module.v1.ModuleService/ValidateConfig': grpclib.const.Handler(self.ValidateConfig, grpclib.const.Cardinality.UNARY_UNARY, module.v1.module_pb2.ValidateConfigRequest, module.v1.module_pb2.ValidateConfigResponse)}

class UnimplementedModuleServiceBase(ModuleServiceBase):

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

class ModuleServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.AddResource = grpclib.client.UnaryUnaryMethod(channel, '/viam.module.v1.ModuleService/AddResource', module.v1.module_pb2.AddResourceRequest, module.v1.module_pb2.AddResourceResponse)
        self.ReconfigureResource = grpclib.client.UnaryUnaryMethod(channel, '/viam.module.v1.ModuleService/ReconfigureResource', module.v1.module_pb2.ReconfigureResourceRequest, module.v1.module_pb2.ReconfigureResourceResponse)
        self.RemoveResource = grpclib.client.UnaryUnaryMethod(channel, '/viam.module.v1.ModuleService/RemoveResource', module.v1.module_pb2.RemoveResourceRequest, module.v1.module_pb2.RemoveResourceResponse)
        self.Ready = grpclib.client.UnaryUnaryMethod(channel, '/viam.module.v1.ModuleService/Ready', module.v1.module_pb2.ReadyRequest, module.v1.module_pb2.ReadyResponse)
        self.ValidateConfig = grpclib.client.UnaryUnaryMethod(channel, '/viam.module.v1.ModuleService/ValidateConfig', module.v1.module_pb2.ValidateConfigRequest, module.v1.module_pb2.ValidateConfigResponse)