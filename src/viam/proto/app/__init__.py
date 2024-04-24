"""
@generated by Viam.
Do not edit manually!
"""
from ...gen.app.v1.app_grpc import AppServiceBase, AppServiceStub
from ...gen.app.v1.app_pb2 import (
    AddRoleRequest,
    AddRoleResponse,
    APIKey,
    APIKeyWithAuthorizations,
    Authorization,
    AuthorizationDetails,
    AuthorizedPermissions,
    ChangeRoleRequest,
    ChangeRoleResponse,
    CheckPermissionsRequest,
    CheckPermissionsResponse,
    CreateFragmentRequest,
    CreateFragmentResponse,
    CreateKeyFromExistingKeyAuthorizationsRequest,
    CreateKeyFromExistingKeyAuthorizationsResponse,
    CreateKeyRequest,
    CreateKeyResponse,
    CreateLocationRequest,
    CreateLocationResponse,
    CreateLocationSecretRequest,
    CreateLocationSecretResponse,
    CreateModuleRequest,
    CreateModuleResponse,
    CreateOrganizationInviteRequest,
    CreateOrganizationInviteResponse,
    CreateOrganizationRequest,
    CreateOrganizationResponse,
    CreateRegistryItemRequest,
    CreateRegistryItemResponse,
    CreateRobotPartSecretRequest,
    CreateRobotPartSecretResponse,
    DeleteFragmentRequest,
    DeleteFragmentResponse,
    DeleteKeyRequest,
    DeleteKeyResponse,
    DeleteLocationRequest,
    DeleteLocationResponse,
    DeleteLocationSecretRequest,
    DeleteLocationSecretResponse,
    DeleteOrganizationInviteRequest,
    DeleteOrganizationInviteResponse,
    DeleteOrganizationMemberRequest,
    DeleteOrganizationMemberResponse,
    DeleteOrganizationRequest,
    DeleteOrganizationResponse,
    DeleteRegistryItemRequest,
    DeleteRegistryItemResponse,
    DeleteRobotPartRequest,
    DeleteRobotPartResponse,
    DeleteRobotPartSecretRequest,
    DeleteRobotPartSecretResponse,
    DeleteRobotRequest,
    DeleteRobotResponse,
    Fragment,
    GetFragmentRequest,
    GetFragmentResponse,
    GetLocationRequest,
    GetLocationResponse,
    GetModuleRequest,
    GetModuleResponse,
    GetOrganizationNamespaceAvailabilityRequest,
    GetOrganizationNamespaceAvailabilityResponse,
    GetOrganizationRequest,
    GetOrganizationResponse,
    GetOrganizationsWithAccessToLocationRequest,
    GetOrganizationsWithAccessToLocationResponse,
    GetRegistryItemRequest,
    GetRegistryItemResponse,
    GetRobotAPIKeysRequest,
    GetRobotAPIKeysResponse,
    GetRobotPartHistoryRequest,
    GetRobotPartHistoryResponse,
    GetRobotPartLogsRequest,
    GetRobotPartLogsResponse,
    GetRobotPartRequest,
    GetRobotPartResponse,
    GetRobotPartsRequest,
    GetRobotPartsResponse,
    GetRobotRequest,
    GetRobotResponse,
    GetRoverRentalRobotsRequest,
    GetRoverRentalRobotsResponse,
    GetUserIDByEmailRequest,
    GetUserIDByEmailResponse,
    ListAuthorizationsRequest,
    ListAuthorizationsResponse,
    ListFragmentsRequest,
    ListFragmentsResponse,
    ListKeysRequest,
    ListKeysResponse,
    ListLocationsRequest,
    ListLocationsResponse,
    ListModulesRequest,
    ListModulesResponse,
    ListOrganizationMembersRequest,
    ListOrganizationMembersResponse,
    ListOrganizationsByUserRequest,
    ListOrganizationsByUserResponse,
    ListOrganizationsRequest,
    ListOrganizationsResponse,
    ListRegistryItemsRequest,
    ListRegistryItemsResponse,
    ListRobotsRequest,
    ListRobotsResponse,
    Location,
    LocationAuth,
    LocationAuthRequest,
    LocationAuthResponse,
    LocationOrganization,
    MarkPartAsMainRequest,
    MarkPartAsMainResponse,
    MarkPartForRestartRequest,
    MarkPartForRestartResponse,
    MLModelMetadata,
    MLTrainingMetadata,
    Model,
    Module,
    ModuleFileInfo,
    ModuleMetadata,
    ModuleVersion,
    NewRobotPartRequest,
    NewRobotPartResponse,
    NewRobotRequest,
    NewRobotResponse,
    Organization,
    OrganizationIdentity,
    OrganizationInvite,
    OrganizationMember,
    OrgDetails,
    RegistryItem,
    RegistryItemStatus,
    RemoveRoleRequest,
    RemoveRoleResponse,
    ResendOrganizationInviteRequest,
    ResendOrganizationInviteResponse,
    Robot,
    RobotPart,
    RobotPartHistoryEntry,
    RotateKeyRequest,
    RotateKeyResponse,
    RoverRentalRobot,
    SharedSecret,
    ShareLocationRequest,
    ShareLocationResponse,
    StorageConfig,
    TailRobotPartLogsRequest,
    TailRobotPartLogsResponse,
    UnshareLocationRequest,
    UnshareLocationResponse,
    UpdateFragmentRequest,
    UpdateFragmentResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateModuleRequest,
    UpdateModuleResponse,
    UpdateOrganizationInviteAuthorizationsRequest,
    UpdateOrganizationInviteAuthorizationsResponse,
    UpdateOrganizationRequest,
    UpdateOrganizationResponse,
    UpdateRegistryItemRequest,
    UpdateRegistryItemResponse,
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
    UploadModuleFileRequest,
    UploadModuleFileResponse,
    Uploads,
    VersionHistory,
    Visibility,
)
from ...gen.app.v1.app_unimplemented_grpc import UnimplementedAppServiceBase

