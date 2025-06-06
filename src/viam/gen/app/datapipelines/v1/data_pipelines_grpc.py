import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import app
import google.protobuf.timestamp_pb2

class DataPipelinesServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.GetDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.GetDataPipelineResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListDataPipelines(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.ListDataPipelinesRequest, app.datapipelines.v1.data_pipelines_pb2.ListDataPipelinesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.CreateDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.CreateDataPipelineResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.UpdateDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.UpdateDataPipelineResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.DeleteDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.DeleteDataPipelineResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EnableDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.EnableDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.EnableDataPipelineResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DisableDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.DisableDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.DisableDataPipelineResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListDataPipelineRuns(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.ListDataPipelineRunsRequest, app.datapipelines.v1.data_pipelines_pb2.ListDataPipelineRunsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.datapipelines.v1.DataPipelinesService/GetDataPipeline': grpclib.const.Handler(self.GetDataPipeline, grpclib.const.Cardinality.UNARY_UNARY, app.datapipelines.v1.data_pipelines_pb2.GetDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.GetDataPipelineResponse), '/viam.app.datapipelines.v1.DataPipelinesService/ListDataPipelines': grpclib.const.Handler(self.ListDataPipelines, grpclib.const.Cardinality.UNARY_UNARY, app.datapipelines.v1.data_pipelines_pb2.ListDataPipelinesRequest, app.datapipelines.v1.data_pipelines_pb2.ListDataPipelinesResponse), '/viam.app.datapipelines.v1.DataPipelinesService/CreateDataPipeline': grpclib.const.Handler(self.CreateDataPipeline, grpclib.const.Cardinality.UNARY_UNARY, app.datapipelines.v1.data_pipelines_pb2.CreateDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.CreateDataPipelineResponse), '/viam.app.datapipelines.v1.DataPipelinesService/UpdateDataPipeline': grpclib.const.Handler(self.UpdateDataPipeline, grpclib.const.Cardinality.UNARY_UNARY, app.datapipelines.v1.data_pipelines_pb2.UpdateDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.UpdateDataPipelineResponse), '/viam.app.datapipelines.v1.DataPipelinesService/DeleteDataPipeline': grpclib.const.Handler(self.DeleteDataPipeline, grpclib.const.Cardinality.UNARY_UNARY, app.datapipelines.v1.data_pipelines_pb2.DeleteDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.DeleteDataPipelineResponse), '/viam.app.datapipelines.v1.DataPipelinesService/EnableDataPipeline': grpclib.const.Handler(self.EnableDataPipeline, grpclib.const.Cardinality.UNARY_UNARY, app.datapipelines.v1.data_pipelines_pb2.EnableDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.EnableDataPipelineResponse), '/viam.app.datapipelines.v1.DataPipelinesService/DisableDataPipeline': grpclib.const.Handler(self.DisableDataPipeline, grpclib.const.Cardinality.UNARY_UNARY, app.datapipelines.v1.data_pipelines_pb2.DisableDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.DisableDataPipelineResponse), '/viam.app.datapipelines.v1.DataPipelinesService/ListDataPipelineRuns': grpclib.const.Handler(self.ListDataPipelineRuns, grpclib.const.Cardinality.UNARY_UNARY, app.datapipelines.v1.data_pipelines_pb2.ListDataPipelineRunsRequest, app.datapipelines.v1.data_pipelines_pb2.ListDataPipelineRunsResponse)}

class UnimplementedDataPipelinesServiceBase(DataPipelinesServiceBase):

    async def GetDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.GetDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.GetDataPipelineResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListDataPipelines(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.ListDataPipelinesRequest, app.datapipelines.v1.data_pipelines_pb2.ListDataPipelinesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.CreateDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.CreateDataPipelineResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.UpdateDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.UpdateDataPipelineResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.DeleteDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.DeleteDataPipelineResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EnableDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.EnableDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.EnableDataPipelineResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DisableDataPipeline(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.DisableDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.DisableDataPipelineResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListDataPipelineRuns(self, stream: 'grpclib.server.Stream[app.datapipelines.v1.data_pipelines_pb2.ListDataPipelineRunsRequest, app.datapipelines.v1.data_pipelines_pb2.ListDataPipelineRunsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class DataPipelinesServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetDataPipeline = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.datapipelines.v1.DataPipelinesService/GetDataPipeline', app.datapipelines.v1.data_pipelines_pb2.GetDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.GetDataPipelineResponse)
        self.ListDataPipelines = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.datapipelines.v1.DataPipelinesService/ListDataPipelines', app.datapipelines.v1.data_pipelines_pb2.ListDataPipelinesRequest, app.datapipelines.v1.data_pipelines_pb2.ListDataPipelinesResponse)
        self.CreateDataPipeline = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.datapipelines.v1.DataPipelinesService/CreateDataPipeline', app.datapipelines.v1.data_pipelines_pb2.CreateDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.CreateDataPipelineResponse)
        self.UpdateDataPipeline = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.datapipelines.v1.DataPipelinesService/UpdateDataPipeline', app.datapipelines.v1.data_pipelines_pb2.UpdateDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.UpdateDataPipelineResponse)
        self.DeleteDataPipeline = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.datapipelines.v1.DataPipelinesService/DeleteDataPipeline', app.datapipelines.v1.data_pipelines_pb2.DeleteDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.DeleteDataPipelineResponse)
        self.EnableDataPipeline = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.datapipelines.v1.DataPipelinesService/EnableDataPipeline', app.datapipelines.v1.data_pipelines_pb2.EnableDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.EnableDataPipelineResponse)
        self.DisableDataPipeline = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.datapipelines.v1.DataPipelinesService/DisableDataPipeline', app.datapipelines.v1.data_pipelines_pb2.DisableDataPipelineRequest, app.datapipelines.v1.data_pipelines_pb2.DisableDataPipelineResponse)
        self.ListDataPipelineRuns = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.datapipelines.v1.DataPipelinesService/ListDataPipelineRuns', app.datapipelines.v1.data_pipelines_pb2.ListDataPipelineRunsRequest, app.datapipelines.v1.data_pipelines_pb2.ListDataPipelineRunsResponse)