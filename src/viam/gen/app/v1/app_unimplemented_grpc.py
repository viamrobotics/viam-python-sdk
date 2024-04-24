import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import app
from ... import common
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from ... import tagger
from .app_grpc import AppServiceBase as _AppServiceBase

class UnimplementedAppServiceBase(_AppServiceBase):

    async def GetUserIDByEmail(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetUserIDByEmailRequest, app.v1.app_pb2.GetUserIDByEmailResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateOrganization(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateOrganizationRequest, app.v1.app_pb2.CreateOrganizationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListOrganizations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListOrganizationsRequest, app.v1.app_pb2.ListOrganizationsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetOrganizationsWithAccessToLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetOrganizationsWithAccessToLocationRequest, app.v1.app_pb2.GetOrganizationsWithAccessToLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListOrganizationsByUser(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListOrganizationsByUserRequest, app.v1.app_pb2.ListOrganizationsByUserResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetOrganization(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetOrganizationRequest, app.v1.app_pb2.GetOrganizationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetOrganizationNamespaceAvailability(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetOrganizationNamespaceAvailabilityRequest, app.v1.app_pb2.GetOrganizationNamespaceAvailabilityResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateOrganization(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateOrganizationRequest, app.v1.app_pb2.UpdateOrganizationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteOrganization(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteOrganizationRequest, app.v1.app_pb2.DeleteOrganizationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListOrganizationMembers(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListOrganizationMembersRequest, app.v1.app_pb2.ListOrganizationMembersResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateOrganizationInvite(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateOrganizationInviteRequest, app.v1.app_pb2.CreateOrganizationInviteResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateOrganizationInviteAuthorizations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateOrganizationInviteAuthorizationsRequest, app.v1.app_pb2.UpdateOrganizationInviteAuthorizationsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteOrganizationMember(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteOrganizationMemberRequest, app.v1.app_pb2.DeleteOrganizationMemberResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteOrganizationInvite(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteOrganizationInviteRequest, app.v1.app_pb2.DeleteOrganizationInviteResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ResendOrganizationInvite(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ResendOrganizationInviteRequest, app.v1.app_pb2.ResendOrganizationInviteResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateLocationRequest, app.v1.app_pb2.CreateLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetLocationRequest, app.v1.app_pb2.GetLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateLocationRequest, app.v1.app_pb2.UpdateLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteLocationRequest, app.v1.app_pb2.DeleteLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListLocations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListLocationsRequest, app.v1.app_pb2.ListLocationsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ShareLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ShareLocationRequest, app.v1.app_pb2.ShareLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UnshareLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UnshareLocationRequest, app.v1.app_pb2.UnshareLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def LocationAuth(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.LocationAuthRequest, app.v1.app_pb2.LocationAuthResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateLocationSecret(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateLocationSecretRequest, app.v1.app_pb2.CreateLocationSecretResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteLocationSecret(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteLocationSecretRequest, app.v1.app_pb2.DeleteLocationSecretResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotRequest, app.v1.app_pb2.GetRobotResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetRoverRentalRobots(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRoverRentalRobotsRequest, app.v1.app_pb2.GetRoverRentalRobotsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetRobotParts(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartsRequest, app.v1.app_pb2.GetRobotPartsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartRequest, app.v1.app_pb2.GetRobotPartResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetRobotPartLogs(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartLogsRequest, app.v1.app_pb2.GetRobotPartLogsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def TailRobotPartLogs(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.TailRobotPartLogsRequest, app.v1.app_pb2.TailRobotPartLogsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetRobotPartHistory(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartHistoryRequest, app.v1.app_pb2.GetRobotPartHistoryResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateRobotPartRequest, app.v1.app_pb2.UpdateRobotPartResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def NewRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.NewRobotPartRequest, app.v1.app_pb2.NewRobotPartResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteRobotPartRequest, app.v1.app_pb2.DeleteRobotPartResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetRobotAPIKeys(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotAPIKeysRequest, app.v1.app_pb2.GetRobotAPIKeysResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def MarkPartAsMain(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.MarkPartAsMainRequest, app.v1.app_pb2.MarkPartAsMainResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def MarkPartForRestart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.MarkPartForRestartRequest, app.v1.app_pb2.MarkPartForRestartResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateRobotPartSecret(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateRobotPartSecretRequest, app.v1.app_pb2.CreateRobotPartSecretResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteRobotPartSecret(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteRobotPartSecretRequest, app.v1.app_pb2.DeleteRobotPartSecretResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListRobots(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListRobotsRequest, app.v1.app_pb2.ListRobotsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def NewRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.NewRobotRequest, app.v1.app_pb2.NewRobotResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateRobotRequest, app.v1.app_pb2.UpdateRobotResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteRobotRequest, app.v1.app_pb2.DeleteRobotResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListFragments(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListFragmentsRequest, app.v1.app_pb2.ListFragmentsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetFragment(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetFragmentRequest, app.v1.app_pb2.GetFragmentResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateFragment(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateFragmentRequest, app.v1.app_pb2.CreateFragmentResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateFragment(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateFragmentRequest, app.v1.app_pb2.UpdateFragmentResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteFragment(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteFragmentRequest, app.v1.app_pb2.DeleteFragmentResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AddRole(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.AddRoleRequest, app.v1.app_pb2.AddRoleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RemoveRole(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.RemoveRoleRequest, app.v1.app_pb2.RemoveRoleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ChangeRole(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ChangeRoleRequest, app.v1.app_pb2.ChangeRoleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListAuthorizations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListAuthorizationsRequest, app.v1.app_pb2.ListAuthorizationsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CheckPermissions(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CheckPermissionsRequest, app.v1.app_pb2.CheckPermissionsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetRegistryItem(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRegistryItemRequest, app.v1.app_pb2.GetRegistryItemResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateRegistryItem(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateRegistryItemRequest, app.v1.app_pb2.CreateRegistryItemResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateRegistryItem(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateRegistryItemRequest, app.v1.app_pb2.UpdateRegistryItemResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListRegistryItems(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListRegistryItemsRequest, app.v1.app_pb2.ListRegistryItemsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteRegistryItem(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteRegistryItemRequest, app.v1.app_pb2.DeleteRegistryItemResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateModule(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateModuleRequest, app.v1.app_pb2.CreateModuleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateModule(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateModuleRequest, app.v1.app_pb2.UpdateModuleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UploadModuleFile(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UploadModuleFileRequest, app.v1.app_pb2.UploadModuleFileResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetModule(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetModuleRequest, app.v1.app_pb2.GetModuleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListModules(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListModulesRequest, app.v1.app_pb2.ListModulesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateKey(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateKeyRequest, app.v1.app_pb2.CreateKeyResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteKey(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteKeyRequest, app.v1.app_pb2.DeleteKeyResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListKeys(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListKeysRequest, app.v1.app_pb2.ListKeysResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RotateKey(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.RotateKeyRequest, app.v1.app_pb2.RotateKeyResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateKeyFromExistingKeyAuthorizations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateKeyFromExistingKeyAuthorizationsRequest, app.v1.app_pb2.CreateKeyFromExistingKeyAuthorizationsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)