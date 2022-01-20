# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/firestore/v1/firestore.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.firestore.v1 import common_pb2 as google_dot_firestore_dot_v1_dot_common__pb2
from google.firestore.v1 import document_pb2 as google_dot_firestore_dot_v1_dot_document__pb2
from google.firestore.v1 import query_pb2 as google_dot_firestore_dot_v1_dot_query__pb2
from google.firestore.v1 import write_pb2 as google_dot_firestore_dot_v1_dot_write__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/firestore/v1/firestore.proto\x12\x13google.firestore.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a google/firestore/v1/common.proto\x1a\"google/firestore/v1/document.proto\x1a\x1fgoogle/firestore/v1/query.proto\x1a\x1fgoogle/firestore/v1/write.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\xdc\x01\n\x12GetDocumentRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12\x35\n\x04mask\x18\x02 \x01(\x0b\x32!.google.firestore.v1.DocumentMaskR\x04mask\x12\"\n\x0btransaction\x18\x03 \x01(\x0cH\x00R\x0btransaction\x12\x39\n\tread_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\x08readTimeB\x16\n\x14\x63onsistency_selector\"\x87\x03\n\x14ListDocumentsRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12)\n\rcollection_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0c\x63ollectionId\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x19\n\x08order_by\x18\x06 \x01(\tR\x07orderBy\x12\x35\n\x04mask\x18\x07 \x01(\x0b\x32!.google.firestore.v1.DocumentMaskR\x04mask\x12\"\n\x0btransaction\x18\x08 \x01(\x0cH\x00R\x0btransaction\x12\x39\n\tread_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\x08readTime\x12!\n\x0cshow_missing\x18\x0c \x01(\x08R\x0bshowMissingB\x16\n\x14\x63onsistency_selector\"|\n\x15ListDocumentsResponse\x12;\n\tdocuments\x18\x01 \x03(\x0b\x32\x1d.google.firestore.v1.DocumentR\tdocuments\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xf9\x01\n\x15\x43reateDocumentRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12)\n\rcollection_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0c\x63ollectionId\x12\x1f\n\x0b\x64ocument_id\x18\x03 \x01(\tR\ndocumentId\x12?\n\x08\x64ocument\x18\x04 \x01(\x0b\x32\x1d.google.firestore.v1.DocumentB\x04\xe2\x41\x01\x02R\x08\x64ocument\x12\x35\n\x04mask\x18\x05 \x01(\x0b\x32!.google.firestore.v1.DocumentMaskR\x04mask\"\xa1\x02\n\x15UpdateDocumentRequest\x12?\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\x1d.google.firestore.v1.DocumentB\x04\xe2\x41\x01\x02R\x08\x64ocument\x12\x42\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32!.google.firestore.v1.DocumentMaskR\nupdateMask\x12\x35\n\x04mask\x18\x03 \x01(\x0b\x32!.google.firestore.v1.DocumentMaskR\x04mask\x12L\n\x10\x63urrent_document\x18\x04 \x01(\x0b\x32!.google.firestore.v1.PreconditionR\x0f\x63urrentDocument\"\x7f\n\x15\x44\x65leteDocumentRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12L\n\x10\x63urrent_document\x18\x02 \x01(\x0b\x32!.google.firestore.v1.PreconditionR\x0f\x63urrentDocument\"\xdc\x02\n\x18\x42\x61tchGetDocumentsRequest\x12 \n\x08\x64\x61tabase\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x64\x61tabase\x12\x1c\n\tdocuments\x18\x02 \x03(\tR\tdocuments\x12\x35\n\x04mask\x18\x03 \x01(\x0b\x32!.google.firestore.v1.DocumentMaskR\x04mask\x12\"\n\x0btransaction\x18\x04 \x01(\x0cH\x00R\x0btransaction\x12R\n\x0fnew_transaction\x18\x05 \x01(\x0b\x32\'.google.firestore.v1.TransactionOptionsH\x00R\x0enewTransaction\x12\x39\n\tread_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\x08readTimeB\x16\n\x14\x63onsistency_selector\"\xd3\x01\n\x19\x42\x61tchGetDocumentsResponse\x12\x35\n\x05\x66ound\x18\x01 \x01(\x0b\x32\x1d.google.firestore.v1.DocumentH\x00R\x05\x66ound\x12\x1a\n\x07missing\x18\x02 \x01(\tH\x00R\x07missing\x12 \n\x0btransaction\x18\x03 \x01(\x0cR\x0btransaction\x12\x37\n\tread_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08readTimeB\x08\n\x06result\"~\n\x17\x42\x65ginTransactionRequest\x12 \n\x08\x64\x61tabase\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x64\x61tabase\x12\x41\n\x07options\x18\x02 \x01(\x0b\x32\'.google.firestore.v1.TransactionOptionsR\x07options\"<\n\x18\x42\x65ginTransactionResponse\x12 \n\x0btransaction\x18\x01 \x01(\x0cR\x0btransaction\"\x87\x01\n\rCommitRequest\x12 \n\x08\x64\x61tabase\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x64\x61tabase\x12\x32\n\x06writes\x18\x02 \x03(\x0b\x32\x1a.google.firestore.v1.WriteR\x06writes\x12 \n\x0btransaction\x18\x03 \x01(\x0cR\x0btransaction\"\x94\x01\n\x0e\x43ommitResponse\x12\x45\n\rwrite_results\x18\x01 \x03(\x0b\x32 .google.firestore.v1.WriteResultR\x0cwriteResults\x12;\n\x0b\x63ommit_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncommitTime\"[\n\x0fRollbackRequest\x12 \n\x08\x64\x61tabase\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x64\x61tabase\x12&\n\x0btransaction\x18\x02 \x01(\x0c\x42\x04\xe2\x41\x01\x02R\x0btransaction\"\xdb\x02\n\x0fRunQueryRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12Q\n\x10structured_query\x18\x02 \x01(\x0b\x32$.google.firestore.v1.StructuredQueryH\x00R\x0fstructuredQuery\x12\"\n\x0btransaction\x18\x05 \x01(\x0cH\x01R\x0btransaction\x12R\n\x0fnew_transaction\x18\x06 \x01(\x0b\x32\'.google.firestore.v1.TransactionOptionsH\x01R\x0enewTransaction\x12\x39\n\tread_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01R\x08readTimeB\x0c\n\nquery_typeB\x16\n\x14\x63onsistency_selector\"\xd1\x01\n\x10RunQueryResponse\x12 \n\x0btransaction\x18\x02 \x01(\x0cR\x0btransaction\x12\x39\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\x1d.google.firestore.v1.DocumentR\x08\x64ocument\x12\x37\n\tread_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08readTime\x12\'\n\x0fskipped_results\x18\x04 \x01(\x05R\x0eskippedResults\"\xfb\x01\n\x15PartitionQueryRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12Q\n\x10structured_query\x18\x02 \x01(\x0b\x32$.google.firestore.v1.StructuredQueryH\x00R\x0fstructuredQuery\x12\'\n\x0fpartition_count\x18\x03 \x01(\x03R\x0epartitionCount\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x05 \x01(\x05R\x08pageSizeB\x0c\n\nquery_type\"}\n\x16PartitionQueryResponse\x12;\n\npartitions\x18\x01 \x03(\x0b\x32\x1b.google.firestore.v1.CursorR\npartitions\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xa6\x02\n\x0cWriteRequest\x12 \n\x08\x64\x61tabase\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x64\x61tabase\x12\x1b\n\tstream_id\x18\x02 \x01(\tR\x08streamId\x12\x32\n\x06writes\x18\x03 \x03(\x0b\x32\x1a.google.firestore.v1.WriteR\x06writes\x12!\n\x0cstream_token\x18\x04 \x01(\x0cR\x0bstreamToken\x12\x45\n\x06labels\x18\x05 \x03(\x0b\x32-.google.firestore.v1.WriteRequest.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xd3\x01\n\rWriteResponse\x12\x1b\n\tstream_id\x18\x01 \x01(\tR\x08streamId\x12!\n\x0cstream_token\x18\x02 \x01(\x0cR\x0bstreamToken\x12\x45\n\rwrite_results\x18\x03 \x03(\x0b\x32 .google.firestore.v1.WriteResultR\x0cwriteResults\x12;\n\x0b\x63ommit_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncommitTime\"\xaa\x02\n\rListenRequest\x12 \n\x08\x64\x61tabase\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x64\x61tabase\x12<\n\nadd_target\x18\x02 \x01(\x0b\x32\x1b.google.firestore.v1.TargetH\x00R\taddTarget\x12%\n\rremove_target\x18\x03 \x01(\x05H\x00R\x0cremoveTarget\x12\x46\n\x06labels\x18\x04 \x03(\x0b\x32..google.firestore.v1.ListenRequest.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x0f\n\rtarget_change\"\x9b\x03\n\x0eListenResponse\x12H\n\rtarget_change\x18\x02 \x01(\x0b\x32!.google.firestore.v1.TargetChangeH\x00R\x0ctargetChange\x12N\n\x0f\x64ocument_change\x18\x03 \x01(\x0b\x32#.google.firestore.v1.DocumentChangeH\x00R\x0e\x64ocumentChange\x12N\n\x0f\x64ocument_delete\x18\x04 \x01(\x0b\x32#.google.firestore.v1.DocumentDeleteH\x00R\x0e\x64ocumentDelete\x12N\n\x0f\x64ocument_remove\x18\x06 \x01(\x0b\x32#.google.firestore.v1.DocumentRemoveH\x00R\x0e\x64ocumentRemove\x12>\n\x06\x66ilter\x18\x05 \x01(\x0b\x32$.google.firestore.v1.ExistenceFilterH\x00R\x06\x66ilterB\x0f\n\rresponse_type\"\xff\x03\n\x06Target\x12?\n\x05query\x18\x02 \x01(\x0b\x32\'.google.firestore.v1.Target.QueryTargetH\x00R\x05query\x12K\n\tdocuments\x18\x03 \x01(\x0b\x32+.google.firestore.v1.Target.DocumentsTargetH\x00R\tdocuments\x12#\n\x0cresume_token\x18\x04 \x01(\x0cH\x01R\x0bresumeToken\x12\x39\n\tread_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01R\x08readTime\x12\x1b\n\ttarget_id\x18\x05 \x01(\x05R\x08targetId\x12\x12\n\x04once\x18\x06 \x01(\x08R\x04once\x1a/\n\x0f\x44ocumentsTarget\x12\x1c\n\tdocuments\x18\x02 \x03(\tR\tdocuments\x1a\x86\x01\n\x0bQueryTarget\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12Q\n\x10structured_query\x18\x02 \x01(\x0b\x32$.google.firestore.v1.StructuredQueryH\x00R\x0fstructuredQueryB\x0c\n\nquery_typeB\r\n\x0btarget_typeB\r\n\x0bresume_type\"\xe5\x02\n\x0cTargetChange\x12`\n\x12target_change_type\x18\x01 \x01(\x0e\x32\x32.google.firestore.v1.TargetChange.TargetChangeTypeR\x10targetChangeType\x12\x1d\n\ntarget_ids\x18\x02 \x03(\x05R\ttargetIds\x12(\n\x05\x63\x61use\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x05\x63\x61use\x12!\n\x0cresume_token\x18\x04 \x01(\x0cR\x0bresumeToken\x12\x37\n\tread_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08readTime\"N\n\x10TargetChangeType\x12\r\n\tNO_CHANGE\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\x12\x0b\n\x07\x43URRENT\x10\x03\x12\t\n\x05RESET\x10\x04\"t\n\x18ListCollectionIdsRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"j\n\x19ListCollectionIdsResponse\x12%\n\x0e\x63ollection_ids\x18\x01 \x03(\tR\rcollectionIds\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xf0\x01\n\x11\x42\x61tchWriteRequest\x12 \n\x08\x64\x61tabase\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x64\x61tabase\x12\x32\n\x06writes\x18\x02 \x03(\x0b\x32\x1a.google.firestore.v1.WriteR\x06writes\x12J\n\x06labels\x18\x03 \x03(\x0b\x32\x32.google.firestore.v1.BatchWriteRequest.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x87\x01\n\x12\x42\x61tchWriteResponse\x12\x45\n\rwrite_results\x18\x01 \x03(\x0b\x32 .google.firestore.v1.WriteResultR\x0cwriteResults\x12*\n\x06status\x18\x02 \x03(\x0b\x32\x12.google.rpc.StatusR\x06status2\xfd\x16\n\tFirestore\x12\x8f\x01\n\x0bGetDocument\x12\'.google.firestore.v1.GetDocumentRequest\x1a\x1d.google.firestore.v1.Document\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/v1/{name=projects/*/databases/*/documents/*/**}\x12\xb2\x01\n\rListDocuments\x12).google.firestore.v1.ListDocumentsRequest\x1a*.google.firestore.v1.ListDocumentsResponse\"J\x82\xd3\xe4\x93\x02\x44\x12\x42/v1/{parent=projects/*/databases/*/documents/*/**}/{collection_id}\x12\xbf\x01\n\x0eUpdateDocument\x12*.google.firestore.v1.UpdateDocumentRequest\x1a\x1d.google.firestore.v1.Document\"b\xda\x41\x14\x64ocument,update_mask\x82\xd3\xe4\x93\x02\x45\x32\x39/v1/{document.name=projects/*/databases/*/documents/*/**}:\x08\x64ocument\x12\x95\x01\n\x0e\x44\x65leteDocument\x12*.google.firestore.v1.DeleteDocumentRequest\x1a\x16.google.protobuf.Empty\"?\xda\x41\x04name\x82\xd3\xe4\x93\x02\x32*0/v1/{name=projects/*/databases/*/documents/*/**}\x12\xb9\x01\n\x11\x42\x61tchGetDocuments\x12-.google.firestore.v1.BatchGetDocumentsRequest\x1a..google.firestore.v1.BatchGetDocumentsResponse\"C\x82\xd3\xe4\x93\x02=\"8/v1/{database=projects/*/databases/*}/documents:batchGet:\x01*0\x01\x12\xc7\x01\n\x10\x42\x65ginTransaction\x12,.google.firestore.v1.BeginTransactionRequest\x1a-.google.firestore.v1.BeginTransactionResponse\"V\xda\x41\x08\x64\x61tabase\x82\xd3\xe4\x93\x02\x45\"@/v1/{database=projects/*/databases/*}/documents:beginTransaction:\x01*\x12\xa6\x01\n\x06\x43ommit\x12\".google.firestore.v1.CommitRequest\x1a#.google.firestore.v1.CommitResponse\"S\xda\x41\x0f\x64\x61tabase,writes\x82\xd3\xe4\x93\x02;\"6/v1/{database=projects/*/databases/*}/documents:commit:\x01*\x12\xa4\x01\n\x08Rollback\x12$.google.firestore.v1.RollbackRequest\x1a\x16.google.protobuf.Empty\"Z\xda\x41\x14\x64\x61tabase,transaction\x82\xd3\xe4\x93\x02=\"8/v1/{database=projects/*/databases/*}/documents:rollback:\x01*\x12\xdf\x01\n\x08RunQuery\x12$.google.firestore.v1.RunQueryRequest\x1a%.google.firestore.v1.RunQueryResponse\"\x83\x01\x82\xd3\xe4\x93\x02}\"6/v1/{parent=projects/*/databases/*/documents}:runQuery:\x01*Z@\";/v1/{parent=projects/*/databases/*/documents/*/**}:runQuery:\x01*0\x01\x12\xfc\x01\n\x0ePartitionQuery\x12*.google.firestore.v1.PartitionQueryRequest\x1a+.google.firestore.v1.PartitionQueryResponse\"\x90\x01\x82\xd3\xe4\x93\x02\x89\x01\"</v1/{parent=projects/*/databases/*/documents}:partitionQuery:\x01*ZF\"A/v1/{parent=projects/*/databases/*/documents/*/**}:partitionQuery:\x01*\x12\x94\x01\n\x05Write\x12!.google.firestore.v1.WriteRequest\x1a\".google.firestore.v1.WriteResponse\"@\x82\xd3\xe4\x93\x02:\"5/v1/{database=projects/*/databases/*}/documents:write:\x01*(\x01\x30\x01\x12\x98\x01\n\x06Listen\x12\".google.firestore.v1.ListenRequest\x1a#.google.firestore.v1.ListenResponse\"A\x82\xd3\xe4\x93\x02;\"6/v1/{database=projects/*/databases/*}/documents:listen:\x01*(\x01\x30\x01\x12\x94\x02\n\x11ListCollectionIds\x12-.google.firestore.v1.ListCollectionIdsRequest\x1a..google.firestore.v1.ListCollectionIdsResponse\"\x9f\x01\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x8f\x01\"?/v1/{parent=projects/*/databases/*/documents}:listCollectionIds:\x01*ZI\"D/v1/{parent=projects/*/databases/*/documents/*/**}:listCollectionIds:\x01*\x12\xa4\x01\n\nBatchWrite\x12&.google.firestore.v1.BatchWriteRequest\x1a\'.google.firestore.v1.BatchWriteResponse\"E\x82\xd3\xe4\x93\x02?\":/v1/{database=projects/*/databases/*}/documents:batchWrite:\x01*\x12\xaf\x01\n\x0e\x43reateDocument\x12*.google.firestore.v1.CreateDocumentRequest\x1a\x1d.google.firestore.v1.Document\"R\x82\xd3\xe4\x93\x02L\"@/v1/{parent=projects/*/databases/*/documents/**}/{collection_id}:\x08\x64ocument\x1av\xca\x41\x18\x66irestore.googleapis.com\xd2\x41Xhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastoreB\xc7\x01\n\x17\x63om.google.firestore.v1B\x0e\x46irestoreProtoP\x01Z<google.golang.org/genproto/googleapis/firestore/v1;firestore\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1b\x06proto3')



_GETDOCUMENTREQUEST = DESCRIPTOR.message_types_by_name['GetDocumentRequest']
_LISTDOCUMENTSREQUEST = DESCRIPTOR.message_types_by_name['ListDocumentsRequest']
_LISTDOCUMENTSRESPONSE = DESCRIPTOR.message_types_by_name['ListDocumentsResponse']
_CREATEDOCUMENTREQUEST = DESCRIPTOR.message_types_by_name['CreateDocumentRequest']
_UPDATEDOCUMENTREQUEST = DESCRIPTOR.message_types_by_name['UpdateDocumentRequest']
_DELETEDOCUMENTREQUEST = DESCRIPTOR.message_types_by_name['DeleteDocumentRequest']
_BATCHGETDOCUMENTSREQUEST = DESCRIPTOR.message_types_by_name['BatchGetDocumentsRequest']
_BATCHGETDOCUMENTSRESPONSE = DESCRIPTOR.message_types_by_name['BatchGetDocumentsResponse']
_BEGINTRANSACTIONREQUEST = DESCRIPTOR.message_types_by_name['BeginTransactionRequest']
_BEGINTRANSACTIONRESPONSE = DESCRIPTOR.message_types_by_name['BeginTransactionResponse']
_COMMITREQUEST = DESCRIPTOR.message_types_by_name['CommitRequest']
_COMMITRESPONSE = DESCRIPTOR.message_types_by_name['CommitResponse']
_ROLLBACKREQUEST = DESCRIPTOR.message_types_by_name['RollbackRequest']
_RUNQUERYREQUEST = DESCRIPTOR.message_types_by_name['RunQueryRequest']
_RUNQUERYRESPONSE = DESCRIPTOR.message_types_by_name['RunQueryResponse']
_PARTITIONQUERYREQUEST = DESCRIPTOR.message_types_by_name['PartitionQueryRequest']
_PARTITIONQUERYRESPONSE = DESCRIPTOR.message_types_by_name['PartitionQueryResponse']
_WRITEREQUEST = DESCRIPTOR.message_types_by_name['WriteRequest']
_WRITEREQUEST_LABELSENTRY = _WRITEREQUEST.nested_types_by_name['LabelsEntry']
_WRITERESPONSE = DESCRIPTOR.message_types_by_name['WriteResponse']
_LISTENREQUEST = DESCRIPTOR.message_types_by_name['ListenRequest']
_LISTENREQUEST_LABELSENTRY = _LISTENREQUEST.nested_types_by_name['LabelsEntry']
_LISTENRESPONSE = DESCRIPTOR.message_types_by_name['ListenResponse']
_TARGET = DESCRIPTOR.message_types_by_name['Target']
_TARGET_DOCUMENTSTARGET = _TARGET.nested_types_by_name['DocumentsTarget']
_TARGET_QUERYTARGET = _TARGET.nested_types_by_name['QueryTarget']
_TARGETCHANGE = DESCRIPTOR.message_types_by_name['TargetChange']
_LISTCOLLECTIONIDSREQUEST = DESCRIPTOR.message_types_by_name['ListCollectionIdsRequest']
_LISTCOLLECTIONIDSRESPONSE = DESCRIPTOR.message_types_by_name['ListCollectionIdsResponse']
_BATCHWRITEREQUEST = DESCRIPTOR.message_types_by_name['BatchWriteRequest']
_BATCHWRITEREQUEST_LABELSENTRY = _BATCHWRITEREQUEST.nested_types_by_name['LabelsEntry']
_BATCHWRITERESPONSE = DESCRIPTOR.message_types_by_name['BatchWriteResponse']
_TARGETCHANGE_TARGETCHANGETYPE = _TARGETCHANGE.enum_types_by_name['TargetChangeType']
GetDocumentRequest = _reflection.GeneratedProtocolMessageType('GetDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDOCUMENTREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.GetDocumentRequest)
  })
_sym_db.RegisterMessage(GetDocumentRequest)

ListDocumentsRequest = _reflection.GeneratedProtocolMessageType('ListDocumentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOCUMENTSREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.ListDocumentsRequest)
  })
_sym_db.RegisterMessage(ListDocumentsRequest)

ListDocumentsResponse = _reflection.GeneratedProtocolMessageType('ListDocumentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOCUMENTSRESPONSE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.ListDocumentsResponse)
  })
_sym_db.RegisterMessage(ListDocumentsResponse)

CreateDocumentRequest = _reflection.GeneratedProtocolMessageType('CreateDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDOCUMENTREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.CreateDocumentRequest)
  })
