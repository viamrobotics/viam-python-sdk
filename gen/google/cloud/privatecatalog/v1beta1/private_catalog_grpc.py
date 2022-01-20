# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/privatecatalog/v1beta1/private_catalog.proto
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
import google.protobuf.any_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.cloud.privatecatalog.v1beta1.private_catalog_pb2


class PrivateCatalogBase(abc.ABC):

    @abc.abstractmethod
    async def SearchCatalogs(self, stream: 'grpclib.server.Stream[google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchCatalogsRequest, google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchCatalogsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SearchProducts(self, stream: 'grpclib.server.Stream[google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchProductsRequest, google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchProductsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SearchVersions(self, stream: 'grpclib.server.Stream[google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchVersionsRequest, google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchVersionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.privatecatalog.v1beta1.PrivateCatalog/SearchCatalogs': grpclib.const.Handler(
                self.SearchCatalogs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchCatalogsRequest,
                google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchCatalogsResponse,
            ),
            '/google.cloud.privatecatalog.v1beta1.PrivateCatalog/SearchProducts': grpclib.const.Handler(
                self.SearchProducts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchProductsRequest,
                google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchProductsResponse,
            ),
            '/google.cloud.privatecatalog.v1beta1.PrivateCatalog/SearchVersions': grpclib.const.Handler(
                self.SearchVersions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchVersionsRequest,
                google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchVersionsResponse,
            ),
        }


class PrivateCatalogStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SearchCatalogs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.privatecatalog.v1beta1.PrivateCatalog/SearchCatalogs',
            google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchCatalogsRequest,
            google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchCatalogsResponse,
        )
        self.SearchProducts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.privatecatalog.v1beta1.PrivateCatalog/SearchProducts',
            google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchProductsRequest,
            google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchProductsResponse,
        )
        self.SearchVersions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.privatecatalog.v1beta1.PrivateCatalog/SearchVersions',
            google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchVersionsRequest,
            google.cloud.privatecatalog.v1beta1.private_catalog_pb2.SearchVersionsResponse,
        )
