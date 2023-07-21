from typing import Mapping

from grpclib.client import Channel

from viam.proto.app import AppServiceStub


class LocationClient:
    """gRPC client for method calls to app.

    Constructor is used by `AppClient` to instantiate relevant service stub. Calls to `LocationClient`  methods should be made through
    `AppClient`.
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str]):
        """Create a `LocationClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
        """
        self._metadata = metadata
        self._location_client = AppServiceStub(channel)

    _location_client: AppServiceStub
    _metadata: Mapping[str, str]

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

    async def create_location(self):
        pass

    async def get_location(self):
        pass

    async def update_location(self):
        pass

    async def delete_location(self):
        pass

    async def list_locations(self):
        pass

    async def share_location(self):
        pass

    async def unshare_location(self):
        pass

    async def location_auth(self):
        raise NotImplementedError()

    async def create_location_secret(self):
        raise NotImplementedError()

    async def delete_location_secret(self):
        raise NotImplementedError()

    async def get_robot(self):
        pass

    async def get_rover_rental_parts(self):
        raise NotImplementedError()

    async def get_robot_parts(self):
        pass

    async def get_robot_part(self):
        pass

    async def get_robot_part_logs(self):
        pass

    async def tail_robot_part_logs(self):
        raise NotImplementedError()

    async def get_robot_part_history(self):
        pass
        raise NotImplementedError(self)

    async def update_robot_part(self):
        pass

    async def new_robot_part(self):
        pass

    async def delete_robot_part(self):
        pass

    async def mark_part_as_main(self):
        raise NotImplementedError()

    async def mark_part_for_restart(self):
        pass

    async def create_robot_part_secret(self):
        raise NotImplementedError()

    async def delete_robot_part_secret(self):
        raise NotImplementedError()

    async def list_robots(self):
        pass

    async def new_robot(self):
        pass

    async def update_robot(self):
        pass

    async def delete_robot(self):
        pass

    async def list_fragments(self):
        pass

    async def get_fragment(self):
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
