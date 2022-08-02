from enum import Enum


class CameraMimeType(str, Enum):
    RAW = "image/raw-rgba"
    BEST = "image/viambest"
    JPEG = "image/jpeg"
    PNG = "image/png"
    PCD = "pointcloud/pcd"
