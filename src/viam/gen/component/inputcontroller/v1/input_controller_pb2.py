"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3component/inputcontroller/v1/input_controller.proto\x12!viam.component.inputcontroller.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"4\n\x12GetControlsRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller"1\n\x13GetControlsResponse\x12\x1a\n\x08controls\x18\x01 \x03(\tR\x08controls"2\n\x10GetEventsRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller"U\n\x11GetEventsResponse\x12@\n\x06events\x18\x01 \x03(\x0b2(.viam.component.inputcontroller.v1.EventR\x06events"u\n\x13TriggerEventRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller\x12>\n\x05event\x18\x02 \x01(\x0b2(.viam.component.inputcontroller.v1.EventR\x05event"\x16\n\x14TriggerEventResponse"}\n\x05Event\x12.\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x04time\x12\x14\n\x05event\x18\x02 \x01(\tR\x05event\x12\x18\n\x07control\x18\x03 \x01(\tR\x07control\x12\x14\n\x05value\x18\x04 \x01(\x01R\x05value"\xf3\x01\n\x13StreamEventsRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller\x12U\n\x06events\x18\x02 \x03(\x0b2=.viam.component.inputcontroller.v1.StreamEventsRequest.EventsR\x06events\x1ae\n\x06Events\x12\x18\n\x07control\x18\x01 \x01(\tR\x07control\x12\x16\n\x06events\x18\x02 \x03(\tR\x06events\x12)\n\x10cancelled_events\x18\x03 \x03(\tR\x0fcancelledEvents"V\n\x14StreamEventsResponse\x12>\n\x05event\x18\x01 \x01(\x0b2(.viam.component.inputcontroller.v1.EventR\x05event"J\n\x06Status\x12@\n\x06events\x18\x01 \x03(\x0b2(.viam.component.inputcontroller.v1.EventR\x06events2\x85\x06\n\x16InputControllerService\x12\xb8\x01\n\x0bGetControls\x125.viam.component.inputcontroller.v1.GetControlsRequest\x1a6.viam.component.inputcontroller.v1.GetControlsResponse":\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/input/{controller}/controls\x12\xb0\x01\n\tGetEvents\x123.viam.component.inputcontroller.v1.GetEventsRequest\x1a4.viam.component.inputcontroller.v1.GetEventsResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/input/{controller}/events\x12\xc1\x01\n\x0cStreamEvents\x126.viam.component.inputcontroller.v1.StreamEventsRequest\x1a7.viam.component.inputcontroller.v1.StreamEventsResponse">\x82\xd3\xe4\x93\x028\x126/viam/api/v1/component/input/{controller}/event_stream0\x01\x12\xb8\x01\n\x0cTriggerEvent\x126.viam.component.inputcontroller.v1.TriggerEventRequest\x1a7.viam.component.inputcontroller.v1.TriggerEventResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/component/input/{controller}/eventBU\n%com.viam.component.inputcontroller.v1Z,go.viam.com/api/component/inputcontroller/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.inputcontroller.v1.input_controller_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n%com.viam.component.inputcontroller.v1Z,go.viam.com/api/component/inputcontroller/v1'
    _INPUTCONTROLLERSERVICE.methods_by_name['GetControls']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['GetControls']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/input/{controller}/controls'
    _INPUTCONTROLLERSERVICE.methods_by_name['GetEvents']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['GetEvents']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/input/{controller}/events'
    _INPUTCONTROLLERSERVICE.methods_by_name['StreamEvents']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['StreamEvents']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/viam/api/v1/component/input/{controller}/event_stream'
    _INPUTCONTROLLERSERVICE.methods_by_name['TriggerEvent']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['TriggerEvent']._serialized_options = b'\x82\xd3\xe4\x93\x021"//viam/api/v1/component/input/{controller}/event'
    _GETCONTROLSREQUEST._serialized_start = 153
    _GETCONTROLSREQUEST._serialized_end = 205
    _GETCONTROLSRESPONSE._serialized_start = 207
    _GETCONTROLSRESPONSE._serialized_end = 256
    _GETEVENTSREQUEST._serialized_start = 258
    _GETEVENTSREQUEST._serialized_end = 308
    _GETEVENTSRESPONSE._serialized_start = 310
    _GETEVENTSRESPONSE._serialized_end = 395
    _TRIGGEREVENTREQUEST._serialized_start = 397
    _TRIGGEREVENTREQUEST._serialized_end = 514
    _TRIGGEREVENTRESPONSE._serialized_start = 516
    _TRIGGEREVENTRESPONSE._serialized_end = 538
    _EVENT._serialized_start = 540
    _EVENT._serialized_end = 665
    _STREAMEVENTSREQUEST._serialized_start = 668
    _STREAMEVENTSREQUEST._serialized_end = 911
    _STREAMEVENTSREQUEST_EVENTS._serialized_start = 810
    _STREAMEVENTSREQUEST_EVENTS._serialized_end = 911
    _STREAMEVENTSRESPONSE._serialized_start = 913
    _STREAMEVENTSRESPONSE._serialized_end = 999
    _STATUS._serialized_start = 1001
    _STATUS._serialized_end = 1075
    _INPUTCONTROLLERSERVICE._serialized_start = 1078
    _INPUTCONTROLLERSERVICE._serialized_end = 1851