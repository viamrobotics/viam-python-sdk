# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/sql/v1/cloud_sql_flags.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.cloud.sql.v1.cloud_sql_resources_pb2
import google.protobuf.wrappers_pb2
import google.api.client_pb2
import google.cloud.sql.v1.cloud_sql_flags_pb2


class SqlFlagsServiceBase(abc.ABC):

    @abc.abstractmethod
    async def List(self, stream: 'grpclib.server.Stream[google.cloud.sql.v1.cloud_sql_flags_pb2.SqlFlagsListRequest, google.cloud.sql.v1.cloud_sql_flags_pb2.FlagsListResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.sql.v1.SqlFlagsService/List': grpclib.const.Handler(
                self.List,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.sql.v1.cloud_sql_flags_pb2.SqlFlagsListRequest,
                google.cloud.sql.v1.cloud_sql_flags_pb2.FlagsListResponse,
            ),
        }


class SqlFlagsServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.List = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.sql.v1.SqlFlagsService/List',
            google.cloud.sql.v1.cloud_sql_flags_pb2.SqlFlagsListRequest,
            google.cloud.sql.v1.cloud_sql_flags_pb2.FlagsListResponse,
        )
