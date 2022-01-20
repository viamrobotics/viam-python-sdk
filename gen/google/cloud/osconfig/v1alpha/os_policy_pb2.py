# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/osconfig/v1alpha/os_policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/osconfig/v1alpha/os_policy.proto\x12\x1dgoogle.cloud.osconfig.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\"\x82\'\n\x08OSPolicy\x12\x14\n\x02id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x02id\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x46\n\x04mode\x18\x03 \x01(\x0e\x32,.google.cloud.osconfig.v1alpha.OSPolicy.ModeB\x04\xe2\x41\x01\x02R\x04mode\x12\x64\n\x0fresource_groups\x18\x04 \x03(\x0b\x32\x35.google.cloud.osconfig.v1alpha.OSPolicy.ResourceGroupB\x04\xe2\x41\x01\x02R\x0eresourceGroups\x12@\n\x1d\x61llow_no_resource_group_match\x18\x05 \x01(\x08R\x19\x61llowNoResourceGroupMatch\x1aM\n\x08OSFilter\x12\"\n\ros_short_name\x18\x01 \x01(\tR\x0bosShortName\x12\x1d\n\nos_version\x18\x02 \x01(\tR\tosVersion\x1a\x88\"\n\x08Resource\x12\x14\n\x02id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x02id\x12T\n\x03pkg\x18\x02 \x01(\x0b\x32@.google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResourceH\x00R\x03pkg\x12\x65\n\nrepository\x18\x03 \x01(\x0b\x32\x43.google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResourceH\x00R\nrepository\x12S\n\x04\x65xec\x18\x04 \x01(\x0b\x32=.google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResourceH\x00R\x04\x65xec\x12S\n\x04\x66ile\x18\x05 \x01(\x0b\x32=.google.cloud.osconfig.v1alpha.OSPolicy.Resource.FileResourceH\x00R\x04\x66ile\x1a\xab\x03\n\x04\x46ile\x12V\n\x06remote\x18\x01 \x01(\x0b\x32<.google.cloud.osconfig.v1alpha.OSPolicy.Resource.File.RemoteH\x00R\x06remote\x12M\n\x03gcs\x18\x02 \x01(\x0b\x32\x39.google.cloud.osconfig.v1alpha.OSPolicy.Resource.File.GcsH\x00R\x03gcs\x12\x1f\n\nlocal_path\x18\x03 \x01(\tH\x00R\tlocalPath\x12%\n\x0e\x61llow_insecure\x18\x04 \x01(\x08R\rallowInsecure\x1aI\n\x06Remote\x12\x16\n\x03uri\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x03uri\x12\'\n\x0fsha256_checksum\x18\x02 \x01(\tR\x0esha256Checksum\x1a\x61\n\x03Gcs\x12\x1c\n\x06\x62ucket\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06\x62ucket\x12\x1c\n\x06object\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x06object\x12\x1e\n\ngeneration\x18\x03 \x01(\x03R\ngenerationB\x06\n\x04type\x1a\xe8\n\n\x0fPackageResource\x12x\n\rdesired_state\x18\x01 \x01(\x0e\x32M.google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.DesiredStateB\x04\xe2\x41\x01\x02R\x0c\x64\x65siredState\x12X\n\x03\x61pt\x18\x02 \x01(\x0b\x32\x44.google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.APTH\x00R\x03\x61pt\x12X\n\x03\x64\x65\x62\x18\x03 \x01(\x0b\x32\x44.google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.DebH\x00R\x03\x64\x65\x62\x12X\n\x03yum\x18\x04 \x01(\x0b\x32\x44.google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.YUMH\x00R\x03yum\x12\x61\n\x06zypper\x18\x05 \x01(\x0b\x32G.google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.ZypperH\x00R\x06zypper\x12X\n\x03rpm\x18\x06 \x01(\x0b\x32\x44.google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.RPMH\x00R\x03rpm\x12\x61\n\x06googet\x18\x07 \x01(\x0b\x32G.google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.GooGetH\x00R\x06googet\x12X\n\x03msi\x18\x08 \x01(\x0b\x32\x44.google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.MSIH\x00R\x03msi\x1aw\n\x03\x44\x65\x62\x12S\n\x06source\x18\x01 \x01(\x0b\x32\x35.google.cloud.osconfig.v1alpha.OSPolicy.Resource.FileB\x04\xe2\x41\x01\x02R\x06source\x12\x1b\n\tpull_deps\x18\x02 \x01(\x08R\x08pullDeps\x1a\x1f\n\x03\x41PT\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x1aw\n\x03RPM\x12S\n\x06source\x18\x01 \x01(\x0b\x32\x35.google.cloud.osconfig.v1alpha.OSPolicy.Resource.FileB\x04\xe2\x41\x01\x02R\x06source\x12\x1b\n\tpull_deps\x18\x02 \x01(\x08R\x08pullDeps\x1a\x1f\n\x03YUM\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x1a\"\n\x06Zypper\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x1a\"\n\x06GooGet\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x1az\n\x03MSI\x12S\n\x06source\x18\x01 \x01(\x0b\x32\x35.google.cloud.osconfig.v1alpha.OSPolicy.Resource.FileB\x04\xe2\x41\x01\x02R\x06source\x12\x1e\n\nproperties\x18\x02 \x03(\tR\nproperties\"I\n\x0c\x44\x65siredState\x12\x1d\n\x19\x44\x45SIRED_STATE_UNSPECIFIED\x10\x00\x12\r\n\tINSTALLED\x10\x01\x12\x0b\n\x07REMOVED\x10\x02\x42\x10\n\x0esystem_package\x1a\xfa\x08\n\x12RepositoryResource\x12\x65\n\x03\x61pt\x18\x01 \x01(\x0b\x32Q.google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.AptRepositoryH\x00R\x03\x61pt\x12\x65\n\x03yum\x18\x02 \x01(\x0b\x32Q.google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.YumRepositoryH\x00R\x03yum\x12n\n\x06zypper\x18\x03 \x01(\x0b\x32T.google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.ZypperRepositoryH\x00R\x06zypper\x12\x65\n\x03goo\x18\x04 \x01(\x0b\x32Q.google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.GooRepositoryH\x00R\x03goo\x1a\xdc\x02\n\rAptRepository\x12\x86\x01\n\x0c\x61rchive_type\x18\x01 \x01(\x0e\x32].google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveTypeB\x04\xe2\x41\x01\x02R\x0b\x61rchiveType\x12\x16\n\x03uri\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x03uri\x12(\n\x0c\x64istribution\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x0c\x64istribution\x12$\n\ncomponents\x18\x04 \x03(\tB\x04\xe2\x41\x01\x02R\ncomponents\x12\x17\n\x07gpg_key\x18\x05 \x01(\tR\x06gpgKey\"A\n\x0b\x41rchiveType\x12\x1c\n\x18\x41RCHIVE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03\x44\x45\x42\x10\x01\x12\x0b\n\x07\x44\x45\x42_SRC\x10\x02\x1a\x84\x01\n\rYumRepository\x12\x14\n\x02id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x02id\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12\x1f\n\x08\x62\x61se_url\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x07\x62\x61seUrl\x12\x19\n\x08gpg_keys\x18\x04 \x03(\tR\x07gpgKeys\x1a\x87\x01\n\x10ZypperRepository\x12\x14\n\x02id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x02id\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12\x1f\n\x08\x62\x61se_url\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x07\x62\x61seUrl\x12\x19\n\x08gpg_keys\x18\x04 \x03(\tR\x07gpgKeys\x1a\x41\n\rGooRepository\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12\x16\n\x03url\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x03urlB\x0c\n\nrepository\x1a\xd3\x04\n\x0c\x45xecResource\x12\x64\n\x08validate\x18\x01 \x01(\x0b\x32\x42.google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource.ExecB\x04\xe2\x41\x01\x02R\x08validate\x12\\\n\x07\x65nforce\x18\x02 \x01(\x0b\x32\x42.google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource.ExecR\x07\x65nforce\x1a\xfe\x02\n\x04\x45xec\x12K\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x35.google.cloud.osconfig.v1alpha.OSPolicy.Resource.FileH\x00R\x04\x66ile\x12\x18\n\x06script\x18\x02 \x01(\tH\x00R\x06script\x12\x12\n\x04\x61rgs\x18\x03 \x03(\tR\x04\x61rgs\x12v\n\x0binterpreter\x18\x04 \x01(\x0e\x32N.google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource.Exec.InterpreterB\x04\xe2\x41\x01\x02R\x0binterpreter\x12(\n\x10output_file_path\x18\x05 \x01(\tR\x0eoutputFilePath\"O\n\x0bInterpreter\x12\x1b\n\x17INTERPRETER_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\t\n\x05SHELL\x10\x02\x12\x0e\n\nPOWERSHELL\x10\x03\x42\x08\n\x06source\x1a\x81\x03\n\x0c\x46ileResource\x12K\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x35.google.cloud.osconfig.v1alpha.OSPolicy.Resource.FileH\x00R\x04\x66ile\x12\x1a\n\x07\x63ontent\x18\x02 \x01(\tH\x00R\x07\x63ontent\x12\x18\n\x04path\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x04path\x12\x66\n\x05state\x18\x04 \x01(\x0e\x32J.google.cloud.osconfig.v1alpha.OSPolicy.Resource.FileResource.DesiredStateB\x04\xe2\x41\x01\x02R\x05state\x12 \n\x0bpermissions\x18\x05 \x01(\tR\x0bpermissions\"Z\n\x0c\x44\x65siredState\x12\x1d\n\x19\x44\x45SIRED_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PRESENT\x10\x01\x12\n\n\x06\x41\x42SENT\x10\x02\x12\x12\n\x0e\x43ONTENTS_MATCH\x10\x03\x42\x08\n\x06sourceB\x0f\n\rresource_type\x1a\xb4\x01\n\rResourceGroup\x12M\n\tos_filter\x18\x01 \x01(\x0b\x32\x30.google.cloud.osconfig.v1alpha.OSPolicy.OSFilterR\x08osFilter\x12T\n\tresources\x18\x02 \x03(\x0b\x32\x30.google.cloud.osconfig.v1alpha.OSPolicy.ResourceB\x04\xe2\x41\x01\x02R\tresources\"=\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0e\n\nVALIDATION\x10\x01\x12\x0f\n\x0b\x45NFORCEMENT\x10\x02\x42\xde\x01\n!com.google.cloud.osconfig.v1alphaB\rOSPolicyProtoP\x01ZEgoogle.golang.org/genproto/googleapis/cloud/osconfig/v1alpha;osconfig\xaa\x02\x1dGoogle.Cloud.OsConfig.V1Alpha\xca\x02\x1dGoogle\\Cloud\\OsConfig\\V1alpha\xea\x02 Google::Cloud::OsConfig::V1alphab\x06proto3')



