from typing import Dict, Optional
from tests.mocks.services import MockMLModel
from viam.services.mlmodel import Metadata, MLModel
from viam.utils import ValueTypes


class ExampleMLModel(MLModel):
    def __init__(self, name: str):
        self.input_data = MockMLModel.INPUT_DATA
        self.output_data = MockMLModel.OUTPUT_DATA
        self.meta = MockMLModel.META
        super().__init__(name)

    async def infer(self, input_data: Dict[str, ValueTypes], *, timeout: Optional[float] = None) -> Dict[str, ValueTypes]:
        return self.output_data

    async def metadata(self, *, timeout: Optional[float] = None) -> Metadata:
        return self.meta
