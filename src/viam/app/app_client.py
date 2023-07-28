import json
from datetime import datetime
from typing import Any, List, Mapping, Optional

from grpclib.client import Channel
from typing_extensions import Self

from viam import logging
from viam.proto.app import (
    AppServiceStub,
    CreateLocationRequest,
    CreateLocationResponse,
    DeleteLocationRequest,
    DeleteRobotPartRequest,
    DeleteRobotRequest,
)
from viam.proto.app import Fragment as FragmentPB
from viam.proto.app import (
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
)
from viam.proto.app import LogEntry as LogEntryPB
from viam.proto.app import (
    MarkPartForRestartRequest,
    NewRobotPartRequest,
    NewRobotPartResponse,
    NewRobotRequest,
    NewRobotResponse,
    Organization,
    Robot,
)
from viam.proto.app import RobotPart as RobotPartPB
from viam.proto.app import (
    SharedSecret,
    ShareLocationRequest,
    UnshareLocationRequest,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
)
from viam.utils import datetime_to_timestamp, dict_to_struct, struct_to_dict

LOGGER = logging.getLogger(__name__)


class RobotPart:
    """A class that mirrors the `RobotPart` proto message.

    Use this class to make the attributes of a `viam.proto.app.RobotPart` more accessible and easier to read/interpret.
    """

    @classmethod
    def from_proto(cls, robot_part: RobotPartPB) -> Self:
        """Create a `RobotPart` from the .proto defined `RobotPart`.

        Args:
            robot_part (viam.proto.app.RobotPart): The object to copy from.

        Returns:
            RobotPart: The `RobotPart`.
        """
        self = cls()
        self.id = robot_part.id
        self.name = robot_part.name
        self.dns_name = robot_part.dns_name
        self.secret = robot_part.secret
        self.robot = robot_part.robot
        self.location_id = robot_part.location_id
        self.robot_config = struct_to_dict(robot_part.robot_config) if robot_part.HasField("robot_config") else None
        self.last_access = robot_part.last_access.ToDatetime() if robot_part.HasField("last_access") else None
        self.user_supplied_info = struct_to_dict(robot_part.user_supplied_info) if robot_part.HasField("user_supplied_info") else None
        self.main_part = robot_part.main_part
        self.fqdn = robot_part.fqdn
        self.local_fqdn = robot_part.fqdn
        self.created_on = robot_part.created_on.ToDatetime() if robot_part.HasField("created_on") else None
        self.secrets = robot_part.secrets
        return self

    id: str
    name: str
    dns_name: str
    secret: str
    robot: str
    location_id: str
    robot_config: Optional[Mapping[str, Any]]
    last_access: Optional[datetime]
    user_supplied_info: Optional[Mapping[str, Any]]
    main_part: bool
    fqdn: str
    local_fqdn: str
    created_on: Optional[datetime]
    secrets: List[SharedSecret]

    @property
    def proto(self) -> RobotPartPB:
        return RobotPartPB(
            id=self.id,
            name=self.name,
            dns_name=self.dns_name,
            secret=self.secret,
            robot=self.robot,
            location_id=self.location_id,
            robot_config=dict_to_struct(self.robot_config) if self.robot_config else None,
            last_access=datetime_to_timestamp(self.last_access) if self.last_access else None,
            user_supplied_info=dict_to_struct(self.user_supplied_info) if self.user_supplied_info else None,
            main_part=self.main_part,
            fqdn=self.fqdn,
            local_fqdn=self.local_fqdn,
            created_on=datetime_to_timestamp(self.created_on) if self.created_on else None,
            secrets=self.secrets,
        )


