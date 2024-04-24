import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import provisioning

class ProvisioningServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetSmartMachineStatus(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.GetSmartMachineStatusRequest, provisioning.v1.provisioning_pb2.GetSmartMachineStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetNetworkCredentials(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.SetNetworkCredentialsRequest, provisioning.v1.provisioning_pb2.SetNetworkCredentialsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetSmartMachineCredentials(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.SetSmartMachineCredentialsRequest, provisioning.v1.provisioning_pb2.SetSmartMachineCredentialsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetNetworkList(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.GetNetworkListRequest, provisioning.v1.provisioning_pb2.GetNetworkListResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.provisioning.v1.ProvisioningService/GetSmartMachineStatus': grpclib.const.Handler(self.GetSmartMachineStatus, grpclib.const.Cardinality.UNARY_UNARY, provisioning.v1.provisioning_pb2.GetSmartMachineStatusRequest, provisioning.v1.provisioning_pb2.GetSmartMachineStatusResponse), '/viam.provisioning.v1.ProvisioningService/SetNetworkCredentials': grpclib.const.Handler(self.SetNetworkCredentials, grpclib.const.Cardinality.UNARY_UNARY, provisioning.v1.provisioning_pb2.SetNetworkCredentialsRequest, provisioning.v1.provisioning_pb2.SetNetworkCredentialsResponse), '/viam.provisioning.v1.ProvisioningService/SetSmartMachineCredentials': grpclib.const.Handler(self.SetSmartMachineCredentials, grpclib.const.Cardinality.UNARY_UNARY, provisioning.v1.provisioning_pb2.SetSmartMachineCredentialsRequest, provisioning.v1.provisioning_pb2.SetSmartMachineCredentialsResponse), '/viam.provisioning.v1.ProvisioningService/GetNetworkList': grpclib.const.Handler(self.GetNetworkList, grpclib.const.Cardinality.UNARY_UNARY, provisioning.v1.provisioning_pb2.GetNetworkListRequest, provisioning.v1.provisioning_pb2.GetNetworkListResponse)}

class UnimplementedProvisioningServiceBase(ProvisioningServiceBase):

    async def GetSmartMachineStatus(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.GetSmartMachineStatusRequest, provisioning.v1.provisioning_pb2.GetSmartMachineStatusResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetNetworkCredentials(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.SetNetworkCredentialsRequest, provisioning.v1.provisioning_pb2.SetNetworkCredentialsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetSmartMachineCredentials(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.SetSmartMachineCredentialsRequest, provisioning.v1.provisioning_pb2.SetSmartMachineCredentialsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetNetworkList(self, stream: 'grpclib.server.Stream[provisioning.v1.provisioning_pb2.GetNetworkListRequest, provisioning.v1.provisioning_pb2.GetNetworkListResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class ProvisioningServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetSmartMachineStatus = grpclib.client.UnaryUnaryMethod(channel, '/viam.provisioning.v1.ProvisioningService/GetSmartMachineStatus', provisioning.v1.provisioning_pb2.GetSmartMachineStatusRequest, provisioning.v1.provisioning_pb2.GetSmartMachineStatusResponse)
        self.SetNetworkCredentials = grpclib.client.UnaryUnaryMethod(channel, '/viam.provisioning.v1.ProvisioningService/SetNetworkCredentials', provisioning.v1.provisioning_pb2.SetNetworkCredentialsRequest, provisioning.v1.provisioning_pb2.SetNetworkCredentialsResponse)
        self.SetSmartMachineCredentials = grpclib.client.UnaryUnaryMethod(channel, '/viam.provisioning.v1.ProvisioningService/SetSmartMachineCredentials', provisioning.v1.provisioning_pb2.SetSmartMachineCredentialsRequest, provisioning.v1.provisioning_pb2.SetSmartMachineCredentialsResponse)
        self.GetNetworkList = grpclib.client.UnaryUnaryMethod(channel, '/viam.provisioning.v1.ProvisioningService/GetNetworkList', provisioning.v1.provisioning_pb2.GetNetworkListRequest, provisioning.v1.provisioning_pb2.GetNetworkListResponse)