_OSPOLICY = DESCRIPTOR.message_types_by_name['OSPolicy']
_OSPOLICY_OSFILTER = _OSPOLICY.nested_types_by_name['OSFilter']
_OSPOLICY_RESOURCE = _OSPOLICY.nested_types_by_name['Resource']
_OSPOLICY_RESOURCE_FILE = _OSPOLICY_RESOURCE.nested_types_by_name['File']
_OSPOLICY_RESOURCE_FILE_REMOTE = _OSPOLICY_RESOURCE_FILE.nested_types_by_name['Remote']
_OSPOLICY_RESOURCE_FILE_GCS = _OSPOLICY_RESOURCE_FILE.nested_types_by_name['Gcs']
_OSPOLICY_RESOURCE_PACKAGERESOURCE = _OSPOLICY_RESOURCE.nested_types_by_name['PackageResource']
_OSPOLICY_RESOURCE_PACKAGERESOURCE_DEB = _OSPOLICY_RESOURCE_PACKAGERESOURCE.nested_types_by_name['Deb']
_OSPOLICY_RESOURCE_PACKAGERESOURCE_APT = _OSPOLICY_RESOURCE_PACKAGERESOURCE.nested_types_by_name['APT']
_OSPOLICY_RESOURCE_PACKAGERESOURCE_RPM = _OSPOLICY_RESOURCE_PACKAGERESOURCE.nested_types_by_name['RPM']
_OSPOLICY_RESOURCE_PACKAGERESOURCE_YUM = _OSPOLICY_RESOURCE_PACKAGERESOURCE.nested_types_by_name['YUM']
_OSPOLICY_RESOURCE_PACKAGERESOURCE_ZYPPER = _OSPOLICY_RESOURCE_PACKAGERESOURCE.nested_types_by_name['Zypper']
_OSPOLICY_RESOURCE_PACKAGERESOURCE_GOOGET = _OSPOLICY_RESOURCE_PACKAGERESOURCE.nested_types_by_name['GooGet']
_OSPOLICY_RESOURCE_PACKAGERESOURCE_MSI = _OSPOLICY_RESOURCE_PACKAGERESOURCE.nested_types_by_name['MSI']
_OSPOLICY_RESOURCE_REPOSITORYRESOURCE = _OSPOLICY_RESOURCE.nested_types_by_name['RepositoryResource']
_OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY = _OSPOLICY_RESOURCE_REPOSITORYRESOURCE.nested_types_by_name['AptRepository']
_OSPOLICY_RESOURCE_REPOSITORYRESOURCE_YUMREPOSITORY = _OSPOLICY_RESOURCE_REPOSITORYRESOURCE.nested_types_by_name['YumRepository']
_OSPOLICY_RESOURCE_REPOSITORYRESOURCE_ZYPPERREPOSITORY = _OSPOLICY_RESOURCE_REPOSITORYRESOURCE.nested_types_by_name['ZypperRepository']
_OSPOLICY_RESOURCE_REPOSITORYRESOURCE_GOOREPOSITORY = _OSPOLICY_RESOURCE_REPOSITORYRESOURCE.nested_types_by_name['GooRepository']
_OSPOLICY_RESOURCE_EXECRESOURCE = _OSPOLICY_RESOURCE.nested_types_by_name['ExecResource']
_OSPOLICY_RESOURCE_EXECRESOURCE_EXEC = _OSPOLICY_RESOURCE_EXECRESOURCE.nested_types_by_name['Exec']
_OSPOLICY_RESOURCE_FILERESOURCE = _OSPOLICY_RESOURCE.nested_types_by_name['FileResource']
_OSPOLICY_RESOURCEGROUP = _OSPOLICY.nested_types_by_name['ResourceGroup']
_OSPOLICY_RESOURCE_PACKAGERESOURCE_DESIREDSTATE = _OSPOLICY_RESOURCE_PACKAGERESOURCE.enum_types_by_name['DesiredState']
_OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY_ARCHIVETYPE = _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY.enum_types_by_name['ArchiveType']
_OSPOLICY_RESOURCE_EXECRESOURCE_EXEC_INTERPRETER = _OSPOLICY_RESOURCE_EXECRESOURCE_EXEC.enum_types_by_name['Interpreter']
_OSPOLICY_RESOURCE_FILERESOURCE_DESIREDSTATE = _OSPOLICY_RESOURCE_FILERESOURCE.enum_types_by_name['DesiredState']
_OSPOLICY_MODE = _OSPOLICY.enum_types_by_name['Mode']
OSPolicy = _reflection.GeneratedProtocolMessageType('OSPolicy', (_message.Message,), {

  'OSFilter' : _reflection.GeneratedProtocolMessageType('OSFilter', (_message.Message,), {
    'DESCRIPTOR' : _OSPOLICY_OSFILTER,
    '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.OSFilter)
    })
  ,

  'Resource' : _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), {

    'File' : _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {

      'Remote' : _reflection.GeneratedProtocolMessageType('Remote', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_FILE_REMOTE,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.File.Remote)
        })
      ,

      'Gcs' : _reflection.GeneratedProtocolMessageType('Gcs', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_FILE_GCS,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.File.Gcs)
        })
      ,
      'DESCRIPTOR' : _OSPOLICY_RESOURCE_FILE,
      '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.File)
      })
    ,

    'PackageResource' : _reflection.GeneratedProtocolMessageType('PackageResource', (_message.Message,), {

      'Deb' : _reflection.GeneratedProtocolMessageType('Deb', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_PACKAGERESOURCE_DEB,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.Deb)
        })
      ,

      'APT' : _reflection.GeneratedProtocolMessageType('APT', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_PACKAGERESOURCE_APT,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.APT)
        })
      ,

      'RPM' : _reflection.GeneratedProtocolMessageType('RPM', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_PACKAGERESOURCE_RPM,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.RPM)
        })
      ,

      'YUM' : _reflection.GeneratedProtocolMessageType('YUM', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_PACKAGERESOURCE_YUM,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.YUM)
        })
      ,

      'Zypper' : _reflection.GeneratedProtocolMessageType('Zypper', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_PACKAGERESOURCE_ZYPPER,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.Zypper)
        })
      ,

      'GooGet' : _reflection.GeneratedProtocolMessageType('GooGet', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_PACKAGERESOURCE_GOOGET,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.GooGet)
        })
      ,

      'MSI' : _reflection.GeneratedProtocolMessageType('MSI', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_PACKAGERESOURCE_MSI,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource.MSI)
        })
      ,
      'DESCRIPTOR' : _OSPOLICY_RESOURCE_PACKAGERESOURCE,
      '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.PackageResource)
      })
    ,

    'RepositoryResource' : _reflection.GeneratedProtocolMessageType('RepositoryResource', (_message.Message,), {

      'AptRepository' : _reflection.GeneratedProtocolMessageType('AptRepository', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.AptRepository)
        })
      ,

      'YumRepository' : _reflection.GeneratedProtocolMessageType('YumRepository', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_YUMREPOSITORY,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.YumRepository)
        })
      ,

      'ZypperRepository' : _reflection.GeneratedProtocolMessageType('ZypperRepository', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_ZYPPERREPOSITORY,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.ZypperRepository)
        })
      ,

      'GooRepository' : _reflection.GeneratedProtocolMessageType('GooRepository', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_GOOREPOSITORY,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.GooRepository)
        })
      ,
      'DESCRIPTOR' : _OSPOLICY_RESOURCE_REPOSITORYRESOURCE,
      '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource)
      })
    ,

    'ExecResource' : _reflection.GeneratedProtocolMessageType('ExecResource', (_message.Message,), {

      'Exec' : _reflection.GeneratedProtocolMessageType('Exec', (_message.Message,), {
        'DESCRIPTOR' : _OSPOLICY_RESOURCE_EXECRESOURCE_EXEC,
        '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource.Exec)
        })
      ,
      'DESCRIPTOR' : _OSPOLICY_RESOURCE_EXECRESOURCE,
      '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource)
      })
    ,

    'FileResource' : _reflection.GeneratedProtocolMessageType('FileResource', (_message.Message,), {
      'DESCRIPTOR' : _OSPOLICY_RESOURCE_FILERESOURCE,
      '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource.FileResource)
      })
    ,
    'DESCRIPTOR' : _OSPOLICY_RESOURCE,
    '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.Resource)
    })
  ,

  'ResourceGroup' : _reflection.GeneratedProtocolMessageType('ResourceGroup', (_message.Message,), {
    'DESCRIPTOR' : _OSPOLICY_RESOURCEGROUP,
    '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy.ResourceGroup)
    })
  ,
  'DESCRIPTOR' : _OSPOLICY,
  '__module__' : 'google.cloud.osconfig.v1alpha.os_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.osconfig.v1alpha.OSPolicy)
  })
