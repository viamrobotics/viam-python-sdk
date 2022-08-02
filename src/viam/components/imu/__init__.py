from viam.registry import ComponentRegistration, Registry

from .client import IMUClient
from .imu import IMU, Acceleration, AngularVelocity, EulerAngles, Magnetometer, Orientation
from .service import IMUService

__all__ = [
    "IMU",
    "Orientation",
    "Acceleration",
    "AngularVelocity",
    "EulerAngles",
    "Magnetometer",
]

Registry.register(
    ComponentRegistration(
        IMU,
        "imu",
        IMUService,
        lambda name, channel: IMUClient(name, channel),
    )
)