_sym_db.RegisterMessage(CreateDocumentRequest)

UpdateDocumentRequest = _reflection.GeneratedProtocolMessageType('UpdateDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDOCUMENTREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.UpdateDocumentRequest)
  })
_sym_db.RegisterMessage(UpdateDocumentRequest)

DeleteDocumentRequest = _reflection.GeneratedProtocolMessageType('DeleteDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDOCUMENTREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.DeleteDocumentRequest)
  })
_sym_db.RegisterMessage(DeleteDocumentRequest)

BatchGetDocumentsRequest = _reflection.GeneratedProtocolMessageType('BatchGetDocumentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHGETDOCUMENTSREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.BatchGetDocumentsRequest)
  })
_sym_db.RegisterMessage(BatchGetDocumentsRequest)

BatchGetDocumentsResponse = _reflection.GeneratedProtocolMessageType('BatchGetDocumentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHGETDOCUMENTSRESPONSE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.BatchGetDocumentsResponse)
  })
_sym_db.RegisterMessage(BatchGetDocumentsResponse)

BeginTransactionRequest = _reflection.GeneratedProtocolMessageType('BeginTransactionRequest', (_message.Message,), {
  'DESCRIPTOR' : _BEGINTRANSACTIONREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.BeginTransactionRequest)
  })
