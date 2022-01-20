# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/sql/v1/cloud_sql_users.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.field_behavior_pb2
import google.cloud.sql.v1.cloud_sql_resources_pb2
import google.api.client_pb2
import google.cloud.sql.v1.cloud_sql_users_pb2


class SqlUsersServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Delete(self, stream: 'grpclib.server.Stream[google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersDeleteRequest, google.cloud.sql.v1.cloud_sql_resources_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def Insert(self, stream: 'grpclib.server.Stream[google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersInsertRequest, google.cloud.sql.v1.cloud_sql_resources_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def List(self, stream: 'grpclib.server.Stream[google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersListRequest, google.cloud.sql.v1.cloud_sql_users_pb2.UsersListResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Update(self, stream: 'grpclib.server.Stream[google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersUpdateRequest, google.cloud.sql.v1.cloud_sql_resources_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.sql.v1.SqlUsersService/Delete': grpclib.const.Handler(
                self.Delete,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersDeleteRequest,
                google.cloud.sql.v1.cloud_sql_resources_pb2.Operation,
            ),
            '/google.cloud.sql.v1.SqlUsersService/Insert': grpclib.const.Handler(
                self.Insert,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersInsertRequest,
                google.cloud.sql.v1.cloud_sql_resources_pb2.Operation,
            ),
            '/google.cloud.sql.v1.SqlUsersService/List': grpclib.const.Handler(
                self.List,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersListRequest,
                google.cloud.sql.v1.cloud_sql_users_pb2.UsersListResponse,
            ),
            '/google.cloud.sql.v1.SqlUsersService/Update': grpclib.const.Handler(
                self.Update,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersUpdateRequest,
                google.cloud.sql.v1.cloud_sql_resources_pb2.Operation,
            ),
        }


class SqlUsersServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Delete = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.sql.v1.SqlUsersService/Delete',
            google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersDeleteRequest,
            google.cloud.sql.v1.cloud_sql_resources_pb2.Operation,
        )
        self.Insert = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.sql.v1.SqlUsersService/Insert',
            google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersInsertRequest,
            google.cloud.sql.v1.cloud_sql_resources_pb2.Operation,
        )
        self.List = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.sql.v1.SqlUsersService/List',
            google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersListRequest,
            google.cloud.sql.v1.cloud_sql_users_pb2.UsersListResponse,
        )
        self.Update = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.sql.v1.SqlUsersService/Update',
            google.cloud.sql.v1.cloud_sql_users_pb2.SqlUsersUpdateRequest,
            google.cloud.sql.v1.cloud_sql_resources_pb2.Operation,
        )
