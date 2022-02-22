from typing import List

from grpclib.reflection.service import ServerReflection
from grpclib.server import Server as GRPCServer
from grpclib.utils import graceful_exit

from viam.components.base import ComponentBase
from viam.components.resource_manager import ResourceManager
from viam.components.servo import ServoService
from viam.metadata.service import MetadataService


class Server(ResourceManager):
    """
    gRPC Server
    """

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
        super().__init__(components)

        services = [
            MetadataService(manager=self),
            ServoService(manager=self),
        ]
        services = ServerReflection.extend(services)
        self._server = GRPCServer(services)

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
