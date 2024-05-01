import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.duration_pb2
import google.protobuf.struct_pb2
from .... import app

class AgentDeviceServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DeviceAgentConfig(self, stream: 'grpclib.server.Stream[app.agent.v1.agent_pb2.DeviceAgentConfigRequest, app.agent.v1.agent_pb2.DeviceAgentConfigResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.agent.v1.AgentDeviceService/DeviceAgentConfig': grpclib.const.Handler(self.DeviceAgentConfig, grpclib.const.Cardinality.UNARY_UNARY, app.agent.v1.agent_pb2.DeviceAgentConfigRequest, app.agent.v1.agent_pb2.DeviceAgentConfigResponse)}

class UnimplementedAgentDeviceServiceBase(AgentDeviceServiceBase):

    async def DeviceAgentConfig(self, stream: 'grpclib.server.Stream[app.agent.v1.agent_pb2.DeviceAgentConfigRequest, app.agent.v1.agent_pb2.DeviceAgentConfigResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class AgentDeviceServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DeviceAgentConfig = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.agent.v1.AgentDeviceService/DeviceAgentConfig', app.agent.v1.agent_pb2.DeviceAgentConfigRequest, app.agent.v1.agent_pb2.DeviceAgentConfigResponse)