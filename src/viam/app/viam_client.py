from datetime import datetime
from typing import Mapping, Optional, List

from grpclib.client import Channel
from typing_extensions import Self

from viam import logging
from viam.app.app_client import AppClient
from viam.app.data_client import DataClient
from viam.app.ml_training_client import MLTrainingClient
from viam.rpc.dial import DialOptions, _dial_app, _get_access_token
from viam.proto.app.data import (
    CaptureInterval,
    Filter,
    TagsFilter,
)
from viam.utils import datetime_to_timestamp

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

    def close(self):
        """Close opened channels used for the various service stubs initialized."""
        if self._closed:
            LOGGER.debug("ViamClient is already closed.")
            return
        LOGGER.debug("Closing gRPC channel to app.")
        self._channel.close()
        self._closed = True

    @staticmethod
    def create_filter(
        component_name: Optional[str] = None,
        component_type: Optional[str] = None,
        method: Optional[str] = None,
        robot_name: Optional[str] = None,
        robot_id: Optional[str] = None,
        part_name: Optional[str] = None,
        part_id: Optional[str] = None,
        location_ids: Optional[List[str]] = None,
        organization_ids: Optional[List[str]] = None,
        mime_type: Optional[List[str]] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        tags: Optional[List[str]] = None,
        bbox_labels: Optional[List[str]] = None,
    ) -> Filter:
        """Create a `Filter`.

        Args:
            component_name (Optional[str]): Optional name of the component that captured the data being filtered (e.g., "left_motor").
            component_type (Optional[str]): Optional type of the componenet that captured the data being filtered (e.g., "motor").
            method (Optional[str]): Optional name of the method used to capture the data being filtered (e.g., "IsPowered").
            robot_name (Optional[str]): Optional name of the robot associated with the data being filtered (e.g., "viam_rover_1").
            robot_id (Optional[str]): Optional ID of the robot associated with the data being filtered.
            part_name (Optional[str]): Optional name of the system part associated with the data being filtered (e.g., "viam_rover_1-main").
            part_id (Optional[str]): Optional ID of the system part associated with the data being filtered.
            location_ids (Optional[List[str]]): Optional list of location IDs associated with the data being filtered.
            organization_ids (Optional[List[str]]): Optional list of organization IDs associated with the data being filtered.
            mime_type (Optional[List[str]]): Optional mime type of data being filtered (e.g., "image/png").
            start_time (Optional[datetime.datetime]): Optional start time of an interval to filter data by.
            end_time (Optional[datetime.datetime]): Optional end time of an interval to filter data by.
            tags (Optional[List[str]]): Optional list of tags attached to the data being filtered (e.g., ["test"]).
            bbox_labels (Optional[List[str]]): Optional list of bounding box labels attached to the data being filtered (e.g., ["square",
                "circle"]).

        Returns:
            viam.proto.app.data.Filter: The `Filter` object.
        """
        return Filter(
            component_name=component_name if component_name else "",
            component_type=component_type if component_type else "",
            method=method if method else "",
            robot_name=robot_name if robot_name else "",
            robot_id=robot_id if robot_id else "",
            part_name=part_name if part_name else "",
            part_id=part_id if part_id else "",
            location_ids=location_ids,
            organization_ids=organization_ids,
            mime_type=mime_type,
            interval=(
                CaptureInterval(
                    start=datetime_to_timestamp(start_time),
                    end=datetime_to_timestamp(end_time),
                )
            )
            if start_time or end_time
            else None,
            tags_filter=TagsFilter(tags=tags),
            bbox_labels=bbox_labels,
        )
