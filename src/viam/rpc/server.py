from typing import TYPE_CHECKING, Callable, List, Optional

from grpclib import GRPCError, Status
from grpclib._typing import IServable
from grpclib.const import Handler
from grpclib.events import RecvRequest, listen
from grpclib.reflection.service import ServerReflection
from grpclib.server import Server as GRPCServer
from grpclib.utils import graceful_exit

from viam import logging
from viam.errors import ViamGRPCError
from viam.resource.base import ResourceBase
from viam.resource.manager import ResourceManager
from viam.resource.registry import Registry
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.robot.service import RobotService

from .signaling import SignalingService

if TYPE_CHECKING:
    from viam.module.service import ModuleService

LOGGER = logging.getLogger(__name__)


class Server(ResourceManager):
    """
    gRPC Server
    """

    def __init__(self, components: List[ResourceBase], *, module_service: Optional["ModuleService"] = None):
        """
        Initialize the Server with a list of components
        to be managed.

        Args:
            components (List[ComponentBase]): List of components to be managed
        """
        super().__init__(components)

        services = [SignalingService(), RobotService(manager=self)]
        for registration in Registry.REGISTERED_SUBTYPES().values():
            if issubclass(registration.rpc_service, ResourceRPCServiceBase):
                services.append(registration.rpc_service(manager=self))
            else:
                services.append(registration.rpc_service())

        if module_service is not None:
            services.append(module_service)
        services = ServerReflection.extend(services)
        services = _patch_mappings(services)

        self._server = GRPCServer(services)

    async def _grpc_event_handler(self, event: RecvRequest):
        host = None
        port = None
        address = event.peer.addr()
        if address:
            host = address[0]
            port = address[1]
        msg = f"[gRPC Request] {host or 'xxxx'}:{port or 'xxxx'} - {event.method_name}"
        LOGGER.info(msg)

    async def serve(
        self,
        host: Optional[str] = "localhost",
        port: Optional[int] = 9090,
        log_level: Optional[int] = logging.INFO,
        *,
        path: Optional[str] = None,
    ):
        """
        Server the gRPC server on the provided host and port

        Args:
            host (Optional[str], optional): Desired hostname of the server. Defaults to "localhost".
            port (Optional[int], optional): Desired port of the server. Defaults to 9090.
            log_level (Optional[int], optional): The minimum log level. To not receive any logs, set to None. Defaults to logging.INFO.
            path (Optional[str], optional): UNIX socket path. Takes precedence over `host` and `port` if set. Defaults to None.
        """
        if log_level is None:
            logging.silence()
        else:
            logging.setLevel(log_level)
        listen(self._server, RecvRequest, self._grpc_event_handler)

        with graceful_exit([self._server]):
            if path:
                await self._server.start(path=path)
                LOGGER.info(f"Serving on {path}")
            else:
                await self._server.start(host, port)
                LOGGER.info(f"Serving on {host}:{port}")
            await self._server.wait_closed()
            LOGGER.debug("gRPC server closed")

    @classmethod
    async def create_and_serve(
        cls,
        components: List[ResourceBase],
        host: Optional[str] = "localhost",
        port: Optional[int] = 9090,
        log_level: int = logging.INFO,
        *,
        path: Optional[str] = None,
    ):
        """
        Convenience method to create and start the server.

        Args:
            components (List[ComponentBase]): List of components to manage
            host (str, optional): Desired hostname. Defaults to "localhost".
            port (int, optional): Desired port. Defaults to 9090.
            log_level(int, optional): The minimum log level.
                To not receive any logs, set to None.
                Defaults to logging.INFO
            path (Optional[str], optional): UNIX socket path. Takes precedence over `host` and `port` if set. Defaults to None.
        """
        server = cls(components)
        await server.serve(host, port, log_level, path=path)


def _grpc_error_wrapper(func: Callable):
    """
    Wrap a function so that any exceptions get raised as GRPCErrors to the client.

    Args:
        func (Callable): The function that should be wrapped

    Returns:
        The method that is now wrapped to raise GRPCErrors
    """

    async def interceptor(*args, **kwargs):
        try:
            new_func = await func(*args, **kwargs)
            return new_func
        except GRPCError:
            raise
        except ViamGRPCError as e:
            raise e.grpc_error
        except Exception as e:
            raise GRPCError(Status.UNKNOWN, f"{e.__class__.__name__} - {e}")

    return interceptor


def _patch_mappings(services: List[IServable]) -> List[IServable]:
    """Replace the methods of all given services with a wrapped method that has error handling

    Args:
        services (List[IServable]): The services that should be patched

    Returns:
        services (List[IServable]): The patched services with new mapping functions
    """
    for service in services:

        def patch_mapping():
            mapping = service.__mapping__()
            new_mapping = {}
            for method, handler in mapping.items():
                new_method = _grpc_error_wrapper(handler[0])
                new_mapping[method] = Handler(new_method, *handler[1:])

            return lambda: new_mapping

        service.__mapping__ = patch_mapping()
    return services
