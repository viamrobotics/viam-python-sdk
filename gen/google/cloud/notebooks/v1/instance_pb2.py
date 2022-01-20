# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/notebooks/v1/instance.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.notebooks.v1 import environment_pb2 as google_dot_cloud_dot_notebooks_dot_v1_dot_environment__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/notebooks/v1/instance.proto\x12\x19google.cloud.notebooks.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/notebooks/v1/environment.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa1\x02\n\x13ReservationAffinity\x12s\n\x18\x63onsume_reservation_type\x18\x01 \x01(\x0e\x32\x33.google.cloud.notebooks.v1.ReservationAffinity.TypeB\x04\xe2\x41\x01\x01R\x16\x63onsumeReservationType\x12\x16\n\x03key\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\x03key\x12\x1c\n\x06values\x18\x03 \x03(\tB\x04\xe2\x41\x01\x01R\x06values\"_\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eNO_RESERVATION\x10\x01\x12\x13\n\x0f\x41NY_RESERVATION\x10\x02\x12\x18\n\x14SPECIFIC_RESERVATION\x10\x03\"\xf6!\n\x08Instance\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12?\n\x08vm_image\x18\x02 \x01(\x0b\x32\".google.cloud.notebooks.v1.VmImageH\x00R\x07vmImage\x12T\n\x0f\x63ontainer_image\x18\x03 \x01(\x0b\x32).google.cloud.notebooks.v1.ContainerImageH\x00R\x0e\x63ontainerImage\x12.\n\x13post_startup_script\x18\x04 \x01(\tR\x11postStartupScript\x12!\n\tproxy_uri\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\x08proxyUri\x12-\n\x0finstance_owners\x18\x06 \x03(\tB\x04\xe2\x41\x01\x04R\x0einstanceOwners\x12\'\n\x0fservice_account\x18\x07 \x01(\tR\x0eserviceAccount\x12:\n\x16service_account_scopes\x18\x1f \x03(\tB\x04\xe2\x41\x01\x01R\x14serviceAccountScopes\x12\'\n\x0cmachine_type\x18\x08 \x01(\tB\x04\xe2\x41\x01\x02R\x0bmachineType\x12\x64\n\x12\x61\x63\x63\x65lerator_config\x18\t \x01(\x0b\x32\x35.google.cloud.notebooks.v1.Instance.AcceleratorConfigR\x11\x61\x63\x63\x65leratorConfig\x12\x45\n\x05state\x18\n \x01(\x0e\x32).google.cloud.notebooks.v1.Instance.StateB\x04\xe2\x41\x01\x03R\x05state\x12,\n\x12install_gpu_driver\x18\x0b \x01(\x08R\x10installGpuDriver\x12\x33\n\x16\x63ustom_gpu_driver_path\x18\x0c \x01(\tR\x13\x63ustomGpuDriverPath\x12X\n\x0e\x62oot_disk_type\x18\r \x01(\x0e\x32,.google.cloud.notebooks.v1.Instance.DiskTypeB\x04\xe2\x41\x01\x04R\x0c\x62ootDiskType\x12/\n\x11\x62oot_disk_size_gb\x18\x0e \x01(\x03\x42\x04\xe2\x41\x01\x04R\x0e\x62ootDiskSizeGb\x12X\n\x0e\x64\x61ta_disk_type\x18\x19 \x01(\x0e\x32,.google.cloud.notebooks.v1.Instance.DiskTypeB\x04\xe2\x41\x01\x04R\x0c\x64\x61taDiskType\x12/\n\x11\x64\x61ta_disk_size_gb\x18\x1a \x01(\x03\x42\x04\xe2\x41\x01\x04R\x0e\x64\x61taDiskSizeGb\x12\x33\n\x13no_remove_data_disk\x18\x1b \x01(\x08\x42\x04\xe2\x41\x01\x04R\x10noRemoveDataDisk\x12\x61\n\x0f\x64isk_encryption\x18\x0f \x01(\x0e\x32\x32.google.cloud.notebooks.v1.Instance.DiskEncryptionB\x04\xe2\x41\x01\x04R\x0e\x64iskEncryption\x12\x1d\n\x07kms_key\x18\x10 \x01(\tB\x04\xe2\x41\x01\x04R\x06kmsKey\x12\x44\n\x05\x64isks\x18\x1c \x03(\x0b\x32(.google.cloud.notebooks.v1.Instance.DiskB\x04\xe2\x41\x01\x03R\x05\x64isks\x12z\n\x18shielded_instance_config\x18\x1e \x01(\x0b\x32:.google.cloud.notebooks.v1.Instance.ShieldedInstanceConfigB\x04\xe2\x41\x01\x01R\x16shieldedInstanceConfig\x12 \n\x0cno_public_ip\x18\x11 \x01(\x08R\nnoPublicIp\x12&\n\x0fno_proxy_access\x18\x12 \x01(\x08R\rnoProxyAccess\x12\x18\n\x07network\x18\x13 \x01(\tR\x07network\x12\x16\n\x06subnet\x18\x14 \x01(\tR\x06subnet\x12G\n\x06labels\x18\x15 \x03(\x0b\x32/.google.cloud.notebooks.v1.Instance.LabelsEntryR\x06labels\x12M\n\x08metadata\x18\x16 \x03(\x0b\x32\x31.google.cloud.notebooks.v1.Instance.MetadataEntryR\x08metadata\x12\x18\n\x04tags\x18  \x03(\tB\x04\xe2\x41\x01\x01R\x04tags\x12`\n\x0fupgrade_history\x18\x1d \x03(\x0b\x32\x37.google.cloud.notebooks.v1.Instance.UpgradeHistoryEntryR\x0eupgradeHistory\x12L\n\x08nic_type\x18! \x01(\x0e\x32+.google.cloud.notebooks.v1.Instance.NicTypeB\x04\xe2\x41\x01\x01R\x07nicType\x12g\n\x14reservation_affinity\x18\" \x01(\x0b\x32..google.cloud.notebooks.v1.ReservationAffinityB\x04\xe2\x41\x01\x01R\x13reservationAffinity\x12\x41\n\x0b\x63reate_time\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x18 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x1a{\n\x11\x41\x63\x63\x65leratorConfig\x12G\n\x04type\x18\x01 \x01(\x0e\x32\x33.google.cloud.notebooks.v1.Instance.AcceleratorTypeR\x04type\x12\x1d\n\ncore_count\x18\x02 \x01(\x03R\tcoreCount\x1a\xad\x03\n\x04\x44isk\x12\x1f\n\x0b\x61uto_delete\x18\x01 \x01(\x08R\nautoDelete\x12\x12\n\x04\x62oot\x18\x02 \x01(\x08R\x04\x62oot\x12\x1f\n\x0b\x64\x65vice_name\x18\x03 \x01(\tR\ndeviceName\x12 \n\x0c\x64isk_size_gb\x18\x04 \x01(\x03R\ndiskSizeGb\x12\x63\n\x11guest_os_features\x18\x05 \x03(\x0b\x32\x37.google.cloud.notebooks.v1.Instance.Disk.GuestOsFeatureR\x0fguestOsFeatures\x12\x14\n\x05index\x18\x06 \x01(\x03R\x05index\x12\x1c\n\tinterface\x18\x07 \x01(\tR\tinterface\x12\x12\n\x04kind\x18\x08 \x01(\tR\x04kind\x12\x1a\n\x08licenses\x18\t \x03(\tR\x08licenses\x12\x12\n\x04mode\x18\n \x01(\tR\x04mode\x12\x16\n\x06source\x18\x0b \x01(\tR\x06source\x12\x12\n\x04type\x18\x0c \x01(\tR\x04type\x1a$\n\x0eGuestOsFeature\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x1a\xa7\x01\n\x16ShieldedInstanceConfig\x12,\n\x12\x65nable_secure_boot\x18\x01 \x01(\x08R\x10\x65nableSecureBoot\x12\x1f\n\x0b\x65nable_vtpm\x18\x02 \x01(\x08R\nenableVtpm\x12>\n\x1b\x65nable_integrity_monitoring\x18\x03 \x01(\x08R\x19\x65nableIntegrityMonitoring\x1a\xea\x04\n\x13UpgradeHistoryEntry\x12\x1a\n\x08snapshot\x18\x01 \x01(\tR\x08snapshot\x12\x19\n\x08vm_image\x18\x02 \x01(\tR\x07vmImage\x12\'\n\x0f\x63ontainer_image\x18\x03 \x01(\tR\x0e\x63ontainerImage\x12\x1c\n\tframework\x18\x04 \x01(\tR\tframework\x12\x18\n\x07version\x18\x05 \x01(\tR\x07version\x12S\n\x05state\x18\x06 \x01(\x0e\x32=.google.cloud.notebooks.v1.Instance.UpgradeHistoryEntry.StateR\x05state\x12;\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12%\n\x0ctarget_image\x18\x08 \x01(\tB\x02\x18\x01R\x0btargetImage\x12V\n\x06\x61\x63tion\x18\t \x01(\x0e\x32>.google.cloud.notebooks.v1.Instance.UpgradeHistoryEntry.ActionR\x06\x61\x63tion\x12%\n\x0etarget_version\x18\n \x01(\tR\rtargetVersion\"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\";\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\x0b\n\x07UPGRADE\x10\x01\x12\x0c\n\x08ROLLBACK\x10\x02\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x9d\x02\n\x0f\x41\x63\x63\x65leratorType\x12 \n\x1c\x41\x43\x43\x45LERATOR_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10NVIDIA_TESLA_K80\x10\x01\x12\x15\n\x11NVIDIA_TESLA_P100\x10\x02\x12\x15\n\x11NVIDIA_TESLA_V100\x10\x03\x12\x13\n\x0fNVIDIA_TESLA_P4\x10\x04\x12\x13\n\x0fNVIDIA_TESLA_T4\x10\x05\x12\x15\n\x11NVIDIA_TESLA_A100\x10\x0b\x12\x17\n\x13NVIDIA_TESLA_T4_VWS\x10\x08\x12\x19\n\x15NVIDIA_TESLA_P100_VWS\x10\t\x12\x17\n\x13NVIDIA_TESLA_P4_VWS\x10\n\x12\n\n\x06TPU_V2\x10\x06\x12\n\n\x06TPU_V3\x10\x07\"\xa4\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STARTING\x10\x01\x12\x10\n\x0cPROVISIONING\x10\x02\x12\n\n\x06\x41\x43TIVE\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\x0b\n\x07\x44\x45LETED\x10\x06\x12\r\n\tUPGRADING\x10\x07\x12\x10\n\x0cINITIALIZING\x10\x08\x12\x0f\n\x0bREGISTERING\x10\t\"S\n\x08\x44iskType\x12\x19\n\x15\x44ISK_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPD_STANDARD\x10\x01\x12\n\n\x06PD_SSD\x10\x02\x12\x0f\n\x0bPD_BALANCED\x10\x03\"E\n\x0e\x44iskEncryption\x12\x1f\n\x1b\x44ISK_ENCRYPTION_UNSPECIFIED\x10\x00\x12\x08\n\x04GMEK\x10\x01\x12\x08\n\x04\x43MEK\x10\x02\">\n\x07NicType\x12\x18\n\x14UNSPECIFIED_NIC_TYPE\x10\x00\x12\x0e\n\nVIRTIO_NET\x10\x01\x12\t\n\x05GVNIC\x10\x02:O\xea\x41L\n!notebooks.googleapis.com/Instance\x12\'projects/{project}/instances/{instance}B\r\n\x0b\x65nvironmentB\xcb\x01\n\x1d\x63om.google.cloud.notebooks.v1B\rInstanceProtoP\x01ZBgoogle.golang.org/genproto/googleapis/cloud/notebooks/v1;notebooks\xaa\x02\x19Google.Cloud.Notebooks.V1\xca\x02\x19Google\\Cloud\\Notebooks\\V1\xea\x02\x1cGoogle::Cloud::Notebooks::V1b\x06proto3')