_sym_db.RegisterMessage(BeginTransactionRequest)

BeginTransactionResponse = _reflection.GeneratedProtocolMessageType('BeginTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _BEGINTRANSACTIONRESPONSE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.BeginTransactionResponse)
  })
_sym_db.RegisterMessage(BeginTransactionResponse)

CommitRequest = _reflection.GeneratedProtocolMessageType('CommitRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMITREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.CommitRequest)
  })
_sym_db.RegisterMessage(CommitRequest)

CommitResponse = _reflection.GeneratedProtocolMessageType('CommitResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMITRESPONSE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.CommitResponse)
  })
_sym_db.RegisterMessage(CommitResponse)

RollbackRequest = _reflection.GeneratedProtocolMessageType('RollbackRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLLBACKREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.RollbackRequest)
  })
_sym_db.RegisterMessage(RollbackRequest)

RunQueryRequest = _reflection.GeneratedProtocolMessageType('RunQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNQUERYREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.RunQueryRequest)
  })
_sym_db.RegisterMessage(RunQueryRequest)

RunQueryResponse = _reflection.GeneratedProtocolMessageType('RunQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNQUERYRESPONSE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.RunQueryResponse)
  })
_sym_db.RegisterMessage(RunQueryResponse)

PartitionQueryRequest = _reflection.GeneratedProtocolMessageType('PartitionQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _PARTITIONQUERYREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.PartitionQueryRequest)
  })
