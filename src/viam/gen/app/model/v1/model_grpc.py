import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.timestamp_pb2
from .... import app

class ModelServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Upload(self, stream: 'grpclib.server.Stream[app.model.v1.model_pb2.UploadRequest, app.model.v1.model_pb2.UploadResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Delete(self, stream: 'grpclib.server.Stream[app.model.v1.model_pb2.DeleteRequest, app.model.v1.model_pb2.DeleteResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Deploy(self, stream: 'grpclib.server.Stream[app.model.v1.model_pb2.DeployRequest, app.model.v1.model_pb2.DeployResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.model.v1.ModelService/Upload': grpclib.const.Handler(self.Upload, grpclib.const.Cardinality.STREAM_UNARY, app.model.v1.model_pb2.UploadRequest, app.model.v1.model_pb2.UploadResponse), '/viam.app.model.v1.ModelService/Delete': grpclib.const.Handler(self.Delete, grpclib.const.Cardinality.UNARY_UNARY, app.model.v1.model_pb2.DeleteRequest, app.model.v1.model_pb2.DeleteResponse), '/viam.app.model.v1.ModelService/Deploy': grpclib.const.Handler(self.Deploy, grpclib.const.Cardinality.UNARY_UNARY, app.model.v1.model_pb2.DeployRequest, app.model.v1.model_pb2.DeployResponse)}

class ModelServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Upload = grpclib.client.StreamUnaryMethod(channel, '/viam.app.model.v1.ModelService/Upload', app.model.v1.model_pb2.UploadRequest, app.model.v1.model_pb2.UploadResponse)
        self.Delete = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.model.v1.ModelService/Delete', app.model.v1.model_pb2.DeleteRequest, app.model.v1.model_pb2.DeleteResponse)
        self.Deploy = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.model.v1.ModelService/Deploy', app.model.v1.model_pb2.DeployRequest, app.model.v1.model_pb2.DeployResponse)