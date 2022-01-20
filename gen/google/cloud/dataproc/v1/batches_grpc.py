# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dataproc/v1/batches.proto
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
import google.cloud.dataproc.v1.shared_pb2
import google.longrunning.operations_pb2
import google.protobuf.empty_pb2
import google.protobuf.timestamp_pb2
import google.cloud.dataproc.v1.batches_pb2


class BatchControllerBase(abc.ABC):

    @abc.abstractmethod
    async def CreateBatch(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.batches_pb2.CreateBatchRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetBatch(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.batches_pb2.GetBatchRequest, google.cloud.dataproc.v1.batches_pb2.Batch]') -> None:
        pass

    @abc.abstractmethod
    async def ListBatches(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.batches_pb2.ListBatchesRequest, google.cloud.dataproc.v1.batches_pb2.ListBatchesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteBatch(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.batches_pb2.DeleteBatchRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dataproc.v1.BatchController/CreateBatch': grpclib.const.Handler(
                self.CreateBatch,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.batches_pb2.CreateBatchRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dataproc.v1.BatchController/GetBatch': grpclib.const.Handler(
                self.GetBatch,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.batches_pb2.GetBatchRequest,
                google.cloud.dataproc.v1.batches_pb2.Batch,
            ),
            '/google.cloud.dataproc.v1.BatchController/ListBatches': grpclib.const.Handler(
                self.ListBatches,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.batches_pb2.ListBatchesRequest,
                google.cloud.dataproc.v1.batches_pb2.ListBatchesResponse,
            ),
            '/google.cloud.dataproc.v1.BatchController/DeleteBatch': grpclib.const.Handler(
                self.DeleteBatch,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.batches_pb2.DeleteBatchRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class BatchControllerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateBatch = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.BatchController/CreateBatch',
            google.cloud.dataproc.v1.batches_pb2.CreateBatchRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetBatch = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.BatchController/GetBatch',
            google.cloud.dataproc.v1.batches_pb2.GetBatchRequest,
            google.cloud.dataproc.v1.batches_pb2.Batch,
        )
        self.ListBatches = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.BatchController/ListBatches',
            google.cloud.dataproc.v1.batches_pb2.ListBatchesRequest,
            google.cloud.dataproc.v1.batches_pb2.ListBatchesResponse,
        )
        self.DeleteBatch = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.BatchController/DeleteBatch',
            google.cloud.dataproc.v1.batches_pb2.DeleteBatchRequest,
            google.protobuf.empty_pb2.Empty,
        )
