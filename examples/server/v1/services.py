from datetime import datetime
from numpy.typing import NDArray
from typing import Dict, List, Optional, Tuple
from tests.mocks.services import MockMLModel, MockSLAM
from viam.services.slam import Pose, MappingMode, SLAM
from viam.services.mlmodel import Metadata, MLModel


class ExampleMLModel(MLModel):
    def __init__(self, name: str):
        self.input_data = MockMLModel.EMPTY_NDARRAYS
        self.output_data = MockMLModel.EMPTY_NDARRAYS
        self.meta = MockMLModel.META
        super().__init__(name)

    async def infer(self, input_tensors: Dict[str, NDArray], *, timeout: Optional[float] = None) -> Dict[str, NDArray]:
        return self.output_data

    async def metadata(self, *, timeout: Optional[float] = None) -> Metadata:
        return self.meta


class ExampleSLAM(SLAM):
    def __init__(self, name: str):
        self.position = MockSLAM.POSITION
        self.internal_chunks = MockSLAM.INTERNAL_STATE_CHUNKS
        self.point_cloud_chunks = MockSLAM.POINT_CLOUD_PCD_CHUNKS
        self.cloud_slam = MockSLAM.CLOUD_SLAM
        self.mapping_mode = MockSLAM.MAPPING_MODE
        super().__init__(name)

    async def get_internal_state(self, **kwargs) -> List[bytes]:
        return self.internal_chunks

    async def get_point_cloud_map(self, **kwargs) -> List[bytes]:
        return self.point_cloud_chunks

    async def get_position(self, **kwargs) -> Pose:
        return self.position

    async def get_properties(self, **kwargs) -> Tuple[bool, MappingMode.ValueType]:
        return (self.cloud_slam, self.mapping_mode)
