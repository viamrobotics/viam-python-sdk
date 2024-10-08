"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"provisioning/v1/provisioning.proto\x12\x14viam.provisioning.v1"\x1e\n\x1cGetSmartMachineStatusRequest"\xcb\x02\n\x1dGetSmartMachineStatusResponse\x12S\n\x11provisioning_info\x18\x01 \x01(\x0b2&.viam.provisioning.v1.ProvisioningInfoR\x10provisioningInfo\x12A\n\x1dhas_smart_machine_credentials\x18\x02 \x01(\x08R\x1ahasSmartMachineCredentials\x12\x1b\n\tis_online\x18\x03 \x01(\x08R\x08isOnline\x12]\n\x19latest_connection_attempt\x18\x04 \x01(\x0b2!.viam.provisioning.v1.NetworkInfoR\x17latestConnectionAttempt\x12\x16\n\x06errors\x18\x05 \x03(\tR\x06errors"X\n\x1cSetNetworkCredentialsRequest\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x12\n\x04ssid\x18\x02 \x01(\tR\x04ssid\x12\x10\n\x03psk\x18\x03 \x01(\tR\x03psk"\x1f\n\x1dSetNetworkCredentialsResponse"\\\n!SetSmartMachineCredentialsRequest\x127\n\x05cloud\x18\x01 \x01(\x0b2!.viam.provisioning.v1.CloudConfigR\x05cloud"$\n"SetSmartMachineCredentialsResponse"\x17\n\x15GetNetworkListRequest"W\n\x16GetNetworkListResponse\x12=\n\x08networks\x18\x01 \x03(\x0b2!.viam.provisioning.v1.NetworkInfoR\x08networks"m\n\x10ProvisioningInfo\x12\x1f\n\x0bfragment_id\x18\x01 \x01(\tR\nfragmentId\x12\x14\n\x05model\x18\x02 \x01(\tR\x05model\x12"\n\x0cmanufacturer\x18\x03 \x01(\tR\x0cmanufacturer"\xa6\x01\n\x0bNetworkInfo\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x12\n\x04ssid\x18\x02 \x01(\tR\x04ssid\x12\x1a\n\x08security\x18\x03 \x01(\tR\x08security\x12\x16\n\x06signal\x18\x04 \x01(\x05R\x06signal\x12\x1c\n\tconnected\x18\x05 \x01(\x08R\tconnected\x12\x1d\n\nlast_error\x18\x06 \x01(\tR\tlastError"V\n\x0bCloudConfig\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06secret\x18\x02 \x01(\tR\x06secret\x12\x1f\n\x0bapp_address\x18\x03 \x01(\tR\nappAddress2\x9a\x04\n\x13ProvisioningService\x12\x80\x01\n\x15GetSmartMachineStatus\x122.viam.provisioning.v1.GetSmartMachineStatusRequest\x1a3.viam.provisioning.v1.GetSmartMachineStatusResponse\x12\x80\x01\n\x15SetNetworkCredentials\x122.viam.provisioning.v1.SetNetworkCredentialsRequest\x1a3.viam.provisioning.v1.SetNetworkCredentialsResponse\x12\x8f\x01\n\x1aSetSmartMachineCredentials\x127.viam.provisioning.v1.SetSmartMachineCredentialsRequest\x1a8.viam.provisioning.v1.SetSmartMachineCredentialsResponse\x12k\n\x0eGetNetworkList\x12+.viam.provisioning.v1.GetNetworkListRequest\x1a,.viam.provisioning.v1.GetNetworkListResponseB!Z\x1fgo.viam.com/api/provisioning/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'provisioning.v1.provisioning_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1fgo.viam.com/api/provisioning/v1'
    _GETSMARTMACHINESTATUSREQUEST._serialized_start = 60
    _GETSMARTMACHINESTATUSREQUEST._serialized_end = 90
    _GETSMARTMACHINESTATUSRESPONSE._serialized_start = 93
    _GETSMARTMACHINESTATUSRESPONSE._serialized_end = 424
    _SETNETWORKCREDENTIALSREQUEST._serialized_start = 426
    _SETNETWORKCREDENTIALSREQUEST._serialized_end = 514
    _SETNETWORKCREDENTIALSRESPONSE._serialized_start = 516
    _SETNETWORKCREDENTIALSRESPONSE._serialized_end = 547
    _SETSMARTMACHINECREDENTIALSREQUEST._serialized_start = 549
    _SETSMARTMACHINECREDENTIALSREQUEST._serialized_end = 641
    _SETSMARTMACHINECREDENTIALSRESPONSE._serialized_start = 643
    _SETSMARTMACHINECREDENTIALSRESPONSE._serialized_end = 679
    _GETNETWORKLISTREQUEST._serialized_start = 681
    _GETNETWORKLISTREQUEST._serialized_end = 704
    _GETNETWORKLISTRESPONSE._serialized_start = 706
    _GETNETWORKLISTRESPONSE._serialized_end = 793
    _PROVISIONINGINFO._serialized_start = 795
    _PROVISIONINGINFO._serialized_end = 904
    _NETWORKINFO._serialized_start = 907
    _NETWORKINFO._serialized_end = 1073
    _CLOUDCONFIG._serialized_start = 1075
    _CLOUDCONFIG._serialized_end = 1161
    _PROVISIONINGSERVICE._serialized_start = 1164
    _PROVISIONINGSERVICE._serialized_end = 1702