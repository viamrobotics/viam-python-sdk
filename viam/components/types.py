from enum import Enum


class ComponentType(Enum):
    ARM = 'arm'
    BASE = 'base'
    BOARD = 'board'
    CAMERA = 'camera'
    GANTRY = 'gantry'
    GPS = 'gps'
    GRIPPER = 'gripper'
    IMU = 'imu'
    MOTOR = 'motor'
    POSE_TRACKER = 'pose_tracker'
    SENSOR = 'sensor'
    SERVO = 'servo'
