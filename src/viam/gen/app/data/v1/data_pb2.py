"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16app/data/v1/data.proto\x12\x10viam.app.data.v1\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa1\x01\n\x0bDataRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x14\n\x05limit\x18\x02 \x01(\x04R\x05limit\x12\x12\n\x04last\x18\x03 \x01(\tR\x04last\x126\n\nsort_order\x18\x04 \x01(\x0e2\x17.viam.app.data.v1.OrderR\tsortOrder"\x8b\x04\n\x06Filter\x12%\n\x0ecomponent_name\x18\x01 \x01(\tR\rcomponentName\x12%\n\x0ecomponent_type\x18\x02 \x01(\tR\rcomponentType\x12\x16\n\x06method\x18\x04 \x01(\tR\x06method\x12\x1d\n\nrobot_name\x18\x06 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x07 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x08 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\t \x01(\tR\x06partId\x12!\n\x0clocation_ids\x18\n \x03(\tR\x0blocationIds\x12)\n\x10organization_ids\x18\x0b \x03(\tR\x0forganizationIds\x12\x1b\n\tmime_type\x18\x0c \x03(\tR\x08mimeType\x12=\n\x08interval\x18\r \x01(\x0b2!.viam.app.data.v1.CaptureIntervalR\x08interval\x12=\n\x0btags_filter\x18\x0e \x01(\x0b2\x1c.viam.app.data.v1.TagsFilterR\ntagsFilter\x12\x1f\n\x0bbbox_labels\x18\x0f \x03(\tR\nbboxLabelsJ\x04\x08\x03\x10\x04J\x04\x08\x05\x10\x06R\x0fcomponent_modelR\x04tags"V\n\nTagsFilter\x124\n\x04type\x18\x01 \x01(\x0e2 .viam.app.data.v1.TagsFilterTypeR\x04type\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"\xc3\x04\n\x0fCaptureMetadata\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId\x12\x1d\n\nrobot_name\x18\x03 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x04 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x05 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\x06 \x01(\tR\x06partId\x12%\n\x0ecomponent_type\x18\x07 \x01(\tR\rcomponentType\x12%\n\x0ecomponent_name\x18\t \x01(\tR\rcomponentName\x12\x1f\n\x0bmethod_name\x18\n \x01(\tR\nmethodName\x12d\n\x11method_parameters\x18\x0b \x03(\x0b27.viam.app.data.v1.CaptureMetadata.MethodParametersEntryR\x10methodParameters\x12\x12\n\x04tags\x18\x0c \x03(\tR\x04tags\x12\x1b\n\tmime_type\x18\r \x01(\tR\x08mimeType\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01J\x04\x08\x08\x10\tR\x0fcomponent_model"q\n\x0fCaptureInterval\x120\n\x05start\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03end\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x03end"}\n\x1aTabularDataByFilterRequest\x12@\n\x0cdata_request\x18\x01 \x01(\x0b2\x1d.viam.app.data.v1.DataRequestR\x0bdataRequest\x12\x1d\n\ncount_only\x18\x02 \x01(\x08R\tcountOnly"\xe3\x01\n\x1bTabularDataByFilterResponse\x12=\n\x08metadata\x18\x01 \x03(\x0b2!.viam.app.data.v1.CaptureMetadataR\x08metadata\x121\n\x04data\x18\x02 \x03(\x0b2\x1d.viam.app.data.v1.TabularDataR\x04data\x12\x14\n\x05count\x18\x03 \x01(\x04R\x05count\x12\x12\n\x04last\x18\x04 \x01(\tR\x04last\x12(\n\x10total_size_bytes\x18\x05 \x01(\x04R\x0etotalSizeBytes"\xe5\x01\n\x0bTabularData\x12+\n\x04data\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x04data\x12%\n\x0emetadata_index\x18\x02 \x01(\rR\rmetadataIndex\x12A\n\x0etime_requested\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived"b\n\nBinaryData\x12\x16\n\x06binary\x18\x01 \x01(\x0cR\x06binary\x12<\n\x08metadata\x18\x02 \x01(\x0b2 .viam.app.data.v1.BinaryMetadataR\x08metadata"\xa3\x01\n\x19BinaryDataByFilterRequest\x12@\n\x0cdata_request\x18\x01 \x01(\x0b2\x1d.viam.app.data.v1.DataRequestR\x0bdataRequest\x12%\n\x0einclude_binary\x18\x02 \x01(\x08R\rincludeBinary\x12\x1d\n\ncount_only\x18\x03 \x01(\x08R\tcountOnly"\xa2\x01\n\x1aBinaryDataByFilterResponse\x120\n\x04data\x18\x01 \x03(\x0b2\x1c.viam.app.data.v1.BinaryDataR\x04data\x12\x14\n\x05count\x18\x02 \x01(\x04R\x05count\x12\x12\n\x04last\x18\x03 \x01(\tR\x04last\x12(\n\x10total_size_bytes\x18\x04 \x01(\x04R\x0etotalSizeBytes"m\n\x08BinaryID\x12\x17\n\x07file_id\x18\x01 \x01(\tR\x06fileId\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId\x12\x1f\n\x0blocation_id\x18\x03 \x01(\tR\nlocationId"\x99\x01\n\x16BinaryDataByIDsRequest\x12%\n\x0einclude_binary\x18\x02 \x01(\x08R\rincludeBinary\x129\n\nbinary_ids\x18\x03 \x03(\x0b2\x1a.viam.app.data.v1.BinaryIDR\tbinaryIds\x12\x1d\n\x08file_ids\x18\x01 \x03(\tB\x02\x18\x01R\x07fileIds"a\n\x17BinaryDataByIDsResponse\x120\n\x04data\x18\x01 \x03(\x0b2\x1c.viam.app.data.v1.BinaryDataR\x04data\x12\x14\n\x05count\x18\x02 \x01(\x04R\x05count"\xdb\x01\n\x0bBoundingBox\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x14\n\x05label\x18\x02 \x01(\tR\x05label\x12(\n\x10x_min_normalized\x18\x03 \x01(\x01R\x0exMinNormalized\x12(\n\x10y_min_normalized\x18\x04 \x01(\x01R\x0eyMinNormalized\x12(\n\x10x_max_normalized\x18\x05 \x01(\x01R\x0exMaxNormalized\x12(\n\x10y_max_normalized\x18\x06 \x01(\x01R\x0eyMaxNormalized"D\n\x0bAnnotations\x125\n\x06bboxes\x18\x01 \x03(\x0b2\x1d.viam.app.data.v1.BoundingBoxR\x06bboxes"\xfd\x02\n\x0eBinaryMetadata\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12L\n\x10capture_metadata\x18\x02 \x01(\x0b2!.viam.app.data.v1.CaptureMetadataR\x0fcaptureMetadata\x12A\n\x0etime_requested\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived\x12\x1b\n\tfile_name\x18\x05 \x01(\tR\x08fileName\x12\x19\n\x08file_ext\x18\x06 \x01(\tR\x07fileExt\x12\x10\n\x03uri\x18\x07 \x01(\tR\x03uri\x12?\n\x0bannotations\x18\x08 \x01(\x0b2\x1d.viam.app.data.v1.AnnotationsR\x0bannotations"T\n DeleteTabularDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter"V\n!DeleteTabularDataByFilterResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCountJ\x04\x08\x02\x10\x03R\x06result"S\n\x1fDeleteBinaryDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter"U\n DeleteBinaryDataByFilterResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCountJ\x04\x08\x02\x10\x03R\x06result"x\n\x1cDeleteBinaryDataByIDsRequest\x129\n\nbinary_ids\x18\x02 \x03(\x0b2\x1a.viam.app.data.v1.BinaryIDR\tbinaryIds\x12\x1d\n\x08file_ids\x18\x01 \x03(\tB\x02\x18\x01R\x07fileIds"R\n\x1dDeleteBinaryDataByIDsResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCountJ\x04\x08\x02\x10\x03R\x06result"\x8f\x01\n\x1fAddTagsToBinaryDataByIDsRequest\x129\n\nbinary_ids\x18\x03 \x03(\x0b2\x1a.viam.app.data.v1.BinaryIDR\tbinaryIds\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags\x12\x1d\n\x08file_ids\x18\x01 \x03(\tB\x02\x18\x01R\x07fileIds""\n AddTagsToBinaryDataByIDsResponse"j\n"AddTagsToBinaryDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"%\n#AddTagsToBinaryDataByFilterResponse"\x94\x01\n$RemoveTagsFromBinaryDataByIDsRequest\x129\n\nbinary_ids\x18\x03 \x03(\x0b2\x1a.viam.app.data.v1.BinaryIDR\tbinaryIds\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags\x12\x1d\n\x08file_ids\x18\x01 \x03(\tB\x02\x18\x01R\x07fileIds"L\n%RemoveTagsFromBinaryDataByIDsResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCount"o\n\'RemoveTagsFromBinaryDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"O\n(RemoveTagsFromBinaryDataByFilterResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCount"G\n\x13TagsByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter"*\n\x14TagsByFilterResponse\x12\x12\n\x04tags\x18\x01 \x03(\tR\x04tags"\xb6\x02\n AddBoundingBoxToImageByIDRequest\x127\n\tbinary_id\x18\x07 \x01(\x0b2\x1a.viam.app.data.v1.BinaryIDR\x08binaryId\x12\x14\n\x05label\x18\x02 \x01(\tR\x05label\x12(\n\x10x_min_normalized\x18\x03 \x01(\x01R\x0exMinNormalized\x12(\n\x10y_min_normalized\x18\x04 \x01(\x01R\x0eyMinNormalized\x12(\n\x10x_max_normalized\x18\x05 \x01(\x01R\x0exMaxNormalized\x12(\n\x10y_max_normalized\x18\x06 \x01(\x01R\x0eyMaxNormalized\x12\x1b\n\x07file_id\x18\x01 \x01(\tB\x02\x18\x01R\x06fileId"<\n!AddBoundingBoxToImageByIDResponse\x12\x17\n\x07bbox_id\x18\x01 \x01(\tR\x06bboxId"\x96\x01\n%RemoveBoundingBoxFromImageByIDRequest\x127\n\tbinary_id\x18\x03 \x01(\x0b2\x1a.viam.app.data.v1.BinaryIDR\x08binaryId\x12\x17\n\x07bbox_id\x18\x02 \x01(\tR\x06bboxId\x12\x1b\n\x07file_id\x18\x01 \x01(\tB\x02\x18\x01R\x06fileId"(\n&RemoveBoundingBoxFromImageByIDResponse"T\n BoundingBoxLabelsByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter";\n!BoundingBoxLabelsByFilterResponse\x12\x16\n\x06labels\x18\x01 \x03(\tR\x06labels*I\n\x05Order\x12\x15\n\x11ORDER_UNSPECIFIED\x10\x00\x12\x14\n\x10ORDER_DESCENDING\x10\x01\x12\x13\n\x0fORDER_ASCENDING\x10\x02*\x90\x01\n\x0eTagsFilterType\x12 \n\x1cTAGS_FILTER_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1cTAGS_FILTER_TYPE_MATCH_BY_OR\x10\x01\x12\x1b\n\x17TAGS_FILTER_TYPE_TAGGED\x10\x02\x12\x1d\n\x19TAGS_FILTER_TYPE_UNTAGGED\x10\x032\xa2\x0e\n\x0bDataService\x12r\n\x13TabularDataByFilter\x12,.viam.app.data.v1.TabularDataByFilterRequest\x1a-.viam.app.data.v1.TabularDataByFilterResponse\x12o\n\x12BinaryDataByFilter\x12+.viam.app.data.v1.BinaryDataByFilterRequest\x1a,.viam.app.data.v1.BinaryDataByFilterResponse\x12f\n\x0fBinaryDataByIDs\x12(.viam.app.data.v1.BinaryDataByIDsRequest\x1a).viam.app.data.v1.BinaryDataByIDsResponse\x12\x84\x01\n\x19DeleteTabularDataByFilter\x122.viam.app.data.v1.DeleteTabularDataByFilterRequest\x1a3.viam.app.data.v1.DeleteTabularDataByFilterResponse\x12\x81\x01\n\x18DeleteBinaryDataByFilter\x121.viam.app.data.v1.DeleteBinaryDataByFilterRequest\x1a2.viam.app.data.v1.DeleteBinaryDataByFilterResponse\x12x\n\x15DeleteBinaryDataByIDs\x12..viam.app.data.v1.DeleteBinaryDataByIDsRequest\x1a/.viam.app.data.v1.DeleteBinaryDataByIDsResponse\x12\x81\x01\n\x18AddTagsToBinaryDataByIDs\x121.viam.app.data.v1.AddTagsToBinaryDataByIDsRequest\x1a2.viam.app.data.v1.AddTagsToBinaryDataByIDsResponse\x12\x8a\x01\n\x1bAddTagsToBinaryDataByFilter\x124.viam.app.data.v1.AddTagsToBinaryDataByFilterRequest\x1a5.viam.app.data.v1.AddTagsToBinaryDataByFilterResponse\x12\x90\x01\n\x1dRemoveTagsFromBinaryDataByIDs\x126.viam.app.data.v1.RemoveTagsFromBinaryDataByIDsRequest\x1a7.viam.app.data.v1.RemoveTagsFromBinaryDataByIDsResponse\x12\x99\x01\n RemoveTagsFromBinaryDataByFilter\x129.viam.app.data.v1.RemoveTagsFromBinaryDataByFilterRequest\x1a:.viam.app.data.v1.RemoveTagsFromBinaryDataByFilterResponse\x12]\n\x0cTagsByFilter\x12%.viam.app.data.v1.TagsByFilterRequest\x1a&.viam.app.data.v1.TagsByFilterResponse\x12\x84\x01\n\x19AddBoundingBoxToImageByID\x122.viam.app.data.v1.AddBoundingBoxToImageByIDRequest\x1a3.viam.app.data.v1.AddBoundingBoxToImageByIDResponse\x12\x93\x01\n\x1eRemoveBoundingBoxFromImageByID\x127.viam.app.data.v1.RemoveBoundingBoxFromImageByIDRequest\x1a8.viam.app.data.v1.RemoveBoundingBoxFromImageByIDResponse\x12\x84\x01\n\x19BoundingBoxLabelsByFilter\x122.viam.app.data.v1.BoundingBoxLabelsByFilterRequest\x1a3.viam.app.data.v1.BoundingBoxLabelsByFilterResponseB\x1dZ\x1bgo.viam.com/api/app/data/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.data.v1.data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1bgo.viam.com/api/app/data/v1'
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._options = None
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_options = b'8\x01'
    _BINARYDATABYIDSREQUEST.fields_by_name['file_ids']._options = None
    _BINARYDATABYIDSREQUEST.fields_by_name['file_ids']._serialized_options = b'\x18\x01'
    _DELETEBINARYDATABYIDSREQUEST.fields_by_name['file_ids']._options = None
    _DELETEBINARYDATABYIDSREQUEST.fields_by_name['file_ids']._serialized_options = b'\x18\x01'
    _ADDTAGSTOBINARYDATABYIDSREQUEST.fields_by_name['file_ids']._options = None
    _ADDTAGSTOBINARYDATABYIDSREQUEST.fields_by_name['file_ids']._serialized_options = b'\x18\x01'
    _REMOVETAGSFROMBINARYDATABYIDSREQUEST.fields_by_name['file_ids']._options = None
    _REMOVETAGSFROMBINARYDATABYIDSREQUEST.fields_by_name['file_ids']._serialized_options = b'\x18\x01'
    _ADDBOUNDINGBOXTOIMAGEBYIDREQUEST.fields_by_name['file_id']._options = None
    _ADDBOUNDINGBOXTOIMAGEBYIDREQUEST.fields_by_name['file_id']._serialized_options = b'\x18\x01'
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDREQUEST.fields_by_name['file_id']._options = None
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDREQUEST.fields_by_name['file_id']._serialized_options = b'\x18\x01'
    _ORDER._serialized_start = 5809
    _ORDER._serialized_end = 5882
    _TAGSFILTERTYPE._serialized_start = 5885
    _TAGSFILTERTYPE._serialized_end = 6029
    _DATAREQUEST._serialized_start = 135
    _DATAREQUEST._serialized_end = 296
    _FILTER._serialized_start = 299
    _FILTER._serialized_end = 822
    _TAGSFILTER._serialized_start = 824
    _TAGSFILTER._serialized_end = 910
    _CAPTUREMETADATA._serialized_start = 913
    _CAPTUREMETADATA._serialized_end = 1492
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_start = 1380
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_end = 1469
    _CAPTUREINTERVAL._serialized_start = 1494
    _CAPTUREINTERVAL._serialized_end = 1607
    _TABULARDATABYFILTERREQUEST._serialized_start = 1609
    _TABULARDATABYFILTERREQUEST._serialized_end = 1734
    _TABULARDATABYFILTERRESPONSE._serialized_start = 1737
    _TABULARDATABYFILTERRESPONSE._serialized_end = 1964
    _TABULARDATA._serialized_start = 1967
    _TABULARDATA._serialized_end = 2196
    _BINARYDATA._serialized_start = 2198
    _BINARYDATA._serialized_end = 2296
    _BINARYDATABYFILTERREQUEST._serialized_start = 2299
    _BINARYDATABYFILTERREQUEST._serialized_end = 2462
    _BINARYDATABYFILTERRESPONSE._serialized_start = 2465
    _BINARYDATABYFILTERRESPONSE._serialized_end = 2627
    _BINARYID._serialized_start = 2629
    _BINARYID._serialized_end = 2738
    _BINARYDATABYIDSREQUEST._serialized_start = 2741
    _BINARYDATABYIDSREQUEST._serialized_end = 2894
    _BINARYDATABYIDSRESPONSE._serialized_start = 2896
    _BINARYDATABYIDSRESPONSE._serialized_end = 2993
    _BOUNDINGBOX._serialized_start = 2996
    _BOUNDINGBOX._serialized_end = 3215
    _ANNOTATIONS._serialized_start = 3217
    _ANNOTATIONS._serialized_end = 3285
    _BINARYMETADATA._serialized_start = 3288
    _BINARYMETADATA._serialized_end = 3669
    _DELETETABULARDATABYFILTERREQUEST._serialized_start = 3671
    _DELETETABULARDATABYFILTERREQUEST._serialized_end = 3755
    _DELETETABULARDATABYFILTERRESPONSE._serialized_start = 3757
    _DELETETABULARDATABYFILTERRESPONSE._serialized_end = 3843
    _DELETEBINARYDATABYFILTERREQUEST._serialized_start = 3845
    _DELETEBINARYDATABYFILTERREQUEST._serialized_end = 3928
    _DELETEBINARYDATABYFILTERRESPONSE._serialized_start = 3930
    _DELETEBINARYDATABYFILTERRESPONSE._serialized_end = 4015
    _DELETEBINARYDATABYIDSREQUEST._serialized_start = 4017
    _DELETEBINARYDATABYIDSREQUEST._serialized_end = 4137
    _DELETEBINARYDATABYIDSRESPONSE._serialized_start = 4139
    _DELETEBINARYDATABYIDSRESPONSE._serialized_end = 4221
    _ADDTAGSTOBINARYDATABYIDSREQUEST._serialized_start = 4224
    _ADDTAGSTOBINARYDATABYIDSREQUEST._serialized_end = 4367
    _ADDTAGSTOBINARYDATABYIDSRESPONSE._serialized_start = 4369
    _ADDTAGSTOBINARYDATABYIDSRESPONSE._serialized_end = 4403
    _ADDTAGSTOBINARYDATABYFILTERREQUEST._serialized_start = 4405
    _ADDTAGSTOBINARYDATABYFILTERREQUEST._serialized_end = 4511
    _ADDTAGSTOBINARYDATABYFILTERRESPONSE._serialized_start = 4513
    _ADDTAGSTOBINARYDATABYFILTERRESPONSE._serialized_end = 4550
    _REMOVETAGSFROMBINARYDATABYIDSREQUEST._serialized_start = 4553
    _REMOVETAGSFROMBINARYDATABYIDSREQUEST._serialized_end = 4701
    _REMOVETAGSFROMBINARYDATABYIDSRESPONSE._serialized_start = 4703
    _REMOVETAGSFROMBINARYDATABYIDSRESPONSE._serialized_end = 4779
    _REMOVETAGSFROMBINARYDATABYFILTERREQUEST._serialized_start = 4781
    _REMOVETAGSFROMBINARYDATABYFILTERREQUEST._serialized_end = 4892
    _REMOVETAGSFROMBINARYDATABYFILTERRESPONSE._serialized_start = 4894
    _REMOVETAGSFROMBINARYDATABYFILTERRESPONSE._serialized_end = 4973
    _TAGSBYFILTERREQUEST._serialized_start = 4975
    _TAGSBYFILTERREQUEST._serialized_end = 5046
    _TAGSBYFILTERRESPONSE._serialized_start = 5048
    _TAGSBYFILTERRESPONSE._serialized_end = 5090
    _ADDBOUNDINGBOXTOIMAGEBYIDREQUEST._serialized_start = 5093
    _ADDBOUNDINGBOXTOIMAGEBYIDREQUEST._serialized_end = 5403
    _ADDBOUNDINGBOXTOIMAGEBYIDRESPONSE._serialized_start = 5405
    _ADDBOUNDINGBOXTOIMAGEBYIDRESPONSE._serialized_end = 5465
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDREQUEST._serialized_start = 5468
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDREQUEST._serialized_end = 5618
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDRESPONSE._serialized_start = 5620
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDRESPONSE._serialized_end = 5660
    _BOUNDINGBOXLABELSBYFILTERREQUEST._serialized_start = 5662
    _BOUNDINGBOXLABELSBYFILTERREQUEST._serialized_end = 5746
    _BOUNDINGBOXLABELSBYFILTERRESPONSE._serialized_start = 5748
    _BOUNDINGBOXLABELSBYFILTERRESPONSE._serialized_end = 5807
    _DATASERVICE._serialized_start = 6032
    _DATASERVICE._serialized_end = 7858