_RESERVATIONAFFINITY = DESCRIPTOR.message_types_by_name['ReservationAffinity']
_INSTANCE = DESCRIPTOR.message_types_by_name['Instance']
_INSTANCE_ACCELERATORCONFIG = _INSTANCE.nested_types_by_name['AcceleratorConfig']
_INSTANCE_DISK = _INSTANCE.nested_types_by_name['Disk']
_INSTANCE_DISK_GUESTOSFEATURE = _INSTANCE_DISK.nested_types_by_name['GuestOsFeature']
_INSTANCE_SHIELDEDINSTANCECONFIG = _INSTANCE.nested_types_by_name['ShieldedInstanceConfig']
_INSTANCE_UPGRADEHISTORYENTRY = _INSTANCE.nested_types_by_name['UpgradeHistoryEntry']
_INSTANCE_LABELSENTRY = _INSTANCE.nested_types_by_name['LabelsEntry']
_INSTANCE_METADATAENTRY = _INSTANCE.nested_types_by_name['MetadataEntry']
_RESERVATIONAFFINITY_TYPE = _RESERVATIONAFFINITY.enum_types_by_name['Type']
_INSTANCE_UPGRADEHISTORYENTRY_STATE = _INSTANCE_UPGRADEHISTORYENTRY.enum_types_by_name['State']
_INSTANCE_UPGRADEHISTORYENTRY_ACTION = _INSTANCE_UPGRADEHISTORYENTRY.enum_types_by_name['Action']
_INSTANCE_ACCELERATORTYPE = _INSTANCE.enum_types_by_name['AcceleratorType']
_INSTANCE_STATE = _INSTANCE.enum_types_by_name['State']
_INSTANCE_DISKTYPE = _INSTANCE.enum_types_by_name['DiskType']
_INSTANCE_DISKENCRYPTION = _INSTANCE.enum_types_by_name['DiskEncryption']
_INSTANCE_NICTYPE = _INSTANCE.enum_types_by_name['NicType']
ReservationAffinity = _reflection.GeneratedProtocolMessageType('ReservationAffinity', (_message.Message,), {
  'DESCRIPTOR' : _RESERVATIONAFFINITY,
  '__module__' : 'google.cloud.notebooks.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1.ReservationAffinity)
  })
