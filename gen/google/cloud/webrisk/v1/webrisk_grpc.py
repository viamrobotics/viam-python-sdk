# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/webrisk/v1/webrisk.proto
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
import google.protobuf.timestamp_pb2
import google.cloud.webrisk.v1.webrisk_pb2


class WebRiskServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ComputeThreatListDiff(self, stream: 'grpclib.server.Stream[google.cloud.webrisk.v1.webrisk_pb2.ComputeThreatListDiffRequest, google.cloud.webrisk.v1.webrisk_pb2.ComputeThreatListDiffResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SearchUris(self, stream: 'grpclib.server.Stream[google.cloud.webrisk.v1.webrisk_pb2.SearchUrisRequest, google.cloud.webrisk.v1.webrisk_pb2.SearchUrisResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SearchHashes(self, stream: 'grpclib.server.Stream[google.cloud.webrisk.v1.webrisk_pb2.SearchHashesRequest, google.cloud.webrisk.v1.webrisk_pb2.SearchHashesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateSubmission(self, stream: 'grpclib.server.Stream[google.cloud.webrisk.v1.webrisk_pb2.CreateSubmissionRequest, google.cloud.webrisk.v1.webrisk_pb2.Submission]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.webrisk.v1.WebRiskService/ComputeThreatListDiff': grpclib.const.Handler(
                self.ComputeThreatListDiff,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.webrisk.v1.webrisk_pb2.ComputeThreatListDiffRequest,
                google.cloud.webrisk.v1.webrisk_pb2.ComputeThreatListDiffResponse,
            ),
            '/google.cloud.webrisk.v1.WebRiskService/SearchUris': grpclib.const.Handler(
                self.SearchUris,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.webrisk.v1.webrisk_pb2.SearchUrisRequest,
                google.cloud.webrisk.v1.webrisk_pb2.SearchUrisResponse,
            ),
            '/google.cloud.webrisk.v1.WebRiskService/SearchHashes': grpclib.const.Handler(
                self.SearchHashes,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.webrisk.v1.webrisk_pb2.SearchHashesRequest,
                google.cloud.webrisk.v1.webrisk_pb2.SearchHashesResponse,
            ),
            '/google.cloud.webrisk.v1.WebRiskService/CreateSubmission': grpclib.const.Handler(
                self.CreateSubmission,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.webrisk.v1.webrisk_pb2.CreateSubmissionRequest,
                google.cloud.webrisk.v1.webrisk_pb2.Submission,
            ),
        }


class WebRiskServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ComputeThreatListDiff = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.webrisk.v1.WebRiskService/ComputeThreatListDiff',
            google.cloud.webrisk.v1.webrisk_pb2.ComputeThreatListDiffRequest,
            google.cloud.webrisk.v1.webrisk_pb2.ComputeThreatListDiffResponse,
        )
        self.SearchUris = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.webrisk.v1.WebRiskService/SearchUris',
            google.cloud.webrisk.v1.webrisk_pb2.SearchUrisRequest,
            google.cloud.webrisk.v1.webrisk_pb2.SearchUrisResponse,
        )
        self.SearchHashes = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.webrisk.v1.WebRiskService/SearchHashes',
            google.cloud.webrisk.v1.webrisk_pb2.SearchHashesRequest,
            google.cloud.webrisk.v1.webrisk_pb2.SearchHashesResponse,
        )
        self.CreateSubmission = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.webrisk.v1.WebRiskService/CreateSubmission',
            google.cloud.webrisk.v1.webrisk_pb2.CreateSubmissionRequest,
            google.cloud.webrisk.v1.webrisk_pb2.Submission,
        )
