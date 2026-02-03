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
        self.message = f"Requested address {self.address} is insecure" + f'{" and will not send credentials" if self.authenticated else ""}'
        super().__init__(self.message)


class DuplicateResourceError(ViamError):
    """
    Exception raised when attempting to register a resource
    with the same name as an existing resource already in
    the registry
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.message = f'Cannot add resource with duplicate name "{name}" to the registry'
        super().__init__(self.message)


class ViamGRPCError(ViamError):
    """
    Exception raised if it could happen as a part of GRPC calls.
    """

    def __init__(self, message: str = "", grpc_code: Status = Status.INTERNAL) -> None:
        self.message = message
        self.grpc_code = grpc_code

    @property
    def grpc_error(self) -> GRPCError:
        return GRPCError(self.grpc_code, self.message)


class ResourceNotFoundError(ViamGRPCError):
    """
    Exception raised when a resource is not found in the registry
    """

    def __init__(self, resource: str, name: str) -> None:
        self.resource = resource
        self.name = name
        self.message = f'No {resource} with name "{name}" ' + "found in the registry"
        self.grpc_code = Status.NOT_FOUND


class MethodNotImplementedError(ViamGRPCError):
    """
    Exception raised when specific methods are unimplemented.
    """

    def __init__(self, method_name: str):
        self.message = f"Method {method_name} not implemented."
        self.grpc_code = Status.UNIMPLEMENTED


class NotSupportedError(ViamGRPCError):
    """
    Exception raised when specific component functionality is not supported
    """

    def __init__(self, message: str):
        self.message = message
        self.grpc_code = Status.UNIMPLEMENTED


class ValidationError(ViamGRPCError):
    """
    Exception raised when there is an error during module validation
    """

    def __init__(self, message: str):
        self.message = message
        self.grpc_code = Status.INVALID_ARGUMENT


class NoCaptureToStoreError(ViamGRPCError):
    """
    Exception raised in filter module to signal that data capture should not be stored
    """

    def __init__(self):
        self.message = "no capture from filter module"  # Do not change the contents of this string
        self.grpc_code = Status.FAILED_PRECONDITION
