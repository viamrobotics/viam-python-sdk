from enum import Enum


class CameraMimeType(Enum):
    RAW = 'image/raw-rgba'
    BEST = 'image/viambest'
    JPEG = 'image/jpeg'
    PNG = 'image/png'
    PCD = 'pointcloud/pcd'