_sym_db.RegisterMessage(PartitionQueryRequest)

PartitionQueryResponse = _reflection.GeneratedProtocolMessageType('PartitionQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _PARTITIONQUERYRESPONSE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.PartitionQueryResponse)
  })
_sym_db.RegisterMessage(PartitionQueryResponse)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _WRITEREQUEST_LABELSENTRY,
    '__module__' : 'google.firestore.v1.firestore_pb2'
    # @@protoc_insertion_point(class_scope:google.firestore.v1.WriteRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)
_sym_db.RegisterMessage(WriteRequest.LabelsEntry)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESPONSE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.WriteResponse)
  })
_sym_db.RegisterMessage(WriteResponse)

ListenRequest = _reflection.GeneratedProtocolMessageType('ListenRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTENREQUEST_LABELSENTRY,
    '__module__' : 'google.firestore.v1.firestore_pb2'
    # @@protoc_insertion_point(class_scope:google.firestore.v1.ListenRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTENREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.ListenRequest)
  })
_sym_db.RegisterMessage(ListenRequest)
_sym_db.RegisterMessage(ListenRequest.LabelsEntry)

ListenResponse = _reflection.GeneratedProtocolMessageType('ListenResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTENRESPONSE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.ListenResponse)
  })
_sym_db.RegisterMessage(ListenResponse)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {

  'DocumentsTarget' : _reflection.GeneratedProtocolMessageType('DocumentsTarget', (_message.Message,), {
    'DESCRIPTOR' : _TARGET_DOCUMENTSTARGET,
    '__module__' : 'google.firestore.v1.firestore_pb2'
    # @@protoc_insertion_point(class_scope:google.firestore.v1.Target.DocumentsTarget)
    })
  ,

  'QueryTarget' : _reflection.GeneratedProtocolMessageType('QueryTarget', (_message.Message,), {
    'DESCRIPTOR' : _TARGET_QUERYTARGET,
    '__module__' : 'google.firestore.v1.firestore_pb2'
    # @@protoc_insertion_point(class_scope:google.firestore.v1.Target.QueryTarget)
    })
  ,
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.Target)
  })
