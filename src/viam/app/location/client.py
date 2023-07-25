import json
from typing import Any, List, Mapping, Optional

from grpclib.client import Channel

from viam import logging
from viam.proto.app import (
    AppServiceStub,
    CreateLocationRequest,
    CreateLocationResponse,
    DeleteLocationRequest,
    DeleteLocationResponse,
    DeleteRobotPartRequest,
    DeleteRobotPartResponse,
    DeleteRobotRequest,
    DeleteRobotResponse,
    Fragment,
    GetFragmentRequest,
    GetFragmentResponse,
    GetLocationRequest,
    GetLocationResponse,
    GetRobotPartLogsRequest,
    GetRobotPartLogsResponse,
    GetRobotPartRequest,
    GetRobotPartResponse,
    GetRobotPartsRequest,
    GetRobotPartsResponse,
    GetRobotRequest,
    GetRobotResponse,
    ListFragmentsRequest,
    ListFragmentsResponse,
    ListLocationsRequest,
    ListLocationsResponse,
    ListOrganizationsRequest,
    ListOrganizationsResponse,
    ListRobotsRequest,
    ListRobotsResponse,
    Location,
    LogEntry,
    MarkPartForRestartRequest,
    MarkPartForRestartResponse,
    NewRobotPartRequest,
    NewRobotPartResponse,
    NewRobotRequest,
    NewRobotResponse,
    Robot,
    RobotPart,
    ShareLocationRequest,
    ShareLocationResponse,
    UnshareLocationRequest,
    UnshareLocationResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
)
from viam.utils import dict_to_struct

LOGGER = logging.getLogger(__name__)

# WEIRD TYPES:
# Location {
#     LocationAuth {
#         List[SharedSecret]
#     },
#     List[LocationOrganization],
#     StorageConfig
# }
# Robot {
#   Timestamp,
#   Timestamp
# }
# RobotPart {
#   Struct,
#   Timestamp,
#   Struct,
#   Timestamp,
#   List[SharedSecret]
# }
# LogEntry {
#     Timestamp,
#     Struct,
#     List[Struct]
# }
# Fragment {
#     Struct,
#     Timestamp
# }


