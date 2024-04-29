import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.timestamp_pb2
from .... import app

class DatasetServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateDataset(self, stream: 'grpclib.server.Stream[app.dataset.v1.dataset_pb2.CreateDatasetRequest, app.dataset.v1.dataset_pb2.CreateDatasetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteDataset(self, stream: 'grpclib.server.Stream[app.dataset.v1.dataset_pb2.DeleteDatasetRequest, app.dataset.v1.dataset_pb2.DeleteDatasetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RenameDataset(self, stream: 'grpclib.server.Stream[app.dataset.v1.dataset_pb2.RenameDatasetRequest, app.dataset.v1.dataset_pb2.RenameDatasetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListDatasetsByOrganizationID(self, stream: 'grpclib.server.Stream[app.dataset.v1.dataset_pb2.ListDatasetsByOrganizationIDRequest, app.dataset.v1.dataset_pb2.ListDatasetsByOrganizationIDResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListDatasetsByIDs(self, stream: 'grpclib.server.Stream[app.dataset.v1.dataset_pb2.ListDatasetsByIDsRequest, app.dataset.v1.dataset_pb2.ListDatasetsByIDsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.dataset.v1.DatasetService/CreateDataset': grpclib.const.Handler(self.CreateDataset, grpclib.const.Cardinality.UNARY_UNARY, app.dataset.v1.dataset_pb2.CreateDatasetRequest, app.dataset.v1.dataset_pb2.CreateDatasetResponse), '/viam.app.dataset.v1.DatasetService/DeleteDataset': grpclib.const.Handler(self.DeleteDataset, grpclib.const.Cardinality.UNARY_UNARY, app.dataset.v1.dataset_pb2.DeleteDatasetRequest, app.dataset.v1.dataset_pb2.DeleteDatasetResponse), '/viam.app.dataset.v1.DatasetService/RenameDataset': grpclib.const.Handler(self.RenameDataset, grpclib.const.Cardinality.UNARY_UNARY, app.dataset.v1.dataset_pb2.RenameDatasetRequest, app.dataset.v1.dataset_pb2.RenameDatasetResponse), '/viam.app.dataset.v1.DatasetService/ListDatasetsByOrganizationID': grpclib.const.Handler(self.ListDatasetsByOrganizationID, grpclib.const.Cardinality.UNARY_UNARY, app.dataset.v1.dataset_pb2.ListDatasetsByOrganizationIDRequest, app.dataset.v1.dataset_pb2.ListDatasetsByOrganizationIDResponse), '/viam.app.dataset.v1.DatasetService/ListDatasetsByIDs': grpclib.const.Handler(self.ListDatasetsByIDs, grpclib.const.Cardinality.UNARY_UNARY, app.dataset.v1.dataset_pb2.ListDatasetsByIDsRequest, app.dataset.v1.dataset_pb2.ListDatasetsByIDsResponse)}

class UnimplementedDatasetServiceBase(DatasetServiceBase):

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

class DatasetServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateDataset = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.dataset.v1.DatasetService/CreateDataset', app.dataset.v1.dataset_pb2.CreateDatasetRequest, app.dataset.v1.dataset_pb2.CreateDatasetResponse)
        self.DeleteDataset = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.dataset.v1.DatasetService/DeleteDataset', app.dataset.v1.dataset_pb2.DeleteDatasetRequest, app.dataset.v1.dataset_pb2.DeleteDatasetResponse)
        self.RenameDataset = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.dataset.v1.DatasetService/RenameDataset', app.dataset.v1.dataset_pb2.RenameDatasetRequest, app.dataset.v1.dataset_pb2.RenameDatasetResponse)
        self.ListDatasetsByOrganizationID = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.dataset.v1.DatasetService/ListDatasetsByOrganizationID', app.dataset.v1.dataset_pb2.ListDatasetsByOrganizationIDRequest, app.dataset.v1.dataset_pb2.ListDatasetsByOrganizationIDResponse)
        self.ListDatasetsByIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.dataset.v1.DatasetService/ListDatasetsByIDs', app.dataset.v1.dataset_pb2.ListDatasetsByIDsRequest, app.dataset.v1.dataset_pb2.ListDatasetsByIDsResponse)