_sym_db.RegisterMessage(ReservationAffinity)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), {

  'AcceleratorConfig' : _reflection.GeneratedProtocolMessageType('AcceleratorConfig', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_ACCELERATORCONFIG,
    '__module__' : 'google.cloud.notebooks.v1.instance_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1.Instance.AcceleratorConfig)
    })
  ,

  'Disk' : _reflection.GeneratedProtocolMessageType('Disk', (_message.Message,), {

    'GuestOsFeature' : _reflection.GeneratedProtocolMessageType('GuestOsFeature', (_message.Message,), {
      'DESCRIPTOR' : _INSTANCE_DISK_GUESTOSFEATURE,
      '__module__' : 'google.cloud.notebooks.v1.instance_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1.Instance.Disk.GuestOsFeature)
      })
    ,
    'DESCRIPTOR' : _INSTANCE_DISK,
    '__module__' : 'google.cloud.notebooks.v1.instance_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1.Instance.Disk)
    })
  ,

  'ShieldedInstanceConfig' : _reflection.GeneratedProtocolMessageType('ShieldedInstanceConfig', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_SHIELDEDINSTANCECONFIG,
    '__module__' : 'google.cloud.notebooks.v1.instance_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1.Instance.ShieldedInstanceConfig)
    })
  ,

  'UpgradeHistoryEntry' : _reflection.GeneratedProtocolMessageType('UpgradeHistoryEntry', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_UPGRADEHISTORYENTRY,
    '__module__' : 'google.cloud.notebooks.v1.instance_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1.Instance.UpgradeHistoryEntry)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_LABELSENTRY,
    '__module__' : 'google.cloud.notebooks.v1.instance_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1.Instance.LabelsEntry)
    })
  ,

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_METADATAENTRY,
    '__module__' : 'google.cloud.notebooks.v1.instance_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1.Instance.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _INSTANCE,
  '__module__' : 'google.cloud.notebooks.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.notebooks.v1.Instance)
  })
