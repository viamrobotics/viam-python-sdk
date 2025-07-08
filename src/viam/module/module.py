import argparse
import io
import logging as pylogging
import os
import sys
from collections.abc import Iterable
from inspect import iscoroutinefunction
from threading import Lock
from typing import List, Mapping, Optional, Sequence, Tuple

from grpclib.metadata import Deadline
from grpclib.utils import _service_name
from typing_extensions import Self

from viam import logging
from viam.errors import ResourceNotFoundError, ValidationError
from viam.logging import update_log_level
from viam.proto.app.robot import ComponentConfig
from viam.proto.module import (
    AddResourceRequest,
    HandlerDefinition,
    HandlerMap,
    ReadyRequest,
    ReadyResponse,
    ReconfigureResourceRequest,
    RemoveResourceRequest,
    ValidateConfigRequest,
    ValidateConfigResponse,
)
from viam.proto.robot import ResourceRPCSubtype
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry
from viam.resource.types import API, RESOURCE_TYPE_COMPONENT, RESOURCE_TYPE_SERVICE, Model, ResourceName, resource_name_from_string
from viam.robot.client import RobotClient
from viam.rpc.dial import DialOptions, _host_port_from_url
from viam.rpc.server import Server

# These imports are required to register build-in resources with the registry
from ..components.arm import Arm  # noqa: F401
from ..components.audio_input import AudioInput  # noqa: F401
from ..components.base import Base  # noqa: F401
from ..components.board import Board  # noqa: F401
from ..components.button import Button  # noqa: F401
from ..components.camera import Camera  # noqa: F401
from ..components.encoder import Encoder  # noqa: F401
from ..components.gantry import Gantry  # noqa: F401
from ..components.generic import Generic as GenericComponent  # noqa: F401
from ..components.gripper import Gripper  # noqa: F401
from ..components.input import Controller  # noqa: F401
from ..components.motor import Motor  # noqa: F401
from ..components.movement_sensor import MovementSensor  # noqa: F401
from ..components.pose_tracker import PoseTracker  # noqa: F401
from ..components.power_sensor import PowerSensor  # noqa: F401
from ..components.sensor import Sensor  # noqa: F401
from ..components.servo import Servo  # noqa: F401
from ..components.switch import Switch  # noqa: F401
from ..services.discovery import Discovery  # noqa: F401
from ..services.generic import Generic as GenericService  # noqa: F401
from ..services.motion import Motion  # noqa: F401
from ..services.navigation import Navigation  # noqa: F401
from ..services.slam import SLAM  # noqa: F401
from ..services.vision import Vision  # noqa: F401

try:
    from ..services.mlmodel import MLModel  # noqa: F401
except ImportError:
    pass

from .service import ModuleRPCService
from .types import Reconfigurable, Stoppable


def _parse_module_args() -> argparse.Namespace:
    """
    Parse command-line args. Used by the various `Module` entrypoints.
    """
    p = argparse.ArgumentParser(description="Start this viam python module")
    p.add_argument("socket_path", help="path where this module will serve a unix socket")
    p.add_argument("--log-level", type=lambda name: pylogging._nameToLevel[name.upper()], default=logging.INFO)
    p.add_argument("--tcp-mode", action="store_true")
    return p.parse_known_args()[0]


