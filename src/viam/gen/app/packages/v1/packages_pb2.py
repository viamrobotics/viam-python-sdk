"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....tagger.v1 import tagger_pb2 as tagger_dot_v1_dot_tagger__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eapp/packages/v1/packages.proto\x12\x14viam.app.packages.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16tagger/v1/tagger.proto"2\n\x08FileInfo\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04size\x18\x02 \x01(\x04R\x04size"\x86\x02\n\x0bPackageInfo\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\x125\n\x04type\x18\x04 \x01(\x0e2!.viam.app.packages.v1.PackageTypeR\x04type\x124\n\x05files\x18\x05 \x03(\x0b2\x1e.viam.app.packages.v1.FileInfoR\x05files\x123\n\x08metadata\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x08metadata"x\n\x14CreatePackageRequest\x127\n\x04info\x18\x01 \x01(\x0b2!.viam.app.packages.v1.PackageInfoH\x00R\x04info\x12\x1c\n\x08contents\x18\x02 \x01(\x0cH\x00R\x08contentsB\t\n\x07package"A\n\x15CreatePackageResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version"@\n\x14DeletePackageRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version"\x17\n\x15DeletePackageResponse"\xb9\x01\n\x07Package\x125\n\x04info\x18\x01 \x01(\x0b2!.viam.app.packages.v1.PackageInfoR\x04info\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x129\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedOn\x12\x1a\n\x08checksum\x18\x04 \x01(\tR\x08checksum\x12\x0e\n\x02id\x18\x05 \x01(\tR\x02id"\x8a\x06\n\x0fInternalPackage\x12[\n\x0forganization_id\x18\x01 \x01(\tB2\x9a\x84\x9e\x03-bson:"organization_id" json:"organization_id"R\x0eorganizationId\x120\n\x04name\x18\x02 \x01(\tB\x1c\x9a\x84\x9e\x03\x17bson:"name" json:"name"R\x04name\x12<\n\x07version\x18\x03 \x01(\tB"\x9a\x84\x9e\x03\x1dbson:"version" json:"version"R\x07version\x12S\n\x04type\x18\x04 \x01(\x0e2!.viam.app.packages.v1.PackageTypeB\x1c\x9a\x84\x9e\x03\x17bson:"type" json:"type"R\x04type\x12T\n\x05files\x18\x05 \x03(\x0b2\x1e.viam.app.packages.v1.FileInfoB\x1e\x9a\x84\x9e\x03\x19bson:"files" json:"files"R\x05files\x12Y\n\x08metadata\x18\x06 \x01(\x0b2\x17.google.protobuf.StructB$\x9a\x84\x9e\x03\x1fbson:"metadata" json:"metadata"R\x08metadata\x12C\n\tblob_path\x18\x07 \x01(\tB&\x9a\x84\x9e\x03!bson:"blob_path" json:"blob_path"R\x08blobPath\x12c\n\ncreated_on\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB(\x9a\x84\x9e\x03#bson:"created_on" json:"created_on"R\tcreatedOn\x12@\n\x08checksum\x18\t \x01(\tB$\x9a\x84\x9e\x03\x1fbson:"checksum" json:"checksum"R\x08checksum\x128\n\x06latest\x18\n \x01(\x08B \x9a\x84\x9e\x03\x1bbson:"latest" json:"latest"R\x06latest"s\n\x11GetPackageRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12$\n\x0binclude_url\x18\x03 \x01(\x08H\x00R\nincludeUrl\x88\x01\x01B\x0e\n\x0c_include_url"M\n\x12GetPackageResponse\x127\n\x07package\x18\x01 \x01(\x0b2\x1d.viam.app.packages.v1.PackageR\x07package"\x86\x02\n\x13ListPackagesRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x12\x1d\n\x07version\x18\x03 \x01(\tH\x01R\x07version\x88\x01\x01\x12:\n\x04type\x18\x04 \x01(\x0e2!.viam.app.packages.v1.PackageTypeH\x02R\x04type\x88\x01\x01\x12$\n\x0binclude_url\x18\x05 \x01(\x08H\x03R\nincludeUrl\x88\x01\x01B\x07\n\x05_nameB\n\n\x08_versionB\x07\n\x05_typeB\x0e\n\x0c_include_url"Q\n\x14ListPackagesResponse\x129\n\x08packages\x18\x01 \x03(\x0b2\x1d.viam.app.packages.v1.PackageR\x08packages*`\n\x0bPackageType\x12\x1c\n\x18PACKAGE_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14PACKAGE_TYPE_ARCHIVE\x10\x01\x12\x19\n\x15PACKAGE_TYPE_ML_MODEL\x10\x022\xa0\x04\n\x0ePackageService\x12\x87\x01\n\rCreatePackage\x12*.viam.app.packages.v1.CreatePackageRequest\x1a+.viam.app.packages.v1.CreatePackageResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x13/packages/v1/create(\x01\x12\x85\x01\n\rDeletePackage\x12*.viam.app.packages.v1.DeletePackageRequest\x1a+.viam.app.packages.v1.DeletePackageResponse"\x1b\x82\xd3\xe4\x93\x02\x15*\x13/packages/v1/delete\x12y\n\nGetPackage\x12\'.viam.app.packages.v1.GetPackageRequest\x1a(.viam.app.packages.v1.GetPackageResponse"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/packages/v1/get\x12\x80\x01\n\x0cListPackages\x12).viam.app.packages.v1.ListPackagesRequest\x1a*.viam.app.packages.v1.ListPackagesResponse"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/packages/v1/listB!Z\x1fgo.viam.com/api/app/packages/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.packages.v1.packages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1fgo.viam.com/api/app/packages/v1'
    _INTERNALPACKAGE.fields_by_name['organization_id']._options = None
    _INTERNALPACKAGE.fields_by_name['organization_id']._serialized_options = b'\x9a\x84\x9e\x03-bson:"organization_id" json:"organization_id"'
    _INTERNALPACKAGE.fields_by_name['name']._options = None
    _INTERNALPACKAGE.fields_by_name['name']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"name" json:"name"'
    _INTERNALPACKAGE.fields_by_name['version']._options = None
    _INTERNALPACKAGE.fields_by_name['version']._serialized_options = b'\x9a\x84\x9e\x03\x1dbson:"version" json:"version"'
    _INTERNALPACKAGE.fields_by_name['type']._options = None
    _INTERNALPACKAGE.fields_by_name['type']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"type" json:"type"'
    _INTERNALPACKAGE.fields_by_name['files']._options = None
    _INTERNALPACKAGE.fields_by_name['files']._serialized_options = b'\x9a\x84\x9e\x03\x19bson:"files" json:"files"'
    _INTERNALPACKAGE.fields_by_name['metadata']._options = None
    _INTERNALPACKAGE.fields_by_name['metadata']._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"metadata" json:"metadata"'
    _INTERNALPACKAGE.fields_by_name['blob_path']._options = None
    _INTERNALPACKAGE.fields_by_name['blob_path']._serialized_options = b'\x9a\x84\x9e\x03!bson:"blob_path" json:"blob_path"'
    _INTERNALPACKAGE.fields_by_name['created_on']._options = None
    _INTERNALPACKAGE.fields_by_name['created_on']._serialized_options = b'\x9a\x84\x9e\x03#bson:"created_on" json:"created_on"'
    _INTERNALPACKAGE.fields_by_name['checksum']._options = None
    _INTERNALPACKAGE.fields_by_name['checksum']._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"checksum" json:"checksum"'
    _INTERNALPACKAGE.fields_by_name['latest']._options = None
    _INTERNALPACKAGE.fields_by_name['latest']._serialized_options = b'\x9a\x84\x9e\x03\x1bbson:"latest" json:"latest"'
    _PACKAGESERVICE.methods_by_name['CreatePackage']._options = None
    _PACKAGESERVICE.methods_by_name['CreatePackage']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x13/packages/v1/create'
    _PACKAGESERVICE.methods_by_name['DeletePackage']._options = None
    _PACKAGESERVICE.methods_by_name['DeletePackage']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15*\x13/packages/v1/delete'
    _PACKAGESERVICE.methods_by_name['GetPackage']._options = None
    _PACKAGESERVICE.methods_by_name['GetPackage']._serialized_options = b'\x82\xd3\xe4\x93\x02\x12\x12\x10/packages/v1/get'
    _PACKAGESERVICE.methods_by_name['ListPackages']._options = None
    _PACKAGESERVICE.methods_by_name['ListPackages']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13\x12\x11/packages/v1/list'
    _PACKAGETYPE._serialized_start = 2283
    _PACKAGETYPE._serialized_end = 2379
    _FILEINFO._serialized_start = 173
    _FILEINFO._serialized_end = 223
    _PACKAGEINFO._serialized_start = 226
    _PACKAGEINFO._serialized_end = 488
    _CREATEPACKAGEREQUEST._serialized_start = 490
    _CREATEPACKAGEREQUEST._serialized_end = 610
    _CREATEPACKAGERESPONSE._serialized_start = 612
    _CREATEPACKAGERESPONSE._serialized_end = 677
    _DELETEPACKAGEREQUEST._serialized_start = 679
    _DELETEPACKAGEREQUEST._serialized_end = 743
    _DELETEPACKAGERESPONSE._serialized_start = 745
    _DELETEPACKAGERESPONSE._serialized_end = 768
    _PACKAGE._serialized_start = 771
    _PACKAGE._serialized_end = 956
    _INTERNALPACKAGE._serialized_start = 959
    _INTERNALPACKAGE._serialized_end = 1737
    _GETPACKAGEREQUEST._serialized_start = 1739
    _GETPACKAGEREQUEST._serialized_end = 1854
    _GETPACKAGERESPONSE._serialized_start = 1856
    _GETPACKAGERESPONSE._serialized_end = 1933
    _LISTPACKAGESREQUEST._serialized_start = 1936
    _LISTPACKAGESREQUEST._serialized_end = 2198
    _LISTPACKAGESRESPONSE._serialized_start = 2200
    _LISTPACKAGESRESPONSE._serialized_end = 2281
    _PACKAGESERVICE._serialized_start = 2382
    _PACKAGESERVICE._serialized_end = 2926