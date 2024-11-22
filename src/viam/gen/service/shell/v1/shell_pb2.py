"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 2, '', 'service/shell/v1/shell.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cservice/shell/v1/shell.proto\x12\x15viam.service.shell.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"j\n\x0cShellRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x17\n\x07data_in\x18\x02 \x01(\tR\x06dataIn\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"W\n\rShellResponse\x12\x19\n\x08data_out\x18\x01 \x01(\tR\x07dataOut\x12\x19\n\x08data_err\x18\x02 \x01(\tR\x07dataErr\x12\x10\n\x03eof\x18\x03 \x01(\x08R\x03eof"\xda\x01\n\x08FileData\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04size\x18\x02 \x01(\x03R\x04size\x12\x15\n\x06is_dir\x18\x03 \x01(\x08R\x05isDir\x12\x12\n\x04data\x18\x04 \x01(\x0cR\x04data\x12\x10\n\x03eof\x18\x05 \x01(\x08R\x03eof\x12:\n\x08mod_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x07modTime\x88\x01\x01\x12\x17\n\x04mode\x18\x07 \x01(\rH\x01R\x04mode\x88\x01\x01B\x0b\n\t_mod_timeB\x07\n\x05_mode"\xf1\x01\n!CopyFilesToMachineRequestMetadata\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12K\n\x0bsource_type\x18\x02 \x01(\x0e2*.viam.service.shell.v1.CopyFilesSourceTypeR\nsourceType\x12 \n\x0bdestination\x18\x03 \x01(\tR\x0bdestination\x12\x1a\n\x08preserve\x18\x04 \x01(\x08R\x08preserve\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xbe\x01\n\x19CopyFilesToMachineRequest\x12V\n\x08metadata\x18\x01 \x01(\x0b28.viam.service.shell.v1.CopyFilesToMachineRequestMetadataH\x00R\x08metadata\x12>\n\tfile_data\x18\x02 \x01(\x0b2\x1f.viam.service.shell.v1.FileDataH\x00R\x08fileDataB\t\n\x07request"@\n\x1aCopyFilesToMachineResponse\x12"\n\rack_last_file\x18\x01 \x01(\x08R\x0backLastFile"\xc3\x01\n#CopyFilesFromMachineRequestMetadata\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05paths\x18\x02 \x03(\tR\x05paths\x12\'\n\x0fallow_recursion\x18\x03 \x01(\x08R\x0eallowRecursion\x12\x1a\n\x08preserve\x18\x04 \x01(\x08R\x08preserve\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xa8\x01\n\x1bCopyFilesFromMachineRequest\x12X\n\x08metadata\x18\x01 \x01(\x0b2:.viam.service.shell.v1.CopyFilesFromMachineRequestMetadataH\x00R\x08metadata\x12$\n\rack_last_file\x18\x02 \x01(\x08H\x00R\x0backLastFileB\t\n\x07request"s\n$CopyFilesFromMachineResponseMetadata\x12K\n\x0bsource_type\x18\x01 \x01(\x0e2*.viam.service.shell.v1.CopyFilesSourceTypeR\nsourceType"\xc5\x01\n\x1cCopyFilesFromMachineResponse\x12Y\n\x08metadata\x18\x01 \x01(\x0b2;.viam.service.shell.v1.CopyFilesFromMachineResponseMetadataH\x00R\x08metadata\x12>\n\tfile_data\x18\x02 \x01(\x0b2\x1f.viam.service.shell.v1.FileDataH\x00R\x08fileDataB\n\n\x08response*\xbd\x01\n\x13CopyFilesSourceType\x12&\n"COPY_FILES_SOURCE_TYPE_UNSPECIFIED\x10\x00\x12&\n"COPY_FILES_SOURCE_TYPE_SINGLE_FILE\x10\x01\x12+\n\'COPY_FILES_SOURCE_TYPE_SINGLE_DIRECTORY\x10\x02\x12)\n%COPY_FILES_SOURCE_TYPE_MULTIPLE_FILES\x10\x032\xf4\x03\n\x0cShellService\x12V\n\x05Shell\x12#.viam.service.shell.v1.ShellRequest\x1a$.viam.service.shell.v1.ShellResponse(\x010\x01\x12}\n\x12CopyFilesToMachine\x120.viam.service.shell.v1.CopyFilesToMachineRequest\x1a1.viam.service.shell.v1.CopyFilesToMachineResponse(\x010\x01\x12\x83\x01\n\x14CopyFilesFromMachine\x122.viam.service.shell.v1.CopyFilesFromMachineRequest\x1a3.viam.service.shell.v1.CopyFilesFromMachineResponse(\x010\x01\x12\x86\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"4\x82\xd3\xe4\x93\x02.",/viam/api/v1/service/shell/{name}/do_commandB=\n\x19com.viam.service.shell.v1Z go.viam.com/api/service/shell/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.shell.v1.shell_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.viam.service.shell.v1Z go.viam.com/api/service/shell/v1'
    _globals['_SHELLSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_SHELLSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02.",/viam/api/v1/service/shell/{name}/do_command'
    _globals['_COPYFILESSOURCETYPE']._serialized_start = 1780
    _globals['_COPYFILESSOURCETYPE']._serialized_end = 1969
    _globals['_SHELLREQUEST']._serialized_start = 172
    _globals['_SHELLREQUEST']._serialized_end = 278
    _globals['_SHELLRESPONSE']._serialized_start = 280
    _globals['_SHELLRESPONSE']._serialized_end = 367
    _globals['_FILEDATA']._serialized_start = 370
    _globals['_FILEDATA']._serialized_end = 588
    _globals['_COPYFILESTOMACHINEREQUESTMETADATA']._serialized_start = 591
    _globals['_COPYFILESTOMACHINEREQUESTMETADATA']._serialized_end = 832
    _globals['_COPYFILESTOMACHINEREQUEST']._serialized_start = 835
    _globals['_COPYFILESTOMACHINEREQUEST']._serialized_end = 1025
    _globals['_COPYFILESTOMACHINERESPONSE']._serialized_start = 1027
    _globals['_COPYFILESTOMACHINERESPONSE']._serialized_end = 1091
    _globals['_COPYFILESFROMMACHINEREQUESTMETADATA']._serialized_start = 1094
    _globals['_COPYFILESFROMMACHINEREQUESTMETADATA']._serialized_end = 1289
    _globals['_COPYFILESFROMMACHINEREQUEST']._serialized_start = 1292
    _globals['_COPYFILESFROMMACHINEREQUEST']._serialized_end = 1460
    _globals['_COPYFILESFROMMACHINERESPONSEMETADATA']._serialized_start = 1462
    _globals['_COPYFILESFROMMACHINERESPONSEMETADATA']._serialized_end = 1577
    _globals['_COPYFILESFROMMACHINERESPONSE']._serialized_start = 1580
    _globals['_COPYFILESFROMMACHINERESPONSE']._serialized_end = 1777
    _globals['_SHELLSERVICE']._serialized_start = 1972
    _globals['_SHELLSERVICE']._serialized_end = 2472