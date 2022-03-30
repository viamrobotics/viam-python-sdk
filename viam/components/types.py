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


class CameraMimeType(Enum):
    RAW = 'image/raw-rgba'
    BEST = 'image/viambest'
    JPEG = 'image/jpeg'
    PNG = 'image/png'
    PCD = 'pointcloud/pcd'
