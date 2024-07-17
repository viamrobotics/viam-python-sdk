from typing import Mapping, Optional

from grpclib.client import Channel
from typing_extensions import Self

from viam import logging
from viam.app.app_client import AppClient
from viam.app.billing_client import BillingClient
from viam.app.data_client import DataClient
from viam.app.ml_training_client import MLTrainingClient
from viam.app.provisioning_client import ProvisioningClient
from viam.robot.client import RobotClient
from viam.rpc.dial import DialOptions, _dial_app, _get_access_token

LOGGER = logging.getLogger(__name__)


class ViamClient:
    """gRPC client for all communication and interaction with app.

    `ViamClient` class for creating and managing specialized client instances.
    There is currently 1 way to instantiate a `ViamClient` object::

        ViamClient.create_from_dial_options(...)
    """

    @classmethod
    async def create_from_dial_options(cls, dial_options: DialOptions, app_url: Optional[str] = None) -> Self:
        """Create `ViamClient` that establishes a connection to the Viam app.

        ::

            dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
            ViamClient.create_from_dial_options(dial_options)

        Args:
            dial_options (viam.rpc.dial.DialOptions): Required information for authorization and connection to app.
                `creds` and `auth_entity` fields are required.
            app_url: (Optional[str]): URL of app. Uses app.viam.com if not specified.

        Raises:
            ValueError: If the input parameters are missing a required field or simply invalid.

        Returns:
            Self: The `ViamClient`.
        """
        if dial_options.credentials is None:
            raise ValueError("dial_options.credentials cannot be None.")
        if dial_options.credentials.type == "robot-secret":
            raise ValueError("dial_options.credentials.type cannot be 'robot-secret'")
        if dial_options.auth_entity is None:
            raise ValueError("dial_options.auth_entity cannot be None.")

        self = cls()
        self._dial_options = dial_options
        self._location_id = None
        if dial_options.credentials.type == "robot-location-secret":
            self._location_id = dial_options.auth_entity.split(".")[1]
        if app_url is None:
            app_url = "app.viam.com"
        self._channel = await _dial_app(app_url)
        access_token = await _get_access_token(self._channel, dial_options.auth_entity, dial_options)
        self._metadata = {"authorization": f"Bearer {access_token}"}
        return self

    _channel: Channel
    _metadata: Mapping[str, str]
    _closed: bool = False
    _location_id: Optional[str]
    _dial_options: DialOptions

    @property
    def data_client(self) -> DataClient:
        """Instantiate and return a `DataClient` object used to make `data` and `data_sync` method calls.
        To use the `DataClient`, you must first instantiate a `ViamClient`.

        ::

            async def connect() -> ViamClient:
                # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
                dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
                return await ViamClient.create_from_dial_options(dial_options)

            async def main():
                viam_client = await connect()

                # Instantiate a DataClient to run data client API methods on
                data_client = viam_client.data_client
        """
        return DataClient(self._channel, self._metadata)

    @property
    def app_client(self) -> AppClient:
        """Instantiate and return an `AppClient` used to make  `app` method calls.
        To use the `AppClient`, you must first instantiate a `ViamClient`.

        ::

            async def connect() -> ViamClient:
                # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
                dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
                return await ViamClient.create_from_dial_options(dial_options)


            async def main():
                viam_client = await connect()

                # Instantiate an AppClient called "fleet" to run fleet management API methods on
                fleet = viam_client.app_client
        """
        return AppClient(self._channel, self._metadata, self._location_id)

    @property
    def ml_training_client(self) -> MLTrainingClient:
        """Instantiate and return a `MLTrainingClient` used to make `ml_training` method calls.
        To use the `MLTrainingClient`, you must first instantiate a `ViamClient`.

        ::

            async def connect() -> ViamClient:
                # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
                dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
                return await ViamClient.create_from_dial_options(dial_options)


            async def main():
                viam_client = await connect()

                # Instantiate an MLTrainingClient to run ML training client API methods on
                ml_training_client = viam_client.ml_training_client
        """
        return MLTrainingClient(self._channel, self._metadata)

    @property
    def billing_client(self) -> BillingClient:
        """Instantiate and return a `BillingClient` used to make `billing` method calls.
            To use the `BillingClient`, you must first instantiate a `ViamClient`.

        ::

            async def connect() -> ViamClient:
                # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
                dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
                return await ViamClient.create_from_dial_options(dial_options)


            async def main():
                viam_client = await connect()

                # Instantiate a BillingClient to run billing client API methods on
                billing_client = viam_client.billing_client
        """

        return BillingClient(self._channel, self._metadata)

    @property
    def provisioning_client(self) -> ProvisioningClient:
        """Instantiate and return a `ProvisioningClient` used to make  `provisioning` method calls.
        To use the `ProvisioningClient`, you must first instantiate a `ViamClient`.

        ::

            async def connect() -> ViamClient:
                # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
                dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
                return await ViamClient.create_from_dial_options(dial_options)


            async def main():
                viam_client = await connect()

                # Instantiate a ProvisioningClient to run provisioning API methods on
                provisioning_client = viam_client.provisioning_client
        """
        return ProvisioningClient(self._channel, self._metadata)

    def close(self):
        """Close opened channels used for the various service stubs initialized."""
        if self._closed:
            LOGGER.debug("ViamClient is already closed.")
            return
        LOGGER.debug("Closing gRPC channel to app.")
        self._channel.close()
        self._closed = True

    async def connect_to_machine(self, *, address: Optional[str] = None, id: Optional[str] = None) -> RobotClient:
        """Connect to a machine using existing credentials.

        A connection can be attempted using either the machine's address or its ID.
        If both an address and ID are provided, the address will take precedence and the ID will be ignored.

        ::

            async def connect() -> ViamClient:
                # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
                dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
                return await ViamClient.create_from_dial_options(dial_options)


            async def main():
                viam_client = await connect()

                # Connect to a machine and obtain a RobotClient
                # Replace "<MACHINE_ADDRESS>" (including brackets) with your machine's connection address
                machine = await viam_client.connect_to_machine(address="<MACHINE_ADDRESS>")

        Args:
            address (Optional[str]): The address (FQDN) of the machine. Defaults to None.
            id (Optional[str]): The ID (as a UUID) of the machine. Defaults to None.

        Raises:
            ValueError: If neither an address nor ID is provided.

        Returns:
            RobotClient: The active connection to the machine.
        """
        if address is None and id is None:
            raise ValueError("Either a machine address or ID must be provided")

        if id is not None and address is None:
            parts = await self.app_client.get_robot_parts(id)
            main_part = next(p for p in parts if p.main_part)
            address = main_part.fqdn

        opts = RobotClient.Options(dial_options=self._dial_options)

        assert address is not None
        return await RobotClient.at_address(address, opts)
