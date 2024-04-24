import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import app
from .packages_grpc import PackageServiceBase as _PackageServiceBase

class UnimplementedPackageServiceBase(_PackageServiceBase):

    async def CreatePackage(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.CreatePackageRequest, app.packages.v1.packages_pb2.CreatePackageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeletePackage(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.DeletePackageRequest, app.packages.v1.packages_pb2.DeletePackageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPackage(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.GetPackageRequest, app.packages.v1.packages_pb2.GetPackageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListPackages(self, stream: 'grpclib.server.Stream[app.packages.v1.packages_pb2.ListPackagesRequest, app.packages.v1.packages_pb2.ListPackagesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)