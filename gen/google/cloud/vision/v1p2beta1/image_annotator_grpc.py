# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/vision/v1p2beta1/image_annotator.proto
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
import google.cloud.vision.v1p2beta1.geometry_pb2
import google.cloud.vision.v1p2beta1.text_annotation_pb2
import google.cloud.vision.v1p2beta1.web_detection_pb2
import google.longrunning.operations_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import google.type.color_pb2
import google.type.latlng_pb2
import google.cloud.vision.v1p2beta1.image_annotator_pb2


class ImageAnnotatorBase(abc.ABC):

    @abc.abstractmethod
    async def BatchAnnotateImages(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p2beta1.image_annotator_pb2.BatchAnnotateImagesRequest, google.cloud.vision.v1p2beta1.image_annotator_pb2.BatchAnnotateImagesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AsyncBatchAnnotateFiles(self, stream: 'grpclib.server.Stream[google.cloud.vision.v1p2beta1.image_annotator_pb2.AsyncBatchAnnotateFilesRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.vision.v1p2beta1.ImageAnnotator/BatchAnnotateImages': grpclib.const.Handler(
                self.BatchAnnotateImages,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p2beta1.image_annotator_pb2.BatchAnnotateImagesRequest,
                google.cloud.vision.v1p2beta1.image_annotator_pb2.BatchAnnotateImagesResponse,
            ),
            '/google.cloud.vision.v1p2beta1.ImageAnnotator/AsyncBatchAnnotateFiles': grpclib.const.Handler(
                self.AsyncBatchAnnotateFiles,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.vision.v1p2beta1.image_annotator_pb2.AsyncBatchAnnotateFilesRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class ImageAnnotatorStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.BatchAnnotateImages = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p2beta1.ImageAnnotator/BatchAnnotateImages',
            google.cloud.vision.v1p2beta1.image_annotator_pb2.BatchAnnotateImagesRequest,
            google.cloud.vision.v1p2beta1.image_annotator_pb2.BatchAnnotateImagesResponse,
        )
        self.AsyncBatchAnnotateFiles = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.vision.v1p2beta1.ImageAnnotator/AsyncBatchAnnotateFiles',
            google.cloud.vision.v1p2beta1.image_annotator_pb2.AsyncBatchAnnotateFilesRequest,
            google.longrunning.operations_pb2.Operation,
        )