__all__ = [
    "AppServiceBase",
    "AppServiceStub",
    "APIKey",
    "APIKeyWithAuthorizations",
    "AddRoleRequest",
    "AddRoleResponse",
    "Authorization",
    "AuthorizationDetails",
    "AuthorizedPermissions",
    "ChangeRoleRequest",
    "ChangeRoleResponse",
    "CheckPermissionsRequest",
    "CheckPermissionsResponse",
    "CreateFragmentRequest",
    "CreateFragmentResponse",
    "CreateKeyFromExistingKeyAuthorizationsRequest",
    "CreateKeyFromExistingKeyAuthorizationsResponse",
    "CreateKeyRequest",
    "CreateKeyResponse",
    "CreateLocationRequest",
    "CreateLocationResponse",
    "CreateLocationSecretRequest",
    "CreateLocationSecretResponse",
    "CreateModuleRequest",
    "CreateModuleResponse",
    "CreateOrganizationInviteRequest",
    "CreateOrganizationInviteResponse",
    "CreateOrganizationRequest",
    "CreateOrganizationResponse",
    "CreateRegistryItemRequest",
    "CreateRegistryItemResponse",
    "CreateRobotPartSecretRequest",
    "CreateRobotPartSecretResponse",
    "DeleteFragmentRequest",
    "DeleteFragmentResponse",
    "DeleteKeyRequest",
    "DeleteKeyResponse",
    "DeleteLocationRequest",
    "DeleteLocationResponse",
    "DeleteLocationSecretRequest",
    "DeleteLocationSecretResponse",
    "DeleteOrganizationInviteRequest",
    "DeleteOrganizationInviteResponse",
    "DeleteOrganizationMemberRequest",
    "DeleteOrganizationMemberResponse",
    "DeleteOrganizationRequest",
    "DeleteOrganizationResponse",
    "DeleteRegistryItemRequest",
    "DeleteRegistryItemResponse",
    "DeleteRobotPartRequest",
    "DeleteRobotPartResponse",
    "DeleteRobotPartSecretRequest",
    "DeleteRobotPartSecretResponse",
    "DeleteRobotRequest",
    "DeleteRobotResponse",
    "Fragment",
    "GetFragmentRequest",
    "GetFragmentResponse",
    "GetLocationRequest",
    "GetLocationResponse",
    "GetModuleRequest",
    "GetModuleResponse",
    "GetOrganizationNamespaceAvailabilityRequest",
    "GetOrganizationNamespaceAvailabilityResponse",
    "GetOrganizationRequest",
    "GetOrganizationResponse",
    "GetOrganizationsWithAccessToLocationRequest",
    "GetOrganizationsWithAccessToLocationResponse",
    "GetRegistryItemRequest",
    "GetRegistryItemResponse",
    "GetRobotAPIKeysRequest",
    "GetRobotAPIKeysResponse",
    "GetRobotPartHistoryRequest",
    "GetRobotPartHistoryResponse",
    "GetRobotPartLogsRequest",
    "GetRobotPartLogsResponse",
    "GetRobotPartRequest",
    "GetRobotPartResponse",
    "GetRobotPartsRequest",
    "GetRobotPartsResponse",
    "GetRobotRequest",
    "GetRobotResponse",
    "GetRoverRentalRobotsRequest",
    "GetRoverRentalRobotsResponse",
    "GetUserIDByEmailRequest",
    "GetUserIDByEmailResponse",
    "ListAuthorizationsRequest",
    "ListAuthorizationsResponse",
    "ListFragmentsRequest",
    "ListFragmentsResponse",
    "ListKeysRequest",
    "ListKeysResponse",
    "ListLocationsRequest",
    "ListLocationsResponse",
    "ListModulesRequest",
    "ListModulesResponse",
    "ListOrganizationMembersRequest",
    "ListOrganizationMembersResponse",
    "ListOrganizationsByUserRequest",
    "ListOrganizationsByUserResponse",
    "ListOrganizationsRequest",
    "ListOrganizationsResponse",
    "ListRegistryItemsRequest",
    "ListRegistryItemsResponse",
    "ListRobotsRequest",
    "ListRobotsResponse",
    "Location",
    "LocationAuth",
    "LocationAuthRequest",
    "LocationAuthResponse",
    "LocationOrganization",
    "MLModelMetadata",
    "MLTrainingMetadata",
    "MarkPartAsMainRequest",
    "MarkPartAsMainResponse",
    "MarkPartForRestartRequest",
    "MarkPartForRestartResponse",
    "Model",
    "Module",
    "ModuleFileInfo",
    "ModuleMetadata",
    "ModuleVersion",
    "NewRobotPartRequest",
    "NewRobotPartResponse",
    "NewRobotRequest",
    "NewRobotResponse",
    "OrgDetails",
    "Organization",
    "OrganizationIdentity",
    "OrganizationInvite",
    "OrganizationMember",
    "RegistryItem",
    "RegistryItemStatus",
    "RemoveRoleRequest",
    "RemoveRoleResponse",
    "ResendOrganizationInviteRequest",
    "ResendOrganizationInviteResponse",
    "Robot",
    "RobotPart",
    "RobotPartHistoryEntry",
    "RotateKeyRequest",
    "RotateKeyResponse",
    "RoverRentalRobot",
    "ShareLocationRequest",
    "ShareLocationResponse",
    "SharedSecret",
    "StorageConfig",
    "TailRobotPartLogsRequest",
    "TailRobotPartLogsResponse",
    "UnshareLocationRequest",
    "UnshareLocationResponse",
    "UpdateFragmentRequest",
    "UpdateFragmentResponse",
    "UpdateLocationRequest",
    "UpdateLocationResponse",
    "UpdateModuleRequest",
    "UpdateModuleResponse",
    "UpdateOrganizationInviteAuthorizationsRequest",
    "UpdateOrganizationInviteAuthorizationsResponse",
    "UpdateOrganizationRequest",
    "UpdateOrganizationResponse",
    "UpdateRegistryItemRequest",
    "UpdateRegistryItemResponse",
    "UpdateRobotPartRequest",
    "UpdateRobotPartResponse",
    "UpdateRobotRequest",
    "UpdateRobotResponse",
    "UploadModuleFileRequest",
    "UploadModuleFileResponse",
    "Uploads",
    "VersionHistory",
    "Visibility",
    "UnimplementedAppServiceBase",
]
