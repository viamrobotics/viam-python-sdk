"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-proto/api/component/v1/input_controller.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"J\n(InputControllerServiceGetControlsRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller"G\n)InputControllerServiceGetControlsResponse\x12\x1a\n\x08controls\x18\x01 \x03(\tR\x08controls"H\n&InputControllerServiceGetEventsRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller"v\n\'InputControllerServiceGetEventsResponse\x12K\n\x06events\x18\x01 \x03(\x0b23.proto.api.component.v1.InputControllerServiceEventR\x06events"\x96\x01\n)InputControllerServiceTriggerEventRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller\x12I\n\x05event\x18\x02 \x01(\x0b23.proto.api.component.v1.InputControllerServiceEventR\x05event",\n*InputControllerServiceTriggerEventResponse"\x93\x01\n\x1bInputControllerServiceEvent\x12.\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x04time\x12\x14\n\x05event\x18\x02 \x01(\tR\x05event\x12\x18\n\x07control\x18\x03 \x01(\tR\x07control\x12\x14\n\x05value\x18\x04 \x01(\x01R\x05value"\x94\x02\n)InputControllerServiceStreamEventsRequest\x12\x1e\n\ncontroller\x18\x01 \x01(\tR\ncontroller\x12`\n\x06events\x18\x02 \x03(\x0b2H.proto.api.component.v1.InputControllerServiceStreamEventsRequest.EventsR\x06events\x1ae\n\x06Events\x12\x18\n\x07control\x18\x01 \x01(\tR\x07control\x12\x16\n\x06events\x18\x02 \x03(\tR\x06events\x12)\n\x10cancelled_events\x18\x03 \x03(\tR\x0fcancelledEvents"w\n*InputControllerServiceStreamEventsResponse\x12I\n\x05event\x18\x01 \x01(\x0b23.proto.api.component.v1.InputControllerServiceEventR\x05event2\xc9\x06\n\x16InputControllerService\x12\xc9\x01\n\x0bGetControls\x12@.proto.api.component.v1.InputControllerServiceGetControlsRequest\x1aA.proto.api.component.v1.InputControllerServiceGetControlsResponse"5\x82\xd3\xe4\x93\x02/\x12-/api/v1/component/input/{controller}/controls\x12\xc1\x01\n\tGetEvents\x12>.proto.api.component.v1.InputControllerServiceGetEventsRequest\x1a?.proto.api.component.v1.InputControllerServiceGetEventsResponse"3\x82\xd3\xe4\x93\x02-\x12+/api/v1/component/input/{controller}/events\x12\xd2\x01\n\x0cStreamEvents\x12A.proto.api.component.v1.InputControllerServiceStreamEventsRequest\x1aB.proto.api.component.v1.InputControllerServiceStreamEventsResponse"9\x82\xd3\xe4\x93\x023\x121/api/v1/component/input/{controller}/event_stream0\x01\x12\xc9\x01\n\x0cTriggerEvent\x12A.proto.api.component.v1.InputControllerServiceTriggerEventRequest\x1aB.proto.api.component.v1.InputControllerServiceTriggerEventResponse"2\x82\xd3\xe4\x93\x02,"*/api/v1/component/input/{controller}/eventBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_INPUTCONTROLLERSERVICEGETCONTROLSREQUEST = DESCRIPTOR.message_types_by_name['InputControllerServiceGetControlsRequest']
_INPUTCONTROLLERSERVICEGETCONTROLSRESPONSE = DESCRIPTOR.message_types_by_name['InputControllerServiceGetControlsResponse']
_INPUTCONTROLLERSERVICEGETEVENTSREQUEST = DESCRIPTOR.message_types_by_name['InputControllerServiceGetEventsRequest']
_INPUTCONTROLLERSERVICEGETEVENTSRESPONSE = DESCRIPTOR.message_types_by_name['InputControllerServiceGetEventsResponse']
_INPUTCONTROLLERSERVICETRIGGEREVENTREQUEST = DESCRIPTOR.message_types_by_name['InputControllerServiceTriggerEventRequest']
_INPUTCONTROLLERSERVICETRIGGEREVENTRESPONSE = DESCRIPTOR.message_types_by_name['InputControllerServiceTriggerEventResponse']
_INPUTCONTROLLERSERVICEEVENT = DESCRIPTOR.message_types_by_name['InputControllerServiceEvent']
_INPUTCONTROLLERSERVICESTREAMEVENTSREQUEST = DESCRIPTOR.message_types_by_name['InputControllerServiceStreamEventsRequest']
_INPUTCONTROLLERSERVICESTREAMEVENTSREQUEST_EVENTS = _INPUTCONTROLLERSERVICESTREAMEVENTSREQUEST.nested_types_by_name['Events']
_INPUTCONTROLLERSERVICESTREAMEVENTSRESPONSE = DESCRIPTOR.message_types_by_name['InputControllerServiceStreamEventsResponse']
InputControllerServiceGetControlsRequest = _reflection.GeneratedProtocolMessageType('InputControllerServiceGetControlsRequest', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLERSERVICEGETCONTROLSREQUEST, '__module__': 'proto.api.component.v1.input_controller_pb2'})
_sym_db.RegisterMessage(InputControllerServiceGetControlsRequest)
InputControllerServiceGetControlsResponse = _reflection.GeneratedProtocolMessageType('InputControllerServiceGetControlsResponse', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLERSERVICEGETCONTROLSRESPONSE, '__module__': 'proto.api.component.v1.input_controller_pb2'})
_sym_db.RegisterMessage(InputControllerServiceGetControlsResponse)
InputControllerServiceGetEventsRequest = _reflection.GeneratedProtocolMessageType('InputControllerServiceGetEventsRequest', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLERSERVICEGETEVENTSREQUEST, '__module__': 'proto.api.component.v1.input_controller_pb2'})
_sym_db.RegisterMessage(InputControllerServiceGetEventsRequest)
InputControllerServiceGetEventsResponse = _reflection.GeneratedProtocolMessageType('InputControllerServiceGetEventsResponse', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLERSERVICEGETEVENTSRESPONSE, '__module__': 'proto.api.component.v1.input_controller_pb2'})
_sym_db.RegisterMessage(InputControllerServiceGetEventsResponse)
InputControllerServiceTriggerEventRequest = _reflection.GeneratedProtocolMessageType('InputControllerServiceTriggerEventRequest', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLERSERVICETRIGGEREVENTREQUEST, '__module__': 'proto.api.component.v1.input_controller_pb2'})
_sym_db.RegisterMessage(InputControllerServiceTriggerEventRequest)
InputControllerServiceTriggerEventResponse = _reflection.GeneratedProtocolMessageType('InputControllerServiceTriggerEventResponse', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLERSERVICETRIGGEREVENTRESPONSE, '__module__': 'proto.api.component.v1.input_controller_pb2'})
_sym_db.RegisterMessage(InputControllerServiceTriggerEventResponse)
InputControllerServiceEvent = _reflection.GeneratedProtocolMessageType('InputControllerServiceEvent', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLERSERVICEEVENT, '__module__': 'proto.api.component.v1.input_controller_pb2'})
_sym_db.RegisterMessage(InputControllerServiceEvent)
InputControllerServiceStreamEventsRequest = _reflection.GeneratedProtocolMessageType('InputControllerServiceStreamEventsRequest', (_message.Message,), {'Events': _reflection.GeneratedProtocolMessageType('Events', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLERSERVICESTREAMEVENTSREQUEST_EVENTS, '__module__': 'proto.api.component.v1.input_controller_pb2'}), 'DESCRIPTOR': _INPUTCONTROLLERSERVICESTREAMEVENTSREQUEST, '__module__': 'proto.api.component.v1.input_controller_pb2'})
_sym_db.RegisterMessage(InputControllerServiceStreamEventsRequest)
_sym_db.RegisterMessage(InputControllerServiceStreamEventsRequest.Events)
InputControllerServiceStreamEventsResponse = _reflection.GeneratedProtocolMessageType('InputControllerServiceStreamEventsResponse', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLERSERVICESTREAMEVENTSRESPONSE, '__module__': 'proto.api.component.v1.input_controller_pb2'})
_sym_db.RegisterMessage(InputControllerServiceStreamEventsResponse)
_INPUTCONTROLLERSERVICE = DESCRIPTOR.services_by_name['InputControllerService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _INPUTCONTROLLERSERVICE.methods_by_name['GetControls']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['GetControls']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/api/v1/component/input/{controller}/controls'
    _INPUTCONTROLLERSERVICE.methods_by_name['GetEvents']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['GetEvents']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/api/v1/component/input/{controller}/events'
    _INPUTCONTROLLERSERVICE.methods_by_name['StreamEvents']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['StreamEvents']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/api/v1/component/input/{controller}/event_stream'
    _INPUTCONTROLLERSERVICE.methods_by_name['TriggerEvent']._options = None
    _INPUTCONTROLLERSERVICE.methods_by_name['TriggerEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02,"*/api/v1/component/input/{controller}/event'
    _INPUTCONTROLLERSERVICEGETCONTROLSREQUEST._serialized_start = 136
    _INPUTCONTROLLERSERVICEGETCONTROLSREQUEST._serialized_end = 210
    _INPUTCONTROLLERSERVICEGETCONTROLSRESPONSE._serialized_start = 212
    _INPUTCONTROLLERSERVICEGETCONTROLSRESPONSE._serialized_end = 283
    _INPUTCONTROLLERSERVICEGETEVENTSREQUEST._serialized_start = 285
    _INPUTCONTROLLERSERVICEGETEVENTSREQUEST._serialized_end = 357
    _INPUTCONTROLLERSERVICEGETEVENTSRESPONSE._serialized_start = 359
    _INPUTCONTROLLERSERVICEGETEVENTSRESPONSE._serialized_end = 477
    _INPUTCONTROLLERSERVICETRIGGEREVENTREQUEST._serialized_start = 480
    _INPUTCONTROLLERSERVICETRIGGEREVENTREQUEST._serialized_end = 630
    _INPUTCONTROLLERSERVICETRIGGEREVENTRESPONSE._serialized_start = 632
    _INPUTCONTROLLERSERVICETRIGGEREVENTRESPONSE._serialized_end = 676
    _INPUTCONTROLLERSERVICEEVENT._serialized_start = 679
    _INPUTCONTROLLERSERVICEEVENT._serialized_end = 826
    _INPUTCONTROLLERSERVICESTREAMEVENTSREQUEST._serialized_start = 829
    _INPUTCONTROLLERSERVICESTREAMEVENTSREQUEST._serialized_end = 1105
    _INPUTCONTROLLERSERVICESTREAMEVENTSREQUEST_EVENTS._serialized_start = 1004
    _INPUTCONTROLLERSERVICESTREAMEVENTSREQUEST_EVENTS._serialized_end = 1105
    _INPUTCONTROLLERSERVICESTREAMEVENTSRESPONSE._serialized_start = 1107
    _INPUTCONTROLLERSERVICESTREAMEVENTSRESPONSE._serialized_end = 1226
    _INPUTCONTROLLERSERVICE._serialized_start = 1229
    _INPUTCONTROLLERSERVICE._serialized_end = 2070