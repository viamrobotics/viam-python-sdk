from typing import Mapping, Optional

from grpclib.client import Channel
from typing_extensions import Self

from viam import logging
from viam.app.app_client import AppClient
from viam.app.billing_client import BillingClient
from viam.app.data_client import DataClient
from viam.app.ml_training_client import MLTrainingClient
from viam.rpc.dial import DialOptions, _dial_app, _get_access_token

LOGGER = logging.getLogger(__name__)


class ViamClient:
    """gRPC client for all communication and interaction with app.

    There is currently 1 way to instantiate a `ViamClient` object::

        ViamClient.create_from_dial_options(...)
    """

    @classmethod
    async def create_from_dial_options(cls, dial_options: DialOptions, app_url: Optional[str] = None) -> Self:
        """Create `ViamClient` that establishes a connection to the Viam app.

        Args:

            dial_options (viam.rpc.dial.DialOptions): Required information for authorization and connection to app. `creds` and
                `auth_entity` fields are required.
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

    @property
    def data_client(self) -> DataClient:
        """Insantiate and return a `DataClient` used to make `data` and `data_sync` method calls."""
        return DataClient(self._channel, self._metadata)

    @property
    def app_client(self) -> AppClient:
        """Insantiate and return an `AppClient` used to make  `app` method calls."""
        return AppClient(self._channel, self._metadata, self._location_id)

    @property
    def ml_training_client(self) -> MLTrainingClient:
        """Instantiate and return a `MLTrainingClient` used to make `ml_training` method calls."""
        return MLTrainingClient(self._channel, self._metadata)

    @property
    def billing_client(self) -> BillingClient:
        """Instantiate and return a `BillingClient` used to make `billing` method calls."""
        return BillingClient(self._channel, self._metadata)

    def close(self):
        """Close opened channels used for the various service stubs initialized."""
        if self._closed:
            LOGGER.debug("ViamClient is already closed.")
            return
        LOGGER.debug("Closing gRPC channel to app.")
        self._channel.close()
        self._closed = True
