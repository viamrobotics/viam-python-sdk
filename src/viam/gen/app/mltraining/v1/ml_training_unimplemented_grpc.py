import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
from .... import tagger
from .... import app
from .ml_training_grpc import MLTrainingServiceBase as _MLTrainingServiceBase

class UnimplementedMLTrainingServiceBase(_MLTrainingServiceBase):

    async def SubmitTrainingJob(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.SubmitTrainingJobRequest, app.mltraining.v1.ml_training_pb2.SubmitTrainingJobResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SubmitCustomTrainingJob(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.SubmitCustomTrainingJobRequest, app.mltraining.v1.ml_training_pb2.SubmitCustomTrainingJobResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetTrainingJob(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.GetTrainingJobRequest, app.mltraining.v1.ml_training_pb2.GetTrainingJobResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListTrainingJobs(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.ListTrainingJobsRequest, app.mltraining.v1.ml_training_pb2.ListTrainingJobsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CancelTrainingJob(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.CancelTrainingJobRequest, app.mltraining.v1.ml_training_pb2.CancelTrainingJobResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteCompletedTrainingJob(self, stream: 'grpclib.server.Stream[app.mltraining.v1.ml_training_pb2.DeleteCompletedTrainingJobRequest, app.mltraining.v1.ml_training_pb2.DeleteCompletedTrainingJobResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)