class LogEntry:
    """A class that mirrors the `LogEntry` proto message.

    Use this class to make the attributes of a `viam.proto.app.LogEntry` more accessible and easier to read/interpret.
    """

    @classmethod
    def from_proto(cls, log_entry: LogEntryPB) -> Self:
        """Create a `LogEntry` from the .proto defined `LogEntry`.

        Args:
            log_entry (viam.proto.app.LogEntry): The object to copy from.

        Returns:
            LogEntry: The `LogEntry`.
        """
        self = cls()
        self.host = log_entry.host
        self.level = log_entry.level
        self.time = log_entry.time.ToDatetime() if log_entry.HasField("time") else None
        self.logger_name = log_entry.logger_name
        self.message = log_entry.message
        self.caller = struct_to_dict(log_entry.caller) if log_entry.HasField("caller") else None
        self.stack = log_entry.stack
        self.fields = [struct_to_dict(struct) for struct in log_entry.fields]
        return self

    host: str
    level: str
    time: Optional[datetime]
    logger_name: str
    message: str
    caller: Optional[Mapping[str, Any]]
    stack: str
    fields: List[Mapping[str, Any]]

    @property
    def proto(self) -> LogEntryPB:
        return LogEntryPB(
            host=self.host,
            level=self.level,
            time=datetime_to_timestamp(self.time) if self.time else None,
            logger_name=self.logger_name,
            message=self.message,
            caller=dict_to_struct(self.caller) if self.caller else None,
            stack=self.stack,
            fields=[dict_to_struct(field) for field in self.fields],
        )


class Fragment:
    """A class that mirrors the `Fragment` proto message.

    Use this class to make the attributes of a `viam.proto.app.RobotPart` more accessible and easier to read/interpret.
    """

    @classmethod
    def from_proto(cls, fragment: FragmentPB) -> Self:
        """Create a `Fragment` from the .proto defined `Fragment`.

        Args:
            fragment (viam.proto.app.Fragment): The object to copy from.

        Returns:
            Fragment: The `Fragment`.
        """
        self = cls()
        self.id = fragment.id
        self.name = fragment.name
        self.fragment = struct_to_dict(fragment.fragment) if fragment.HasField("fragment") else None
        self.organization_owner = fragment.organization_owner
        self.public = fragment.public
        self.created_on = fragment.created_on.ToDatetime() if fragment.HasField("created_on") else None
        self.organization_name = fragment.organization_name
        self.robot_part_count = fragment.robot_part_count
        self.organization_count = fragment.organization_count
        self.only_used_by_owner = fragment.only_used_by_owner
        return self

    id: str
    name: str
    fragment: Optional[Mapping[str, Any]]
    organization_owner: str
    public: bool
    created_on: Optional[datetime]
    organization_name: str
    robot_part_count: int
    organization_count: int
    only_used_by_owner: int

    @property
    def proto(self):
        return FragmentPB(
            id=self.id,
            name=self.name,
            fragment=dict_to_struct(self.fragment) if self.fragment else None,
            organization_owner=self.organization_owner,
            public=self.public,
            created_on=datetime_to_timestamp(self.created_on) if self.created_on else None,
            organization_name=self.organization_name,
            robot_part_count=self.robot_part_count,
            organization_count=self.organization_count,
            only_used_by_owner=self.only_used_by_owner,
        )


