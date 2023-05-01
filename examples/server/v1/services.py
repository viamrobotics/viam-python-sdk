from typing import Dict, Optional
from viam.services.mlmodel import File, LabelType, Metadata, MLModelService, TensorInfo
from viam.utils import ValueTypes


class ExampleMLModelService(MLModelService):
    def __init__(self, name: str):
        self.input_data = {"image": [10, 10, 255, 0, 0, 255, 255, 0, 100]}
        self.output_data = {
            "n_detections": [3],
            "confidence_scores": [[0.9084375, 0.7359375, 0.33984375]],
            "labels": [[0, 0, 4]],
            "locations": [[0.1, 0.4, 0.22, 0.4], [0.02, 0.22, 0.77, 0.90], [0.40, 0.50, 0.40, 0.50]],
        }
        meta_inputs = [TensorInfo(name="image", description="i0", data_type="uint8", shape=[300, 200])]
        meta_outputs = [
            TensorInfo(name="n_detections", description="o0", data_type="int32", shape=[1]),
            TensorInfo(name="confidence_scores", description="o1", data_type="float32", shape=[3, 1]),
            TensorInfo(
                name="labels",
                description="o2",
                data_type="int32",
                shape=[3, 1],
                associated_files=[
                    File(
                        name="category_labels.txt",
                        description="these labels represent types of plants",
                        label_type=LabelType.LABEL_TYPE_TENSOR_VALUE,
                    )
                ],
            ),
            TensorInfo(name="locations", description="o3", data_type="float32", shape=[4, 3, 1]),
        ]
        self.meta = Metadata(
            name="fake_detector", type="object_detector", description="desc", input_info=meta_inputs, output_info=meta_outputs
        )
        super().__init__(name)

    async def infer(self, input_data: Dict[str, ValueTypes], *, timeout: Optional[float] = None) -> Dict[str, ValueTypes]:
        return self.output_data

    async def metadata(self, *, timeout: Optional[float] = None) -> Metadata:
        return self.meta
