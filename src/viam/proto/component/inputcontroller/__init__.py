"""
@generated by Viam.
Do not edit manually!
"""
from ....gen.component.inputcontroller.v1.input_controller_grpc import InputControllerServiceBase, InputControllerServiceStub
from ....gen.component.inputcontroller.v1.input_controller_pb2 import (
    Event,
    GetControlsRequest,
    GetControlsResponse,
    GetEventsRequest,
    GetEventsResponse,
    Status,
    StreamEventsRequest,
    StreamEventsResponse,
    TriggerEventRequest,
    TriggerEventResponse,
)
from ....gen.component.inputcontroller.v1.input_controller_unimplemented_grpc import UnimplementedInputControllerServiceBase

__all__ = [
    "InputControllerServiceBase",
    "InputControllerServiceStub",
    "Event",
    "GetControlsRequest",
    "GetControlsResponse",
    "GetEventsRequest",
    "GetEventsResponse",
    "Status",
    "StreamEventsRequest",
    "StreamEventsResponse",
    "TriggerEventRequest",
    "TriggerEventResponse",
    "UnimplementedInputControllerServiceBase",
]
