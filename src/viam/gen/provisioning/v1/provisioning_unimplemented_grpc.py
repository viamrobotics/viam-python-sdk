import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import provisioning
from .provisioning_grpc import ProvisioningServiceBase as _ProvisioningServiceBase

class UnimplementedProvisioningServiceBase(_ProvisioningServiceBase):

    async def GetSmartMachineStatus(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.GetSmartMachineStatusRequest, provisioning.v1.provisioning_pb2.GetSmartMachineStatusResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetNetworkCredentials(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.SetNetworkCredentialsRequest, provisioning.v1.provisioning_pb2.SetNetworkCredentialsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetSmartMachineCredentials(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.SetSmartMachineCredentialsRequest, provisioning.v1.provisioning_pb2.SetSmartMachineCredentialsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetNetworkList(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.GetNetworkListRequest, provisioning.v1.provisioning_pb2.GetNetworkListResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)