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