_sym_db.RegisterMessage(OSPolicy)
_sym_db.RegisterMessage(OSPolicy.OSFilter)
_sym_db.RegisterMessage(OSPolicy.Resource)
_sym_db.RegisterMessage(OSPolicy.Resource.File)
_sym_db.RegisterMessage(OSPolicy.Resource.File.Remote)
_sym_db.RegisterMessage(OSPolicy.Resource.File.Gcs)
_sym_db.RegisterMessage(OSPolicy.Resource.PackageResource)
_sym_db.RegisterMessage(OSPolicy.Resource.PackageResource.Deb)
_sym_db.RegisterMessage(OSPolicy.Resource.PackageResource.APT)
_sym_db.RegisterMessage(OSPolicy.Resource.PackageResource.RPM)
_sym_db.RegisterMessage(OSPolicy.Resource.PackageResource.YUM)
_sym_db.RegisterMessage(OSPolicy.Resource.PackageResource.Zypper)
_sym_db.RegisterMessage(OSPolicy.Resource.PackageResource.GooGet)
_sym_db.RegisterMessage(OSPolicy.Resource.PackageResource.MSI)
_sym_db.RegisterMessage(OSPolicy.Resource.RepositoryResource)
_sym_db.RegisterMessage(OSPolicy.Resource.RepositoryResource.AptRepository)
_sym_db.RegisterMessage(OSPolicy.Resource.RepositoryResource.YumRepository)
_sym_db.RegisterMessage(OSPolicy.Resource.RepositoryResource.ZypperRepository)
_sym_db.RegisterMessage(OSPolicy.Resource.RepositoryResource.GooRepository)
_sym_db.RegisterMessage(OSPolicy.Resource.ExecResource)
_sym_db.RegisterMessage(OSPolicy.Resource.ExecResource.Exec)
_sym_db.RegisterMessage(OSPolicy.Resource.FileResource)
_sym_db.RegisterMessage(OSPolicy.ResourceGroup)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.cloud.osconfig.v1alphaB\rOSPolicyProtoP\001ZEgoogle.golang.org/genproto/googleapis/cloud/osconfig/v1alpha;osconfig\252\002\035Google.Cloud.OsConfig.V1Alpha\312\002\035Google\\Cloud\\OsConfig\\V1alpha\352\002 Google::Cloud::OsConfig::V1alpha'
  _OSPOLICY_RESOURCE_FILE_REMOTE.fields_by_name['uri']._options = None
  _OSPOLICY_RESOURCE_FILE_REMOTE.fields_by_name['uri']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_FILE_GCS.fields_by_name['bucket']._options = None
  _OSPOLICY_RESOURCE_FILE_GCS.fields_by_name['bucket']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_FILE_GCS.fields_by_name['object']._options = None
  _OSPOLICY_RESOURCE_FILE_GCS.fields_by_name['object']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_DEB.fields_by_name['source']._options = None
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_DEB.fields_by_name['source']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_APT.fields_by_name['name']._options = None
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_APT.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_RPM.fields_by_name['source']._options = None
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_RPM.fields_by_name['source']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_YUM.fields_by_name['name']._options = None
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_YUM.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_ZYPPER.fields_by_name['name']._options = None
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_ZYPPER.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_GOOGET.fields_by_name['name']._options = None
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_GOOGET.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_MSI.fields_by_name['source']._options = None
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_MSI.fields_by_name['source']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_PACKAGERESOURCE.fields_by_name['desired_state']._options = None
  _OSPOLICY_RESOURCE_PACKAGERESOURCE.fields_by_name['desired_state']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY.fields_by_name['archive_type']._options = None
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY.fields_by_name['archive_type']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY.fields_by_name['uri']._options = None
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY.fields_by_name['uri']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY.fields_by_name['distribution']._options = None
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY.fields_by_name['distribution']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY.fields_by_name['components']._options = None
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY.fields_by_name['components']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_YUMREPOSITORY.fields_by_name['id']._options = None
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_YUMREPOSITORY.fields_by_name['id']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_YUMREPOSITORY.fields_by_name['base_url']._options = None
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_YUMREPOSITORY.fields_by_name['base_url']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_ZYPPERREPOSITORY.fields_by_name['id']._options = None
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_ZYPPERREPOSITORY.fields_by_name['id']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_ZYPPERREPOSITORY.fields_by_name['base_url']._options = None
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_ZYPPERREPOSITORY.fields_by_name['base_url']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_GOOREPOSITORY.fields_by_name['name']._options = None
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_GOOREPOSITORY.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_GOOREPOSITORY.fields_by_name['url']._options = None
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_GOOREPOSITORY.fields_by_name['url']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_EXECRESOURCE_EXEC.fields_by_name['interpreter']._options = None
  _OSPOLICY_RESOURCE_EXECRESOURCE_EXEC.fields_by_name['interpreter']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_EXECRESOURCE.fields_by_name['validate']._options = None
  _OSPOLICY_RESOURCE_EXECRESOURCE.fields_by_name['validate']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_FILERESOURCE.fields_by_name['path']._options = None
  _OSPOLICY_RESOURCE_FILERESOURCE.fields_by_name['path']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE_FILERESOURCE.fields_by_name['state']._options = None
  _OSPOLICY_RESOURCE_FILERESOURCE.fields_by_name['state']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCE.fields_by_name['id']._options = None
  _OSPOLICY_RESOURCE.fields_by_name['id']._serialized_options = b'\342A\001\002'
  _OSPOLICY_RESOURCEGROUP.fields_by_name['resources']._options = None
  _OSPOLICY_RESOURCEGROUP.fields_by_name['resources']._serialized_options = b'\342A\001\002'
  _OSPOLICY.fields_by_name['id']._options = None
  _OSPOLICY.fields_by_name['id']._serialized_options = b'\342A\001\002'
  _OSPOLICY.fields_by_name['mode']._options = None
  _OSPOLICY.fields_by_name['mode']._serialized_options = b'\342A\001\002'
  _OSPOLICY.fields_by_name['resource_groups']._options = None
  _OSPOLICY.fields_by_name['resource_groups']._serialized_options = b'\342A\001\002'
  _OSPOLICY._serialized_start=114
  _OSPOLICY._serialized_end=5108
  _OSPOLICY_OSFILTER._serialized_start=422
  _OSPOLICY_OSFILTER._serialized_end=499
  _OSPOLICY_RESOURCE._serialized_start=502
  _OSPOLICY_RESOURCE._serialized_end=4862
  _OSPOLICY_RESOURCE_FILE._serialized_start=896
  _OSPOLICY_RESOURCE_FILE._serialized_end=1323
  _OSPOLICY_RESOURCE_FILE_REMOTE._serialized_start=1143
  _OSPOLICY_RESOURCE_FILE_REMOTE._serialized_end=1216
  _OSPOLICY_RESOURCE_FILE_GCS._serialized_start=1218
  _OSPOLICY_RESOURCE_FILE_GCS._serialized_end=1315
  _OSPOLICY_RESOURCE_PACKAGERESOURCE._serialized_start=1326
  _OSPOLICY_RESOURCE_PACKAGERESOURCE._serialized_end=2710
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_DEB._serialized_start=2115
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_DEB._serialized_end=2234
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_APT._serialized_start=2236
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_APT._serialized_end=2267
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_RPM._serialized_start=2269
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_RPM._serialized_end=2388
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_YUM._serialized_start=2390
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_YUM._serialized_end=2421
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_ZYPPER._serialized_start=2423
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_ZYPPER._serialized_end=2457
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_GOOGET._serialized_start=2459
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_GOOGET._serialized_end=2493
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_MSI._serialized_start=2495
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_MSI._serialized_end=2617
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_DESIREDSTATE._serialized_start=2619
  _OSPOLICY_RESOURCE_PACKAGERESOURCE_DESIREDSTATE._serialized_end=2692
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE._serialized_start=2713
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE._serialized_end=3859
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY._serialized_start=3157
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY._serialized_end=3505
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY_ARCHIVETYPE._serialized_start=3440
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_APTREPOSITORY_ARCHIVETYPE._serialized_end=3505
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_YUMREPOSITORY._serialized_start=3508
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_YUMREPOSITORY._serialized_end=3640
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_ZYPPERREPOSITORY._serialized_start=3643
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_ZYPPERREPOSITORY._serialized_end=3778
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_GOOREPOSITORY._serialized_start=3780
  _OSPOLICY_RESOURCE_REPOSITORYRESOURCE_GOOREPOSITORY._serialized_end=3845
  _OSPOLICY_RESOURCE_EXECRESOURCE._serialized_start=3862
  _OSPOLICY_RESOURCE_EXECRESOURCE._serialized_end=4457
  _OSPOLICY_RESOURCE_EXECRESOURCE_EXEC._serialized_start=4075
  _OSPOLICY_RESOURCE_EXECRESOURCE_EXEC._serialized_end=4457
  _OSPOLICY_RESOURCE_EXECRESOURCE_EXEC_INTERPRETER._serialized_start=4368
  _OSPOLICY_RESOURCE_EXECRESOURCE_EXEC_INTERPRETER._serialized_end=4447
  _OSPOLICY_RESOURCE_FILERESOURCE._serialized_start=4460
  _OSPOLICY_RESOURCE_FILERESOURCE._serialized_end=4845
  _OSPOLICY_RESOURCE_FILERESOURCE_DESIREDSTATE._serialized_start=4745
  _OSPOLICY_RESOURCE_FILERESOURCE_DESIREDSTATE._serialized_end=4835
  _OSPOLICY_RESOURCEGROUP._serialized_start=4865
  _OSPOLICY_RESOURCEGROUP._serialized_end=5045
  _OSPOLICY_MODE._serialized_start=5047
  _OSPOLICY_MODE._serialized_end=5108
# @@protoc_insertion_point(module_scope)
