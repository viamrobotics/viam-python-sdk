import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import app

class PackageServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreatePackage(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.CreatePackageRequest, app.packages.v1.packages_pb2.CreatePackageResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeletePackage(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.DeletePackageRequest, app.packages.v1.packages_pb2.DeletePackageResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPackage(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.GetPackageRequest, app.packages.v1.packages_pb2.GetPackageResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListPackages(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.ListPackagesRequest, app.packages.v1.packages_pb2.ListPackagesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.packages.v1.PackageService/CreatePackage': grpclib.const.Handler(self.CreatePackage, grpclib.const.Cardinality.STREAM_UNARY, app.packages.v1.packages_pb2.CreatePackageRequest, app.packages.v1.packages_pb2.CreatePackageResponse), '/viam.app.packages.v1.PackageService/DeletePackage': grpclib.const.Handler(self.DeletePackage, grpclib.const.Cardinality.UNARY_UNARY, app.packages.v1.packages_pb2.DeletePackageRequest, app.packages.v1.packages_pb2.DeletePackageResponse), '/viam.app.packages.v1.PackageService/GetPackage': grpclib.const.Handler(self.GetPackage, grpclib.const.Cardinality.UNARY_UNARY, app.packages.v1.packages_pb2.GetPackageRequest, app.packages.v1.packages_pb2.GetPackageResponse), '/viam.app.packages.v1.PackageService/ListPackages': grpclib.const.Handler(self.ListPackages, grpclib.const.Cardinality.UNARY_UNARY, app.packages.v1.packages_pb2.ListPackagesRequest, app.packages.v1.packages_pb2.ListPackagesResponse)}

class UnimplementedPackageServiceBase(PackageServiceBase):

    async def CreatePackage(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.CreatePackageRequest, app.packages.v1.packages_pb2.CreatePackageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeletePackage(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.DeletePackageRequest, app.packages.v1.packages_pb2.DeletePackageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPackage(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.GetPackageRequest, app.packages.v1.packages_pb2.GetPackageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListPackages(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.ListPackagesRequest, app.packages.v1.packages_pb2.ListPackagesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class PackageServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreatePackage = grpclib.client.StreamUnaryMethod(channel, '/viam.app.packages.v1.PackageService/CreatePackage', app.packages.v1.packages_pb2.CreatePackageRequest, app.packages.v1.packages_pb2.CreatePackageResponse)
        self.DeletePackage = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.packages.v1.PackageService/DeletePackage', app.packages.v1.packages_pb2.DeletePackageRequest, app.packages.v1.packages_pb2.DeletePackageResponse)
        self.GetPackage = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.packages.v1.PackageService/GetPackage', app.packages.v1.packages_pb2.GetPackageRequest, app.packages.v1.packages_pb2.GetPackageResponse)
        self.ListPackages = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.packages.v1.PackageService/ListPackages', app.packages.v1.packages_pb2.ListPackagesRequest, app.packages.v1.packages_pb2.ListPackagesResponse)