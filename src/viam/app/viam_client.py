from typing import Mapping

from grpclib.client import Channel
from typing_extensions import Self

from viam import logging
from viam.app.app_client import AppClient
from viam.app.data_client import DataClient
from viam.rpc.dial import DialOptions, _dial_app, _get_access_token

LOGGER = logging.getLogger(__name__)


class ViamClient:
    """gRPC client for all communication and interaction with app.

    Use create() to instantiate a ViamClient::

        ViamClient.create(...)
    """

    @classmethod
    async def create_from_dial_options(cls, dial_options: DialOptions) -> Self:
        """Create `ViamClient` that establishes a connection to app.viam.com.

        Args:

            dial_options (viam.rpc.dial.DialOptions): Required information for authorization and connection to app. `creds` and
                `auth_entity` fields are required.

        Raises:
            AssertionError: If the type provided in the credentials of the `DialOptions` object is 'robot-secret'.

        Returns:
            Self: The `ViamClient`.
        """
        assert dial_options.credentials.type != "robot-secret"
        self = cls()
        self._location_id = dial_options.auth_entity.split(".")[1]
        self._channel = await _dial_app(dial_options)
        access_token = await _get_access_token(self._channel, dial_options.auth_entity, dial_options)
        self._metadata = {"authorization": f"Bearer {access_token}"}
        return self

    _channel: Channel
    _metadata: Mapping[str, str]
    _closed: bool = False
    _location_id: str

    @property
    def data_client(self) -> DataClient:
        """Insantiate and return a `DataClient` used to make `data` and `data_sync` method calls."""
        return DataClient(self._channel, self._metadata)

    @property
    def app_client(self) -> AppClient:
        """Insantiate and return an `AppClient` used to make  `app` method calls."""
        return AppClient(self._channel, self._metadata, self._location_id)

    def close(self):
        """Close opened channels used for the various service stubs initialized."""
        if self._closed:
            LOGGER.debug("AppClient is already closed.")
            return
        LOGGER.debug("Closing gRPC channel to app.")
        self._channel.close()
        self._closed = True
