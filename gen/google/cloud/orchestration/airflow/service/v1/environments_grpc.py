# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/orchestration/airflow/service/v1/environments.proto
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
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.orchestration.airflow.service.v1.environments_pb2


class EnvironmentsBase(abc.ABC):

    @abc.abstractmethod
    async def CreateEnvironment(self, stream: 'grpclib.server.Stream[google.cloud.orchestration.airflow.service.v1.environments_pb2.CreateEnvironmentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetEnvironment(self, stream: 'grpclib.server.Stream[google.cloud.orchestration.airflow.service.v1.environments_pb2.GetEnvironmentRequest, google.cloud.orchestration.airflow.service.v1.environments_pb2.Environment]') -> None:
        pass

    @abc.abstractmethod
    async def ListEnvironments(self, stream: 'grpclib.server.Stream[google.cloud.orchestration.airflow.service.v1.environments_pb2.ListEnvironmentsRequest, google.cloud.orchestration.airflow.service.v1.environments_pb2.ListEnvironmentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateEnvironment(self, stream: 'grpclib.server.Stream[google.cloud.orchestration.airflow.service.v1.environments_pb2.UpdateEnvironmentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteEnvironment(self, stream: 'grpclib.server.Stream[google.cloud.orchestration.airflow.service.v1.environments_pb2.DeleteEnvironmentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.orchestration.airflow.service.v1.Environments/CreateEnvironment': grpclib.const.Handler(
                self.CreateEnvironment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.orchestration.airflow.service.v1.environments_pb2.CreateEnvironmentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.orchestration.airflow.service.v1.Environments/GetEnvironment': grpclib.const.Handler(
                self.GetEnvironment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.orchestration.airflow.service.v1.environments_pb2.GetEnvironmentRequest,
                google.cloud.orchestration.airflow.service.v1.environments_pb2.Environment,
            ),
            '/google.cloud.orchestration.airflow.service.v1.Environments/ListEnvironments': grpclib.const.Handler(
                self.ListEnvironments,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.orchestration.airflow.service.v1.environments_pb2.ListEnvironmentsRequest,
                google.cloud.orchestration.airflow.service.v1.environments_pb2.ListEnvironmentsResponse,
            ),
            '/google.cloud.orchestration.airflow.service.v1.Environments/UpdateEnvironment': grpclib.const.Handler(
                self.UpdateEnvironment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.orchestration.airflow.service.v1.environments_pb2.UpdateEnvironmentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.orchestration.airflow.service.v1.Environments/DeleteEnvironment': grpclib.const.Handler(
                self.DeleteEnvironment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.orchestration.airflow.service.v1.environments_pb2.DeleteEnvironmentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class EnvironmentsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateEnvironment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.orchestration.airflow.service.v1.Environments/CreateEnvironment',
            google.cloud.orchestration.airflow.service.v1.environments_pb2.CreateEnvironmentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetEnvironment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.orchestration.airflow.service.v1.Environments/GetEnvironment',
            google.cloud.orchestration.airflow.service.v1.environments_pb2.GetEnvironmentRequest,
            google.cloud.orchestration.airflow.service.v1.environments_pb2.Environment,
        )
        self.ListEnvironments = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.orchestration.airflow.service.v1.Environments/ListEnvironments',
            google.cloud.orchestration.airflow.service.v1.environments_pb2.ListEnvironmentsRequest,
            google.cloud.orchestration.airflow.service.v1.environments_pb2.ListEnvironmentsResponse,
        )
        self.UpdateEnvironment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.orchestration.airflow.service.v1.Environments/UpdateEnvironment',
            google.cloud.orchestration.airflow.service.v1.environments_pb2.UpdateEnvironmentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteEnvironment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.orchestration.airflow.service.v1.Environments/DeleteEnvironment',
            google.cloud.orchestration.airflow.service.v1.environments_pb2.DeleteEnvironmentRequest,
            google.longrunning.operations_pb2.Operation,
        )
