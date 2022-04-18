from grpclib import GRPCError, Status


class ViamError(Exception):
    """
    Base Viam Error
    """
    pass


class InsecureConnectionError(ViamError):
    """
    Exception raised when establishing an insecure connection

    Attributes:
        address: The endpoint of the connection
        authenticated: True if the insecure connection provided credentials
        message: Explanation of the error
    """

    def __init__(self, address: str, authenticated: bool = False) -> None:
        self.address = address
        self.authenticated = authenticated
        self.message = f'Requested address {self.address} is insecure' + \
            f'{" and will not send credentials" if self.authenticated else ""}'
        super().__init__(self.message)


class DuplicateComponentError(ViamError):
    """
    Exception raised when attempting to register a component
    with the same name as an existing component already in
    the registry
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.message = 'Cannot add component with ' + \
            f'duplicate name "{name}" to the registry'
        super().__init__(self.message)


class ComponentNotFoundError(ViamError):
    """
    Exception raised when a component is not found in the registry
    """

    def __init__(self, component: str, name: str) -> None:
        self.component = component
        self.name = name
        self.message = f'No {component} with name "{name}" ' + \
            'found in the registry'
        super().__init__(self.message)

    def grpc_error(self):
        return GRPCError(
            Status.NOT_FOUND,
            self.message
        )


class ComponentNotImplementedError(ViamError):
    """
    Exception raised when a component type is not implemented
    """

    def __init__(self, component: str):
        self.component = component
        self.message = f'Component {component} is not implemented'
        super().__init__(self.message)


class ServiceNotImplementedError(ViamError):
    """
    Exception raised when a service is not implemented on the Robot
    """

    def __init__(self, service: str):
        self.service = service
        self.message = f'Service {service} is not implemented on the Robot'
