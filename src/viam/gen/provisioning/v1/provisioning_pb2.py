"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'provisioning/v1/provisioning.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"provisioning/v1/provisioning.proto\x12\x14viam.provisioning.v1"\x19\n\x17ExitProvisioningRequest"\x1a\n\x18ExitProvisioningResponse"\x1e\n\x1cGetSmartMachineStatusRequest"\xf0\x02\n\x1dGetSmartMachineStatusResponse\x12S\n\x11provisioning_info\x18\x01 \x01(\x0b2&.viam.provisioning.v1.ProvisioningInfoR\x10provisioningInfo\x12A\n\x1dhas_smart_machine_credentials\x18\x02 \x01(\x08R\x1ahasSmartMachineCredentials\x12\x1b\n\tis_online\x18\x03 \x01(\x08R\x08isOnline\x12]\n\x19latest_connection_attempt\x18\x04 \x01(\x0b2!.viam.provisioning.v1.NetworkInfoR\x17latestConnectionAttempt\x12\x16\n\x06errors\x18\x05 \x03(\tR\x06errors\x12#\n\ragent_version\x18\x06 \x01(\tR\x0cagentVersion"X\n\x1cSetNetworkCredentialsRequest\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x12\n\x04ssid\x18\x02 \x01(\tR\x04ssid\x12\x10\n\x03psk\x18\x03 \x01(\tR\x03psk"\x1f\n\x1dSetNetworkCredentialsResponse"\\\n!SetSmartMachineCredentialsRequest\x127\n\x05cloud\x18\x01 \x01(\x0b2!.viam.provisioning.v1.CloudConfigR\x05cloud"$\n"SetSmartMachineCredentialsResponse"\x17\n\x15GetNetworkListRequest"W\n\x16GetNetworkListResponse\x12=\n\x08networks\x18\x01 \x03(\x0b2!.viam.provisioning.v1.NetworkInfoR\x08networks"m\n\x10ProvisioningInfo\x12\x1f\n\x0bfragment_id\x18\x01 \x01(\tR\nfragmentId\x12\x14\n\x05model\x18\x02 \x01(\tR\x05model\x12"\n\x0cmanufacturer\x18\x03 \x01(\tR\x0cmanufacturer"\xa6\x01\n\x0bNetworkInfo\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x12\n\x04ssid\x18\x02 \x01(\tR\x04ssid\x12\x1a\n\x08security\x18\x03 \x01(\tR\x08security\x12\x16\n\x06signal\x18\x04 \x01(\x05R\x06signal\x12\x1c\n\tconnected\x18\x05 \x01(\x08R\tconnected\x12\x1d\n\nlast_error\x18\x06 \x01(\tR\tlastError"V\n\x0bCloudConfig\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06secret\x18\x02 \x01(\tR\x06secret\x12\x1f\n\x0bapp_address\x18\x03 \x01(\tR\nappAddress2\x8d\x05\n\x13ProvisioningService\x12\x80\x01\n\x15GetSmartMachineStatus\x122.viam.provisioning.v1.GetSmartMachineStatusRequest\x1a3.viam.provisioning.v1.GetSmartMachineStatusResponse\x12\x80\x01\n\x15SetNetworkCredentials\x122.viam.provisioning.v1.SetNetworkCredentialsRequest\x1a3.viam.provisioning.v1.SetNetworkCredentialsResponse\x12\x8f\x01\n\x1aSetSmartMachineCredentials\x127.viam.provisioning.v1.SetSmartMachineCredentialsRequest\x1a8.viam.provisioning.v1.SetSmartMachineCredentialsResponse\x12k\n\x0eGetNetworkList\x12+.viam.provisioning.v1.GetNetworkListRequest\x1a,.viam.provisioning.v1.GetNetworkListResponse\x12q\n\x10ExitProvisioning\x12-.viam.provisioning.v1.ExitProvisioningRequest\x1a..viam.provisioning.v1.ExitProvisioningResponseB!Z\x1fgo.viam.com/api/provisioning/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'provisioning.v1.provisioning_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1fgo.viam.com/api/provisioning/v1'
    _globals['_EXITPROVISIONINGREQUEST']._serialized_start = 60
    _globals['_EXITPROVISIONINGREQUEST']._serialized_end = 85
    _globals['_EXITPROVISIONINGRESPONSE']._serialized_start = 87
    _globals['_EXITPROVISIONINGRESPONSE']._serialized_end = 113
    _globals['_GETSMARTMACHINESTATUSREQUEST']._serialized_start = 115
    _globals['_GETSMARTMACHINESTATUSREQUEST']._serialized_end = 145
    _globals['_GETSMARTMACHINESTATUSRESPONSE']._serialized_start = 148
    _globals['_GETSMARTMACHINESTATUSRESPONSE']._serialized_end = 516
    _globals['_SETNETWORKCREDENTIALSREQUEST']._serialized_start = 518
    _globals['_SETNETWORKCREDENTIALSREQUEST']._serialized_end = 606
    _globals['_SETNETWORKCREDENTIALSRESPONSE']._serialized_start = 608
    _globals['_SETNETWORKCREDENTIALSRESPONSE']._serialized_end = 639
    _globals['_SETSMARTMACHINECREDENTIALSREQUEST']._serialized_start = 641
    _globals['_SETSMARTMACHINECREDENTIALSREQUEST']._serialized_end = 733
    _globals['_SETSMARTMACHINECREDENTIALSRESPONSE']._serialized_start = 735
    _globals['_SETSMARTMACHINECREDENTIALSRESPONSE']._serialized_end = 771
    _globals['_GETNETWORKLISTREQUEST']._serialized_start = 773
    _globals['_GETNETWORKLISTREQUEST']._serialized_end = 796
    _globals['_GETNETWORKLISTRESPONSE']._serialized_start = 798
    _globals['_GETNETWORKLISTRESPONSE']._serialized_end = 885
    _globals['_PROVISIONINGINFO']._serialized_start = 887
    _globals['_PROVISIONINGINFO']._serialized_end = 996
    _globals['_NETWORKINFO']._serialized_start = 999
    _globals['_NETWORKINFO']._serialized_end = 1165
    _globals['_CLOUDCONFIG']._serialized_start = 1167
    _globals['_CLOUDCONFIG']._serialized_end = 1253
    _globals['_PROVISIONINGSERVICE']._serialized_start = 1256
    _globals['_PROVISIONINGSERVICE']._serialized_end = 1909