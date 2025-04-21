import asyncio
import importlib
import pkgutil
import sys
from copy import deepcopy
from datetime import timedelta
from enum import IntEnum
from threading import Lock, Thread
from typing import MutableMapping, Optional

from grpclib import Status
from grpclib.client import Channel
from grpclib.events import RecvTrailingMetadata, SendRequest, listen
from grpclib.exceptions import GRPCError, StreamTerminatedError
from grpclib.metadata import _MetadataLike

from viam import logging
from viam.gen.common.v1.common_pb2 import safety_heartbeat_monitored
from viam.proto.robot import RobotServiceStub, SendSessionHeartbeatRequest, StartSessionRequest, StartSessionResponse
from viam.rpc.dial import DialOptions, dial

LOGGER = logging.getLogger(__name__)
SESSION_METADATA_KEY = "viam-sid"


class _SupportedState(IntEnum):
    UNKNOWN = 0
    TRUE = 1
    FALSE = 2


class SessionsClient:
    """
    A Session allows a client to express that it is actively connected and
    supports stopping actuating components when it's not.
    """

    channel: Channel
    client: RobotServiceStub
    _address: str  # direct dial address, when using webRTC this is the local socket rather than a robot address
    _robot_address: Optional[str]  # the actual machine address on app.viam.com. important for creating a sessions client on Windows
    _dial_options: DialOptions
    _disabled: bool
    _lock: Lock
    _current_id: str
    _heartbeat_interval: Optional[timedelta]
    _supported: _SupportedState
    _thread: Optional[Thread]

    _HEARTBEAT_MONITORED_METHODS: MutableMapping[str, bool] = {}

    def __init__(
        self,
        channel: Channel,
        direct_dial_address: str,
        dial_options: Optional[DialOptions],
        *,
        disabled: bool = False,
        robot_addr: Optional[str] = None,
    ):
        self.channel = channel
        self.client = RobotServiceStub(channel)
        self._address = direct_dial_address
        self._robot_address = robot_addr
        self._disabled = disabled
        self._dial_options = deepcopy(dial_options) if dial_options is not None else DialOptions()
        if sys.platform != "win32" and sys.platform != "cygwin":
            self._dial_options.disable_webrtc = True
        self._lock = Lock()
        self._current_id = ""
        self._heartbeat_interval = None
        self._supported = _SupportedState.UNKNOWN
        self._thread = None

        listen(self.channel, SendRequest, self._send_request)
        listen(self.channel, RecvTrailingMetadata, self._recv_trailers)

    def reset(self):
        with self._lock:
            self._reset()

    def _reset(self):
        LOGGER.debug("resetting session")
        self._supported = _SupportedState.UNKNOWN
        self._current_id = ""
        self._heartbeat_interval = None
        if self._thread is not None:
            try:
                self._thread.join(timeout=1)
            except RuntimeError:
                LOGGER.debug("failed to join session heartbeat thread")
            self._thread = None

    async def _send_request(self, event: SendRequest):
        if self._disabled:
            return

        if not self._is_safety_heartbeat_monitored(event.method_name):
            return

        event.metadata.update(await self.metadata)

    async def _recv_trailers(self, event: RecvTrailingMetadata):
        if event.status == Status.INVALID_ARGUMENT and event.status_message == "SESSION_EXPIRED":
            LOGGER.debug("Session expired")
            self.reset()

    @property
    async def metadata(self) -> _MetadataLike:
        with self._lock:
            if self._disabled or self._supported != _SupportedState.UNKNOWN:
                return self._metadata

        request = StartSessionRequest(resume=self._current_id)
        try:
            response: StartSessionResponse = await self.client.StartSession(request)
        except GRPCError as error:
            if error.status == Status.UNIMPLEMENTED:
                with self._lock:
                    self._reset()
                    self._supported = _SupportedState.FALSE
                    return self._metadata
            else:
                raise

        if response is None:
            raise GRPCError(status=Status.INTERNAL, message="Expected response to start session")

        if response.heartbeat_window is None:
            raise GRPCError(status=Status.INTERNAL, message="Expected heartbeat window in response to start session")

        with self._lock:
            self._supported = _SupportedState.TRUE
            self._heartbeat_interval = response.heartbeat_window.ToTimedelta()
            self._current_id = response.id

        # tick once to ensure heartbeats are supported
        await self._heartbeat_tick(self.client)

        with self._lock:
            if self._thread is not None:
                self._reset()
            if self._supported == _SupportedState.TRUE:
                # We send heartbeats faster than the interval window to
                # ensure that we don't fall outside of it and expire the session.
                wait = self._heartbeat_interval.total_seconds() / 5

                self._thread = Thread(
                    name="heartbeat-thread",
                    target=asyncio.run,
                    args=(self._heartbeat_process(wait),),
                    daemon=True,
                )
                self._thread.start()

            return self._metadata

    async def _heartbeat_tick(self, client: RobotServiceStub):
        with self._lock:
            if not self._current_id:
                LOGGER.debug("Failed to send heartbeat, session client reset")
                return
            request = SendSessionHeartbeatRequest(id=self._current_id)

        try:
            await client.SendSessionHeartbeat(request)
        except (GRPCError, StreamTerminatedError):
            LOGGER.debug("Heartbeat terminated", exc_info=True)
            self.reset()
        else:
            LOGGER.debug("Sent heartbeat successfully")

    def _get_local_addr(self) -> str:
        if sys.platform != "win32" and sys.platform != "cygwin":
            # if we're not on windows, we want the direct dial address
            return self._address

        # return `robot_address` if it exists, otherwise fallback
        # when using TCP (i.e., on Windows), we need to create a connection to the actual
        # robot address for a sessions client to maintain connectivity successfully
        return self._robot_address if self._robot_address is not None else self._address

    async def _heartbeat_process(self, wait: float):
        addr = self._get_local_addr()
        channel = await dial(address=addr, options=self._dial_options)
        client = RobotServiceStub(channel.channel)
        while True:
            with self._lock:
                if self._supported != _SupportedState.TRUE:
                    return
            await self._heartbeat_tick(client)
            await asyncio.sleep(wait)

    @property
    def _metadata(self) -> _MetadataLike:
        if self._supported == _SupportedState.TRUE and self._current_id != "":
            return {SESSION_METADATA_KEY: self._current_id}

        return {}

    def _is_safety_heartbeat_monitored(self, method: str) -> bool:
        if method in self._HEARTBEAT_MONITORED_METHODS:
            return self._HEARTBEAT_MONITORED_METHODS[method]

        parts = method.split("/")
        if len(parts) != 3:
            self._HEARTBEAT_MONITORED_METHODS[method] = False
            return False
        service_path = parts[1]
        method_name = parts[2]

        parts = service_path.split(".")
        if len(parts) < 5:
            self._HEARTBEAT_MONITORED_METHODS[method] = False
            return False
        if parts[0] != "viam":
            self._HEARTBEAT_MONITORED_METHODS[method] = False
            return False
        resource_type = parts[1]
        resource_subtype = parts[2]
        version = parts[3]
        service_name = parts[4]
        try:
            module = importlib.import_module(f"viam.gen.{resource_type}.{resource_subtype}.{version}")
            submods = pkgutil.iter_modules(module.__path__)
            for mod in submods:
                if "_pb2" in mod.name:
                    submod = getattr(module, mod.name)
                    DESCRIPTOR = getattr(submod, "DESCRIPTOR")
                    for service in DESCRIPTOR.services_by_name.values():
                        if service.name == service_name:
                            for method_actual in service.methods:
                                if method_actual.name == method_name:
                                    options = method_actual.GetOptions()
                                    if options.HasExtension(safety_heartbeat_monitored):
                                        is_monitored = options.Extensions[safety_heartbeat_monitored]
                                        self._HEARTBEAT_MONITORED_METHODS[method] = is_monitored
                                        return is_monitored
                                    self._HEARTBEAT_MONITORED_METHODS[method] = False
                                    return False
            self._HEARTBEAT_MONITORED_METHODS[method] = False
            return False
        except Exception:
            self._HEARTBEAT_MONITORED_METHODS[method] = False
            return False