class Module:
    _address: str
    _parent_address: Optional[str] = None
    _ready: bool
    _log_level: int
    _lock: Lock
    _tcp_mode: bool
    parent: Optional[RobotClient] = None
    server: Server
    logger: pylogging.Logger

    @classmethod
    def from_args(cls) -> Self:
        """Create a new Module with the args provided in the command line. The first argument after the command must be
        the socket path. If the second argument after the command is "--log-level=debug", the Module's logger will be
        DEBUG level. Otherwise, it will be INFO level. See LogLevel documentation in the RDK for more information on how
        to start modules with a "log-level" commandline argument.

        Raises:
            Exception: If there is no socket path provided in the command line argument

        Returns:
            Module: a new Module instance
        """
        args = _parse_module_args()
        return cls(args.socket_path, log_level=args.log_level, tcp_mode=args.tcp_mode)

    @classmethod
    async def run_with_models(cls, *models: ResourceBase):
        """
        Module entrypoint that takes a list of ResourceBase implementations.
        In most cases you'll want to use run_from_registry instead (see below).
        """
        module = cls.from_args()
        for model in models:
            if not hasattr(model, "MODEL"):
                raise TypeError(f"missing MODEL field on {model}. Resource implementations must define MODEL")
            module.add_model_from_registry(model.API, model.MODEL)  # pyright: ignore [reportAttributeAccessIssue]
        await module.start()

    @classmethod
    async def run_from_registry(cls):
        """
        Module entrypoint that automatically includes all the resources you've created in your program.

        Example:

        if __name__ == '__main__':
            asyncio.run(Module.run_from_registry())

        Full example at examples/easy_resource/main.py.
        """
        module = cls.from_args()
        for key in Registry.REGISTERED_RESOURCE_CREATORS().keys():
            module.add_model_from_registry(*key.split("/"))  # pyright: ignore [reportArgumentType]
        await module.start()

    def __init__(self, address: str, *, log_level: int = logging.INFO, tcp_mode: bool = False) -> None:
        # When a module is launched by viam-server, its stdout is not connected to a tty.  In
        # response, python disables line buffering, which prevents `print` statements from being
        # immediately flushed to viam-server. This behavior can be confusing, interfere with
        # debugging, and is non-standard when compared to other languages.  Here, stdout and stderr
        # are reconfigured to immediately flush.
        if isinstance(sys.stdout, io.TextIOWrapper):
            sys.stdout.reconfigure(line_buffering=True)
        if isinstance(sys.stderr, io.TextIOWrapper):
            sys.stderr.reconfigure(line_buffering=True)
        self._address = address
        self._tcp_mode = tcp_mode
        self.server = Server(resources=[], module_service=ModuleRPCService(self))
        self._log_level = log_level

        module_name = os.environ.get("VIAM_MODULE_NAME")
        # this can happen if the user is running an old version of viam-server that doesn't set `VIAM_MODULE_NAME`
        if module_name is None:
            module_name = __name__
        self.logger = logging.getLogger(module_name)
        self._ready = True
        self._lock = Lock()

    async def _connect_to_parent(self):
        if self.parent is None:
            if self._parent_address is None:
                raise ValueError("Parent address not found")
            self.parent = await RobotClient.at_address(
                self._parent_address,
                RobotClient.Options(
                    dial_options=DialOptions(disable_webrtc=True, insecure=True),
                    log_level=self._log_level,
                ),
            )
            self.logger.debug("Starting module logging")
            logging.setParent(self.parent)

    async def _get_resource(self, name: ResourceName) -> ResourceBase:
        await self._connect_to_parent()
        assert self.parent is not None
        await self.parent.refresh()
        if name.type == RESOURCE_TYPE_COMPONENT:
            return self.parent.get_component(name)
        elif name.type == RESOURCE_TYPE_SERVICE:
            return self.parent.get_service(name)
        raise ValueError("Dependency does not describe a component nor a service")

    async def _get_dependencies(self, dependencies: Sequence[str]) -> Mapping[ResourceName, ResourceBase]:
        deps: Mapping[ResourceName, ResourceBase] = {}
        for dep in dependencies:
            rn = resource_name_from_string(dep)
            deps[rn] = await self._get_resource(rn)
        return deps

    async def start(self):
        """Start the module service and gRPC server"""
        try:
            if self._tcp_mode:
                host, port = _host_port_from_url(self._address)
                await self.server.serve(log_level=self._log_level, host=host, port=port)
            else:
                await self.server.serve(log_level=self._log_level, path=self._address)
        finally:
            await self.stop()

    async def stop(self):
        """Stop the module service and gRPC server"""
        self.logger.debug("Shutting down module")
        try:
            logging.shutdown()
            if self.parent is not None:
                await self.parent.close()
        except Exception as e:
            self.logger.error("Encountered error while shutting down module", exc_info=e)

    def set_ready(self, ready: bool):
        """Set the module's ready state. The module automatically sets to READY on load. Setting to False can be useful
        in instances where the module is not instantly ready (for example waiting on hardware)

        Args:
            ready (bool): Whether the module is ready
        """
        with self._lock:
            self._ready = ready

    async def add_resource(self, request: AddResourceRequest, *, deadline: Optional[Deadline] = None):
        dependencies = await self._get_dependencies(request.dependencies)
        config: ComponentConfig = request.config
        api = API.from_string(config.api)
        model = Model.from_string(config.model, ignore_errors=True)
        creator = Registry.lookup_resource_creator(api, model)
        resource = creator(config, dependencies)
        if deadline is not None and deadline.time_remaining() <= 0:
            raise TimeoutError("Deadline expired")
        update_log_level(resource.logger, config.log_configuration.level.upper())
        self.server.register(resource)

    async def reconfigure_resource(self, request: ReconfigureResourceRequest):
        dependencies = await self._get_dependencies(request.dependencies)
        config: ComponentConfig = request.config
        api = API.from_string(config.api)
        name = config.name
        rn = ResourceName(namespace=api.namespace, type=api.resource_type, subtype=api.resource_subtype, name=name)
        resource = self.server.get_resource(ResourceBase, rn)
        if isinstance(resource, Reconfigurable):
            resource.reconfigure(config, dependencies)
        else:
            if isinstance(resource, Stoppable):
                if iscoroutinefunction(resource.stop):
                    await resource.stop()
                else:
                    resource.stop()
            add_request = AddResourceRequest(config=request.config, dependencies=request.dependencies)
            await self.server.remove_resource(rn)
            await self.add_resource(add_request)

    async def remove_resource(self, request: RemoveResourceRequest):
        rn = resource_name_from_string(request.name)
        resource = self.server.get_resource(ResourceBase, rn)
        if isinstance(resource, Stoppable):
            if iscoroutinefunction(resource.stop):
                await resource.stop()
            else:
                resource.stop()
        await self.server.remove_resource(rn)

    async def ready(self, request: ReadyRequest) -> ReadyResponse:
        self._parent_address = request.parent_address
        await self._connect_to_parent()

        svcname_to_models: Mapping[Tuple[str, API], List[Model]] = {}
        for api_model_str in Registry.REGISTERED_RESOURCE_CREATORS().keys():
            api_str, model_str = api_model_str.split("/")
            api = API.from_string(api_str)
            model = Model.from_string(model_str)

            registration = Registry.lookup_api(api)
            service = registration.rpc_service(self.server)
            service_name = _service_name(service)

            models = svcname_to_models.get((service_name, api), [])
            models.append(model)
            svcname_to_models[(service_name, api)] = models

        handlers: List[HandlerDefinition] = []
        for key, value in svcname_to_models.items():
            svc_name, api = key
            rpc_subtype = ResourceRPCSubtype(
                subtype=ResourceName(
                    namespace=api.namespace,
                    type=api.resource_type,
                    subtype=api.resource_subtype,
                    name="",
                ),
                proto_service=svc_name,
            )
            handler_def = HandlerDefinition(subtype=rpc_subtype, models=[str(model) for model in value])
            handlers.append(handler_def)

        return ReadyResponse(ready=self._ready, handlermap=HandlerMap(handlers=handlers))

    def add_model_from_registry(self, api: API, model: Model):
        """Add a pre-registered model to this Module"""

        # All we need to do is double check that the model has already been registered
        try:
            Registry.lookup_resource_creator(api, model)
        except ResourceNotFoundError:
            raise ValueError(f"Cannot add model because it has not been registered. API: {api}. Model: {model}")

    async def validate_config(self, request: ValidateConfigRequest) -> ValidateConfigResponse:
        config: ComponentConfig = request.config
        api = API.from_string(config.api)
        model = Model.from_string(config.model)
        validator = Registry.lookup_validator(api, model)
        try:
            # backwards compatibility. Support both ([], []) or [] with deprecation warning.
            # If user's validate returns [str], it will be treated as required dependencies only.
            # Incorect formats, e.g. int, will raise ValidationError.
            _validator_return_test = validator(config)
            if not (isinstance(_validator_return_test, tuple) and len(_validator_return_test) == 2):
                msg = f"Your validate function {validator.__name__} did not return \
                        type tuple[Sequence[str], Sequence[str]]. Got {_validator_return_test}."
                self.logger.warning(msg)
                if (isinstance(_validator_return_test, Iterable) and not isinstance(_validator_return_test, str)) and all(
                    isinstance(e, str)
                    for e in _validator_return_test  # type: ignore
                ):
                    self.logger.warning(
                        f"Detected deprecated validate function signature. \
                                        Treating all dependencies {_validator_return_test} as required dependencies. \
                                        Please update to new signature Tuple[Sequence[str], Sequence[str]] soon."
                    )
                    return ValidateConfigResponse(dependencies=_validator_return_test)
                else:
                    raise ValidationError(msg)

            dependencies, optional_dependencies = _validator_return_test
            return ValidateConfigResponse(dependencies=dependencies, optional_dependencies=optional_dependencies)
        except Exception as e:
            raise ValidationError(f"{type(Exception)}: {e}").grpc_error