_sym_db.RegisterMessage(Target)
_sym_db.RegisterMessage(Target.DocumentsTarget)
_sym_db.RegisterMessage(Target.QueryTarget)

TargetChange = _reflection.GeneratedProtocolMessageType('TargetChange', (_message.Message,), {
  'DESCRIPTOR' : _TARGETCHANGE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.TargetChange)
  })
_sym_db.RegisterMessage(TargetChange)

ListCollectionIdsRequest = _reflection.GeneratedProtocolMessageType('ListCollectionIdsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOLLECTIONIDSREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.ListCollectionIdsRequest)
  })
_sym_db.RegisterMessage(ListCollectionIdsRequest)

ListCollectionIdsResponse = _reflection.GeneratedProtocolMessageType('ListCollectionIdsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOLLECTIONIDSRESPONSE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.ListCollectionIdsResponse)
  })
_sym_db.RegisterMessage(ListCollectionIdsResponse)

BatchWriteRequest = _reflection.GeneratedProtocolMessageType('BatchWriteRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BATCHWRITEREQUEST_LABELSENTRY,
    '__module__' : 'google.firestore.v1.firestore_pb2'
    # @@protoc_insertion_point(class_scope:google.firestore.v1.BatchWriteRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _BATCHWRITEREQUEST,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.BatchWriteRequest)
  })
