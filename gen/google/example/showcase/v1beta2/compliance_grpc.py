# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/example/showcase/v1beta2/compliance.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.example.showcase.v1beta2.compliance_pb2


class ComplianceBase(abc.ABC):

    @abc.abstractmethod
    async def RepeatDataBody(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.compliance_pb2.RepeatRequest, google.example.showcase.v1beta2.compliance_pb2.RepeatResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RepeatDataBodyInfo(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.compliance_pb2.RepeatRequest, google.example.showcase.v1beta2.compliance_pb2.RepeatResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RepeatDataQuery(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.compliance_pb2.RepeatRequest, google.example.showcase.v1beta2.compliance_pb2.RepeatResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RepeatDataSimplePath(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.compliance_pb2.RepeatRequest, google.example.showcase.v1beta2.compliance_pb2.RepeatResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RepeatDataPathResource(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.compliance_pb2.RepeatRequest, google.example.showcase.v1beta2.compliance_pb2.RepeatResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RepeatDataPathTrailingResource(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.compliance_pb2.RepeatRequest, google.example.showcase.v1beta2.compliance_pb2.RepeatResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.example.showcase.v1beta2.Compliance/RepeatDataBody': grpclib.const.Handler(
                self.RepeatDataBody,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
                google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
            ),
            '/google.example.showcase.v1beta2.Compliance/RepeatDataBodyInfo': grpclib.const.Handler(
                self.RepeatDataBodyInfo,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
                google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
            ),
            '/google.example.showcase.v1beta2.Compliance/RepeatDataQuery': grpclib.const.Handler(
                self.RepeatDataQuery,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
                google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
            ),
            '/google.example.showcase.v1beta2.Compliance/RepeatDataSimplePath': grpclib.const.Handler(
                self.RepeatDataSimplePath,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
                google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
            ),
            '/google.example.showcase.v1beta2.Compliance/RepeatDataPathResource': grpclib.const.Handler(
                self.RepeatDataPathResource,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
                google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
            ),
            '/google.example.showcase.v1beta2.Compliance/RepeatDataPathTrailingResource': grpclib.const.Handler(
                self.RepeatDataPathTrailingResource,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
                google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
            ),
        }


class ComplianceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.RepeatDataBody = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Compliance/RepeatDataBody',
            google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
            google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
        )
        self.RepeatDataBodyInfo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Compliance/RepeatDataBodyInfo',
            google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
            google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
        )
        self.RepeatDataQuery = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Compliance/RepeatDataQuery',
            google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
            google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
        )
        self.RepeatDataSimplePath = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Compliance/RepeatDataSimplePath',
            google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
            google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
        )
        self.RepeatDataPathResource = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Compliance/RepeatDataPathResource',
            google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
            google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
        )
        self.RepeatDataPathTrailingResource = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Compliance/RepeatDataPathTrailingResource',
            google.example.showcase.v1beta2.compliance_pb2.RepeatRequest,
            google.example.showcase.v1beta2.compliance_pb2.RepeatResponse,
        )
