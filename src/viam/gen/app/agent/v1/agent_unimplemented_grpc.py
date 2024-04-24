import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.duration_pb2
import google.protobuf.struct_pb2
from .... import tagger
from .... import app
from .agent_grpc import AgentAppServiceBase as _AgentAppServiceBase

class UnimplementedAgentAppServiceBase(_AgentAppServiceBase):

    async def GetAgentConfig(self, stream: 'grpclib.server.Stream[app.agent.v1.agent_pb2.GetAgentConfigRequest, app.agent.v1.agent_pb2.GetAgentConfigResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateAgentConfig(self, stream: 'grpclib.server.Stream[app.agent.v1.agent_pb2.UpdateAgentConfigRequest, app.agent.v1.agent_pb2.UpdateAgentConfigResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)
from .agent_grpc import AgentDeviceServiceBase as _AgentDeviceServiceBase

class UnimplementedAgentDeviceServiceBase(_AgentDeviceServiceBase):

    async def DeviceAgentConfig(self, stream: 'grpclib.server.Stream[app.agent.v1.agent_pb2.DeviceAgentConfigRequest, app.agent.v1.agent_pb2.DeviceAgentConfigResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)