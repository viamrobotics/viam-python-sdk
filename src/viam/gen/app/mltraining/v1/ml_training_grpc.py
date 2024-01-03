import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
from .... import tagger
from .... import app

class MLTrainingServiceBase(abc.ABC):

    @abc.abstractmethod
    async def SubmitTrainingJob(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.SubmitTrainingJobRequest, app.mltraining.v1.ml_training_pb2.SubmitTrainingJobResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetTrainingJob(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.GetTrainingJobRequest, app.mltraining.v1.ml_training_pb2.GetTrainingJobResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListTrainingJobs(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.ListTrainingJobsRequest, app.mltraining.v1.ml_training_pb2.ListTrainingJobsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CancelTrainingJob(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.CancelTrainingJobRequest, app.mltraining.v1.ml_training_pb2.CancelTrainingJobResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteCompletedTrainingJob(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.DeleteCompletedTrainingJobRequest, app.mltraining.v1.ml_training_pb2.DeleteCompletedTrainingJobResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.mltraining.v1.MLTrainingService/SubmitTrainingJob': grpclib.const.Handler(self.SubmitTrainingJob, grpclib.const.Cardinality.UNARY_UNARY, app.mltraining.v1.ml_training_pb2.SubmitTrainingJobRequest, app.mltraining.v1.ml_training_pb2.SubmitTrainingJobResponse), '/viam.app.mltraining.v1.MLTrainingService/GetTrainingJob': grpclib.const.Handler(self.GetTrainingJob, grpclib.const.Cardinality.UNARY_UNARY, app.mltraining.v1.ml_training_pb2.GetTrainingJobRequest, app.mltraining.v1.ml_training_pb2.GetTrainingJobResponse), '/viam.app.mltraining.v1.MLTrainingService/ListTrainingJobs': grpclib.const.Handler(self.ListTrainingJobs, grpclib.const.Cardinality.UNARY_UNARY, app.mltraining.v1.ml_training_pb2.ListTrainingJobsRequest, app.mltraining.v1.ml_training_pb2.ListTrainingJobsResponse), '/viam.app.mltraining.v1.MLTrainingService/CancelTrainingJob': grpclib.const.Handler(self.CancelTrainingJob, grpclib.const.Cardinality.UNARY_UNARY, app.mltraining.v1.ml_training_pb2.CancelTrainingJobRequest, app.mltraining.v1.ml_training_pb2.CancelTrainingJobResponse), '/viam.app.mltraining.v1.MLTrainingService/DeleteCompletedTrainingJob': grpclib.const.Handler(self.DeleteCompletedTrainingJob, grpclib.const.Cardinality.UNARY_UNARY, app.mltraining.v1.ml_training_pb2.DeleteCompletedTrainingJobRequest, app.mltraining.v1.ml_training_pb2.DeleteCompletedTrainingJobResponse)}

class MLTrainingServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SubmitTrainingJob = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.mltraining.v1.MLTrainingService/SubmitTrainingJob', app.mltraining.v1.ml_training_pb2.SubmitTrainingJobRequest, app.mltraining.v1.ml_training_pb2.SubmitTrainingJobResponse)
        self.GetTrainingJob = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.mltraining.v1.MLTrainingService/GetTrainingJob', app.mltraining.v1.ml_training_pb2.GetTrainingJobRequest, app.mltraining.v1.ml_training_pb2.GetTrainingJobResponse)
        self.ListTrainingJobs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.mltraining.v1.MLTrainingService/ListTrainingJobs', app.mltraining.v1.ml_training_pb2.ListTrainingJobsRequest, app.mltraining.v1.ml_training_pb2.ListTrainingJobsResponse)
        self.CancelTrainingJob = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.mltraining.v1.MLTrainingService/CancelTrainingJob', app.mltraining.v1.ml_training_pb2.CancelTrainingJobRequest, app.mltraining.v1.ml_training_pb2.CancelTrainingJobResponse)
        self.DeleteCompletedTrainingJob = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.mltraining.v1.MLTrainingService/DeleteCompletedTrainingJob', app.mltraining.v1.ml_training_pb2.DeleteCompletedTrainingJobRequest, app.mltraining.v1.ml_training_pb2.DeleteCompletedTrainingJobResponse)