class AppClient:
    """gRPC client for method calls to app.

    Constructor is used by `ViamClient` to instantiate relevant service stub. Calls to `AppClient`  methods should be made through
    `ViamClient`.
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str], location_id: Optional[str] = None):
        """Create an `AppClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
            location_id (Optional[str]): Default location ID.
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

    async def list_organizations(self) -> List[Organization]:
        """List the organization(s) the user is an authorized owner of.

        Returns:
            List[viam.proto.app.Organization]: The list of organizations.
        """
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
            parent_location_id (Optional[str]): Optional parent location to put the location under. Defaults to the location ID provided at
                `AppClient` instantiation. A root level location is created if no default location ID exists.

        Raises:
            GRPCError: If either an invalid organization ID, name, or parent location ID is passed.

        Returns:
            viam.proto.app.Location: The newly created location.
        """
        location_id = parent_location_id if parent_location_id else self._location_id
        request = CreateLocationRequest(organization_id=organization_id, name=name, parent_location_id=location_id)
        response: CreateLocationResponse = await self._location_client.CreateLocation(request, metadata=self._metadata)
        return response.location

    async def get_location(self, location_id: Optional[str] = None) -> Location:
        """Get a location.

        Args:
            location_id (Optional[str]): ID of the location to get. Defaults to the location ID provided at `AppClient` instantiation.
                If no default location ID was passed, a GRPCError will be thrown.

        Raises:
            GRPCError: If an invalid location ID is passed.

        Returns:
            viam.proto.app.Location: The location.
        """
        location_id = location_id if location_id else self._location_id
        request = GetLocationRequest(location_id=location_id)
        response: GetLocationResponse = await self._location_client.GetLocation(request, metadata=self._metadata)
        return response.location

    async def update_location(
        self, location_id: str, name: Optional[str] = None, parent_location_id: Optional[str] = None, region: str = None
    ) -> Location:
        """Change the name of a location and/or assign it a new parent location.

        Args:
            location_id (str): ID of the location to update.
            name (Optional[str]): Optional new name to be updated on the location. Defaults to the empty string "" (i.e., the name doesn't
                change).
            parent_location_id(Optional[str]): Optional new parent location to move the location under. Defaults to the empty string ""
                (i.e., no new parent location is assigned).
            name (Optional[str]): Optional new GCS region to associate the location with. Currently, this parameter is not explicitly used
                in app.

        Raises:
            GRPCError: If either an invalid location ID, name, or parent location ID is passed.

        Returns:
            viam.proto.app.Location: The newly updated location.
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
        await self._location_client.DeleteLocation(request, metadata=self._metadata)

    async def list_locations(self, organization_id: str) -> List[Location]:
        """Get a list of all locations under the specified organization.

        Args:
            organization_id (str): ID of the organization to retrieve the locations from.

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

        Raises:
            GRPCError: Permission denied. A location can only be shared by users who are owners of both organizations involved. An
                `AppClient` cannot be an authorized owner of two organizations. Permission will always be denied when calling this method. A
                GRPCError is also thrown when attempting to share a location with an organization it is already shared with.
        """
        location_id = location_id if location_id else self._location_id
        request = ShareLocationRequest(location_id=location_id, organization_id=organization_id)
        await self._location_client.ShareLocation(request, metadata=self._metadata)

    async def unshare_location(self, organization_id: str, location_id: Optional[str] = None) -> None:
        """Unshare a location with a specific organization.

        Args:
            organization_id (str): ID of the organization to unshare the location with.
            location_id (Optional[str]): ID of the location to be unshared. Defaults to the current authorized location.

        Raises:
            GRPCError: Permission denied. A location can only be unshared by users who are owners of both organizations involved. An
                `AppClient` cannot be an authorized owner of two organizations. Permission will always be denied when calling this method. A
                GRPCError is also thrown when attempting to unshare a location with an organization it is not already shared with.
        """
        location_id = location_id if location_id else self._location_id
        request = UnshareLocationRequest(location_id=location_id, organization_id=organization_id)
        await self._location_client.UnshareLocation(request, metadata=self._metadata)

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
            List[viam.app.app_client.RobotPart]: The list of robot parts.
        """
        request = GetRobotPartsRequest(robot_id=robot_id)
        response: GetRobotPartsResponse = await self._location_client.GetRobotParts(request, metadata=self._metadata)
        return [RobotPart.from_proto(robot_part=part) for part in response.parts]

    async def get_robot_part(self, robot_part_id: Optional[str], dest: Optional[str] = None, indent: Optional[int] = None) -> RobotPart:
        """Get a robot part.

        Args:
            robot_part_id (str): ID of the robot part to get.
            dest (Optional[str]): Optional filepath to write the robot part's config file in JSON format to.
            indent (Optional[int]): Optional size (in number of spaces) of indent when writing config to `dest`. Defaults to 4.

        Raises:
            GRPCError: If an invalid robot part ID is passed.

        Returns:
            viam.app.app_client.RobotPart: The robot part.
        """
        indent = indent if indent else 4
        request = GetRobotPartRequest(id=robot_part_id)
        response: GetRobotPartResponse = await self._location_client.GetRobotPart(request, metadata=self._metadata)

        if dest:
            try:
                file = open(dest, "w")
                file.write(f"{json.dumps(json.loads(response.config_json), indent=indent)}")
            except Exception as e:
                LOGGER.err(f"Failed to write config JSON to file {dest}", exc_info=e)

        return RobotPart.from_proto(robot_part=response.part)

    async def get_robot_part_logs(
        self,
        robot_part_id: str,
        filter: Optional[str] = None,
        dest: Optional[str] = None,
        errors_only: Optional[bool] = None,
        num_pages: Optional[int] = None,
    ) -> List[LogEntry]:
        """Get the logs associated with a robot part.

        Args:
            robot_part_id (str): ID of the robot part to get logs from.
            filter (Optional[str]): Only include logs with messages that contain the string `filter`. Defaults to empty string "" (i.e., no
                filter).
            dest (Optional[str]): Optional filepath to write the log entries to.
            errors_only (Optional[bool]): Optional boolean specifying whether or not to only include error logs. Defaults to True.
            num_pages: Optional number of pages of logs to return. Passing 0 returns all pages. Defaults to 1. All pages or the first
                `num_pages` pages will be returned, whichever comes first.

        Raises:
            GRPCError: If an invalid robot part ID is passed.
            AssertionError: If `num_pages` is less than 0.

        Returns:
            List[viam.app.app_client.LogEntry]: The list of log entries.
        """
        num_pages = num_pages if num_pages is not None else 1
        assert num_pages >= 0
        errors_only = errors_only if errors_only else True
        page_token = ""
        logs = []

        while True:
            next_page_token = await self._get_robot_part_logs(
                robot_part_id=robot_part_id, filter=filter, errors_only=errors_only, page_token=page_token, logs=logs
            )
            num_pages -= 1
            if not next_page_token or len(next_page_token) == 0 or num_pages == 0:
                break
            page_token = next_page_token

        if dest:
            try:
                file = open(dest, "w")
                for log in logs:
                    time = log.time
                    level = log.level.upper()
                    logger_name = log.logger_name.split(".")[0]
                    file_name = log.caller["File"]
                    line_number = int(log.caller["Line"])
                    message = log.message
                    file.write(f"{time}\t\t{level}\t{logger_name}\t{file_name}:{line_number}\t{message}\n")
            except Exception as e:
                LOGGER.error(f"Failed to write robot part logs to file {dest}", exc_info=e)

        return logs

    async def _get_robot_part_logs(
        self, robot_part_id: str, filter: str, errors_only: bool, page_token: str, logs: List[LogEntryPB]
    ) -> str:
        request = GetRobotPartLogsRequest(id=robot_part_id, errors_only=errors_only, filter=filter, page_token=page_token)
        response: GetRobotPartLogsResponse = await self._location_client.GetRobotPartLogs(request, metadata=self._metadata)
        logs += [LogEntry.from_proto(log) for log in response.logs]
        return response.next_page_token

    async def tail_robot_part_logs(self):
        raise NotImplementedError()

    async def get_robot_part_history(self):
        pass
        raise NotImplementedError(self)

    async def update_robot_part(self, robot_part_id: str, name: str, robot_config: Optional[Mapping[str, Any]] = None) -> RobotPart:
        """Change the name and assign an optional new configuration to a robot part.

        Args:
            robot_part_id (str): ID of the robot part to update.
            name (str): New name to be updated on the robot part.
            robot_config (Mapping[str, Any]): Optional new config represented as a dictionary to be updated on the robot part. The robot
                part's config will remain as is (no change) if one isn't passed.

        Raises:
            GRPCError: If either an invalid robot part ID, name, or config is passed.

        Returns:
            viam.app.app_client.RobotPart: The newly updated robot part.
        """
        robot_config_struct = dict_to_struct(robot_config) if robot_config else None
        request = UpdateRobotPartRequest(id=robot_part_id, name=name, robot_config=robot_config_struct)
        response: UpdateRobotPartResponse = await self._location_client.UpdateRobotPart(request, metadata=self._metadata)
        return RobotPart.from_proto(robot_part=response.part)

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
            robot_part_id (str): ID of the robot part to delete. Must be specified.

        Raises:
            GRPCError: If an invalid robot part ID is passed.
        """
        request = DeleteRobotPartRequest(part_id=robot_part_id)
        await self._location_client.DeleteRobotPart(request, metadata=self._metadata)

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
        await self._location_client.MarkPartForRestart(request, metadata=self._metadata)

    async def create_robot_part_secret(self):
        raise NotImplementedError()

    async def delete_robot_part_secret(self):
        raise NotImplementedError()

    async def list_robots(self, location_id: Optional[str] = None) -> List[Robot]:
        """Get a list of all robots under the specified location.

        Args:
            location_id (Optional[str]): ID of the location to retrieve the robots from. Defaults to the location ID provided at
                `AppClient` instantiation.

        Raises:
            GRPCError: If an invalid location ID is passed or one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

        Returns:
            List[viam.proto.app.Robot]: The list of robots.
        """
        location_id = location_id if location_id else self._location_id
        request = ListRobotsRequest(location_id=location_id)
        response: ListRobotsResponse = await self._location_client.ListRobots(request, metadata=self._metadata)
        return response.robots

    async def new_robot(self, name: str = None, location_id: Optional[str] = None) -> str:
        """Create a new robot.

        Args:
            name (str): Name of the new robot.
            location_id (Optional[str]): ID of the location under which to create the robot. Defaults to the current authorized location.

        Raises:
            GRPCError: If an invalid location ID is passed or one isn't passed and there was no location ID provided at `AppClient`
                instantiation.

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
            location_id (Optional[str]): ID of the location under which the robot exists. Defaults to the location ID provided at
                `AppClient` instantiation

        Raises:
            GRPCError: If either an invalid robot ID, name, or location ID is passed or a location ID isn't passed and there was no location
                ID provided at `AppClient` instantiation.

        Returns:
            viam.proto.app.Robot: The newly updated robot.
        """
        location_id = location_id if location_id else self._location_id
        request = UpdateRobotRequest(id=robot_id, name=name, location=location_id)
        response: UpdateRobotResponse = await self._location_client.UpdateRobot(request, metadata=self._metadata)
        return response.robot

    async def delete_robot(self, robot_id: str) -> None:
        """Delete the specified robot.

        Args:
            robot_id (str): ID of the robot to delete.

        Raises:
            GRPCError: If an invalid robot ID is passed.
        """
        request = DeleteRobotRequest(id=robot_id)
        await self._location_client.DeleteRobot(request, metadata=self._metadata)

    async def list_fragments(self, organization_id: str, show_public: Optional[bool] = True) -> List[Fragment]:
        """Get a list of fragments under the specified organization.

        Args:
            organization_id (str): ID of the organization under which to list the fragments.
            show_public: Optional boolean specifiying whether or not to only include public fragments. Defaults to True.

        Raises:
            GRPCError: If an invalid organization ID is passed.

        Returns:
            List[viam.app.app_client.Fragment]: The list of fragments.
        """
        request = ListFragmentsRequest(organization_id=organization_id, show_public=show_public)
        response: ListFragmentsResponse = await self._location_client.ListFragments(request, metadata=self._metadata)
        return [Fragment.from_proto(fragment=fragment) for fragment in response.fragments]

    async def get_fragment(self, fragment_id: str) -> Fragment:
        """Get a fragment.

        Args:
            fragment_id (str): ID of the fragment to get.

        Raises:
            GRPCError: If an invalid fragment ID is passed.

        Returns:
            viam.app.app_client.Fragment: The fragment.
        """
        request = GetFragmentRequest(id=fragment_id)
        response: GetFragmentResponse = await self._location_client.GetFragment(request, metadata=self._metadata)
        return Fragment.from_proto(fragment=response.fragment)

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
