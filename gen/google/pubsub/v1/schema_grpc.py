# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/pubsub/v1/schema.proto
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
import google.pubsub.v1.schema_pb2


class SchemaServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateSchema(self, stream: 'grpclib.server.Stream[google.pubsub.v1.schema_pb2.CreateSchemaRequest, google.pubsub.v1.schema_pb2.Schema]') -> None:
        pass

    @abc.abstractmethod
    async def GetSchema(self, stream: 'grpclib.server.Stream[google.pubsub.v1.schema_pb2.GetSchemaRequest, google.pubsub.v1.schema_pb2.Schema]') -> None:
        pass

    @abc.abstractmethod
    async def ListSchemas(self, stream: 'grpclib.server.Stream[google.pubsub.v1.schema_pb2.ListSchemasRequest, google.pubsub.v1.schema_pb2.ListSchemasResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteSchema(self, stream: 'grpclib.server.Stream[google.pubsub.v1.schema_pb2.DeleteSchemaRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ValidateSchema(self, stream: 'grpclib.server.Stream[google.pubsub.v1.schema_pb2.ValidateSchemaRequest, google.pubsub.v1.schema_pb2.ValidateSchemaResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ValidateMessage(self, stream: 'grpclib.server.Stream[google.pubsub.v1.schema_pb2.ValidateMessageRequest, google.pubsub.v1.schema_pb2.ValidateMessageResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.pubsub.v1.SchemaService/CreateSchema': grpclib.const.Handler(
                self.CreateSchema,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.schema_pb2.CreateSchemaRequest,
                google.pubsub.v1.schema_pb2.Schema,
            ),
            '/google.pubsub.v1.SchemaService/GetSchema': grpclib.const.Handler(
                self.GetSchema,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.schema_pb2.GetSchemaRequest,
                google.pubsub.v1.schema_pb2.Schema,
            ),
            '/google.pubsub.v1.SchemaService/ListSchemas': grpclib.const.Handler(
                self.ListSchemas,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.schema_pb2.ListSchemasRequest,
                google.pubsub.v1.schema_pb2.ListSchemasResponse,
            ),
            '/google.pubsub.v1.SchemaService/DeleteSchema': grpclib.const.Handler(
                self.DeleteSchema,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.schema_pb2.DeleteSchemaRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.pubsub.v1.SchemaService/ValidateSchema': grpclib.const.Handler(
                self.ValidateSchema,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.schema_pb2.ValidateSchemaRequest,
                google.pubsub.v1.schema_pb2.ValidateSchemaResponse,
            ),
            '/google.pubsub.v1.SchemaService/ValidateMessage': grpclib.const.Handler(
                self.ValidateMessage,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.pubsub.v1.schema_pb2.ValidateMessageRequest,
                google.pubsub.v1.schema_pb2.ValidateMessageResponse,
            ),
        }


class SchemaServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateSchema = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.SchemaService/CreateSchema',
            google.pubsub.v1.schema_pb2.CreateSchemaRequest,
            google.pubsub.v1.schema_pb2.Schema,
        )
        self.GetSchema = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.SchemaService/GetSchema',
            google.pubsub.v1.schema_pb2.GetSchemaRequest,
            google.pubsub.v1.schema_pb2.Schema,
        )
        self.ListSchemas = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.SchemaService/ListSchemas',
            google.pubsub.v1.schema_pb2.ListSchemasRequest,
            google.pubsub.v1.schema_pb2.ListSchemasResponse,
        )
        self.DeleteSchema = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.SchemaService/DeleteSchema',
            google.pubsub.v1.schema_pb2.DeleteSchemaRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ValidateSchema = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.SchemaService/ValidateSchema',
            google.pubsub.v1.schema_pb2.ValidateSchemaRequest,
            google.pubsub.v1.schema_pb2.ValidateSchemaResponse,
        )
        self.ValidateMessage = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.pubsub.v1.SchemaService/ValidateMessage',
            google.pubsub.v1.schema_pb2.ValidateMessageRequest,
            google.pubsub.v1.schema_pb2.ValidateMessageResponse,
        )
