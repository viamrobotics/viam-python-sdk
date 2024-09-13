import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import app
from ... import common
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from ... import tagger

class AppServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetUserIDByEmail(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetUserIDByEmailRequest, app.v1.app_pb2.GetUserIDByEmailResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateOrganization(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateOrganizationRequest, app.v1.app_pb2.CreateOrganizationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListOrganizations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListOrganizationsRequest, app.v1.app_pb2.ListOrganizationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetOrganizationsWithAccessToLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetOrganizationsWithAccessToLocationRequest, app.v1.app_pb2.GetOrganizationsWithAccessToLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListOrganizationsByUser(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListOrganizationsByUserRequest, app.v1.app_pb2.ListOrganizationsByUserResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetOrganization(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetOrganizationRequest, app.v1.app_pb2.GetOrganizationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetOrganizationNamespaceAvailability(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetOrganizationNamespaceAvailabilityRequest, app.v1.app_pb2.GetOrganizationNamespaceAvailabilityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateOrganization(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateOrganizationRequest, app.v1.app_pb2.UpdateOrganizationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteOrganization(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteOrganizationRequest, app.v1.app_pb2.DeleteOrganizationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListOrganizationMembers(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListOrganizationMembersRequest, app.v1.app_pb2.ListOrganizationMembersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateOrganizationInvite(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateOrganizationInviteRequest, app.v1.app_pb2.CreateOrganizationInviteResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateOrganizationInviteAuthorizations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateOrganizationInviteAuthorizationsRequest, app.v1.app_pb2.UpdateOrganizationInviteAuthorizationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteOrganizationMember(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteOrganizationMemberRequest, app.v1.app_pb2.DeleteOrganizationMemberResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteOrganizationInvite(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteOrganizationInviteRequest, app.v1.app_pb2.DeleteOrganizationInviteResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResendOrganizationInvite(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ResendOrganizationInviteRequest, app.v1.app_pb2.ResendOrganizationInviteResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateLocationRequest, app.v1.app_pb2.CreateLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetLocationRequest, app.v1.app_pb2.GetLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateLocationRequest, app.v1.app_pb2.UpdateLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteLocationRequest, app.v1.app_pb2.DeleteLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListLocations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListLocationsRequest, app.v1.app_pb2.ListLocationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ShareLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ShareLocationRequest, app.v1.app_pb2.ShareLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UnshareLocation(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UnshareLocationRequest, app.v1.app_pb2.UnshareLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def LocationAuth(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.LocationAuthRequest, app.v1.app_pb2.LocationAuthResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateLocationSecret(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateLocationSecretRequest, app.v1.app_pb2.CreateLocationSecretResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteLocationSecret(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteLocationSecretRequest, app.v1.app_pb2.DeleteLocationSecretResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotRequest, app.v1.app_pb2.GetRobotResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRoverRentalRobots(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRoverRentalRobotsRequest, app.v1.app_pb2.GetRoverRentalRobotsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobotParts(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartsRequest, app.v1.app_pb2.GetRobotPartsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartRequest, app.v1.app_pb2.GetRobotPartResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobotPartLogs(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartLogsRequest, app.v1.app_pb2.GetRobotPartLogsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TailRobotPartLogs(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.TailRobotPartLogsRequest, app.v1.app_pb2.TailRobotPartLogsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobotPartHistory(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotPartHistoryRequest, app.v1.app_pb2.GetRobotPartHistoryResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateRobotPartRequest, app.v1.app_pb2.UpdateRobotPartResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NewRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.NewRobotPartRequest, app.v1.app_pb2.NewRobotPartResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteRobotPart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteRobotPartRequest, app.v1.app_pb2.DeleteRobotPartResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRobotAPIKeys(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRobotAPIKeysRequest, app.v1.app_pb2.GetRobotAPIKeysResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MarkPartAsMain(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.MarkPartAsMainRequest, app.v1.app_pb2.MarkPartAsMainResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MarkPartForRestart(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.MarkPartForRestartRequest, app.v1.app_pb2.MarkPartForRestartResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateRobotPartSecret(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateRobotPartSecretRequest, app.v1.app_pb2.CreateRobotPartSecretResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteRobotPartSecret(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteRobotPartSecretRequest, app.v1.app_pb2.DeleteRobotPartSecretResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListRobots(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListRobotsRequest, app.v1.app_pb2.ListRobotsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NewRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.NewRobotRequest, app.v1.app_pb2.NewRobotResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateRobotRequest, app.v1.app_pb2.UpdateRobotResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteRobot(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteRobotRequest, app.v1.app_pb2.DeleteRobotResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListFragments(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListFragmentsRequest, app.v1.app_pb2.ListFragmentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetFragment(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetFragmentRequest, app.v1.app_pb2.GetFragmentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateFragment(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateFragmentRequest, app.v1.app_pb2.CreateFragmentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateFragment(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateFragmentRequest, app.v1.app_pb2.UpdateFragmentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteFragment(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteFragmentRequest, app.v1.app_pb2.DeleteFragmentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListMachineFragments(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListMachineFragmentsRequest, app.v1.app_pb2.ListMachineFragmentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetFragmentHistory(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetFragmentHistoryRequest, app.v1.app_pb2.GetFragmentHistoryResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddRole(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.AddRoleRequest, app.v1.app_pb2.AddRoleResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveRole(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.RemoveRoleRequest, app.v1.app_pb2.RemoveRoleResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ChangeRole(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ChangeRoleRequest, app.v1.app_pb2.ChangeRoleResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListAuthorizations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListAuthorizationsRequest, app.v1.app_pb2.ListAuthorizationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CheckPermissions(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CheckPermissionsRequest, app.v1.app_pb2.CheckPermissionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRegistryItem(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetRegistryItemRequest, app.v1.app_pb2.GetRegistryItemResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateRegistryItem(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateRegistryItemRequest, app.v1.app_pb2.CreateRegistryItemResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateRegistryItem(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateRegistryItemRequest, app.v1.app_pb2.UpdateRegistryItemResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListRegistryItems(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListRegistryItemsRequest, app.v1.app_pb2.ListRegistryItemsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteRegistryItem(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteRegistryItemRequest, app.v1.app_pb2.DeleteRegistryItemResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TransferRegistryItem(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.TransferRegistryItemRequest, app.v1.app_pb2.TransferRegistryItemResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateModule(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateModuleRequest, app.v1.app_pb2.CreateModuleResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateModule(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UpdateModuleRequest, app.v1.app_pb2.UpdateModuleResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UploadModuleFile(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.UploadModuleFileRequest, app.v1.app_pb2.UploadModuleFileResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetModule(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetModuleRequest, app.v1.app_pb2.GetModuleResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListModules(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListModulesRequest, app.v1.app_pb2.ListModulesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateKey(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateKeyRequest, app.v1.app_pb2.CreateKeyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteKey(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.DeleteKeyRequest, app.v1.app_pb2.DeleteKeyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListKeys(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListKeysRequest, app.v1.app_pb2.ListKeysResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RenameKey(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.RenameKeyRequest, app.v1.app_pb2.RenameKeyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RotateKey(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.RotateKeyRequest, app.v1.app_pb2.RotateKeyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateKeyFromExistingKeyAuthorizations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateKeyFromExistingKeyAuthorizationsRequest, app.v1.app_pb2.CreateKeyFromExistingKeyAuthorizationsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.v1.AppService/GetUserIDByEmail': grpclib.const.Handler(self.GetUserIDByEmail, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetUserIDByEmailRequest, app.v1.app_pb2.GetUserIDByEmailResponse), '/viam.app.v1.AppService/CreateOrganization': grpclib.const.Handler(self.CreateOrganization, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CreateOrganizationRequest, app.v1.app_pb2.CreateOrganizationResponse), '/viam.app.v1.AppService/ListOrganizations': grpclib.const.Handler(self.ListOrganizations, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListOrganizationsRequest, app.v1.app_pb2.ListOrganizationsResponse), '/viam.app.v1.AppService/GetOrganizationsWithAccessToLocation': grpclib.const.Handler(self.GetOrganizationsWithAccessToLocation, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetOrganizationsWithAccessToLocationRequest, app.v1.app_pb2.GetOrganizationsWithAccessToLocationResponse), '/viam.app.v1.AppService/ListOrganizationsByUser': grpclib.const.Handler(self.ListOrganizationsByUser, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListOrganizationsByUserRequest, app.v1.app_pb2.ListOrganizationsByUserResponse), '/viam.app.v1.AppService/GetOrganization': grpclib.const.Handler(self.GetOrganization, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetOrganizationRequest, app.v1.app_pb2.GetOrganizationResponse), '/viam.app.v1.AppService/GetOrganizationNamespaceAvailability': grpclib.const.Handler(self.GetOrganizationNamespaceAvailability, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetOrganizationNamespaceAvailabilityRequest, app.v1.app_pb2.GetOrganizationNamespaceAvailabilityResponse), '/viam.app.v1.AppService/UpdateOrganization': grpclib.const.Handler(self.UpdateOrganization, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UpdateOrganizationRequest, app.v1.app_pb2.UpdateOrganizationResponse), '/viam.app.v1.AppService/DeleteOrganization': grpclib.const.Handler(self.DeleteOrganization, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteOrganizationRequest, app.v1.app_pb2.DeleteOrganizationResponse), '/viam.app.v1.AppService/ListOrganizationMembers': grpclib.const.Handler(self.ListOrganizationMembers, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListOrganizationMembersRequest, app.v1.app_pb2.ListOrganizationMembersResponse), '/viam.app.v1.AppService/CreateOrganizationInvite': grpclib.const.Handler(self.CreateOrganizationInvite, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CreateOrganizationInviteRequest, app.v1.app_pb2.CreateOrganizationInviteResponse), '/viam.app.v1.AppService/UpdateOrganizationInviteAuthorizations': grpclib.const.Handler(self.UpdateOrganizationInviteAuthorizations, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UpdateOrganizationInviteAuthorizationsRequest, app.v1.app_pb2.UpdateOrganizationInviteAuthorizationsResponse), '/viam.app.v1.AppService/DeleteOrganizationMember': grpclib.const.Handler(self.DeleteOrganizationMember, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteOrganizationMemberRequest, app.v1.app_pb2.DeleteOrganizationMemberResponse), '/viam.app.v1.AppService/DeleteOrganizationInvite': grpclib.const.Handler(self.DeleteOrganizationInvite, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteOrganizationInviteRequest, app.v1.app_pb2.DeleteOrganizationInviteResponse), '/viam.app.v1.AppService/ResendOrganizationInvite': grpclib.const.Handler(self.ResendOrganizationInvite, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ResendOrganizationInviteRequest, app.v1.app_pb2.ResendOrganizationInviteResponse), '/viam.app.v1.AppService/CreateLocation': grpclib.const.Handler(self.CreateLocation, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CreateLocationRequest, app.v1.app_pb2.CreateLocationResponse), '/viam.app.v1.AppService/GetLocation': grpclib.const.Handler(self.GetLocation, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetLocationRequest, app.v1.app_pb2.GetLocationResponse), '/viam.app.v1.AppService/UpdateLocation': grpclib.const.Handler(self.UpdateLocation, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UpdateLocationRequest, app.v1.app_pb2.UpdateLocationResponse), '/viam.app.v1.AppService/DeleteLocation': grpclib.const.Handler(self.DeleteLocation, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteLocationRequest, app.v1.app_pb2.DeleteLocationResponse), '/viam.app.v1.AppService/ListLocations': grpclib.const.Handler(self.ListLocations, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListLocationsRequest, app.v1.app_pb2.ListLocationsResponse), '/viam.app.v1.AppService/ShareLocation': grpclib.const.Handler(self.ShareLocation, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ShareLocationRequest, app.v1.app_pb2.ShareLocationResponse), '/viam.app.v1.AppService/UnshareLocation': grpclib.const.Handler(self.UnshareLocation, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UnshareLocationRequest, app.v1.app_pb2.UnshareLocationResponse), '/viam.app.v1.AppService/LocationAuth': grpclib.const.Handler(self.LocationAuth, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.LocationAuthRequest, app.v1.app_pb2.LocationAuthResponse), '/viam.app.v1.AppService/CreateLocationSecret': grpclib.const.Handler(self.CreateLocationSecret, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CreateLocationSecretRequest, app.v1.app_pb2.CreateLocationSecretResponse), '/viam.app.v1.AppService/DeleteLocationSecret': grpclib.const.Handler(self.DeleteLocationSecret, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteLocationSecretRequest, app.v1.app_pb2.DeleteLocationSecretResponse), '/viam.app.v1.AppService/GetRobot': grpclib.const.Handler(self.GetRobot, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotRequest, app.v1.app_pb2.GetRobotResponse), '/viam.app.v1.AppService/GetRoverRentalRobots': grpclib.const.Handler(self.GetRoverRentalRobots, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRoverRentalRobotsRequest, app.v1.app_pb2.GetRoverRentalRobotsResponse), '/viam.app.v1.AppService/GetRobotParts': grpclib.const.Handler(self.GetRobotParts, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotPartsRequest, app.v1.app_pb2.GetRobotPartsResponse), '/viam.app.v1.AppService/GetRobotPart': grpclib.const.Handler(self.GetRobotPart, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotPartRequest, app.v1.app_pb2.GetRobotPartResponse), '/viam.app.v1.AppService/GetRobotPartLogs': grpclib.const.Handler(self.GetRobotPartLogs, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotPartLogsRequest, app.v1.app_pb2.GetRobotPartLogsResponse), '/viam.app.v1.AppService/TailRobotPartLogs': grpclib.const.Handler(self.TailRobotPartLogs, grpclib.const.Cardinality.UNARY_STREAM, app.v1.app_pb2.TailRobotPartLogsRequest, app.v1.app_pb2.TailRobotPartLogsResponse), '/viam.app.v1.AppService/GetRobotPartHistory': grpclib.const.Handler(self.GetRobotPartHistory, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotPartHistoryRequest, app.v1.app_pb2.GetRobotPartHistoryResponse), '/viam.app.v1.AppService/UpdateRobotPart': grpclib.const.Handler(self.UpdateRobotPart, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UpdateRobotPartRequest, app.v1.app_pb2.UpdateRobotPartResponse), '/viam.app.v1.AppService/NewRobotPart': grpclib.const.Handler(self.NewRobotPart, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.NewRobotPartRequest, app.v1.app_pb2.NewRobotPartResponse), '/viam.app.v1.AppService/DeleteRobotPart': grpclib.const.Handler(self.DeleteRobotPart, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteRobotPartRequest, app.v1.app_pb2.DeleteRobotPartResponse), '/viam.app.v1.AppService/GetRobotAPIKeys': grpclib.const.Handler(self.GetRobotAPIKeys, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRobotAPIKeysRequest, app.v1.app_pb2.GetRobotAPIKeysResponse), '/viam.app.v1.AppService/MarkPartAsMain': grpclib.const.Handler(self.MarkPartAsMain, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.MarkPartAsMainRequest, app.v1.app_pb2.MarkPartAsMainResponse), '/viam.app.v1.AppService/MarkPartForRestart': grpclib.const.Handler(self.MarkPartForRestart, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.MarkPartForRestartRequest, app.v1.app_pb2.MarkPartForRestartResponse), '/viam.app.v1.AppService/CreateRobotPartSecret': grpclib.const.Handler(self.CreateRobotPartSecret, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CreateRobotPartSecretRequest, app.v1.app_pb2.CreateRobotPartSecretResponse), '/viam.app.v1.AppService/DeleteRobotPartSecret': grpclib.const.Handler(self.DeleteRobotPartSecret, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteRobotPartSecretRequest, app.v1.app_pb2.DeleteRobotPartSecretResponse), '/viam.app.v1.AppService/ListRobots': grpclib.const.Handler(self.ListRobots, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListRobotsRequest, app.v1.app_pb2.ListRobotsResponse), '/viam.app.v1.AppService/NewRobot': grpclib.const.Handler(self.NewRobot, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.NewRobotRequest, app.v1.app_pb2.NewRobotResponse), '/viam.app.v1.AppService/UpdateRobot': grpclib.const.Handler(self.UpdateRobot, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UpdateRobotRequest, app.v1.app_pb2.UpdateRobotResponse), '/viam.app.v1.AppService/DeleteRobot': grpclib.const.Handler(self.DeleteRobot, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteRobotRequest, app.v1.app_pb2.DeleteRobotResponse), '/viam.app.v1.AppService/ListFragments': grpclib.const.Handler(self.ListFragments, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListFragmentsRequest, app.v1.app_pb2.ListFragmentsResponse), '/viam.app.v1.AppService/GetFragment': grpclib.const.Handler(self.GetFragment, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetFragmentRequest, app.v1.app_pb2.GetFragmentResponse), '/viam.app.v1.AppService/CreateFragment': grpclib.const.Handler(self.CreateFragment, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CreateFragmentRequest, app.v1.app_pb2.CreateFragmentResponse), '/viam.app.v1.AppService/UpdateFragment': grpclib.const.Handler(self.UpdateFragment, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UpdateFragmentRequest, app.v1.app_pb2.UpdateFragmentResponse), '/viam.app.v1.AppService/DeleteFragment': grpclib.const.Handler(self.DeleteFragment, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteFragmentRequest, app.v1.app_pb2.DeleteFragmentResponse), '/viam.app.v1.AppService/ListMachineFragments': grpclib.const.Handler(self.ListMachineFragments, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListMachineFragmentsRequest, app.v1.app_pb2.ListMachineFragmentsResponse), '/viam.app.v1.AppService/GetFragmentHistory': grpclib.const.Handler(self.GetFragmentHistory, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetFragmentHistoryRequest, app.v1.app_pb2.GetFragmentHistoryResponse), '/viam.app.v1.AppService/AddRole': grpclib.const.Handler(self.AddRole, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.AddRoleRequest, app.v1.app_pb2.AddRoleResponse), '/viam.app.v1.AppService/RemoveRole': grpclib.const.Handler(self.RemoveRole, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.RemoveRoleRequest, app.v1.app_pb2.RemoveRoleResponse), '/viam.app.v1.AppService/ChangeRole': grpclib.const.Handler(self.ChangeRole, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ChangeRoleRequest, app.v1.app_pb2.ChangeRoleResponse), '/viam.app.v1.AppService/ListAuthorizations': grpclib.const.Handler(self.ListAuthorizations, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListAuthorizationsRequest, app.v1.app_pb2.ListAuthorizationsResponse), '/viam.app.v1.AppService/CheckPermissions': grpclib.const.Handler(self.CheckPermissions, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CheckPermissionsRequest, app.v1.app_pb2.CheckPermissionsResponse), '/viam.app.v1.AppService/GetRegistryItem': grpclib.const.Handler(self.GetRegistryItem, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetRegistryItemRequest, app.v1.app_pb2.GetRegistryItemResponse), '/viam.app.v1.AppService/CreateRegistryItem': grpclib.const.Handler(self.CreateRegistryItem, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CreateRegistryItemRequest, app.v1.app_pb2.CreateRegistryItemResponse), '/viam.app.v1.AppService/UpdateRegistryItem': grpclib.const.Handler(self.UpdateRegistryItem, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UpdateRegistryItemRequest, app.v1.app_pb2.UpdateRegistryItemResponse), '/viam.app.v1.AppService/ListRegistryItems': grpclib.const.Handler(self.ListRegistryItems, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListRegistryItemsRequest, app.v1.app_pb2.ListRegistryItemsResponse), '/viam.app.v1.AppService/DeleteRegistryItem': grpclib.const.Handler(self.DeleteRegistryItem, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteRegistryItemRequest, app.v1.app_pb2.DeleteRegistryItemResponse), '/viam.app.v1.AppService/TransferRegistryItem': grpclib.const.Handler(self.TransferRegistryItem, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.TransferRegistryItemRequest, app.v1.app_pb2.TransferRegistryItemResponse), '/viam.app.v1.AppService/CreateModule': grpclib.const.Handler(self.CreateModule, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CreateModuleRequest, app.v1.app_pb2.CreateModuleResponse), '/viam.app.v1.AppService/UpdateModule': grpclib.const.Handler(self.UpdateModule, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.UpdateModuleRequest, app.v1.app_pb2.UpdateModuleResponse), '/viam.app.v1.AppService/UploadModuleFile': grpclib.const.Handler(self.UploadModuleFile, grpclib.const.Cardinality.STREAM_UNARY, app.v1.app_pb2.UploadModuleFileRequest, app.v1.app_pb2.UploadModuleFileResponse), '/viam.app.v1.AppService/GetModule': grpclib.const.Handler(self.GetModule, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.GetModuleRequest, app.v1.app_pb2.GetModuleResponse), '/viam.app.v1.AppService/ListModules': grpclib.const.Handler(self.ListModules, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListModulesRequest, app.v1.app_pb2.ListModulesResponse), '/viam.app.v1.AppService/CreateKey': grpclib.const.Handler(self.CreateKey, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CreateKeyRequest, app.v1.app_pb2.CreateKeyResponse), '/viam.app.v1.AppService/DeleteKey': grpclib.const.Handler(self.DeleteKey, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.DeleteKeyRequest, app.v1.app_pb2.DeleteKeyResponse), '/viam.app.v1.AppService/ListKeys': grpclib.const.Handler(self.ListKeys, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.ListKeysRequest, app.v1.app_pb2.ListKeysResponse), '/viam.app.v1.AppService/RenameKey': grpclib.const.Handler(self.RenameKey, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.RenameKeyRequest, app.v1.app_pb2.RenameKeyResponse), '/viam.app.v1.AppService/RotateKey': grpclib.const.Handler(self.RotateKey, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.RotateKeyRequest, app.v1.app_pb2.RotateKeyResponse), '/viam.app.v1.AppService/CreateKeyFromExistingKeyAuthorizations': grpclib.const.Handler(self.CreateKeyFromExistingKeyAuthorizations, grpclib.const.Cardinality.UNARY_UNARY, app.v1.app_pb2.CreateKeyFromExistingKeyAuthorizationsRequest, app.v1.app_pb2.CreateKeyFromExistingKeyAuthorizationsResponse)}

class UnimplementedAppServiceBase(AppServiceBase):

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

    async def ListMachineFragments(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.ListMachineFragmentsRequest, app.v1.app_pb2.ListMachineFragmentsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetFragmentHistory(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.GetFragmentHistoryRequest, app.v1.app_pb2.GetFragmentHistoryResponse]') -> None:
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

    async def TransferRegistryItem(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.TransferRegistryItemRequest, app.v1.app_pb2.TransferRegistryItemResponse]') -> None:
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

    async def RenameKey(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.RenameKeyRequest, app.v1.app_pb2.RenameKeyResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RotateKey(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.RotateKeyRequest, app.v1.app_pb2.RotateKeyResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CreateKeyFromExistingKeyAuthorizations(self, stream: 'grpclib.server.Stream[app.v1.app_pb2.CreateKeyFromExistingKeyAuthorizationsRequest, app.v1.app_pb2.CreateKeyFromExistingKeyAuthorizationsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class AppServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetUserIDByEmail = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetUserIDByEmail', app.v1.app_pb2.GetUserIDByEmailRequest, app.v1.app_pb2.GetUserIDByEmailResponse)
        self.CreateOrganization = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CreateOrganization', app.v1.app_pb2.CreateOrganizationRequest, app.v1.app_pb2.CreateOrganizationResponse)
        self.ListOrganizations = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListOrganizations', app.v1.app_pb2.ListOrganizationsRequest, app.v1.app_pb2.ListOrganizationsResponse)
        self.GetOrganizationsWithAccessToLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetOrganizationsWithAccessToLocation', app.v1.app_pb2.GetOrganizationsWithAccessToLocationRequest, app.v1.app_pb2.GetOrganizationsWithAccessToLocationResponse)
        self.ListOrganizationsByUser = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListOrganizationsByUser', app.v1.app_pb2.ListOrganizationsByUserRequest, app.v1.app_pb2.ListOrganizationsByUserResponse)
        self.GetOrganization = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetOrganization', app.v1.app_pb2.GetOrganizationRequest, app.v1.app_pb2.GetOrganizationResponse)
        self.GetOrganizationNamespaceAvailability = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetOrganizationNamespaceAvailability', app.v1.app_pb2.GetOrganizationNamespaceAvailabilityRequest, app.v1.app_pb2.GetOrganizationNamespaceAvailabilityResponse)
        self.UpdateOrganization = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UpdateOrganization', app.v1.app_pb2.UpdateOrganizationRequest, app.v1.app_pb2.UpdateOrganizationResponse)
        self.DeleteOrganization = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteOrganization', app.v1.app_pb2.DeleteOrganizationRequest, app.v1.app_pb2.DeleteOrganizationResponse)
        self.ListOrganizationMembers = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListOrganizationMembers', app.v1.app_pb2.ListOrganizationMembersRequest, app.v1.app_pb2.ListOrganizationMembersResponse)
        self.CreateOrganizationInvite = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CreateOrganizationInvite', app.v1.app_pb2.CreateOrganizationInviteRequest, app.v1.app_pb2.CreateOrganizationInviteResponse)
        self.UpdateOrganizationInviteAuthorizations = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UpdateOrganizationInviteAuthorizations', app.v1.app_pb2.UpdateOrganizationInviteAuthorizationsRequest, app.v1.app_pb2.UpdateOrganizationInviteAuthorizationsResponse)
        self.DeleteOrganizationMember = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteOrganizationMember', app.v1.app_pb2.DeleteOrganizationMemberRequest, app.v1.app_pb2.DeleteOrganizationMemberResponse)
        self.DeleteOrganizationInvite = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteOrganizationInvite', app.v1.app_pb2.DeleteOrganizationInviteRequest, app.v1.app_pb2.DeleteOrganizationInviteResponse)
        self.ResendOrganizationInvite = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ResendOrganizationInvite', app.v1.app_pb2.ResendOrganizationInviteRequest, app.v1.app_pb2.ResendOrganizationInviteResponse)
        self.CreateLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CreateLocation', app.v1.app_pb2.CreateLocationRequest, app.v1.app_pb2.CreateLocationResponse)
        self.GetLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetLocation', app.v1.app_pb2.GetLocationRequest, app.v1.app_pb2.GetLocationResponse)
        self.UpdateLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UpdateLocation', app.v1.app_pb2.UpdateLocationRequest, app.v1.app_pb2.UpdateLocationResponse)
        self.DeleteLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteLocation', app.v1.app_pb2.DeleteLocationRequest, app.v1.app_pb2.DeleteLocationResponse)
        self.ListLocations = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListLocations', app.v1.app_pb2.ListLocationsRequest, app.v1.app_pb2.ListLocationsResponse)
        self.ShareLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ShareLocation', app.v1.app_pb2.ShareLocationRequest, app.v1.app_pb2.ShareLocationResponse)
        self.UnshareLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UnshareLocation', app.v1.app_pb2.UnshareLocationRequest, app.v1.app_pb2.UnshareLocationResponse)
        self.LocationAuth = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/LocationAuth', app.v1.app_pb2.LocationAuthRequest, app.v1.app_pb2.LocationAuthResponse)
        self.CreateLocationSecret = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CreateLocationSecret', app.v1.app_pb2.CreateLocationSecretRequest, app.v1.app_pb2.CreateLocationSecretResponse)
        self.DeleteLocationSecret = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteLocationSecret', app.v1.app_pb2.DeleteLocationSecretRequest, app.v1.app_pb2.DeleteLocationSecretResponse)
        self.GetRobot = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobot', app.v1.app_pb2.GetRobotRequest, app.v1.app_pb2.GetRobotResponse)
        self.GetRoverRentalRobots = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRoverRentalRobots', app.v1.app_pb2.GetRoverRentalRobotsRequest, app.v1.app_pb2.GetRoverRentalRobotsResponse)
        self.GetRobotParts = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobotParts', app.v1.app_pb2.GetRobotPartsRequest, app.v1.app_pb2.GetRobotPartsResponse)
        self.GetRobotPart = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobotPart', app.v1.app_pb2.GetRobotPartRequest, app.v1.app_pb2.GetRobotPartResponse)
        self.GetRobotPartLogs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobotPartLogs', app.v1.app_pb2.GetRobotPartLogsRequest, app.v1.app_pb2.GetRobotPartLogsResponse)
        self.TailRobotPartLogs = grpclib.client.UnaryStreamMethod(channel, '/viam.app.v1.AppService/TailRobotPartLogs', app.v1.app_pb2.TailRobotPartLogsRequest, app.v1.app_pb2.TailRobotPartLogsResponse)
        self.GetRobotPartHistory = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobotPartHistory', app.v1.app_pb2.GetRobotPartHistoryRequest, app.v1.app_pb2.GetRobotPartHistoryResponse)
        self.UpdateRobotPart = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UpdateRobotPart', app.v1.app_pb2.UpdateRobotPartRequest, app.v1.app_pb2.UpdateRobotPartResponse)
        self.NewRobotPart = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/NewRobotPart', app.v1.app_pb2.NewRobotPartRequest, app.v1.app_pb2.NewRobotPartResponse)
        self.DeleteRobotPart = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteRobotPart', app.v1.app_pb2.DeleteRobotPartRequest, app.v1.app_pb2.DeleteRobotPartResponse)
        self.GetRobotAPIKeys = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRobotAPIKeys', app.v1.app_pb2.GetRobotAPIKeysRequest, app.v1.app_pb2.GetRobotAPIKeysResponse)
        self.MarkPartAsMain = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/MarkPartAsMain', app.v1.app_pb2.MarkPartAsMainRequest, app.v1.app_pb2.MarkPartAsMainResponse)
        self.MarkPartForRestart = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/MarkPartForRestart', app.v1.app_pb2.MarkPartForRestartRequest, app.v1.app_pb2.MarkPartForRestartResponse)
        self.CreateRobotPartSecret = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CreateRobotPartSecret', app.v1.app_pb2.CreateRobotPartSecretRequest, app.v1.app_pb2.CreateRobotPartSecretResponse)
        self.DeleteRobotPartSecret = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteRobotPartSecret', app.v1.app_pb2.DeleteRobotPartSecretRequest, app.v1.app_pb2.DeleteRobotPartSecretResponse)
        self.ListRobots = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListRobots', app.v1.app_pb2.ListRobotsRequest, app.v1.app_pb2.ListRobotsResponse)
        self.NewRobot = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/NewRobot', app.v1.app_pb2.NewRobotRequest, app.v1.app_pb2.NewRobotResponse)
        self.UpdateRobot = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UpdateRobot', app.v1.app_pb2.UpdateRobotRequest, app.v1.app_pb2.UpdateRobotResponse)
        self.DeleteRobot = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteRobot', app.v1.app_pb2.DeleteRobotRequest, app.v1.app_pb2.DeleteRobotResponse)
        self.ListFragments = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListFragments', app.v1.app_pb2.ListFragmentsRequest, app.v1.app_pb2.ListFragmentsResponse)
        self.GetFragment = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetFragment', app.v1.app_pb2.GetFragmentRequest, app.v1.app_pb2.GetFragmentResponse)
        self.CreateFragment = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CreateFragment', app.v1.app_pb2.CreateFragmentRequest, app.v1.app_pb2.CreateFragmentResponse)
        self.UpdateFragment = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UpdateFragment', app.v1.app_pb2.UpdateFragmentRequest, app.v1.app_pb2.UpdateFragmentResponse)
        self.DeleteFragment = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteFragment', app.v1.app_pb2.DeleteFragmentRequest, app.v1.app_pb2.DeleteFragmentResponse)
        self.ListMachineFragments = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListMachineFragments', app.v1.app_pb2.ListMachineFragmentsRequest, app.v1.app_pb2.ListMachineFragmentsResponse)
        self.GetFragmentHistory = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetFragmentHistory', app.v1.app_pb2.GetFragmentHistoryRequest, app.v1.app_pb2.GetFragmentHistoryResponse)
        self.AddRole = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/AddRole', app.v1.app_pb2.AddRoleRequest, app.v1.app_pb2.AddRoleResponse)
        self.RemoveRole = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/RemoveRole', app.v1.app_pb2.RemoveRoleRequest, app.v1.app_pb2.RemoveRoleResponse)
        self.ChangeRole = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ChangeRole', app.v1.app_pb2.ChangeRoleRequest, app.v1.app_pb2.ChangeRoleResponse)
        self.ListAuthorizations = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListAuthorizations', app.v1.app_pb2.ListAuthorizationsRequest, app.v1.app_pb2.ListAuthorizationsResponse)
        self.CheckPermissions = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CheckPermissions', app.v1.app_pb2.CheckPermissionsRequest, app.v1.app_pb2.CheckPermissionsResponse)
        self.GetRegistryItem = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetRegistryItem', app.v1.app_pb2.GetRegistryItemRequest, app.v1.app_pb2.GetRegistryItemResponse)
        self.CreateRegistryItem = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CreateRegistryItem', app.v1.app_pb2.CreateRegistryItemRequest, app.v1.app_pb2.CreateRegistryItemResponse)
        self.UpdateRegistryItem = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UpdateRegistryItem', app.v1.app_pb2.UpdateRegistryItemRequest, app.v1.app_pb2.UpdateRegistryItemResponse)
        self.ListRegistryItems = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListRegistryItems', app.v1.app_pb2.ListRegistryItemsRequest, app.v1.app_pb2.ListRegistryItemsResponse)
        self.DeleteRegistryItem = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteRegistryItem', app.v1.app_pb2.DeleteRegistryItemRequest, app.v1.app_pb2.DeleteRegistryItemResponse)
        self.TransferRegistryItem = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/TransferRegistryItem', app.v1.app_pb2.TransferRegistryItemRequest, app.v1.app_pb2.TransferRegistryItemResponse)
        self.CreateModule = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CreateModule', app.v1.app_pb2.CreateModuleRequest, app.v1.app_pb2.CreateModuleResponse)
        self.UpdateModule = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/UpdateModule', app.v1.app_pb2.UpdateModuleRequest, app.v1.app_pb2.UpdateModuleResponse)
        self.UploadModuleFile = grpclib.client.StreamUnaryMethod(channel, '/viam.app.v1.AppService/UploadModuleFile', app.v1.app_pb2.UploadModuleFileRequest, app.v1.app_pb2.UploadModuleFileResponse)
        self.GetModule = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/GetModule', app.v1.app_pb2.GetModuleRequest, app.v1.app_pb2.GetModuleResponse)
        self.ListModules = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListModules', app.v1.app_pb2.ListModulesRequest, app.v1.app_pb2.ListModulesResponse)
        self.CreateKey = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CreateKey', app.v1.app_pb2.CreateKeyRequest, app.v1.app_pb2.CreateKeyResponse)
        self.DeleteKey = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/DeleteKey', app.v1.app_pb2.DeleteKeyRequest, app.v1.app_pb2.DeleteKeyResponse)
        self.ListKeys = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/ListKeys', app.v1.app_pb2.ListKeysRequest, app.v1.app_pb2.ListKeysResponse)
        self.RenameKey = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/RenameKey', app.v1.app_pb2.RenameKeyRequest, app.v1.app_pb2.RenameKeyResponse)
        self.RotateKey = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/RotateKey', app.v1.app_pb2.RotateKeyRequest, app.v1.app_pb2.RotateKeyResponse)
        self.CreateKeyFromExistingKeyAuthorizations = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.AppService/CreateKeyFromExistingKeyAuthorizations', app.v1.app_pb2.CreateKeyFromExistingKeyAuthorizationsRequest, app.v1.app_pb2.CreateKeyFromExistingKeyAuthorizationsResponse)