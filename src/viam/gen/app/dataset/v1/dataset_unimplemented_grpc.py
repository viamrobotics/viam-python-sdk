import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.timestamp_pb2
from .... import app
from .dataset_grpc import DatasetServiceBase as _DatasetServiceBase

class UnimplementedDatasetServiceBase(_DatasetServiceBase):

    async def CreateDataset(self, stream: 'grpclib.server.Stream[app.dataset.v1.dataset_pb2.CreateDatasetRequest, app.dataset.v1.dataset_pb2.CreateDatasetResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteDataset(self, stream: 'grpclib.server.Stream[app.dataset.v1.dataset_pb2.DeleteDatasetRequest, app.dataset.v1.dataset_pb2.DeleteDatasetResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RenameDataset(self, stream: 'grpclib.server.Stream[app.dataset.v1.dataset_pb2.RenameDatasetRequest, app.dataset.v1.dataset_pb2.RenameDatasetResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListDatasetsByOrganizationID(self, stream: 'grpclib.server.Stream[app.dataset.v1.dataset_pb2.ListDatasetsByOrganizationIDRequest, app.dataset.v1.dataset_pb2.ListDatasetsByOrganizationIDResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListDatasetsByIDs(self, stream: 'grpclib.server.Stream[app.dataset.v1.dataset_pb2.ListDatasetsByIDsRequest, app.dataset.v1.dataset_pb2.ListDatasetsByIDsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)