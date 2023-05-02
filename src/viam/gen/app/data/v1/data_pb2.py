"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16app/data/v1/data.proto\x12\x10viam.app.data.v1\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"T\n\x06Result\x120\n\x06status\x18\x01 \x01(\x0e2\x18.viam.app.data.v1.StatusR\x06status\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"\xa1\x01\n\x0bDataRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x14\n\x05limit\x18\x02 \x01(\x04R\x05limit\x12\x12\n\x04last\x18\x03 \x01(\tR\x04last\x126\n\nsort_order\x18\x04 \x01(\x0e2\x17.viam.app.data.v1.OrderR\tsortOrder"\x97\x04\n\x06Filter\x12%\n\x0ecomponent_name\x18\x01 \x01(\tR\rcomponentName\x12%\n\x0ecomponent_type\x18\x02 \x01(\tR\rcomponentType\x12\'\n\x0fcomponent_model\x18\x03 \x01(\tR\x0ecomponentModel\x12\x16\n\x06method\x18\x04 \x01(\tR\x06method\x12\x1d\n\nrobot_name\x18\x06 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x07 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x08 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\t \x01(\tR\x06partId\x12!\n\x0clocation_ids\x18\n \x03(\tR\x0blocationIds\x12\x17\n\x07org_ids\x18\x0b \x03(\tR\x06orgIds\x12\x1b\n\tmime_type\x18\x0c \x03(\tR\x08mimeType\x12=\n\x08interval\x18\r \x01(\x0b2!.viam.app.data.v1.CaptureIntervalR\x08interval\x12=\n\x0btags_filter\x18\x0e \x01(\x0b2\x1c.viam.app.data.v1.TagsFilterR\ntagsFilter\x12\x1f\n\x0bbbox_labels\x18\x0f \x03(\tR\nbboxLabels\x12\x16\n\x04tags\x18\x05 \x03(\tB\x02\x18\x01R\x04tags"V\n\nTagsFilter\x124\n\x04type\x18\x01 \x01(\x0e2 .viam.app.data.v1.TagsFilterTypeR\x04type\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"\xc3\x04\n\x0fCaptureMetadata\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId\x12\x1d\n\nrobot_name\x18\x03 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x04 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x05 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\x06 \x01(\tR\x06partId\x12%\n\x0ecomponent_type\x18\x07 \x01(\tR\rcomponentType\x12\'\n\x0fcomponent_model\x18\x08 \x01(\tR\x0ecomponentModel\x12%\n\x0ecomponent_name\x18\t \x01(\tR\rcomponentName\x12\x1f\n\x0bmethod_name\x18\n \x01(\tR\nmethodName\x12d\n\x11method_parameters\x18\x0b \x03(\x0b27.viam.app.data.v1.CaptureMetadata.MethodParametersEntryR\x10methodParameters\x12\x12\n\x04tags\x18\x0c \x03(\tR\x04tags\x12\x1b\n\tmime_type\x18\r \x01(\tR\x08mimeType\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01"q\n\x0fCaptureInterval\x120\n\x05start\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03end\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x03end"}\n\x1aTabularDataByFilterRequest\x12@\n\x0cdata_request\x18\x01 \x01(\x0b2\x1d.viam.app.data.v1.DataRequestR\x0bdataRequest\x12\x1d\n\ncount_only\x18\x02 \x01(\x08R\tcountOnly"\xe3\x01\n\x1bTabularDataByFilterResponse\x12=\n\x08metadata\x18\x01 \x03(\x0b2!.viam.app.data.v1.CaptureMetadataR\x08metadata\x121\n\x04data\x18\x02 \x03(\x0b2\x1d.viam.app.data.v1.TabularDataR\x04data\x12\x14\n\x05count\x18\x03 \x01(\x03R\x05count\x12\x12\n\x04last\x18\x04 \x01(\tR\x04last\x12(\n\x10total_size_bytes\x18\x05 \x01(\x04R\x0etotalSizeBytes"\xe5\x01\n\x0bTabularData\x12+\n\x04data\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x04data\x12%\n\x0emetadata_index\x18\x02 \x01(\x05R\rmetadataIndex\x12A\n\x0etime_requested\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived"b\n\nBinaryData\x12\x16\n\x06binary\x18\x01 \x01(\x0cR\x06binary\x12<\n\x08metadata\x18\x02 \x01(\x0b2 .viam.app.data.v1.BinaryMetadataR\x08metadata"\xa3\x01\n\x19BinaryDataByFilterRequest\x12@\n\x0cdata_request\x18\x01 \x01(\x0b2\x1d.viam.app.data.v1.DataRequestR\x0bdataRequest\x12%\n\x0einclude_binary\x18\x02 \x01(\x08R\rincludeBinary\x12\x1d\n\ncount_only\x18\x03 \x01(\x08R\tcountOnly"x\n\x1aBinaryDataByFilterResponse\x120\n\x04data\x18\x01 \x03(\x0b2\x1c.viam.app.data.v1.BinaryDataR\x04data\x12\x14\n\x05count\x18\x02 \x01(\x04R\x05count\x12\x12\n\x04last\x18\x03 \x01(\tR\x04last"Z\n\x16BinaryDataByIDsRequest\x12\x19\n\x08file_ids\x18\x01 \x03(\tR\x07fileIds\x12%\n\x0einclude_binary\x18\x02 \x01(\x08R\rincludeBinary"a\n\x17BinaryDataByIDsResponse\x120\n\x04data\x18\x01 \x03(\x0b2\x1c.viam.app.data.v1.BinaryDataR\x04data\x12\x14\n\x05count\x18\x02 \x01(\x04R\x05count"\xdb\x01\n\x0bBoundingBox\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x14\n\x05label\x18\x02 \x01(\tR\x05label\x12(\n\x10x_min_normalized\x18\x03 \x01(\x01R\x0exMinNormalized\x12(\n\x10y_min_normalized\x18\x04 \x01(\x01R\x0eyMinNormalized\x12(\n\x10x_max_normalized\x18\x05 \x01(\x01R\x0exMaxNormalized\x12(\n\x10y_max_normalized\x18\x06 \x01(\x01R\x0eyMaxNormalized"D\n\x0bAnnotations\x125\n\x06bboxes\x18\x01 \x03(\x0b2\x1d.viam.app.data.v1.BoundingBoxR\x06bboxes"\xfd\x02\n\x0eBinaryMetadata\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12L\n\x10capture_metadata\x18\x02 \x01(\x0b2!.viam.app.data.v1.CaptureMetadataR\x0fcaptureMetadata\x12A\n\x0etime_requested\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived\x12\x1b\n\tfile_name\x18\x05 \x01(\tR\x08fileName\x12\x19\n\x08file_ext\x18\x06 \x01(\tR\x07fileExt\x12\x10\n\x03uri\x18\x07 \x01(\tR\x03uri\x12?\n\x0bannotations\x18\x08 \x01(\x0b2\x1d.viam.app.data.v1.AnnotationsR\x0bannotations"T\n DeleteTabularDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter"z\n!DeleteTabularDataByFilterResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCount\x120\n\x06result\x18\x02 \x01(\x0b2\x18.viam.app.data.v1.ResultR\x06result"S\n\x1fDeleteBinaryDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter"y\n DeleteBinaryDataByFilterResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCount\x120\n\x06result\x18\x02 \x01(\x0b2\x18.viam.app.data.v1.ResultR\x06result"9\n\x1cDeleteBinaryDataByIDsRequest\x12\x19\n\x08file_ids\x18\x01 \x03(\tR\x07fileIds"v\n\x1dDeleteBinaryDataByIDsResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCount\x120\n\x06result\x18\x02 \x01(\x0b2\x18.viam.app.data.v1.ResultR\x06result"T\n#AddTagsToBinaryDataByFileIDsRequest\x12\x19\n\x08file_ids\x18\x01 \x03(\tR\x07fileIds\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"&\n$AddTagsToBinaryDataByFileIDsResponse"j\n"AddTagsToBinaryDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"%\n#AddTagsToBinaryDataByFilterResponse"Y\n(RemoveTagsFromBinaryDataByFileIDsRequest\x12\x19\n\x08file_ids\x18\x01 \x03(\tR\x07fileIds\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"P\n)RemoveTagsFromBinaryDataByFileIDsResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCount"o\n\'RemoveTagsFromBinaryDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"O\n(RemoveTagsFromBinaryDataByFilterResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCount"G\n\x13TagsByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter"*\n\x14TagsByFilterResponse\x12\x12\n\x04tags\x18\x01 \x03(\tR\x04tags"\xf9\x01\n AddBoundingBoxToImageByIDRequest\x12\x17\n\x07file_id\x18\x01 \x01(\tR\x06fileId\x12\x14\n\x05label\x18\x02 \x01(\tR\x05label\x12(\n\x10x_min_normalized\x18\x03 \x01(\x01R\x0exMinNormalized\x12(\n\x10y_min_normalized\x18\x04 \x01(\x01R\x0eyMinNormalized\x12(\n\x10x_max_normalized\x18\x05 \x01(\x01R\x0exMaxNormalized\x12(\n\x10y_max_normalized\x18\x06 \x01(\x01R\x0eyMaxNormalized"<\n!AddBoundingBoxToImageByIDResponse\x12\x17\n\x07bbox_id\x18\x01 \x01(\tR\x06bboxId"Y\n%RemoveBoundingBoxFromImageByIDRequest\x12\x17\n\x07file_id\x18\x01 \x01(\tR\x06fileId\x12\x17\n\x07bbox_id\x18\x02 \x01(\tR\x06bboxId"(\n&RemoveBoundingBoxFromImageByIDResponse"T\n BoundingBoxLabelsByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter";\n!BoundingBoxLabelsByFilterResponse\x12\x16\n\x06labels\x18\x01 \x03(\tR\x06labels*I\n\x05Order\x12\x15\n\x11ORDER_UNSPECIFIED\x10\x00\x12\x14\n\x10ORDER_DESCENDING\x10\x01\x12\x13\n\x0fORDER_ASCENDING\x10\x02*P\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x1a\n\x16STATUS_PARTIAL_SUCCESS\x10\x01\x12\x12\n\x0eSTATUS_SUCCESS\x10\x02*\x90\x01\n\x0eTagsFilterType\x12 \n\x1cTAGS_FILTER_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1cTAGS_FILTER_TYPE_MATCH_BY_OR\x10\x01\x12\x1b\n\x17TAGS_FILTER_TYPE_TAGGED\x10\x02\x12\x1d\n\x19TAGS_FILTER_TYPE_UNTAGGED\x10\x032\xba\x0e\n\x0bDataService\x12r\n\x13TabularDataByFilter\x12,.viam.app.data.v1.TabularDataByFilterRequest\x1a-.viam.app.data.v1.TabularDataByFilterResponse\x12o\n\x12BinaryDataByFilter\x12+.viam.app.data.v1.BinaryDataByFilterRequest\x1a,.viam.app.data.v1.BinaryDataByFilterResponse\x12f\n\x0fBinaryDataByIDs\x12(.viam.app.data.v1.BinaryDataByIDsRequest\x1a).viam.app.data.v1.BinaryDataByIDsResponse\x12\x84\x01\n\x19DeleteTabularDataByFilter\x122.viam.app.data.v1.DeleteTabularDataByFilterRequest\x1a3.viam.app.data.v1.DeleteTabularDataByFilterResponse\x12\x81\x01\n\x18DeleteBinaryDataByFilter\x121.viam.app.data.v1.DeleteBinaryDataByFilterRequest\x1a2.viam.app.data.v1.DeleteBinaryDataByFilterResponse\x12x\n\x15DeleteBinaryDataByIDs\x12..viam.app.data.v1.DeleteBinaryDataByIDsRequest\x1a/.viam.app.data.v1.DeleteBinaryDataByIDsResponse\x12\x8d\x01\n\x1cAddTagsToBinaryDataByFileIDs\x125.viam.app.data.v1.AddTagsToBinaryDataByFileIDsRequest\x1a6.viam.app.data.v1.AddTagsToBinaryDataByFileIDsResponse\x12\x8a\x01\n\x1bAddTagsToBinaryDataByFilter\x124.viam.app.data.v1.AddTagsToBinaryDataByFilterRequest\x1a5.viam.app.data.v1.AddTagsToBinaryDataByFilterResponse\x12\x9c\x01\n!RemoveTagsFromBinaryDataByFileIDs\x12:.viam.app.data.v1.RemoveTagsFromBinaryDataByFileIDsRequest\x1a;.viam.app.data.v1.RemoveTagsFromBinaryDataByFileIDsResponse\x12\x99\x01\n RemoveTagsFromBinaryDataByFilter\x129.viam.app.data.v1.RemoveTagsFromBinaryDataByFilterRequest\x1a:.viam.app.data.v1.RemoveTagsFromBinaryDataByFilterResponse\x12]\n\x0cTagsByFilter\x12%.viam.app.data.v1.TagsByFilterRequest\x1a&.viam.app.data.v1.TagsByFilterResponse\x12\x84\x01\n\x19AddBoundingBoxToImageByID\x122.viam.app.data.v1.AddBoundingBoxToImageByIDRequest\x1a3.viam.app.data.v1.AddBoundingBoxToImageByIDResponse\x12\x93\x01\n\x1eRemoveBoundingBoxFromImageByID\x127.viam.app.data.v1.RemoveBoundingBoxFromImageByIDRequest\x1a8.viam.app.data.v1.RemoveBoundingBoxFromImageByIDResponse\x12\x84\x01\n\x19BoundingBoxLabelsByFilter\x122.viam.app.data.v1.BoundingBoxLabelsByFilterRequest\x1a3.viam.app.data.v1.BoundingBoxLabelsByFilterResponseB\x1dZ\x1bgo.viam.com/api/app/data/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.data.v1.data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1bgo.viam.com/api/app/data/v1'
    _FILTER.fields_by_name['tags']._options = None
    _FILTER.fields_by_name['tags']._serialized_options = b'\x18\x01'
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._options = None
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_options = b'8\x01'
    _ORDER._serialized_start = 5499
    _ORDER._serialized_end = 5572
    _STATUS._serialized_start = 5574
    _STATUS._serialized_end = 5654
    _TAGSFILTERTYPE._serialized_start = 5657
    _TAGSFILTERTYPE._serialized_end = 5801
    _RESULT._serialized_start = 134
    _RESULT._serialized_end = 218
    _DATAREQUEST._serialized_start = 221
    _DATAREQUEST._serialized_end = 382
    _FILTER._serialized_start = 385
    _FILTER._serialized_end = 920
    _TAGSFILTER._serialized_start = 922
    _TAGSFILTER._serialized_end = 1008
    _CAPTUREMETADATA._serialized_start = 1011
    _CAPTUREMETADATA._serialized_end = 1590
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_start = 1501
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_end = 1590
    _CAPTUREINTERVAL._serialized_start = 1592
    _CAPTUREINTERVAL._serialized_end = 1705
    _TABULARDATABYFILTERREQUEST._serialized_start = 1707
    _TABULARDATABYFILTERREQUEST._serialized_end = 1832
    _TABULARDATABYFILTERRESPONSE._serialized_start = 1835
    _TABULARDATABYFILTERRESPONSE._serialized_end = 2062
    _TABULARDATA._serialized_start = 2065
    _TABULARDATA._serialized_end = 2294
    _BINARYDATA._serialized_start = 2296
    _BINARYDATA._serialized_end = 2394
    _BINARYDATABYFILTERREQUEST._serialized_start = 2397
    _BINARYDATABYFILTERREQUEST._serialized_end = 2560
    _BINARYDATABYFILTERRESPONSE._serialized_start = 2562
    _BINARYDATABYFILTERRESPONSE._serialized_end = 2682
    _BINARYDATABYIDSREQUEST._serialized_start = 2684
    _BINARYDATABYIDSREQUEST._serialized_end = 2774
    _BINARYDATABYIDSRESPONSE._serialized_start = 2776
    _BINARYDATABYIDSRESPONSE._serialized_end = 2873
    _BOUNDINGBOX._serialized_start = 2876
    _BOUNDINGBOX._serialized_end = 3095
    _ANNOTATIONS._serialized_start = 3097
    _ANNOTATIONS._serialized_end = 3165
    _BINARYMETADATA._serialized_start = 3168
    _BINARYMETADATA._serialized_end = 3549
    _DELETETABULARDATABYFILTERREQUEST._serialized_start = 3551
    _DELETETABULARDATABYFILTERREQUEST._serialized_end = 3635
    _DELETETABULARDATABYFILTERRESPONSE._serialized_start = 3637
    _DELETETABULARDATABYFILTERRESPONSE._serialized_end = 3759
    _DELETEBINARYDATABYFILTERREQUEST._serialized_start = 3761
    _DELETEBINARYDATABYFILTERREQUEST._serialized_end = 3844
    _DELETEBINARYDATABYFILTERRESPONSE._serialized_start = 3846
    _DELETEBINARYDATABYFILTERRESPONSE._serialized_end = 3967
    _DELETEBINARYDATABYIDSREQUEST._serialized_start = 3969
    _DELETEBINARYDATABYIDSREQUEST._serialized_end = 4026
    _DELETEBINARYDATABYIDSRESPONSE._serialized_start = 4028
    _DELETEBINARYDATABYIDSRESPONSE._serialized_end = 4146
    _ADDTAGSTOBINARYDATABYFILEIDSREQUEST._serialized_start = 4148
    _ADDTAGSTOBINARYDATABYFILEIDSREQUEST._serialized_end = 4232
    _ADDTAGSTOBINARYDATABYFILEIDSRESPONSE._serialized_start = 4234
    _ADDTAGSTOBINARYDATABYFILEIDSRESPONSE._serialized_end = 4272
    _ADDTAGSTOBINARYDATABYFILTERREQUEST._serialized_start = 4274
    _ADDTAGSTOBINARYDATABYFILTERREQUEST._serialized_end = 4380
    _ADDTAGSTOBINARYDATABYFILTERRESPONSE._serialized_start = 4382
    _ADDTAGSTOBINARYDATABYFILTERRESPONSE._serialized_end = 4419
    _REMOVETAGSFROMBINARYDATABYFILEIDSREQUEST._serialized_start = 4421
    _REMOVETAGSFROMBINARYDATABYFILEIDSREQUEST._serialized_end = 4510
    _REMOVETAGSFROMBINARYDATABYFILEIDSRESPONSE._serialized_start = 4512
    _REMOVETAGSFROMBINARYDATABYFILEIDSRESPONSE._serialized_end = 4592
    _REMOVETAGSFROMBINARYDATABYFILTERREQUEST._serialized_start = 4594
    _REMOVETAGSFROMBINARYDATABYFILTERREQUEST._serialized_end = 4705
    _REMOVETAGSFROMBINARYDATABYFILTERRESPONSE._serialized_start = 4707
    _REMOVETAGSFROMBINARYDATABYFILTERRESPONSE._serialized_end = 4786
    _TAGSBYFILTERREQUEST._serialized_start = 4788
    _TAGSBYFILTERREQUEST._serialized_end = 4859
    _TAGSBYFILTERRESPONSE._serialized_start = 4861
    _TAGSBYFILTERRESPONSE._serialized_end = 4903
    _ADDBOUNDINGBOXTOIMAGEBYIDREQUEST._serialized_start = 4906
    _ADDBOUNDINGBOXTOIMAGEBYIDREQUEST._serialized_end = 5155
    _ADDBOUNDINGBOXTOIMAGEBYIDRESPONSE._serialized_start = 5157
    _ADDBOUNDINGBOXTOIMAGEBYIDRESPONSE._serialized_end = 5217
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDREQUEST._serialized_start = 5219
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDREQUEST._serialized_end = 5308
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDRESPONSE._serialized_start = 5310
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDRESPONSE._serialized_end = 5350
    _BOUNDINGBOXLABELSBYFILTERREQUEST._serialized_start = 5352
    _BOUNDINGBOXLABELSBYFILTERREQUEST._serialized_end = 5436
    _BOUNDINGBOXLABELSBYFILTERRESPONSE._serialized_start = 5438
    _BOUNDINGBOXLABELSBYFILTERRESPONSE._serialized_end = 5497
    _DATASERVICE._serialized_start = 5804
    _DATASERVICE._serialized_end = 7654