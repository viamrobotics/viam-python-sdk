from typing import Mapping

from grpclib.client import Channel
from typing_extensions import Self

from viam import logging
from viam.app.data.client import DataClient
from viam.rpc.dial import DialOptions, _dial_app, _get_access_token

LOGGER = logging.getLogger(__name__)


class AppClient:
    """gRPC client for all communication and interaction with app.

    Use create() to instantiate an AppClient::

        AppClient.create(...)
    """

    @classmethod
    async def create(cls, dial_options: DialOptions) -> Self:
        """Create an AppClient that establishes a connection to app.viam.com.

        Args:

            dial_options (viam.rpc.dial.DialOptions): Required information for authorization and connection to app. `creds` and
                `auth_entity` fields are required.

        Returns:
            Self: The `AppClient`.
        """
        self = cls()
        self._channel = await _dial_app(dial_options)
        access_token = await _get_access_token(self._channel, dial_options.auth_entity, dial_options)
        self._metadata = {"authorization": f"Bearer {access_token}"}
        return self

    _channel: Channel
    _metadata: Mapping[str, str]
    _closed: bool = False

    @property
    def data_client(self) -> DataClient:
        """Insantiate and return a DataClient used to make `data` and `data_sync` method calls."""
        return DataClient(self._channel, self._metadata)

    def close(self):
        """Close opened channels used for the various service stubs initialized."""
        if self._closed:
            LOGGER.debug("AppClient is already closed.")
            return
        LOGGER.debug("Closing gRPC channel to app.")
        self._channel.close()
        self._closed = True
