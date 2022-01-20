# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/vision/v1p4beta1/product_search_service.proto
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
import google.cloud.vision.v1p4beta1.geometry_pb2
import google.longrunning.operations_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import google.cloud.vision.v1p4beta1.product_search_service_pb2


class ProductSearchBase(abc.ABC):

    @abc.abstractmethod
    async def CreateProductSet(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.CreateProductSetRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.ProductSet]') -> None:
        pass

    @abc.abstractmethod
    async def ListProductSets(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductSetsRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductSetsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProductSet(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.GetProductSetRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.ProductSet]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateProductSet(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.UpdateProductSetRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.ProductSet]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteProductSet(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.DeleteProductSetRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateProduct(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.CreateProductRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.Product]') -> None:
        pass

    @abc.abstractmethod
    async def ListProducts(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProduct(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.GetProductRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.Product]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateProduct(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.UpdateProductRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.Product]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteProduct(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.DeleteProductRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateReferenceImage(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.CreateReferenceImageRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.ReferenceImage]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteReferenceImage(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.DeleteReferenceImageRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ListReferenceImages(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.ListReferenceImagesRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.ListReferenceImagesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetReferenceImage(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.GetReferenceImageRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.ReferenceImage]') -> None:
        pass

    @abc.abstractmethod
    async def AddProductToProductSet(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.AddProductToProductSetRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveProductFromProductSet(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.RemoveProductFromProductSetRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ListProductsInProductSet(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsInProductSetRequest, google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsInProductSetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ImportProductSets(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.ImportProductSetsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def PurgeProducts(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p4beta1.product_search_service_pb2.PurgeProductsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.vision.v1p4beta1.ProductSearch/CreateProductSet': grpclib.const.Handler(
                self.CreateProductSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.CreateProductSetRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ProductSet,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/ListProductSets': grpclib.const.Handler(
                self.ListProductSets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductSetsRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductSetsResponse,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/GetProductSet': grpclib.const.Handler(
                self.GetProductSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.GetProductSetRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ProductSet,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/UpdateProductSet': grpclib.const.Handler(
                self.UpdateProductSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.UpdateProductSetRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ProductSet,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/DeleteProductSet': grpclib.const.Handler(
                self.DeleteProductSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.DeleteProductSetRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/CreateProduct': grpclib.const.Handler(
                self.CreateProduct,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.CreateProductRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.Product,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/ListProducts': grpclib.const.Handler(
                self.ListProducts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsResponse,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/GetProduct': grpclib.const.Handler(
                self.GetProduct,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.GetProductRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.Product,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/UpdateProduct': grpclib.const.Handler(
                self.UpdateProduct,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.UpdateProductRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.Product,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/DeleteProduct': grpclib.const.Handler(
                self.DeleteProduct,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.DeleteProductRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/CreateReferenceImage': grpclib.const.Handler(
                self.CreateReferenceImage,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.CreateReferenceImageRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ReferenceImage,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/DeleteReferenceImage': grpclib.const.Handler(
                self.DeleteReferenceImage,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.DeleteReferenceImageRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/ListReferenceImages': grpclib.const.Handler(
                self.ListReferenceImages,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ListReferenceImagesRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ListReferenceImagesResponse,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/GetReferenceImage': grpclib.const.Handler(
                self.GetReferenceImage,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.GetReferenceImageRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ReferenceImage,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/AddProductToProductSet': grpclib.const.Handler(
                self.AddProductToProductSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.AddProductToProductSetRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/RemoveProductFromProductSet': grpclib.const.Handler(
                self.RemoveProductFromProductSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.RemoveProductFromProductSetRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/ListProductsInProductSet': grpclib.const.Handler(
                self.ListProductsInProductSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsInProductSetRequest,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsInProductSetResponse,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/ImportProductSets': grpclib.const.Handler(
                self.ImportProductSets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.ImportProductSetsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.vision.v1p4beta1.ProductSearch/PurgeProducts': grpclib.const.Handler(
                self.PurgeProducts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p4beta1.product_search_service_pb2.PurgeProductsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class ProductSearchStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateProductSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/CreateProductSet',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.CreateProductSetRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ProductSet,
        )
        self.ListProductSets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/ListProductSets',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductSetsRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductSetsResponse,
        )
        self.GetProductSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/GetProductSet',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.GetProductSetRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ProductSet,
        )
        self.UpdateProductSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/UpdateProductSet',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.UpdateProductSetRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ProductSet,
        )
        self.DeleteProductSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/DeleteProductSet',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.DeleteProductSetRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateProduct = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/CreateProduct',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.CreateProductRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.Product,
        )
        self.ListProducts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/ListProducts',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsResponse,
        )
        self.GetProduct = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/GetProduct',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.GetProductRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.Product,
        )
        self.UpdateProduct = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/UpdateProduct',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.UpdateProductRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.Product,
        )
        self.DeleteProduct = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/DeleteProduct',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.DeleteProductRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateReferenceImage = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/CreateReferenceImage',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.CreateReferenceImageRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ReferenceImage,
        )
        self.DeleteReferenceImage = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/DeleteReferenceImage',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.DeleteReferenceImageRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ListReferenceImages = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/ListReferenceImages',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ListReferenceImagesRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ListReferenceImagesResponse,
        )
        self.GetReferenceImage = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/GetReferenceImage',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.GetReferenceImageRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ReferenceImage,
        )
        self.AddProductToProductSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/AddProductToProductSet',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.AddProductToProductSetRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.RemoveProductFromProductSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/RemoveProductFromProductSet',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.RemoveProductFromProductSetRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ListProductsInProductSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/ListProductsInProductSet',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsInProductSetRequest,
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ListProductsInProductSetResponse,
        )
        self.ImportProductSets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/ImportProductSets',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.ImportProductSetsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.PurgeProducts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p4beta1.ProductSearch/PurgeProducts',
            google.cloud.vision.v1p4beta1.product_search_service_pb2.PurgeProductsRequest,
            google.longrunning.operations_pb2.Operation,
        )
