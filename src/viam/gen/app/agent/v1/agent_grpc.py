import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.duration_pb2
import google.protobuf.struct_pb2
from .... import tagger
from .... import app

class AgentAppServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetAgentConfig(self, stream: 'grpclib.server.Stream[app.agent.v1.agent_pb2.GetAgentConfigRequest, app.agent.v1.agent_pb2.GetAgentConfigResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateAgentConfig(self, stream: 'grpclib.server.Stream[app.agent.v1.agent_pb2.UpdateAgentConfigRequest, app.agent.v1.agent_pb2.UpdateAgentConfigResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.agent.v1.AgentAppService/GetAgentConfig': grpclib.const.Handler(self.GetAgentConfig, grpclib.const.Cardinality.UNARY_UNARY, app.agent.v1.agent_pb2.GetAgentConfigRequest, app.agent.v1.agent_pb2.GetAgentConfigResponse), '/viam.app.agent.v1.AgentAppService/UpdateAgentConfig': grpclib.const.Handler(self.UpdateAgentConfig, grpclib.const.Cardinality.UNARY_UNARY, app.agent.v1.agent_pb2.UpdateAgentConfigRequest, app.agent.v1.agent_pb2.UpdateAgentConfigResponse)}

class AgentAppServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetAgentConfig = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.agent.v1.AgentAppService/GetAgentConfig', app.agent.v1.agent_pb2.GetAgentConfigRequest, app.agent.v1.agent_pb2.GetAgentConfigResponse)
        self.UpdateAgentConfig = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.agent.v1.AgentAppService/UpdateAgentConfig', app.agent.v1.agent_pb2.UpdateAgentConfigRequest, app.agent.v1.agent_pb2.UpdateAgentConfigResponse)

class AgentDeviceServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DeviceAgentConfig(self, stream: 'grpclib.server.Stream[app.agent.v1.agent_pb2.DeviceAgentConfigRequest, app.agent.v1.agent_pb2.DeviceAgentConfigResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.agent.v1.AgentDeviceService/DeviceAgentConfig': grpclib.const.Handler(self.DeviceAgentConfig, grpclib.const.Cardinality.UNARY_UNARY, app.agent.v1.agent_pb2.DeviceAgentConfigRequest, app.agent.v1.agent_pb2.DeviceAgentConfigResponse)}

class AgentDeviceServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DeviceAgentConfig = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.agent.v1.AgentDeviceService/DeviceAgentConfig', app.agent.v1.agent_pb2.DeviceAgentConfigRequest, app.agent.v1.agent_pb2.DeviceAgentConfigResponse)