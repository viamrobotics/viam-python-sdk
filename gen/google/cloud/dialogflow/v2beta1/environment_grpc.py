# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dialogflow/v2beta1/environment.proto
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
import google.cloud.dialogflow.v2beta1.audio_config_pb2
import google.cloud.dialogflow.v2beta1.fulfillment_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.dialogflow.v2beta1.environment_pb2


class EnvironmentsBase(abc.ABC):

    @abc.abstractmethod
    async def ListEnvironments(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.environment_pb2.ListEnvironmentsRequest, google.cloud.dialogflow.v2beta1.environment_pb2.ListEnvironmentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetEnvironment(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.environment_pb2.GetEnvironmentRequest, google.cloud.dialogflow.v2beta1.environment_pb2.Environment]') -> None:
        pass

    @abc.abstractmethod
    async def CreateEnvironment(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.environment_pb2.CreateEnvironmentRequest, google.cloud.dialogflow.v2beta1.environment_pb2.Environment]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateEnvironment(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.environment_pb2.UpdateEnvironmentRequest, google.cloud.dialogflow.v2beta1.environment_pb2.Environment]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteEnvironment(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.environment_pb2.DeleteEnvironmentRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def GetEnvironmentHistory(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.environment_pb2.GetEnvironmentHistoryRequest, google.cloud.dialogflow.v2beta1.environment_pb2.EnvironmentHistory]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dialogflow.v2beta1.Environments/ListEnvironments': grpclib.const.Handler(
                self.ListEnvironments,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.environment_pb2.ListEnvironmentsRequest,
                google.cloud.dialogflow.v2beta1.environment_pb2.ListEnvironmentsResponse,
            ),
            '/google.cloud.dialogflow.v2beta1.Environments/GetEnvironment': grpclib.const.Handler(
                self.GetEnvironment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.environment_pb2.GetEnvironmentRequest,
                google.cloud.dialogflow.v2beta1.environment_pb2.Environment,
            ),
            '/google.cloud.dialogflow.v2beta1.Environments/CreateEnvironment': grpclib.const.Handler(
                self.CreateEnvironment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.environment_pb2.CreateEnvironmentRequest,
                google.cloud.dialogflow.v2beta1.environment_pb2.Environment,
            ),
            '/google.cloud.dialogflow.v2beta1.Environments/UpdateEnvironment': grpclib.const.Handler(
                self.UpdateEnvironment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.environment_pb2.UpdateEnvironmentRequest,
                google.cloud.dialogflow.v2beta1.environment_pb2.Environment,
            ),
            '/google.cloud.dialogflow.v2beta1.Environments/DeleteEnvironment': grpclib.const.Handler(
                self.DeleteEnvironment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.environment_pb2.DeleteEnvironmentRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.dialogflow.v2beta1.Environments/GetEnvironmentHistory': grpclib.const.Handler(
                self.GetEnvironmentHistory,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.environment_pb2.GetEnvironmentHistoryRequest,
                google.cloud.dialogflow.v2beta1.environment_pb2.EnvironmentHistory,
            ),
        }


class EnvironmentsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListEnvironments = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Environments/ListEnvironments',
            google.cloud.dialogflow.v2beta1.environment_pb2.ListEnvironmentsRequest,
            google.cloud.dialogflow.v2beta1.environment_pb2.ListEnvironmentsResponse,
        )
        self.GetEnvironment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Environments/GetEnvironment',
            google.cloud.dialogflow.v2beta1.environment_pb2.GetEnvironmentRequest,
            google.cloud.dialogflow.v2beta1.environment_pb2.Environment,
        )
        self.CreateEnvironment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Environments/CreateEnvironment',
            google.cloud.dialogflow.v2beta1.environment_pb2.CreateEnvironmentRequest,
            google.cloud.dialogflow.v2beta1.environment_pb2.Environment,
        )
        self.UpdateEnvironment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Environments/UpdateEnvironment',
            google.cloud.dialogflow.v2beta1.environment_pb2.UpdateEnvironmentRequest,
            google.cloud.dialogflow.v2beta1.environment_pb2.Environment,
        )
        self.DeleteEnvironment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Environments/DeleteEnvironment',
            google.cloud.dialogflow.v2beta1.environment_pb2.DeleteEnvironmentRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.GetEnvironmentHistory = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Environments/GetEnvironmentHistory',
            google.cloud.dialogflow.v2beta1.environment_pb2.GetEnvironmentHistoryRequest,
            google.cloud.dialogflow.v2beta1.environment_pb2.EnvironmentHistory,
        )
