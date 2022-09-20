import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import service

class ShellServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Shell(self, stream: 'grpclib.server.Stream[service.shell.v1.shell_pb2.ShellRequest, service.shell.v1.shell_pb2.ShellResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.shell.v1.ShellService/Shell': grpclib.const.Handler(self.Shell, grpclib.const.Cardinality.STREAM_STREAM, service.shell.v1.shell_pb2.ShellRequest, service.shell.v1.shell_pb2.ShellResponse)}

class ShellServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Shell = grpclib.client.StreamStreamMethod(channel, '/viam.service.shell.v1.ShellService/Shell', service.shell.v1.shell_pb2.ShellRequest, service.shell.v1.shell_pb2.ShellResponse)