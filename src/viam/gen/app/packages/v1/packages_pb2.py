"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eapp/packages/v1/packages.proto\x12\x14viam.app.packages.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"k\n\x08FileInfo\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04size\x18\x02 \x01(\x04R\x04size\x12&\n\x0cis_directory\x18\x03 \x01(\x08H\x00R\x0bisDirectory\x88\x01\x01B\x0f\n\r_is_directory"\xb4\x02\n\x0bPackageInfo\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\x125\n\x04type\x18\x04 \x01(\x0e2!.viam.app.packages.v1.PackageTypeR\x04type\x12\x1f\n\x08platform\x18\x07 \x01(\tH\x00R\x08platform\x88\x01\x01\x124\n\x05files\x18\x05 \x03(\x0b2\x1e.viam.app.packages.v1.FileInfoR\x05files\x123\n\x08metadata\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x08metadataB\x0b\n\t_platform"x\n\x14CreatePackageRequest\x127\n\x04info\x18\x01 \x01(\x0b2!.viam.app.packages.v1.PackageInfoH\x00R\x04info\x12\x1c\n\x08contents\x18\x02 \x01(\x0cH\x00R\x08contentsB\t\n\x07package"A\n\x15CreatePackageResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version"w\n\x14DeletePackageRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x125\n\x04type\x18\x03 \x01(\x0e2!.viam.app.packages.v1.PackageTypeR\x04type"\x17\n\x15DeletePackageResponse"\xb9\x01\n\x07Package\x125\n\x04info\x18\x01 \x01(\x0b2!.viam.app.packages.v1.PackageInfoR\x04info\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x129\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedOn\x12\x1a\n\x08checksum\x18\x04 \x01(\tR\x08checksum\x12\x0e\n\x02id\x18\x05 \x01(\tR\x02id"\xe6\x01\n\x11GetPackageRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12$\n\x0binclude_url\x18\x03 \x01(\x08H\x00R\nincludeUrl\x88\x01\x01\x12:\n\x04type\x18\x04 \x01(\x0e2!.viam.app.packages.v1.PackageTypeH\x01R\x04type\x88\x01\x01\x12\x1f\n\x08platform\x18\x05 \x01(\tH\x02R\x08platform\x88\x01\x01B\x0e\n\x0c_include_urlB\x07\n\x05_typeB\x0b\n\t_platform"M\n\x12GetPackageResponse\x127\n\x07package\x18\x01 \x01(\x0b2\x1d.viam.app.packages.v1.PackageR\x07package"\x86\x02\n\x13ListPackagesRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x12\x1d\n\x07version\x18\x03 \x01(\tH\x01R\x07version\x88\x01\x01\x12:\n\x04type\x18\x04 \x01(\x0e2!.viam.app.packages.v1.PackageTypeH\x02R\x04type\x88\x01\x01\x12$\n\x0binclude_url\x18\x05 \x01(\x08H\x03R\nincludeUrl\x88\x01\x01B\x07\n\x05_nameB\n\n\x08_versionB\x07\n\x05_typeB\x0e\n\x0c_include_url"Q\n\x14ListPackagesResponse\x129\n\x08packages\x18\x01 \x03(\x0b2\x1d.viam.app.packages.v1.PackageR\x08packages*\xb2\x01\n\x0bPackageType\x12\x1c\n\x18PACKAGE_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14PACKAGE_TYPE_ARCHIVE\x10\x01\x12\x19\n\x15PACKAGE_TYPE_ML_MODEL\x10\x02\x12\x17\n\x13PACKAGE_TYPE_MODULE\x10\x03\x12\x19\n\x15PACKAGE_TYPE_SLAM_MAP\x10\x04\x12\x1c\n\x18PACKAGE_TYPE_ML_TRAINING\x10\x052\xa0\x04\n\x0ePackageService\x12\x87\x01\n\rCreatePackage\x12*.viam.app.packages.v1.CreatePackageRequest\x1a+.viam.app.packages.v1.CreatePackageResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x13/packages/v1/create(\x01\x12\x85\x01\n\rDeletePackage\x12*.viam.app.packages.v1.DeletePackageRequest\x1a+.viam.app.packages.v1.DeletePackageResponse"\x1b\x82\xd3\xe4\x93\x02\x15*\x13/packages/v1/delete\x12y\n\nGetPackage\x12\'.viam.app.packages.v1.GetPackageRequest\x1a(.viam.app.packages.v1.GetPackageResponse"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/packages/v1/get\x12\x80\x01\n\x0cListPackages\x12).viam.app.packages.v1.ListPackagesRequest\x1a*.viam.app.packages.v1.ListPackagesResponse"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/packages/v1/listB!Z\x1fgo.viam.com/api/app/packages/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.packages.v1.packages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1fgo.viam.com/api/app/packages/v1'
    _PACKAGESERVICE.methods_by_name['CreatePackage']._options = None
    _PACKAGESERVICE.methods_by_name['CreatePackage']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x13/packages/v1/create'
    _PACKAGESERVICE.methods_by_name['DeletePackage']._options = None
    _PACKAGESERVICE.methods_by_name['DeletePackage']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15*\x13/packages/v1/delete'
    _PACKAGESERVICE.methods_by_name['GetPackage']._options = None
    _PACKAGESERVICE.methods_by_name['GetPackage']._serialized_options = b'\x82\xd3\xe4\x93\x02\x12\x12\x10/packages/v1/get'
    _PACKAGESERVICE.methods_by_name['ListPackages']._options = None
    _PACKAGESERVICE.methods_by_name['ListPackages']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13\x12\x11/packages/v1/list'
    _PACKAGETYPE._serialized_start = 1753
    _PACKAGETYPE._serialized_end = 1931
    _FILEINFO._serialized_start = 149
    _FILEINFO._serialized_end = 256
    _PACKAGEINFO._serialized_start = 259
    _PACKAGEINFO._serialized_end = 567
    _CREATEPACKAGEREQUEST._serialized_start = 569
    _CREATEPACKAGEREQUEST._serialized_end = 689
    _CREATEPACKAGERESPONSE._serialized_start = 691
    _CREATEPACKAGERESPONSE._serialized_end = 756
    _DELETEPACKAGEREQUEST._serialized_start = 758
    _DELETEPACKAGEREQUEST._serialized_end = 877
    _DELETEPACKAGERESPONSE._serialized_start = 879
    _DELETEPACKAGERESPONSE._serialized_end = 902
    _PACKAGE._serialized_start = 905
    _PACKAGE._serialized_end = 1090
    _GETPACKAGEREQUEST._serialized_start = 1093
    _GETPACKAGEREQUEST._serialized_end = 1323
    _GETPACKAGERESPONSE._serialized_start = 1325
    _GETPACKAGERESPONSE._serialized_end = 1402
    _LISTPACKAGESREQUEST._serialized_start = 1405
    _LISTPACKAGESREQUEST._serialized_end = 1667
    _LISTPACKAGESRESPONSE._serialized_start = 1669
    _LISTPACKAGESRESPONSE._serialized_end = 1750
    _PACKAGESERVICE._serialized_start = 1934
    _PACKAGESERVICE._serialized_end = 2478