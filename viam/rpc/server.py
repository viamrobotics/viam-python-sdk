from typing import List, Type

from grpclib.server import Server as GRPCServer
from grpclib.utils import graceful_exit

from viam.components.base import ComponentBase
from viam.components.registry import Registry, RegistryManager, ResourceType
from viam.components.servo.server import ServoServer


class Server(RegistryManager):
    """
    gRPC Server
    """

    registry: Registry

    def __init__(
        self,
        components: List[ComponentBase]
    ):
        """
        Initialize the Server with a list of components
        to be managed.

        Args:
            components (List[ComponentBase]): List of components to be managed
        """

        self.registry = Registry(components)

        self._server = GRPCServer(
            [
                ServoServer(manager=self),
            ]
        )

    async def serve(self, host: str = 'localhost', port: int = 9090):
        """
        Server the gRPC server on the provided host and port

        Args:
            host (str, optional): Desired hostname of the server.
                                  Defaults to 'localhost'.
            port (int, optional): Desired port of the server.
                                  Defaults to 9090.
        """
        with graceful_exit([self._server]):
            await self._server.start(host, port)
            print(f'Serving on {host}:{port}')
            await self._server.wait_closed()

    def close(self):
        self._server.close()

    def get_component(
        self,
        of_type: Type[ResourceType],
        name: str
    ) -> ResourceType:
        return super().get_component(of_type, name)

    @classmethod
    async def create_and_serve(
        cls,
        components: List[ComponentBase],
        host: str = "localhost",
        port: int = 9090
    ):
        """
        Convenience method to create and start the server.

        Args:
            components (List[ComponentBase]): List of components to manage
            host (str, optional): Desired hostname. Defaults to "localhost".
            port (int, optional): Desired port. Defaults to 9090.
        """
        server = cls(components)
        await server.serve(host, port)
