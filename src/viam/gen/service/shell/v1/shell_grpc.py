import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import service

class ShellServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Shell(self, stream: 'grpclib.server.Stream[service.shell.v1.shell_pb2.ShellRequest, service.shell.v1.shell_pb2.ShellResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CopyFilesToMachine(self, stream: 'grpclib.server.Stream[service.shell.v1.shell_pb2.CopyFilesToMachineRequest, service.shell.v1.shell_pb2.CopyFilesToMachineResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CopyFilesFromMachine(self, stream: 'grpclib.server.Stream[service.shell.v1.shell_pb2.CopyFilesFromMachineRequest, service.shell.v1.shell_pb2.CopyFilesFromMachineResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.shell.v1.ShellService/Shell': grpclib.const.Handler(self.Shell, grpclib.const.Cardinality.STREAM_STREAM, service.shell.v1.shell_pb2.ShellRequest, service.shell.v1.shell_pb2.ShellResponse), '/viam.service.shell.v1.ShellService/CopyFilesToMachine': grpclib.const.Handler(self.CopyFilesToMachine, grpclib.const.Cardinality.STREAM_STREAM, service.shell.v1.shell_pb2.CopyFilesToMachineRequest, service.shell.v1.shell_pb2.CopyFilesToMachineResponse), '/viam.service.shell.v1.ShellService/CopyFilesFromMachine': grpclib.const.Handler(self.CopyFilesFromMachine, grpclib.const.Cardinality.STREAM_STREAM, service.shell.v1.shell_pb2.CopyFilesFromMachineRequest, service.shell.v1.shell_pb2.CopyFilesFromMachineResponse), '/viam.service.shell.v1.ShellService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedShellServiceBase(ShellServiceBase):

    async def Shell(self, stream: 'grpclib.server.Stream[service.shell.v1.shell_pb2.ShellRequest, service.shell.v1.shell_pb2.ShellResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CopyFilesToMachine(self, stream: 'grpclib.server.Stream[service.shell.v1.shell_pb2.CopyFilesToMachineRequest, service.shell.v1.shell_pb2.CopyFilesToMachineResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CopyFilesFromMachine(self, stream: 'grpclib.server.Stream[service.shell.v1.shell_pb2.CopyFilesFromMachineRequest, service.shell.v1.shell_pb2.CopyFilesFromMachineResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class ShellServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Shell = grpclib.client.StreamStreamMethod(channel, '/viam.service.shell.v1.ShellService/Shell', service.shell.v1.shell_pb2.ShellRequest, service.shell.v1.shell_pb2.ShellResponse)
        self.CopyFilesToMachine = grpclib.client.StreamStreamMethod(channel, '/viam.service.shell.v1.ShellService/CopyFilesToMachine', service.shell.v1.shell_pb2.CopyFilesToMachineRequest, service.shell.v1.shell_pb2.CopyFilesToMachineResponse)
        self.CopyFilesFromMachine = grpclib.client.StreamStreamMethod(channel, '/viam.service.shell.v1.ShellService/CopyFilesFromMachine', service.shell.v1.shell_pb2.CopyFilesFromMachineRequest, service.shell.v1.shell_pb2.CopyFilesFromMachineResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.shell.v1.ShellService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)