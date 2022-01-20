# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/sql/v1/cloud_sql_tiers.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.cloud.sql.v1.cloud_sql_tiers_pb2


class SqlTiersServiceBase(abc.ABC):

    @abc.abstractmethod
    async def List(self, stream: 'grpclib.server.Stream[google.cloud.sql.v1.cloud_sql_tiers_pb2.SqlTiersListRequest, google.cloud.sql.v1.cloud_sql_tiers_pb2.TiersListResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.sql.v1.SqlTiersService/List': grpclib.const.Handler(
                self.List,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.sql.v1.cloud_sql_tiers_pb2.SqlTiersListRequest,
                google.cloud.sql.v1.cloud_sql_tiers_pb2.TiersListResponse,
            ),
        }


class SqlTiersServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.List = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.sql.v1.SqlTiersService/List',
            google.cloud.sql.v1.cloud_sql_tiers_pb2.SqlTiersListRequest,
            google.cloud.sql.v1.cloud_sql_tiers_pb2.TiersListResponse,
        )
