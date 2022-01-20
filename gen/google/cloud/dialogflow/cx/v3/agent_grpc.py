# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dialogflow/cx/v3/agent.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.cloud.dialogflow.cx.v3.advanced_settings_pb2
import google.cloud.dialogflow.cx.v3.flow_pb2
import google.cloud.dialogflow.cx.v3.security_settings_pb2
import google.longrunning.operations_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.cloud.dialogflow.cx.v3.agent_pb2


class AgentsBase(abc.ABC):

    @abc.abstractmethod
    async def ListAgents(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3.agent_pb2.ListAgentsRequest, google.cloud.dialogflow.cx.v3.agent_pb2.ListAgentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3.agent_pb2.GetAgentRequest, google.cloud.dialogflow.cx.v3.agent_pb2.Agent]') -> None:
        pass

    @abc.abstractmethod
    async def CreateAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3.agent_pb2.CreateAgentRequest, google.cloud.dialogflow.cx.v3.agent_pb2.Agent]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3.agent_pb2.UpdateAgentRequest, google.cloud.dialogflow.cx.v3.agent_pb2.Agent]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3.agent_pb2.DeleteAgentRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ExportAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3.agent_pb2.ExportAgentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def RestoreAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3.agent_pb2.RestoreAgentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ValidateAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3.agent_pb2.ValidateAgentRequest, google.cloud.dialogflow.cx.v3.agent_pb2.AgentValidationResult]') -> None:
        pass

    @abc.abstractmethod
    async def GetAgentValidationResult(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3.agent_pb2.GetAgentValidationResultRequest, google.cloud.dialogflow.cx.v3.agent_pb2.AgentValidationResult]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dialogflow.cx.v3.Agents/ListAgents': grpclib.const.Handler(
                self.ListAgents,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3.agent_pb2.ListAgentsRequest,
                google.cloud.dialogflow.cx.v3.agent_pb2.ListAgentsResponse,
            ),
            '/google.cloud.dialogflow.cx.v3.Agents/GetAgent': grpclib.const.Handler(
                self.GetAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3.agent_pb2.GetAgentRequest,
                google.cloud.dialogflow.cx.v3.agent_pb2.Agent,
            ),
            '/google.cloud.dialogflow.cx.v3.Agents/CreateAgent': grpclib.const.Handler(
                self.CreateAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3.agent_pb2.CreateAgentRequest,
                google.cloud.dialogflow.cx.v3.agent_pb2.Agent,
            ),
            '/google.cloud.dialogflow.cx.v3.Agents/UpdateAgent': grpclib.const.Handler(
                self.UpdateAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3.agent_pb2.UpdateAgentRequest,
                google.cloud.dialogflow.cx.v3.agent_pb2.Agent,
            ),
            '/google.cloud.dialogflow.cx.v3.Agents/DeleteAgent': grpclib.const.Handler(
                self.DeleteAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3.agent_pb2.DeleteAgentRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.dialogflow.cx.v3.Agents/ExportAgent': grpclib.const.Handler(
                self.ExportAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3.agent_pb2.ExportAgentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dialogflow.cx.v3.Agents/RestoreAgent': grpclib.const.Handler(
                self.RestoreAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3.agent_pb2.RestoreAgentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dialogflow.cx.v3.Agents/ValidateAgent': grpclib.const.Handler(
                self.ValidateAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3.agent_pb2.ValidateAgentRequest,
                google.cloud.dialogflow.cx.v3.agent_pb2.AgentValidationResult,
            ),
            '/google.cloud.dialogflow.cx.v3.Agents/GetAgentValidationResult': grpclib.const.Handler(
                self.GetAgentValidationResult,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3.agent_pb2.GetAgentValidationResultRequest,
                google.cloud.dialogflow.cx.v3.agent_pb2.AgentValidationResult,
            ),
        }


class AgentsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListAgents = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3.Agents/ListAgents',
            google.cloud.dialogflow.cx.v3.agent_pb2.ListAgentsRequest,
            google.cloud.dialogflow.cx.v3.agent_pb2.ListAgentsResponse,
        )
        self.GetAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3.Agents/GetAgent',
            google.cloud.dialogflow.cx.v3.agent_pb2.GetAgentRequest,
            google.cloud.dialogflow.cx.v3.agent_pb2.Agent,
        )
        self.CreateAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3.Agents/CreateAgent',
            google.cloud.dialogflow.cx.v3.agent_pb2.CreateAgentRequest,
            google.cloud.dialogflow.cx.v3.agent_pb2.Agent,
        )
        self.UpdateAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3.Agents/UpdateAgent',
            google.cloud.dialogflow.cx.v3.agent_pb2.UpdateAgentRequest,
            google.cloud.dialogflow.cx.v3.agent_pb2.Agent,
        )
        self.DeleteAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3.Agents/DeleteAgent',
            google.cloud.dialogflow.cx.v3.agent_pb2.DeleteAgentRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ExportAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3.Agents/ExportAgent',
            google.cloud.dialogflow.cx.v3.agent_pb2.ExportAgentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.RestoreAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3.Agents/RestoreAgent',
            google.cloud.dialogflow.cx.v3.agent_pb2.RestoreAgentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ValidateAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3.Agents/ValidateAgent',
            google.cloud.dialogflow.cx.v3.agent_pb2.ValidateAgentRequest,
            google.cloud.dialogflow.cx.v3.agent_pb2.AgentValidationResult,
        )
        self.GetAgentValidationResult = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3.Agents/GetAgentValidationResult',
            google.cloud.dialogflow.cx.v3.agent_pb2.GetAgentValidationResultRequest,
            google.cloud.dialogflow.cx.v3.agent_pb2.AgentValidationResult,
        )
