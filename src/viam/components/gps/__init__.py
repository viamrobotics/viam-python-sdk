from viam.registry import ComponentRegistration, Registry

from .client import GPSClient
from .gps import GPS, LocalGPS
from .service import GPSService

__all__ = [
    'GPS',
    'LocalGPS',
]

Registry.register(
    ComponentRegistration(
        GPS,
        'gps',
        GPSService,
        lambda name, channel: GPSClient(name, channel),
    )
)
