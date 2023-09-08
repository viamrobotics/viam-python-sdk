from datetime import datetime
from typing import Dict, List, Optional
from tests.mocks.services import MockMLModel, MockSLAM
from viam.services.slam import Pose, SLAM
from viam.services.mlmodel import Metadata, MLModel
from viam.utils import ValueTypes


class ExampleMLModel(MLModel):
    def __init__(self, name: str):
        self.input_data = MockMLModel.EMPTY_NDARRAYS
        self.output_data = MockMLModel.EMPTY_NDARRAYS
        self.meta = MockMLModel.META
        super().__init__(name)

    async def infer(self, input_tensors: Dict[str, ValueTypes], *, timeout: Optional[float] = None) -> Dict[str, ValueTypes]:
        return self.output_data

    async def metadata(self, *, timeout: Optional[float] = None) -> Metadata:
        return self.meta


class ExampleSLAM(SLAM):
    def __init__(self, name: str):
        self.position = MockSLAM.POSITION
        self.internal_chunks = MockSLAM.INTERNAL_STATE_CHUNKS
        self.point_cloud_chunks = MockSLAM.POINT_CLOUD_PCD_CHUNKS
        self.time = MockSLAM.LAST_UPDATE
        super().__init__(name)

    async def get_internal_state(self, **kwargs) -> List[bytes]:
        return self.internal_chunks

    async def get_point_cloud_map(self, **kwargs) -> List[bytes]:
        return self.point_cloud_chunks

    async def get_position(self, **kwargs) -> Pose:
        return self.position

    async def get_latest_map_info(self, **kwargs) -> datetime:
        return self.time
