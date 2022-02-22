"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=proto/api/component/inputcontroller/v1/input_controller.proto\x12&proto.api.component.inputcontroller.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"4\n\x12GetControlsRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller"1\n\x13GetControlsResponse\x12\x1a\n\x08controls\x18\x01 \x03(\tR\x08controls"2\n\x10GetEventsRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller"Z\n\x11GetEventsResponse\x12E\n\x06events\x18\x01 \x03(\x0b2-.proto.api.component.inputcontroller.v1.EventR\x06events"z\n\x13TriggerEventRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller\x12C\n\x05event\x18\x02 \x01(\x0b2-.proto.api.component.inputcontroller.v1.EventR\x05event"\x16\n\x14TriggerEventResponse"}\n\x05Event\x12.\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x04time\x12\x14\n\x05event\x18\x02 \x01(\tR\x05event\x12\x18\n\x07control\x18\x03 \x01(\tR\x07control\x12\x14\n\x05value\x18\x04 \x01(\x01R\x05value"\xf8\x01\n\x13StreamEventsRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller\x12Z\n\x06events\x18\x02 \x03(\x0b2B.proto.api.component.inputcontroller.v1.StreamEventsRequest.EventsR\x06events\x1ae\n\x06Events\x12\x18\n\x07control\x18\x01 \x01(\tR\x07control\x12\x16\n\x06events\x18\x02 \x03(\tR\x06events\x12)\n\x10cancelled_events\x18\x03 \x03(\tR\x0fcancelledEvents"[\n\x14StreamEventsResponse\x12C\n\x05event\x18\x01 \x01(\x0b2-.proto.api.component.inputcontroller.v1.EventR\x05event2\x99\x06\n\x16InputControllerService\x12\xbd\x01\n\x0bGetControls\x12:.proto.api.component.inputcontroller.v1.GetControlsRequest\x1a;.proto.api.component.inputcontroller.v1.GetControlsResponse"5\x82\xd3\xe4\x93\x02/\x12-/api/v1/component/input/{controller}/controls\x12\xb5\x01\n\tGetEvents\x128.proto.api.component.inputcontroller.v1.GetEventsRequest\x1a9.proto.api.component.inputcontroller.v1.GetEventsResponse"3\x82\xd3\xe4\x93\x02-\x12+/api/v1/component/input/{controller}/events\x12\xc6\x01\n\x0cStreamEvents\x12;.proto.api.component.inputcontroller.v1.StreamEventsRequest\x1a<.proto.api.component.inputcontroller.v1.StreamEventsResponse"9\x82\xd3\xe4\x93\x023\x121/api/v1/component/input/{controller}/event_stream0\x01\x12\xbd\x01\n\x0cTriggerEvent\x12;.proto.api.component.inputcontroller.v1.TriggerEventRequest\x1a<.proto.api.component.inputcontroller.v1.TriggerEventResponse"2\x82\xd3\xe4\x93\x02,"*/api/v1/component/input/{controller}/eventBm\n3com.viam.rdk.proto.api.component.inputcontroller.v1Z6go.viam.com/rdk/proto/api/component/inputcontroller/v1b\x06proto3')
_GETCONTROLSREQUEST = DESCRIPTOR.message_types_by_name['GetControlsRequest']
_GETCONTROLSRESPONSE = DESCRIPTOR.message_types_by_name['GetControlsResponse']
_GETEVENTSREQUEST = DESCRIPTOR.message_types_by_name['GetEventsRequest']
_GETEVENTSRESPONSE = DESCRIPTOR.message_types_by_name['GetEventsResponse']
_TRIGGEREVENTREQUEST = DESCRIPTOR.message_types_by_name['TriggerEventRequest']
_TRIGGEREVENTRESPONSE = DESCRIPTOR.message_types_by_name['TriggerEventResponse']
_EVENT = DESCRIPTOR.message_types_by_name['Event']
_STREAMEVENTSREQUEST = DESCRIPTOR.message_types_by_name['StreamEventsRequest']
_STREAMEVENTSREQUEST_EVENTS = _STREAMEVENTSREQUEST.nested_types_by_name['Events']
_STREAMEVENTSRESPONSE = DESCRIPTOR.message_types_by_name['StreamEventsResponse']
GetControlsRequest = _reflection.GeneratedProtocolMessageType('GetControlsRequest', (_message.Message,), {'DESCRIPTOR': _GETCONTROLSREQUEST, '__module__': 'proto.api.component.inputcontroller.v1.input_controller_pb2'})
_sym_db.RegisterMessage(GetControlsRequest)
GetControlsResponse = _reflection.GeneratedProtocolMessageType('GetControlsResponse', (_message.Message,), {'DESCRIPTOR': _GETCONTROLSRESPONSE, '__module__': 'proto.api.component.inputcontroller.v1.input_controller_pb2'})
_sym_db.RegisterMessage(GetControlsResponse)
GetEventsRequest = _reflection.GeneratedProtocolMessageType('GetEventsRequest', (_message.Message,), {'DESCRIPTOR': _GETEVENTSREQUEST, '__module__': 'proto.api.component.inputcontroller.v1.input_controller_pb2'})
_sym_db.RegisterMessage(GetEventsRequest)
GetEventsResponse = _reflection.GeneratedProtocolMessageType('GetEventsResponse', (_message.Message,), {'DESCRIPTOR': _GETEVENTSRESPONSE, '__module__': 'proto.api.component.inputcontroller.v1.input_controller_pb2'})
_sym_db.RegisterMessage(GetEventsResponse)
TriggerEventRequest = _reflection.GeneratedProtocolMessageType('TriggerEventRequest', (_message.Message,), {'DESCRIPTOR': _TRIGGEREVENTREQUEST, '__module__': 'proto.api.component.inputcontroller.v1.input_controller_pb2'})
_sym_db.RegisterMessage(TriggerEventRequest)
TriggerEventResponse = _reflection.GeneratedProtocolMessageType('TriggerEventResponse', (_message.Message,), {'DESCRIPTOR': _TRIGGEREVENTRESPONSE, '__module__': 'proto.api.component.inputcontroller.v1.input_controller_pb2'})
_sym_db.RegisterMessage(TriggerEventResponse)
Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {'DESCRIPTOR': _EVENT, '__module__': 'proto.api.component.inputcontroller.v1.input_controller_pb2'})
_sym_db.RegisterMessage(Event)
StreamEventsRequest = _reflection.GeneratedProtocolMessageType('StreamEventsRequest', (_message.Message,), {'Events': _reflection.GeneratedProtocolMessageType('Events', (_message.Message,), {'DESCRIPTOR': _STREAMEVENTSREQUEST_EVENTS, '__module__': 'proto.api.component.inputcontroller.v1.input_controller_pb2'}), 'DESCRIPTOR': _STREAMEVENTSREQUEST, '__module__': 'proto.api.component.inputcontroller.v1.input_controller_pb2'})
_sym_db.RegisterMessage(StreamEventsRequest)
_sym_db.RegisterMessage(StreamEventsRequest.Events)
StreamEventsResponse = _reflection.GeneratedProtocolMessageType('StreamEventsResponse', (_message.Message,), {'DESCRIPTOR': _STREAMEVENTSRESPONSE, '__module__': 'proto.api.component.inputcontroller.v1.input_controller_pb2'})
_sym_db.RegisterMessage(StreamEventsResponse)
_INPUTCONTROLLERSERVICE = DESCRIPTOR.services_by_name['InputControllerService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n3com.viam.rdk.proto.api.component.inputcontroller.v1Z6go.viam.com/rdk/proto/api/component/inputcontroller/v1'
    _INPUTCONTROLLERSERVICE.methods_by_name['GetControls']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['GetControls']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/api/v1/component/input/{controller}/controls'
    _INPUTCONTROLLERSERVICE.methods_by_name['GetEvents']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['GetEvents']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/api/v1/component/input/{controller}/events'
    _INPUTCONTROLLERSERVICE.methods_by_name['StreamEvents']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['StreamEvents']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/api/v1/component/input/{controller}/event_stream'
    _INPUTCONTROLLERSERVICE.methods_by_name['TriggerEvent']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['TriggerEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02,"*/api/v1/component/input/{controller}/event'
    _GETCONTROLSREQUEST._serialized_start = 168
    _GETCONTROLSREQUEST._serialized_end = 220
    _GETCONTROLSRESPONSE._serialized_start = 222
    _GETCONTROLSRESPONSE._serialized_end = 271
    _GETEVENTSREQUEST._serialized_start = 273
    _GETEVENTSREQUEST._serialized_end = 323
    _GETEVENTSRESPONSE._serialized_start = 325
    _GETEVENTSRESPONSE._serialized_end = 415
    _TRIGGEREVENTREQUEST._serialized_start = 417
    _TRIGGEREVENTREQUEST._serialized_end = 539
    _TRIGGEREVENTRESPONSE._serialized_start = 541
    _TRIGGEREVENTRESPONSE._serialized_end = 563
    _EVENT._serialized_start = 565
    _EVENT._serialized_end = 690
    _STREAMEVENTSREQUEST._serialized_start = 693
    _STREAMEVENTSREQUEST._serialized_end = 941
    _STREAMEVENTSREQUEST_EVENTS._serialized_start = 840
    _STREAMEVENTSREQUEST_EVENTS._serialized_end = 941
    _STREAMEVENTSRESPONSE._serialized_start = 943
    _STREAMEVENTSRESPONSE._serialized_end = 1034
    _INPUTCONTROLLERSERVICE._serialized_start = 1037
    _INPUTCONTROLLERSERVICE._serialized_end = 1830