_sym_db.RegisterMessage(BatchWriteRequest)
_sym_db.RegisterMessage(BatchWriteRequest.LabelsEntry)

BatchWriteResponse = _reflection.GeneratedProtocolMessageType('BatchWriteResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHWRITERESPONSE,
  '__module__' : 'google.firestore.v1.firestore_pb2'
  # @@protoc_insertion_point(class_scope:google.firestore.v1.BatchWriteResponse)
  })
_sym_db.RegisterMessage(BatchWriteResponse)

_FIRESTORE = DESCRIPTOR.services_by_name['Firestore']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.google.firestore.v1B\016FirestoreProtoP\001Z<google.golang.org/genproto/googleapis/firestore/v1;firestore\242\002\004GCFS\252\002\031Google.Cloud.Firestore.V1\312\002\031Google\\Cloud\\Firestore\\V1\352\002\034Google::Cloud::Firestore::V1'
  _GETDOCUMENTREQUEST.fields_by_name['name']._options = None
  _GETDOCUMENTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _LISTDOCUMENTSREQUEST.fields_by_name['parent']._options = None
  _LISTDOCUMENTSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _LISTDOCUMENTSREQUEST.fields_by_name['collection_id']._options = None
  _LISTDOCUMENTSREQUEST.fields_by_name['collection_id']._serialized_options = b'\342A\001\002'
  _CREATEDOCUMENTREQUEST.fields_by_name['parent']._options = None
  _CREATEDOCUMENTREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _CREATEDOCUMENTREQUEST.fields_by_name['collection_id']._options = None
  _CREATEDOCUMENTREQUEST.fields_by_name['collection_id']._serialized_options = b'\342A\001\002'
  _CREATEDOCUMENTREQUEST.fields_by_name['document']._options = None
  _CREATEDOCUMENTREQUEST.fields_by_name['document']._serialized_options = b'\342A\001\002'
  _UPDATEDOCUMENTREQUEST.fields_by_name['document']._options = None
  _UPDATEDOCUMENTREQUEST.fields_by_name['document']._serialized_options = b'\342A\001\002'
  _DELETEDOCUMENTREQUEST.fields_by_name['name']._options = None
  _DELETEDOCUMENTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _BATCHGETDOCUMENTSREQUEST.fields_by_name['database']._options = None
  _BATCHGETDOCUMENTSREQUEST.fields_by_name['database']._serialized_options = b'\342A\001\002'
  _BEGINTRANSACTIONREQUEST.fields_by_name['database']._options = None
  _BEGINTRANSACTIONREQUEST.fields_by_name['database']._serialized_options = b'\342A\001\002'
  _COMMITREQUEST.fields_by_name['database']._options = None
  _COMMITREQUEST.fields_by_name['database']._serialized_options = b'\342A\001\002'
  _ROLLBACKREQUEST.fields_by_name['database']._options = None
  _ROLLBACKREQUEST.fields_by_name['database']._serialized_options = b'\342A\001\002'
  _ROLLBACKREQUEST.fields_by_name['transaction']._options = None
  _ROLLBACKREQUEST.fields_by_name['transaction']._serialized_options = b'\342A\001\002'
  _RUNQUERYREQUEST.fields_by_name['parent']._options = None
  _RUNQUERYREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _PARTITIONQUERYREQUEST.fields_by_name['parent']._options = None
  _PARTITIONQUERYREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _WRITEREQUEST_LABELSENTRY._options = None
  _WRITEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _WRITEREQUEST.fields_by_name['database']._options = None
  _WRITEREQUEST.fields_by_name['database']._serialized_options = b'\342A\001\002'
  _LISTENREQUEST_LABELSENTRY._options = None
  _LISTENREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _LISTENREQUEST.fields_by_name['database']._options = None
  _LISTENREQUEST.fields_by_name['database']._serialized_options = b'\342A\001\002'
  _LISTCOLLECTIONIDSREQUEST.fields_by_name['parent']._options = None
  _LISTCOLLECTIONIDSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _BATCHWRITEREQUEST_LABELSENTRY._options = None
  _BATCHWRITEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _BATCHWRITEREQUEST.fields_by_name['database']._options = None
  _BATCHWRITEREQUEST.fields_by_name['database']._serialized_options = b'\342A\001\002'
  _FIRESTORE._options = None
  _FIRESTORE._serialized_options = b'\312A\030firestore.googleapis.com\322AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastore'
  _FIRESTORE.methods_by_name['GetDocument']._options = None
  _FIRESTORE.methods_by_name['GetDocument']._serialized_options = b'\202\323\344\223\0022\0220/v1/{name=projects/*/databases/*/documents/*/**}'
  _FIRESTORE.methods_by_name['ListDocuments']._options = None
  _FIRESTORE.methods_by_name['ListDocuments']._serialized_options = b'\202\323\344\223\002D\022B/v1/{parent=projects/*/databases/*/documents/*/**}/{collection_id}'
  _FIRESTORE.methods_by_name['UpdateDocument']._options = None
  _FIRESTORE.methods_by_name['UpdateDocument']._serialized_options = b'\332A\024document,update_mask\202\323\344\223\002E29/v1/{document.name=projects/*/databases/*/documents/*/**}:\010document'
  _FIRESTORE.methods_by_name['DeleteDocument']._options = None
  _FIRESTORE.methods_by_name['DeleteDocument']._serialized_options = b'\332A\004name\202\323\344\223\0022*0/v1/{name=projects/*/databases/*/documents/*/**}'
  _FIRESTORE.methods_by_name['BatchGetDocuments']._options = None
  _FIRESTORE.methods_by_name['BatchGetDocuments']._serialized_options = b'\202\323\344\223\002=\"8/v1/{database=projects/*/databases/*}/documents:batchGet:\001*'
  _FIRESTORE.methods_by_name['BeginTransaction']._options = None
  _FIRESTORE.methods_by_name['BeginTransaction']._serialized_options = b'\332A\010database\202\323\344\223\002E\"@/v1/{database=projects/*/databases/*}/documents:beginTransaction:\001*'
  _FIRESTORE.methods_by_name['Commit']._options = None
  _FIRESTORE.methods_by_name['Commit']._serialized_options = b'\332A\017database,writes\202\323\344\223\002;\"6/v1/{database=projects/*/databases/*}/documents:commit:\001*'
  _FIRESTORE.methods_by_name['Rollback']._options = None
  _FIRESTORE.methods_by_name['Rollback']._serialized_options = b'\332A\024database,transaction\202\323\344\223\002=\"8/v1/{database=projects/*/databases/*}/documents:rollback:\001*'
  _FIRESTORE.methods_by_name['RunQuery']._options = None
  _FIRESTORE.methods_by_name['RunQuery']._serialized_options = b'\202\323\344\223\002}\"6/v1/{parent=projects/*/databases/*/documents}:runQuery:\001*Z@\";/v1/{parent=projects/*/databases/*/documents/*/**}:runQuery:\001*'
  _FIRESTORE.methods_by_name['PartitionQuery']._options = None
  _FIRESTORE.methods_by_name['PartitionQuery']._serialized_options = b'\202\323\344\223\002\211\001\"</v1/{parent=projects/*/databases/*/documents}:partitionQuery:\001*ZF\"A/v1/{parent=projects/*/databases/*/documents/*/**}:partitionQuery:\001*'
  _FIRESTORE.methods_by_name['Write']._options = None
  _FIRESTORE.methods_by_name['Write']._serialized_options = b'\202\323\344\223\002:\"5/v1/{database=projects/*/databases/*}/documents:write:\001*'
  _FIRESTORE.methods_by_name['Listen']._options = None
  _FIRESTORE.methods_by_name['Listen']._serialized_options = b'\202\323\344\223\002;\"6/v1/{database=projects/*/databases/*}/documents:listen:\001*'
  _FIRESTORE.methods_by_name['ListCollectionIds']._options = None
  _FIRESTORE.methods_by_name['ListCollectionIds']._serialized_options = b'\332A\006parent\202\323\344\223\002\217\001\"?/v1/{parent=projects/*/databases/*/documents}:listCollectionIds:\001*ZI\"D/v1/{parent=projects/*/databases/*/documents/*/**}:listCollectionIds:\001*'
  _FIRESTORE.methods_by_name['BatchWrite']._options = None
  _FIRESTORE.methods_by_name['BatchWrite']._serialized_options = b'\202\323\344\223\002?\":/v1/{database=projects/*/databases/*}/documents:batchWrite:\001*'
  _FIRESTORE.methods_by_name['CreateDocument']._options = None
  _FIRESTORE.methods_by_name['CreateDocument']._serialized_options = b'\202\323\344\223\002L\"@/v1/{parent=projects/*/databases/*/documents/**}/{collection_id}:\010document'
  _GETDOCUMENTREQUEST._serialized_start=372
  _GETDOCUMENTREQUEST._serialized_end=592
  _LISTDOCUMENTSREQUEST._serialized_start=595
  _LISTDOCUMENTSREQUEST._serialized_end=986
  _LISTDOCUMENTSRESPONSE._serialized_start=988
  _LISTDOCUMENTSRESPONSE._serialized_end=1112
  _CREATEDOCUMENTREQUEST._serialized_start=1115
  _CREATEDOCUMENTREQUEST._serialized_end=1364
  _UPDATEDOCUMENTREQUEST._serialized_start=1367
  _UPDATEDOCUMENTREQUEST._serialized_end=1656
  _DELETEDOCUMENTREQUEST._serialized_start=1658
  _DELETEDOCUMENTREQUEST._serialized_end=1785
  _BATCHGETDOCUMENTSREQUEST._serialized_start=1788
  _BATCHGETDOCUMENTSREQUEST._serialized_end=2136
  _BATCHGETDOCUMENTSRESPONSE._serialized_start=2139
  _BATCHGETDOCUMENTSRESPONSE._serialized_end=2350
  _BEGINTRANSACTIONREQUEST._serialized_start=2352
  _BEGINTRANSACTIONREQUEST._serialized_end=2478
  _BEGINTRANSACTIONRESPONSE._serialized_start=2480
  _BEGINTRANSACTIONRESPONSE._serialized_end=2540
  _COMMITREQUEST._serialized_start=2543
  _COMMITREQUEST._serialized_end=2678
  _COMMITRESPONSE._serialized_start=2681
  _COMMITRESPONSE._serialized_end=2829
  _ROLLBACKREQUEST._serialized_start=2831
  _ROLLBACKREQUEST._serialized_end=2922
  _RUNQUERYREQUEST._serialized_start=2925
  _RUNQUERYREQUEST._serialized_end=3272
  _RUNQUERYRESPONSE._serialized_start=3275
  _RUNQUERYRESPONSE._serialized_end=3484
  _PARTITIONQUERYREQUEST._serialized_start=3487
  _PARTITIONQUERYREQUEST._serialized_end=3738
  _PARTITIONQUERYRESPONSE._serialized_start=3740
  _PARTITIONQUERYRESPONSE._serialized_end=3865
  _WRITEREQUEST._serialized_start=3868
  _WRITEREQUEST._serialized_end=4162
  _WRITEREQUEST_LABELSENTRY._serialized_start=4105
  _WRITEREQUEST_LABELSENTRY._serialized_end=4162
  _WRITERESPONSE._serialized_start=4165
  _WRITERESPONSE._serialized_end=4376
  _LISTENREQUEST._serialized_start=4379
  _LISTENREQUEST._serialized_end=4677
  _LISTENREQUEST_LABELSENTRY._serialized_start=4105
  _LISTENREQUEST_LABELSENTRY._serialized_end=4162
  _LISTENRESPONSE._serialized_start=4680
  _LISTENRESPONSE._serialized_end=5091
  _TARGET._serialized_start=5094
  _TARGET._serialized_end=5605
  _TARGET_DOCUMENTSTARGET._serialized_start=5391
  _TARGET_DOCUMENTSTARGET._serialized_end=5438
  _TARGET_QUERYTARGET._serialized_start=5441
  _TARGET_QUERYTARGET._serialized_end=5575
  _TARGETCHANGE._serialized_start=5608
  _TARGETCHANGE._serialized_end=5965
  _TARGETCHANGE_TARGETCHANGETYPE._serialized_start=5887
  _TARGETCHANGE_TARGETCHANGETYPE._serialized_end=5965
  _LISTCOLLECTIONIDSREQUEST._serialized_start=5967
  _LISTCOLLECTIONIDSREQUEST._serialized_end=6083
  _LISTCOLLECTIONIDSRESPONSE._serialized_start=6085
  _LISTCOLLECTIONIDSRESPONSE._serialized_end=6191
  _BATCHWRITEREQUEST._serialized_start=6194
  _BATCHWRITEREQUEST._serialized_end=6434
  _BATCHWRITEREQUEST_LABELSENTRY._serialized_start=4105
  _BATCHWRITEREQUEST_LABELSENTRY._serialized_end=4162
  _BATCHWRITERESPONSE._serialized_start=6437
  _BATCHWRITERESPONSE._serialized_end=6572
  _FIRESTORE._serialized_start=6575
  _FIRESTORE._serialized_end=9516
# @@protoc_insertion_point(module_scope)
