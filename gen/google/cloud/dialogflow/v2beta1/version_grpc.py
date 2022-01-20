# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dialogflow/v2beta1/version.proto
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
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.dialogflow.v2beta1.version_pb2


class VersionsBase(abc.ABC):

    @abc.abstractmethod
    async def ListVersions(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.version_pb2.ListVersionsRequest, google.cloud.dialogflow.v2beta1.version_pb2.ListVersionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetVersion(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.version_pb2.GetVersionRequest, google.cloud.dialogflow.v2beta1.version_pb2.Version]') -> None:
        pass

    @abc.abstractmethod
    async def CreateVersion(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.version_pb2.CreateVersionRequest, google.cloud.dialogflow.v2beta1.version_pb2.Version]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateVersion(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.version_pb2.UpdateVersionRequest, google.cloud.dialogflow.v2beta1.version_pb2.Version]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteVersion(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.version_pb2.DeleteVersionRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dialogflow.v2beta1.Versions/ListVersions': grpclib.const.Handler(
                self.ListVersions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.version_pb2.ListVersionsRequest,
                google.cloud.dialogflow.v2beta1.version_pb2.ListVersionsResponse,
            ),
            '/google.cloud.dialogflow.v2beta1.Versions/GetVersion': grpclib.const.Handler(
                self.GetVersion,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.version_pb2.GetVersionRequest,
                google.cloud.dialogflow.v2beta1.version_pb2.Version,
            ),
            '/google.cloud.dialogflow.v2beta1.Versions/CreateVersion': grpclib.const.Handler(
                self.CreateVersion,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.version_pb2.CreateVersionRequest,
                google.cloud.dialogflow.v2beta1.version_pb2.Version,
            ),
            '/google.cloud.dialogflow.v2beta1.Versions/UpdateVersion': grpclib.const.Handler(
                self.UpdateVersion,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.version_pb2.UpdateVersionRequest,
                google.cloud.dialogflow.v2beta1.version_pb2.Version,
            ),
            '/google.cloud.dialogflow.v2beta1.Versions/DeleteVersion': grpclib.const.Handler(
                self.DeleteVersion,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.version_pb2.DeleteVersionRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class VersionsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListVersions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Versions/ListVersions',
            google.cloud.dialogflow.v2beta1.version_pb2.ListVersionsRequest,
            google.cloud.dialogflow.v2beta1.version_pb2.ListVersionsResponse,
        )
        self.GetVersion = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Versions/GetVersion',
            google.cloud.dialogflow.v2beta1.version_pb2.GetVersionRequest,
            google.cloud.dialogflow.v2beta1.version_pb2.Version,
        )
        self.CreateVersion = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Versions/CreateVersion',
            google.cloud.dialogflow.v2beta1.version_pb2.CreateVersionRequest,
            google.cloud.dialogflow.v2beta1.version_pb2.Version,
        )
        self.UpdateVersion = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Versions/UpdateVersion',
            google.cloud.dialogflow.v2beta1.version_pb2.UpdateVersionRequest,
            google.cloud.dialogflow.v2beta1.version_pb2.Version,
        )
        self.DeleteVersion = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Versions/DeleteVersion',
            google.cloud.dialogflow.v2beta1.version_pb2.DeleteVersionRequest,
            google.protobuf.empty_pb2.Empty,
        )
