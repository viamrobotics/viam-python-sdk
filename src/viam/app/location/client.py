from typing import Mapping, Optional, Any

from grpclib.client import Channel

from viam.proto.app import AppServiceStub


class LocationClient:
    """gRPC client for method calls to app.

    Constructor is used by `AppClient` to instantiate relevant service stub. Calls to `LocationClient`  methods should be made through
    `AppClient`.
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str], location_id: str):
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

    async def list_organizations(self):
        raise NotImplementedError()

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

    async def create_location(self, organization_id: str, name: str, parent_location_id: Optional[str] = None):
        """
        Args:
            organization_id (str): ID of the organization to create the location under.
            name (str): Name of the location.
            parent_location_id (Optional[str]): Optional new parent location to move the location under. Defaults to the empty string "".
        """
        pass

    async def get_location(self, location_id: str):
        """
        Args:
            location_id (str): ID of the location to get.
        """
        pass

    # `region` parameter is not used in app.
    async def update_location(self, location_id: str, name: Optional[str], parent_location_id: Optional[str], region: str = None):
        """
        Args:
            location_id (str): ID of the location to update.
            name (Optional[str]): Optional new name to be updated on the location. Defaults to the empty string "".
            parent_location_id(Optional[str]): Optional new parent location to move the location under. Defaults to the empty string "".
        """
        pass

    async def delete_location(self, location_id: str):
        """
        Args:
            location_id (str): ID of the location to delete.
        """
        pass

    async def list_locations(self, organization_id: str):
        """
        Args:
            organization_id (str): ID of the organization under which to list the locations.
        """
        pass

    async def share_location(self, location_id: str, organization_id: str):
        """
        Args:
            location_id (str): ID of the location to be shared.
            organization_id (str): ID of the organization to share the location with.
        """
        pass

    async def unshare_location(self, location_id: str, organization_id: str):
        """
        Args:
            location_id (str): ID of the location to be unshared.
            organization_id (str): ID of the organization to unshare the location with.
        """
        pass

    async def location_auth(self):
        raise NotImplementedError()

    async def create_location_secret(self):
        raise NotImplementedError()

    async def delete_location_secret(self):
        raise NotImplementedError()

    async def get_robot(self, robot_id: str):
        """
        Args:
            id (str): ID of the robot to get.
        """
        pass

    async def get_rover_rental_parts(self):
        raise NotImplementedError()

    async def get_robot_parts(self, robot_id: str):
        """
        Args:
            robot_id (str): ID of the robot to get parts from.
        """
        pass

    async def get_robot_part(self, robot_part_id: Optional[str]):
        """
        Args:
            robot_part_id (str): ID of the robot part to get.
        """
        pass

    # Not sure what a page_token is.
    async def get_robot_part_logs(
        self,
        robot_part_id: str,
        filter: Optional[str],
        page_token: Optional[str],
        errors_only: Optional[bool] = False
    ):
        """
        Args:
            id (str): ID of the robot part to get logs from.
            filter (Optional[str]): Only include logs that contain the string `filter`. Defaults to empty string "".
            page_token (Optional[str]): Defaults to empty string "".
            errors_only (Optional[bool]): Optional boolean specifying whether or not to only include error logs. Defaults to False.
        """
        pass

    async def tail_robot_part_logs(self):
        raise NotImplementedError()

    async def get_robot_part_history(self):
        pass
        raise NotImplementedError(self)

    async def update_robot_part(self, robot_part_id: str, name: str, robot_config: Optional[Mapping[str, Any]]):
        """
        Args:
            robot_part_id (str): ID of the robot part to update.
            name (str): New name to be updated on the robot part.
            robot_config (Mapping[str, Any]): New config represented as map to be updated on the robot part.
        """
        pass

    async def new_robot_part(self, robot_id: str, part_name: str):
        """
        Args:
            robot_id (str): ID of the the robot to create a new part for.
            part_name (str): Name of the new part.
        """
        pass

    async def delete_robot_part(self, robot_part_id: str):
        """
        Args:
            robot_part_id (str): ID of the robot part to delete.
        """
        pass

    async def mark_part_as_main(self):
        raise NotImplementedError()

    async def mark_part_for_restart(self, robot_part_id: str):
        """
        Args:
            robot_part_id (str): ID of the robot part to mark for restart.
        """
        pass

    async def create_robot_part_secret(self):
        raise NotImplementedError()

    async def delete_robot_part_secret(self):
        raise NotImplementedError()

    async def list_robots(self, location_id: str):
        """
        Args:
            location_id (str): ID of the location under which to list the robots.
        """
        pass

    async def new_robot(self, name: str, location: str):
        """
        Args:
            name (str): Name of the new robot.
            location_id: ID of the location under which to create the robot.
        """
        pass

    async def update_robot(self, robot_id: str, name: str, location_id: str):
        """
        Args:
            robot_id (str): ID of the robot to update.
            name (str): New name to be updated on the robot.
            location_id (str): ID of the location under which the robot exists.
        """
        pass

    async def delete_robot(self, robot_id: str):
        """
        Args:
            robot_id (str): ID of the robot to delete.
        """
        pass

    async def list_fragments(self, organization_id: str, show_public: Optional[bool] = False):
        """
        Args:
            organization_id (str): ID of the organization under which to list the fragments.
            show_public: Optional boolean specifiying whether or not to show public fragments. Defaults to False.
        """
        pass

    async def get_fragment(self, fragment_id: str):
        """
        Args:
            fragment_id (str): ID of the fragment to get.
        """
        pass

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