class LocationClient:
    """gRPC client for method calls to app.

    Constructor is used by `AppClient` to instantiate relevant service stub. Calls to `LocationClient`  methods should be made through
    `AppClient`.
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str], location_id: Optional[str] = None):
        """Create a `LocationClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
        """
        self._metadata = metadata
        self._location_client = AppServiceStub(channel)
        self._location_id = location_id

    _location_client: AppServiceStub
    _metadata: Mapping[str, str]
    _location_id: str

    async def get_user_id_by_email(self):
        raise NotImplementedError()

    async def create_organization(self):
        raise NotImplementedError()

    # TODO: Unimplement.
    async def list_organizations(self):
        request = ListOrganizationsRequest()
        response: ListOrganizationsResponse = await self._location_client.ListOrganizations(request, metadata=self._metadata)
        return response.organizations

    async def list_organizations_by_user(self):
        raise NotImplementedError()

    async def get_organization(self):
        raise NotImplementedError()

    async def get_organization_namespace_availability(self):
        raise NotImplementedError()

    async def update_organization(self):
        raise NotImplementedError()

    async def delete_organization(self):
        raise NotImplementedError()

    async def list_organization_members(self):
        raise NotImplementedError()

    async def create_organization_invite(self):
        raise NotImplementedError()

    async def update_organization_invite_authorizations(self):
        raise NotImplementedError()

    async def delete_organization_member(self):
        raise NotImplementedError()

    async def delete_organization_invite(self):
        raise NotImplementedError()

    async def resend_organization_invite(self):
        raise NotImplementedError()

    async def create_location(self, organization_id: str, name: str, parent_location_id: Optional[str] = None) -> Location:
        """Create and name a location under the specified organization and parent location.

        Args:
            organization_id (str): ID of the organization to create the location under.
            name (str): Name of the location.
            parent_location_id (Optional[str]): Optional new parent location to move the location under. Defaults to currenty authorized
                location.

        Raises:
            GRPCError: If either an invalid organization ID or parent location ID is passed.

        Returns:
            viam.proto.app.Location: A `Location` object representing the newly created location.
        """
        location_id = parent_location_id if parent_location_id else self._location_id
        request = CreateLocationRequest(organization_id=organization_id, name=name, parent_location_id=location_id)
        response: CreateLocationResponse = await self._location_client.CreateLocation(request, metadata=self._metadata)
        return response.location

    async def get_location(self, location_id: Optional[str] = None) -> Location:
        """Get a location.

        Args:
            location_id (Optional[str]): ID of the location to get. Defaults to the current authorized location.

        Raises:
            GRPCError: If an invalid location ID is passed.

        Location:
            viam.proto.app.Location: The location.
        """
        location_id = location_id if location_id else self._location_id
        request = GetLocationRequest(location_id=location_id)
        response: GetLocationResponse = await self._location_client.GetLocation(request, metadata=self._metadata)
        return response.location

    async def update_location(
        self, location_id: str, name: Optional[str], parent_location_id: Optional[str], region: str = None  # Not used in app.
    ) -> Location:
        """Change the name of a location and/or assign it a new parent location.

        Args:
            location_id (str): ID of the location to update.
            name (Optional[str]): Optional new name to be updated on the location. Defaults to the empty string "". No change if not passed.
            parent_location_id(Optional[str]): Optional new parent location to move the location under. Defaults to the empty string "". No
                change if not passed.

        Raises:
            GRPCError: If an invalid location ID is passed.

        Returns:
            viam.proto.app.Location: A `Location` object representing the newly updated location.
        """
        request = UpdateLocationRequest(location_id=location_id, name=name, parent_location_id=parent_location_id, region=region)
        response: UpdateLocationResponse = await self._location_client.UpdateLocation(request, metadata=self._metadata)
        return response.location

    async def delete_location(self, location_id: str) -> None:
        """Delete a location.

        Args:
            location_id (str): ID of the location to delete. Must be specified.

        Raises:
            GRPCError: If an invalid location ID is passed.
        """
        request = DeleteLocationRequest(location_id=location_id)
        _: DeleteLocationResponse = await self._location_client.DeleteLocation(request, metadata=self._metadata)

    async def list_locations(self, organization_id: str) -> List[Location]:
        """Get a list of all locations under the specified organization.

        Args:
            organization_id (str): ID of the organization under which to list the locations.

        Raises:
            GRPCError: If an invalid organization ID is passed.

        Returns:
            List[viam.proto.app.Location]: The list of locations.
        """
        request = ListLocationsRequest(organization_id=organization_id)
        response: ListLocationsResponse = await self._location_client.ListLocations(request, metadata=self._metadata)
        return response.locations

    async def share_location(self, organization_id: str, location_id: Optional[str] = None) -> None:
        """Share a location with a specific organization.

        Args:
            organization_id (str): ID of the organization to share the location with.
            location_id (Optional[str]): ID of the location to be shared. Defaults to the current authorized location.
        """
        location_id = location_id if location_id else self._location_id
        request = ShareLocationRequest(location_id=location_id, organization_id=organization_id)
        _: ShareLocationResponse = await self._location_client.ShareLocation(request, metadata=self._metadata)

    async def unshare_location(self, organization_id: str, location_id: Optional[str] = None) -> None:
        """Unshare a location with a specific organization.

        Args:
            organization_id (str): ID of the organization to unshare the location with.
            location_id (Optional[str]): ID of the location to be unshared. Defaults to the current authorized location.
        """
        location_id = location_id if location_id else self._location_id
        request = UnshareLocationRequest(location_id=location_id, organization_id=organization_id)
        _: UnshareLocationResponse = await self._location_client.UnshareLocation(request, metadata=self._metadata)

    async def location_auth(self):
        raise NotImplementedError()

    async def create_location_secret(self):
        raise NotImplementedError()

    async def delete_location_secret(self):
        raise NotImplementedError()

    async def get_robot(self, robot_id: str) -> Robot:
        """Get a robot.

        Args:
            id (str): ID of the robot to get.

        Raises:
            GRPCError: If an invalid robot ID is passed.

        Returns:
            viam.proto.app.Robot: The robot.
        """
        request = GetRobotRequest(id=robot_id)
        response: GetRobotResponse = await self._location_client.GetRobot(request, metadata=self._metadata)
        return response.robot

    async def get_rover_rental_parts(self):
        raise NotImplementedError()

    async def get_robot_parts(self, robot_id: str) -> List[RobotPart]:
        """Get a list of all the parts under a specific robot.

        Args:
            robot_id (str): ID of the robot to get parts from.

        Raises:
            GRPCError: If an invalid robot ID is passed.

        Returns:
            List[viam.proto.app.RobotPart]: The list of robot parts.
        """
        request = GetRobotPartsRequest(robot_id=robot_id)
        response: GetRobotPartsResponse = await self._location_client.GetRobotParts(request, metadata=self._metadata)
        return response.parts

    async def get_robot_part(self, robot_part_id: Optional[str], dest: Optional[str] = None, indent: Optional[int] = 4) -> RobotPart:
        """Get a robot part.

        Args:
            robot_part_id (str): ID of the robot part to get.
            dest (Optional[str]): Optional filepath to write the robot part's config file in JSON format to.
            indent (Optional[str]): Optional size of indent when writing config to `dest`.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        Returns:
            RobotPart: The robot part.
        """
        request = GetRobotPartRequest(id=robot_part_id)
        response: GetRobotPartResponse = await self._location_client.GetRobotPart(request, metadata=self._metadata)

        if dest:
            try:
                file = open(dest, "w")
                file.write(f"{json.dumps(json.loads(response.config_json), indent=indent)}")
            except Exception as e:
                LOGGER.err(f"Failed to write config JSON to file {dest}", exc_info=e)
        return response.part

    # Not sure what a page_token is. Response contains `next_page_token`.
    # TODO: write logs to `dest`.
    async def get_robot_part_logs(
        self, robot_part_id: str, filter: Optional[str], page_token: Optional[str], dest: str, errors_only: Optional[bool] = False
    ) -> List[LogEntry]:
        """Get the logs associated with a robot part.

        Args:
            id (str): ID of the robot part to get logs from.
            filter (Optional[str]): Only include logs that contain the string `filter`. Defaults to empty string "".
            page_token (Optional[str]): Defaults to empty string "".
            dest (Optional[str]): Filepath to write the log entries to.
            errors_only (Optional[bool]): Optional boolean specifying whether or not to only include error logs. Defaults to False.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        Returns:
            List[viam.proto.app.LogEntry]: The list of log entries.
        """
        request = GetRobotPartLogsRequest(id=robot_part_id, errors_only=errors_only, filter=filter, page_token=page_token)
        response: GetRobotPartLogsResponse = await self._location_client.GetRobotPartLogs(request, metadata=self._metadata)
        return response.logs

    async def tail_robot_part_logs(self):
        raise NotImplementedError()

    async def get_robot_part_history(self):
        pass
        raise NotImplementedError(self)

    async def update_robot_part(self, robot_part_id: str, name: str, robot_config: Optional[Mapping[str, Any]] = None) -> RobotPart:
        """Change the name and/or assign a new configuration to a robot part.

        Args:
            robot_part_id (str): ID of the robot part to update.
            name (str): New name to be updated on the robot part.
            robot_config (Mapping[str, Any]): New config represented as map to be updated on the robot part.

        Raises:
            GRPCError: If either an invalid robot part ID or name is passed.

        Returns:
            viam.proto.app.RobotPart: A `RobotPart` object representing the newly updated robot part.
        """
        robot_config_struct = dict_to_struct(robot_config) if robot_config else None
        request = UpdateRobotPartRequest(id=robot_part_id, name=name, robot_config=robot_config_struct)
        response: UpdateRobotPartResponse = await self._location_client.UpdateRobotPart(request, metadata=self._metadata)
        return response.part

    async def new_robot_part(self, robot_id: str, part_name: str) -> str:
        """Create a new robot part.

        Args:
            robot_id (str): ID of the the robot to create a new part for.
            part_name (str): Name of the new part.

        Raises:
            GRPCError: If either an invalid robot ID or name is passed.

        Returns:
            str: The new robot part's ID.
        """
        request = NewRobotPartRequest(robot_id=robot_id, part_name=part_name)
        response: NewRobotPartResponse = await self._location_client.NewRobotPart(request, metadata=self._metadata)
        return response.part_id

    async def delete_robot_part(self, robot_part_id: str) -> None:
        """Delete the specified robot part.

        Args:
            robot_part_id (str): ID of the robot part to delete.

        Raises:
            GRPCError: If an invalid robot part ID is passed.
        """
        request = DeleteRobotPartRequest(part_id=robot_part_id)
        _: DeleteRobotPartResponse = await self._location_client.DeleteRobotPart(request, metadata=self._metadata)

    async def mark_part_as_main(self):
        raise NotImplementedError()

    async def mark_part_for_restart(self, robot_part_id: str) -> None:
        """Mark the specified robot part for restart.

        Args:
            robot_part_id (str): ID of the robot part to mark for restart.

        Raises:
            GRPCError: If an invalid robot part ID is passed.
        """
        request = MarkPartForRestartRequest(part_id=robot_part_id)
        _: MarkPartForRestartResponse = await self._location_client.MarkPartForRestart(request, metadata=self._metadata)

    async def create_robot_part_secret(self):
        raise NotImplementedError()

    async def delete_robot_part_secret(self):
        raise NotImplementedError()

    async def list_robots(self, location_id: Optional[str] = None) -> List[Robot]:
        """Get a list of all robots under the specified location.

        Args:
            location_id (Optional[str]): ID of the location under which to list the robots. Defaults to the current authorized location.

        Raises:
            GRPCError: If an invalid location ID is passed.

        Returns:
            List[viam.proto.app.Robot]: The list of robots.
        """
        location_id = location_id if location_id else self._location_id
        request = ListRobotsRequest(location_id=location_id)
        response: ListRobotsResponse = await self._location_client.ListRobots(request, metadata=self._metadata)
        return response.robots

    async def new_robot(self, name: str, location_id: Optional[str] = None) -> str:
        """Create a new robot.

        Args:
            name (str): Name of the new robot.
            location_id (Optional[str]): ID of the location under which to create the robot. Defaults to the current authorized location.

        Raises:
            GRPCError: If an invalid location ID is passed

        Returns:
            str: The new robot's ID.
        """
        location_id = location_id if location_id else self._location_id
        request = NewRobotRequest(name=name, location=location_id)
        response: NewRobotResponse = await self._location_client.NewRobot(request, metadata=self._metadata)
        return response.id

    async def update_robot(self, robot_id: str, name: str, location_id: Optional[str] = None) -> Robot:
        """Change the name of an existing robot.
        Args:
            robot_id (str): ID of the robot to update.
            name (str): New name to be updated on the robot.
            location_id (Optional[str]): ID of the location under which the robot exists. Defaults to the current authorized location.

        Raises:
            GRPCError: If either an invalid robot ID, name, or location ID is passed.

        Returns:
            viam.proto.app.Robot: A `Robot` object representing the newly updated robot.
        """
        location_id = location_id if location_id else self._location_id
        request = UpdateRobotRequest(id=robot_id, name=name, location=location_id)
        response: UpdateRobotResponse = await self._location_client.UpdateRobot(request, metadata=self._metadata)
        return response.robot

    async def delete_robot(self, robot_id: str) -> None:
        """Delete the specified robot.
        Args:
            robot_id (str): ID of the robot to delete.
        """
        request = DeleteRobotRequest(id=robot_id)
        _: DeleteRobotResponse = await self._location_client.DeleteRobot(request, metadata=self._metadata)

    async def list_fragments(self, organization_id: str, show_public: Optional[bool] = False) -> List[Fragment]:
        """Get a list of fragments under the specified organization.

        Args:
            organization_id (str): ID of the organization under which to list the fragments.
            show_public: Optional boolean specifiying whether or not to show public fragments. Defaults to False.

        Returns:
            List[viam.proto.app]: The list of fragments.
        """
        request = ListFragmentsRequest(organization_id=organization_id, show_public=show_public)
        response: ListFragmentsResponse = await self._location_client.ListFragments(request, metadata=self._metadata)
        return response.fragments

    async def get_fragment(self, fragment_id: str) -> Fragment:
        """Get a fragment.

        Args:
            fragment_id (str): ID of the fragment to get.

        Returns:
            viam.proto.app.Fragment: The fragment.
        """
        request = GetFragmentRequest(id=fragment_id)
        response: GetFragmentResponse = await self._location_client.GetFragment(request, metadata=self._metadata)
        return response.fragment

    async def create_fragment(self):
        raise NotImplementedError()

    async def update_fragment(self):
        raise NotImplementedError()

    async def delete_fragments(self):
        raise NotImplementedError()

    async def add_role(self):
        raise NotImplementedError()

    async def remove_role(self):
        raise NotImplementedError()

    async def list_authorizations(self):
        raise NotImplementedError()

    async def check_permissions(self):
        raise NotImplementedError()

    async def create_module(self):
        raise NotImplementedError()

    async def update_module(self):
        raise NotImplementedError()

    async def upload_module_file(self):
        raise NotImplementedError()

    async def get_module(self):
        raise NotImplementedError()

    async def list_modules(self):
        raise NotImplementedError()