_sym_db.RegisterMessage(Instance)
_sym_db.RegisterMessage(Instance.AcceleratorConfig)
_sym_db.RegisterMessage(Instance.Disk)
_sym_db.RegisterMessage(Instance.Disk.GuestOsFeature)
_sym_db.RegisterMessage(Instance.ShieldedInstanceConfig)
_sym_db.RegisterMessage(Instance.UpgradeHistoryEntry)
_sym_db.RegisterMessage(Instance.LabelsEntry)
_sym_db.RegisterMessage(Instance.MetadataEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.google.cloud.notebooks.v1B\rInstanceProtoP\001ZBgoogle.golang.org/genproto/googleapis/cloud/notebooks/v1;notebooks\252\002\031Google.Cloud.Notebooks.V1\312\002\031Google\\Cloud\\Notebooks\\V1\352\002\034Google::Cloud::Notebooks::V1'
  _RESERVATIONAFFINITY.fields_by_name['consume_reservation_type']._options = None
  _RESERVATIONAFFINITY.fields_by_name['consume_reservation_type']._serialized_options = b'\342A\001\001'
  _RESERVATIONAFFINITY.fields_by_name['key']._options = None
  _RESERVATIONAFFINITY.fields_by_name['key']._serialized_options = b'\342A\001\001'
  _RESERVATIONAFFINITY.fields_by_name['values']._options = None
  _RESERVATIONAFFINITY.fields_by_name['values']._serialized_options = b'\342A\001\001'
  _INSTANCE_UPGRADEHISTORYENTRY.fields_by_name['target_image']._options = None
  _INSTANCE_UPGRADEHISTORYENTRY.fields_by_name['target_image']._serialized_options = b'\030\001'
  _INSTANCE_LABELSENTRY._options = None
  _INSTANCE_LABELSENTRY._serialized_options = b'8\001'
  _INSTANCE_METADATAENTRY._options = None
  _INSTANCE_METADATAENTRY._serialized_options = b'8\001'
  _INSTANCE.fields_by_name['name']._options = None
  _INSTANCE.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['proxy_uri']._options = None
  _INSTANCE.fields_by_name['proxy_uri']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['instance_owners']._options = None
  _INSTANCE.fields_by_name['instance_owners']._serialized_options = b'\342A\001\004'
  _INSTANCE.fields_by_name['service_account_scopes']._options = None
  _INSTANCE.fields_by_name['service_account_scopes']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['machine_type']._options = None
  _INSTANCE.fields_by_name['machine_type']._serialized_options = b'\342A\001\002'
  _INSTANCE.fields_by_name['state']._options = None
  _INSTANCE.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['boot_disk_type']._options = None
  _INSTANCE.fields_by_name['boot_disk_type']._serialized_options = b'\342A\001\004'
  _INSTANCE.fields_by_name['boot_disk_size_gb']._options = None
  _INSTANCE.fields_by_name['boot_disk_size_gb']._serialized_options = b'\342A\001\004'
  _INSTANCE.fields_by_name['data_disk_type']._options = None
  _INSTANCE.fields_by_name['data_disk_type']._serialized_options = b'\342A\001\004'
  _INSTANCE.fields_by_name['data_disk_size_gb']._options = None
  _INSTANCE.fields_by_name['data_disk_size_gb']._serialized_options = b'\342A\001\004'
  _INSTANCE.fields_by_name['no_remove_data_disk']._options = None
  _INSTANCE.fields_by_name['no_remove_data_disk']._serialized_options = b'\342A\001\004'
  _INSTANCE.fields_by_name['disk_encryption']._options = None
  _INSTANCE.fields_by_name['disk_encryption']._serialized_options = b'\342A\001\004'
  _INSTANCE.fields_by_name['kms_key']._options = None
  _INSTANCE.fields_by_name['kms_key']._serialized_options = b'\342A\001\004'
  _INSTANCE.fields_by_name['disks']._options = None
  _INSTANCE.fields_by_name['disks']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['shielded_instance_config']._options = None
  _INSTANCE.fields_by_name['shielded_instance_config']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['tags']._options = None
  _INSTANCE.fields_by_name['tags']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['nic_type']._options = None
  _INSTANCE.fields_by_name['nic_type']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['reservation_affinity']._options = None
  _INSTANCE.fields_by_name['reservation_affinity']._serialized_options = b'\342A\001\001'
  _INSTANCE.fields_by_name['create_time']._options = None
  _INSTANCE.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _INSTANCE.fields_by_name['update_time']._options = None
  _INSTANCE.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _INSTANCE._options = None
  _INSTANCE._serialized_options = b'\352AL\n!notebooks.googleapis.com/Instance\022\'projects/{project}/instances/{instance}'
  _RESERVATIONAFFINITY._serialized_start=210
  _RESERVATIONAFFINITY._serialized_end=499
  _RESERVATIONAFFINITY_TYPE._serialized_start=404
  _RESERVATIONAFFINITY_TYPE._serialized_end=499
  _INSTANCE._serialized_start=502
  _INSTANCE._serialized_end=4844
  _INSTANCE_ACCELERATORCONFIG._serialized_start=2607
  _INSTANCE_ACCELERATORCONFIG._serialized_end=2730
  _INSTANCE_DISK._serialized_start=2733
  _INSTANCE_DISK._serialized_end=3162
  _INSTANCE_DISK_GUESTOSFEATURE._serialized_start=3126
  _INSTANCE_DISK_GUESTOSFEATURE._serialized_end=3162
  _INSTANCE_SHIELDEDINSTANCECONFIG._serialized_start=3165
  _INSTANCE_SHIELDEDINSTANCECONFIG._serialized_end=3332
  _INSTANCE_UPGRADEHISTORYENTRY._serialized_start=3335
  _INSTANCE_UPGRADEHISTORYENTRY._serialized_end=3953
  _INSTANCE_UPGRADEHISTORYENTRY_STATE._serialized_start=3822
  _INSTANCE_UPGRADEHISTORYENTRY_STATE._serialized_end=3892
  _INSTANCE_UPGRADEHISTORYENTRY_ACTION._serialized_start=3894
  _INSTANCE_UPGRADEHISTORYENTRY_ACTION._serialized_end=3953
  _INSTANCE_LABELSENTRY._serialized_start=3955
  _INSTANCE_LABELSENTRY._serialized_end=4012
  _INSTANCE_METADATAENTRY._serialized_start=4014
  _INSTANCE_METADATAENTRY._serialized_end=4073
  _INSTANCE_ACCELERATORTYPE._serialized_start=4076
  _INSTANCE_ACCELERATORTYPE._serialized_end=4361
  _INSTANCE_STATE._serialized_start=4364
  _INSTANCE_STATE._serialized_end=4528
  _INSTANCE_DISKTYPE._serialized_start=4530
  _INSTANCE_DISKTYPE._serialized_end=4613
  _INSTANCE_DISKENCRYPTION._serialized_start=4615
  _INSTANCE_DISKENCRYPTION._serialized_end=4684
  _INSTANCE_NICTYPE._serialized_start=4686
  _INSTANCE_NICTYPE._serialized_end=4748
# @@protoc_insertion_point(module_scope)
