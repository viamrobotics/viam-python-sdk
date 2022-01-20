# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/documentai/v1beta2/document.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.documentai.v1beta2 import geometry_pb2 as google_dot_cloud_dot_documentai_dot_v1beta2_dot_geometry__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.type import color_pb2 as google_dot_type_dot_color__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/documentai/v1beta2/document.proto\x12\x1fgoogle.cloud.documentai.v1beta2\x1a\x1fgoogle/api/field_behavior.proto\x1a.google/cloud/documentai/v1beta2/geometry.proto\x1a\x17google/rpc/status.proto\x1a\x17google/type/color.proto\x1a\x1cgoogle/api/annotations.proto\"\xfd\x33\n\x08\x44ocument\x12\x12\n\x03uri\x18\x01 \x01(\tH\x00R\x03uri\x12\x1a\n\x07\x63ontent\x18\x02 \x01(\x0cH\x00R\x07\x63ontent\x12\x1b\n\tmime_type\x18\x03 \x01(\tR\x08mimeType\x12\x12\n\x04text\x18\x04 \x01(\tR\x04text\x12P\n\x0btext_styles\x18\x05 \x03(\x0b\x32/.google.cloud.documentai.v1beta2.Document.StyleR\ntextStyles\x12\x44\n\x05pages\x18\x06 \x03(\x0b\x32..google.cloud.documentai.v1beta2.Document.PageR\x05pages\x12L\n\x08\x65ntities\x18\x07 \x03(\x0b\x32\x30.google.cloud.documentai.v1beta2.Document.EntityR\x08\x65ntities\x12\x63\n\x10\x65ntity_relations\x18\x08 \x03(\x0b\x32\x38.google.cloud.documentai.v1beta2.Document.EntityRelationR\x0f\x65ntityRelations\x12R\n\nshard_info\x18\t \x01(\x0b\x32\x33.google.cloud.documentai.v1beta2.Document.ShardInfoR\tshardInfo\x12G\n\x06labels\x18\x0b \x03(\x0b\x32/.google.cloud.documentai.v1beta2.Document.LabelR\x06labels\x12(\n\x05\x65rror\x18\n \x01(\x0b\x32\x12.google.rpc.StatusR\x05\x65rror\x1an\n\tShardInfo\x12\x1f\n\x0bshard_index\x18\x01 \x01(\x03R\nshardIndex\x12\x1f\n\x0bshard_count\x18\x02 \x01(\x03R\nshardCount\x12\x1f\n\x0btext_offset\x18\x03 \x01(\x03R\ntextOffset\x1aj\n\x05Label\x12#\n\x0c\x61utoml_model\x18\x02 \x01(\tH\x00R\x0b\x61utomlModel\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1e\n\nconfidence\x18\x03 \x01(\x02R\nconfidenceB\x08\n\x06source\x1a\xbb\x03\n\x05Style\x12U\n\x0btext_anchor\x18\x01 \x01(\x0b\x32\x34.google.cloud.documentai.v1beta2.Document.TextAnchorR\ntextAnchor\x12(\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x12.google.type.ColorR\x05\x63olor\x12=\n\x10\x62\x61\x63kground_color\x18\x03 \x01(\x0b\x32\x12.google.type.ColorR\x0f\x62\x61\x63kgroundColor\x12\x1f\n\x0b\x66ont_weight\x18\x04 \x01(\tR\nfontWeight\x12\x1d\n\ntext_style\x18\x05 \x01(\tR\ttextStyle\x12\'\n\x0ftext_decoration\x18\x06 \x01(\tR\x0etextDecoration\x12U\n\tfont_size\x18\x07 \x01(\x0b\x32\x38.google.cloud.documentai.v1beta2.Document.Style.FontSizeR\x08\x66ontSize\x1a\x32\n\x08\x46ontSize\x12\x12\n\x04size\x18\x01 \x01(\x02R\x04size\x12\x12\n\x04unit\x18\x02 \x01(\tR\x04unit\x1a\xb3 \n\x04Page\x12\x1f\n\x0bpage_number\x18\x01 \x01(\x05R\npageNumber\x12V\n\tdimension\x18\x02 \x01(\x0b\x32\x38.google.cloud.documentai.v1beta2.Document.Page.DimensionR\tdimension\x12M\n\x06layout\x18\x03 \x01(\x0b\x32\x35.google.cloud.documentai.v1beta2.Document.Page.LayoutR\x06layout\x12n\n\x12\x64\x65tected_languages\x18\x04 \x03(\x0b\x32?.google.cloud.documentai.v1beta2.Document.Page.DetectedLanguageR\x11\x64\x65tectedLanguages\x12L\n\x06\x62locks\x18\x05 \x03(\x0b\x32\x34.google.cloud.documentai.v1beta2.Document.Page.BlockR\x06\x62locks\x12X\n\nparagraphs\x18\x06 \x03(\x0b\x32\x38.google.cloud.documentai.v1beta2.Document.Page.ParagraphR\nparagraphs\x12I\n\x05lines\x18\x07 \x03(\x0b\x32\x33.google.cloud.documentai.v1beta2.Document.Page.LineR\x05lines\x12L\n\x06tokens\x18\x08 \x03(\x0b\x32\x34.google.cloud.documentai.v1beta2.Document.Page.TokenR\x06tokens\x12\x65\n\x0fvisual_elements\x18\t \x03(\x0b\x32<.google.cloud.documentai.v1beta2.Document.Page.VisualElementR\x0evisualElements\x12L\n\x06tables\x18\n \x03(\x0b\x32\x34.google.cloud.documentai.v1beta2.Document.Page.TableR\x06tables\x12Y\n\x0b\x66orm_fields\x18\x0b \x03(\x0b\x32\x38.google.cloud.documentai.v1beta2.Document.Page.FormFieldR\nformFields\x1aM\n\tDimension\x12\x14\n\x05width\x18\x01 \x01(\x02R\x05width\x12\x16\n\x06height\x18\x02 \x01(\x02R\x06height\x12\x12\n\x04unit\x18\x03 \x01(\tR\x04unit\x1a\xb5\x03\n\x06Layout\x12U\n\x0btext_anchor\x18\x01 \x01(\x0b\x32\x34.google.cloud.documentai.v1beta2.Document.TextAnchorR\ntextAnchor\x12\x1e\n\nconfidence\x18\x02 \x01(\x02R\nconfidence\x12R\n\rbounding_poly\x18\x03 \x01(\x0b\x32-.google.cloud.documentai.v1beta2.BoundingPolyR\x0c\x62oundingPoly\x12\x63\n\x0borientation\x18\x04 \x01(\x0e\x32\x41.google.cloud.documentai.v1beta2.Document.Page.Layout.OrientationR\x0borientation\x12\x14\n\x02id\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01R\x02id\"e\n\x0bOrientation\x12\x1b\n\x17ORIENTATION_UNSPECIFIED\x10\x00\x12\x0b\n\x07PAGE_UP\x10\x01\x12\x0e\n\nPAGE_RIGHT\x10\x02\x12\r\n\tPAGE_DOWN\x10\x03\x12\r\n\tPAGE_LEFT\x10\x04\x1a\xc6\x01\n\x05\x42lock\x12M\n\x06layout\x18\x01 \x01(\x0b\x32\x35.google.cloud.documentai.v1beta2.Document.Page.LayoutR\x06layout\x12n\n\x12\x64\x65tected_languages\x18\x02 \x03(\x0b\x32?.google.cloud.documentai.v1beta2.Document.Page.DetectedLanguageR\x11\x64\x65tectedLanguages\x1a\xca\x01\n\tParagraph\x12M\n\x06layout\x18\x01 \x01(\x0b\x32\x35.google.cloud.documentai.v1beta2.Document.Page.LayoutR\x06layout\x12n\n\x12\x64\x65tected_languages\x18\x02 \x03(\x0b\x32?.google.cloud.documentai.v1beta2.Document.Page.DetectedLanguageR\x11\x64\x65tectedLanguages\x1a\xc5\x01\n\x04Line\x12M\n\x06layout\x18\x01 \x01(\x0b\x32\x35.google.cloud.documentai.v1beta2.Document.Page.LayoutR\x06layout\x12n\n\x12\x64\x65tected_languages\x18\x02 \x03(\x0b\x32?.google.cloud.documentai.v1beta2.Document.Page.DetectedLanguageR\x11\x64\x65tectedLanguages\x1a\xe5\x03\n\x05Token\x12M\n\x06layout\x18\x01 \x01(\x0b\x32\x35.google.cloud.documentai.v1beta2.Document.Page.LayoutR\x06layout\x12i\n\x0e\x64\x65tected_break\x18\x02 \x01(\x0b\x32\x42.google.cloud.documentai.v1beta2.Document.Page.Token.DetectedBreakR\rdetectedBreak\x12n\n\x12\x64\x65tected_languages\x18\x03 \x03(\x0b\x32?.google.cloud.documentai.v1beta2.Document.Page.DetectedLanguageR\x11\x64\x65tectedLanguages\x1a\xb1\x01\n\rDetectedBreak\x12[\n\x04type\x18\x01 \x01(\x0e\x32G.google.cloud.documentai.v1beta2.Document.Page.Token.DetectedBreak.TypeR\x04type\"C\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05SPACE\x10\x01\x12\x0e\n\nWIDE_SPACE\x10\x02\x12\n\n\x06HYPHEN\x10\x03\x1a\xe2\x01\n\rVisualElement\x12M\n\x06layout\x18\x01 \x01(\x0b\x32\x35.google.cloud.documentai.v1beta2.Document.Page.LayoutR\x06layout\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12n\n\x12\x64\x65tected_languages\x18\x03 \x03(\x0b\x32?.google.cloud.documentai.v1beta2.Document.Page.DetectedLanguageR\x11\x64\x65tectedLanguages\x1a\xe7\x05\n\x05Table\x12M\n\x06layout\x18\x01 \x01(\x0b\x32\x35.google.cloud.documentai.v1beta2.Document.Page.LayoutR\x06layout\x12^\n\x0bheader_rows\x18\x02 \x03(\x0b\x32=.google.cloud.documentai.v1beta2.Document.Page.Table.TableRowR\nheaderRows\x12Z\n\tbody_rows\x18\x03 \x03(\x0b\x32=.google.cloud.documentai.v1beta2.Document.Page.Table.TableRowR\x08\x62odyRows\x12n\n\x12\x64\x65tected_languages\x18\x04 \x03(\x0b\x32?.google.cloud.documentai.v1beta2.Document.Page.DetectedLanguageR\x11\x64\x65tectedLanguages\x1a`\n\x08TableRow\x12T\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32>.google.cloud.documentai.v1beta2.Document.Page.Table.TableCellR\x05\x63\x65lls\x1a\x80\x02\n\tTableCell\x12M\n\x06layout\x18\x01 \x01(\x0b\x32\x35.google.cloud.documentai.v1beta2.Document.Page.LayoutR\x06layout\x12\x19\n\x08row_span\x18\x02 \x01(\x05R\x07rowSpan\x12\x19\n\x08\x63ol_span\x18\x03 \x01(\x05R\x07\x63olSpan\x12n\n\x12\x64\x65tected_languages\x18\x04 \x03(\x0b\x32?.google.cloud.documentai.v1beta2.Document.Page.DetectedLanguageR\x11\x64\x65tectedLanguages\x1a\xac\x04\n\tFormField\x12T\n\nfield_name\x18\x01 \x01(\x0b\x32\x35.google.cloud.documentai.v1beta2.Document.Page.LayoutR\tfieldName\x12V\n\x0b\x66ield_value\x18\x02 \x01(\x0b\x32\x35.google.cloud.documentai.v1beta2.Document.Page.LayoutR\nfieldValue\x12w\n\x17name_detected_languages\x18\x03 \x03(\x0b\x32?.google.cloud.documentai.v1beta2.Document.Page.DetectedLanguageR\x15nameDetectedLanguages\x12y\n\x18value_detected_languages\x18\x04 \x03(\x0b\x32?.google.cloud.documentai.v1beta2.Document.Page.DetectedLanguageR\x16valueDetectedLanguages\x12\x1d\n\nvalue_type\x18\x05 \x01(\tR\tvalueType\x12,\n\x12\x63orrected_key_text\x18\x06 \x01(\tR\x10\x63orrectedKeyText\x12\x30\n\x14\x63orrected_value_text\x18\x07 \x01(\tR\x12\x63orrectedValueText\x1aW\n\x10\x44\x65tectedLanguage\x12#\n\rlanguage_code\x18\x01 \x01(\tR\x0clanguageCode\x12\x1e\n\nconfidence\x18\x02 \x01(\x02R\nconfidence\x1a\xc9\x03\n\x06\x45ntity\x12U\n\x0btext_anchor\x18\x01 \x01(\x0b\x32\x34.google.cloud.documentai.v1beta2.Document.TextAnchorR\ntextAnchor\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12!\n\x0cmention_text\x18\x03 \x01(\tR\x0bmentionText\x12\x1d\n\nmention_id\x18\x04 \x01(\tR\tmentionId\x12$\n\nconfidence\x18\x05 \x01(\x02\x42\x04\xe2\x41\x01\x01R\nconfidence\x12[\n\x0bpage_anchor\x18\x06 \x01(\x0b\x32\x34.google.cloud.documentai.v1beta2.Document.PageAnchorB\x04\xe2\x41\x01\x01R\npageAnchor\x12\x14\n\x02id\x18\x07 \x01(\tB\x04\xe2\x41\x01\x01R\x02id\x12y\n\x1f\x62ounding_poly_for_demo_frontend\x18\x08 \x01(\x0b\x32-.google.cloud.documentai.v1beta2.BoundingPolyB\x04\xe2\x41\x01\x01R\x1b\x62oundingPolyForDemoFrontend\x1ah\n\x0e\x45ntityRelation\x12\x1d\n\nsubject_id\x18\x01 \x01(\tR\tsubjectId\x12\x1b\n\tobject_id\x18\x02 \x01(\tR\x08objectId\x12\x1a\n\x08relation\x18\x03 \x01(\tR\x08relation\x1a\xc0\x01\n\nTextAnchor\x12\x65\n\rtext_segments\x18\x01 \x03(\x0b\x32@.google.cloud.documentai.v1beta2.Document.TextAnchor.TextSegmentR\x0ctextSegments\x1aK\n\x0bTextSegment\x12\x1f\n\x0bstart_index\x18\x01 \x01(\x03R\nstartIndex\x12\x1b\n\tend_index\x18\x02 \x01(\x03R\x08\x65ndIndex\x1a\xaa\x03\n\nPageAnchor\x12Y\n\tpage_refs\x18\x01 \x03(\x0b\x32<.google.cloud.documentai.v1beta2.Document.PageAnchor.PageRefR\x08pageRefs\x1a\xc0\x02\n\x07PageRef\x12\x18\n\x04page\x18\x01 \x01(\x03\x42\x04\xe2\x41\x01\x02R\x04page\x12n\n\x0blayout_type\x18\x02 \x01(\x0e\x32G.google.cloud.documentai.v1beta2.Document.PageAnchor.PageRef.LayoutTypeB\x04\xe2\x41\x01\x01R\nlayoutType\x12!\n\tlayout_id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\x08layoutId\"\x87\x01\n\nLayoutType\x12\x1b\n\x17LAYOUT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05\x42LOCK\x10\x01\x12\r\n\tPARAGRAPH\x10\x02\x12\x08\n\x04LINE\x10\x03\x12\t\n\x05TOKEN\x10\x04\x12\x12\n\x0eVISUAL_ELEMENT\x10\x05\x12\t\n\x05TABLE\x10\x06\x12\x0e\n\nFORM_FIELD\x10\x07\x42\x08\n\x06sourceB\xea\x01\n#com.google.cloud.documentai.v1beta2B\rDocumentProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/documentai/v1beta2;documentai\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta2\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta2\xea\x02\"Google::Cloud::DocumentAI::V1beta2b\x06proto3')



_DOCUMENT = DESCRIPTOR.message_types_by_name['Document']
_DOCUMENT_SHARDINFO = _DOCUMENT.nested_types_by_name['ShardInfo']
_DOCUMENT_LABEL = _DOCUMENT.nested_types_by_name['Label']
_DOCUMENT_STYLE = _DOCUMENT.nested_types_by_name['Style']
_DOCUMENT_STYLE_FONTSIZE = _DOCUMENT_STYLE.nested_types_by_name['FontSize']
_DOCUMENT_PAGE = _DOCUMENT.nested_types_by_name['Page']
_DOCUMENT_PAGE_DIMENSION = _DOCUMENT_PAGE.nested_types_by_name['Dimension']
_DOCUMENT_PAGE_LAYOUT = _DOCUMENT_PAGE.nested_types_by_name['Layout']
_DOCUMENT_PAGE_BLOCK = _DOCUMENT_PAGE.nested_types_by_name['Block']
_DOCUMENT_PAGE_PARAGRAPH = _DOCUMENT_PAGE.nested_types_by_name['Paragraph']
_DOCUMENT_PAGE_LINE = _DOCUMENT_PAGE.nested_types_by_name['Line']
_DOCUMENT_PAGE_TOKEN = _DOCUMENT_PAGE.nested_types_by_name['Token']
_DOCUMENT_PAGE_TOKEN_DETECTEDBREAK = _DOCUMENT_PAGE_TOKEN.nested_types_by_name['DetectedBreak']
_DOCUMENT_PAGE_VISUALELEMENT = _DOCUMENT_PAGE.nested_types_by_name['VisualElement']
_DOCUMENT_PAGE_TABLE = _DOCUMENT_PAGE.nested_types_by_name['Table']
_DOCUMENT_PAGE_TABLE_TABLEROW = _DOCUMENT_PAGE_TABLE.nested_types_by_name['TableRow']
_DOCUMENT_PAGE_TABLE_TABLECELL = _DOCUMENT_PAGE_TABLE.nested_types_by_name['TableCell']
_DOCUMENT_PAGE_FORMFIELD = _DOCUMENT_PAGE.nested_types_by_name['FormField']
_DOCUMENT_PAGE_DETECTEDLANGUAGE = _DOCUMENT_PAGE.nested_types_by_name['DetectedLanguage']
_DOCUMENT_ENTITY = _DOCUMENT.nested_types_by_name['Entity']
_DOCUMENT_ENTITYRELATION = _DOCUMENT.nested_types_by_name['EntityRelation']
_DOCUMENT_TEXTANCHOR = _DOCUMENT.nested_types_by_name['TextAnchor']
_DOCUMENT_TEXTANCHOR_TEXTSEGMENT = _DOCUMENT_TEXTANCHOR.nested_types_by_name['TextSegment']
_DOCUMENT_PAGEANCHOR = _DOCUMENT.nested_types_by_name['PageAnchor']
_DOCUMENT_PAGEANCHOR_PAGEREF = _DOCUMENT_PAGEANCHOR.nested_types_by_name['PageRef']
_DOCUMENT_PAGE_LAYOUT_ORIENTATION = _DOCUMENT_PAGE_LAYOUT.enum_types_by_name['Orientation']
_DOCUMENT_PAGE_TOKEN_DETECTEDBREAK_TYPE = _DOCUMENT_PAGE_TOKEN_DETECTEDBREAK.enum_types_by_name['Type']
_DOCUMENT_PAGEANCHOR_PAGEREF_LAYOUTTYPE = _DOCUMENT_PAGEANCHOR_PAGEREF.enum_types_by_name['LayoutType']
Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {

  'ShardInfo' : _reflection.GeneratedProtocolMessageType('ShardInfo', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENT_SHARDINFO,
    '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.ShardInfo)
    })
  ,

  'Label' : _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENT_LABEL,
    '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Label)
    })
  ,

  'Style' : _reflection.GeneratedProtocolMessageType('Style', (_message.Message,), {

    'FontSize' : _reflection.GeneratedProtocolMessageType('FontSize', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_STYLE_FONTSIZE,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Style.FontSize)
      })
    ,
    'DESCRIPTOR' : _DOCUMENT_STYLE,
    '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Style)
    })
  ,

  'Page' : _reflection.GeneratedProtocolMessageType('Page', (_message.Message,), {

    'Dimension' : _reflection.GeneratedProtocolMessageType('Dimension', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_PAGE_DIMENSION,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.Dimension)
      })
    ,

    'Layout' : _reflection.GeneratedProtocolMessageType('Layout', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_PAGE_LAYOUT,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.Layout)
      })
    ,

    'Block' : _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_PAGE_BLOCK,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.Block)
      })
    ,

    'Paragraph' : _reflection.GeneratedProtocolMessageType('Paragraph', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_PAGE_PARAGRAPH,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.Paragraph)
      })
    ,

    'Line' : _reflection.GeneratedProtocolMessageType('Line', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_PAGE_LINE,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.Line)
      })
    ,

    'Token' : _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {

      'DetectedBreak' : _reflection.GeneratedProtocolMessageType('DetectedBreak', (_message.Message,), {
        'DESCRIPTOR' : _DOCUMENT_PAGE_TOKEN_DETECTEDBREAK,
        '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.Token.DetectedBreak)
        })
      ,
      'DESCRIPTOR' : _DOCUMENT_PAGE_TOKEN,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.Token)
      })
    ,

    'VisualElement' : _reflection.GeneratedProtocolMessageType('VisualElement', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_PAGE_VISUALELEMENT,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.VisualElement)
      })
    ,

    'Table' : _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), {

      'TableRow' : _reflection.GeneratedProtocolMessageType('TableRow', (_message.Message,), {
        'DESCRIPTOR' : _DOCUMENT_PAGE_TABLE_TABLEROW,
        '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.Table.TableRow)
        })
      ,

      'TableCell' : _reflection.GeneratedProtocolMessageType('TableCell', (_message.Message,), {
        'DESCRIPTOR' : _DOCUMENT_PAGE_TABLE_TABLECELL,
        '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.Table.TableCell)
        })
      ,
      'DESCRIPTOR' : _DOCUMENT_PAGE_TABLE,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.Table)
      })
    ,

    'FormField' : _reflection.GeneratedProtocolMessageType('FormField', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_PAGE_FORMFIELD,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.FormField)
      })
    ,

    'DetectedLanguage' : _reflection.GeneratedProtocolMessageType('DetectedLanguage', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_PAGE_DETECTEDLANGUAGE,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page.DetectedLanguage)
      })
    ,
    'DESCRIPTOR' : _DOCUMENT_PAGE,
    '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Page)
    })
  ,

  'Entity' : _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENT_ENTITY,
    '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.Entity)
    })
  ,

  'EntityRelation' : _reflection.GeneratedProtocolMessageType('EntityRelation', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENT_ENTITYRELATION,
    '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.EntityRelation)
    })
  ,

  'TextAnchor' : _reflection.GeneratedProtocolMessageType('TextAnchor', (_message.Message,), {

    'TextSegment' : _reflection.GeneratedProtocolMessageType('TextSegment', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_TEXTANCHOR_TEXTSEGMENT,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.TextAnchor.TextSegment)
      })
    ,
    'DESCRIPTOR' : _DOCUMENT_TEXTANCHOR,
    '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.TextAnchor)
    })
  ,

  'PageAnchor' : _reflection.GeneratedProtocolMessageType('PageAnchor', (_message.Message,), {

    'PageRef' : _reflection.GeneratedProtocolMessageType('PageRef', (_message.Message,), {
      'DESCRIPTOR' : _DOCUMENT_PAGEANCHOR_PAGEREF,
      '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.PageAnchor.PageRef)
      })
    ,
    'DESCRIPTOR' : _DOCUMENT_PAGEANCHOR,
    '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document.PageAnchor)
    })
  ,
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'google.cloud.documentai.v1beta2.document_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1beta2.Document)
  })
_sym_db.RegisterMessage(Document)
_sym_db.RegisterMessage(Document.ShardInfo)
_sym_db.RegisterMessage(Document.Label)
_sym_db.RegisterMessage(Document.Style)
_sym_db.RegisterMessage(Document.Style.FontSize)
_sym_db.RegisterMessage(Document.Page)
_sym_db.RegisterMessage(Document.Page.Dimension)
_sym_db.RegisterMessage(Document.Page.Layout)
_sym_db.RegisterMessage(Document.Page.Block)
_sym_db.RegisterMessage(Document.Page.Paragraph)
_sym_db.RegisterMessage(Document.Page.Line)
_sym_db.RegisterMessage(Document.Page.Token)
_sym_db.RegisterMessage(Document.Page.Token.DetectedBreak)
_sym_db.RegisterMessage(Document.Page.VisualElement)
_sym_db.RegisterMessage(Document.Page.Table)
_sym_db.RegisterMessage(Document.Page.Table.TableRow)
_sym_db.RegisterMessage(Document.Page.Table.TableCell)
_sym_db.RegisterMessage(Document.Page.FormField)
_sym_db.RegisterMessage(Document.Page.DetectedLanguage)
_sym_db.RegisterMessage(Document.Entity)
_sym_db.RegisterMessage(Document.EntityRelation)
_sym_db.RegisterMessage(Document.TextAnchor)
_sym_db.RegisterMessage(Document.TextAnchor.TextSegment)
_sym_db.RegisterMessage(Document.PageAnchor)
_sym_db.RegisterMessage(Document.PageAnchor.PageRef)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.documentai.v1beta2B\rDocumentProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/documentai/v1beta2;documentai\252\002\037Google.Cloud.DocumentAI.V1Beta2\312\002\037Google\\Cloud\\DocumentAI\\V1beta2\352\002\"Google::Cloud::DocumentAI::V1beta2'
  _DOCUMENT_PAGE_LAYOUT.fields_by_name['id']._options = None
  _DOCUMENT_PAGE_LAYOUT.fields_by_name['id']._serialized_options = b'\342A\001\001'
  _DOCUMENT_ENTITY.fields_by_name['confidence']._options = None
  _DOCUMENT_ENTITY.fields_by_name['confidence']._serialized_options = b'\342A\001\001'
  _DOCUMENT_ENTITY.fields_by_name['page_anchor']._options = None
  _DOCUMENT_ENTITY.fields_by_name['page_anchor']._serialized_options = b'\342A\001\001'
  _DOCUMENT_ENTITY.fields_by_name['id']._options = None
  _DOCUMENT_ENTITY.fields_by_name['id']._serialized_options = b'\342A\001\001'
  _DOCUMENT_ENTITY.fields_by_name['bounding_poly_for_demo_frontend']._options = None
  _DOCUMENT_ENTITY.fields_by_name['bounding_poly_for_demo_frontend']._serialized_options = b'\342A\001\001'
  _DOCUMENT_PAGEANCHOR_PAGEREF.fields_by_name['page']._options = None
  _DOCUMENT_PAGEANCHOR_PAGEREF.fields_by_name['page']._serialized_options = b'\342A\001\002'
  _DOCUMENT_PAGEANCHOR_PAGEREF.fields_by_name['layout_type']._options = None
  _DOCUMENT_PAGEANCHOR_PAGEREF.fields_by_name['layout_type']._serialized_options = b'\342A\001\001'
  _DOCUMENT_PAGEANCHOR_PAGEREF.fields_by_name['layout_id']._options = None
  _DOCUMENT_PAGEANCHOR_PAGEREF.fields_by_name['layout_id']._serialized_options = b'\342A\001\001'
  _DOCUMENT._serialized_start=245
  _DOCUMENT._serialized_end=6898
  _DOCUMENT_SHARDINFO._serialized_start=884
  _DOCUMENT_SHARDINFO._serialized_end=994
  _DOCUMENT_LABEL._serialized_start=996
  _DOCUMENT_LABEL._serialized_end=1102
  _DOCUMENT_STYLE._serialized_start=1105
  _DOCUMENT_STYLE._serialized_end=1548
  _DOCUMENT_STYLE_FONTSIZE._serialized_start=1498
  _DOCUMENT_STYLE_FONTSIZE._serialized_end=1548
  _DOCUMENT_PAGE._serialized_start=1551
  _DOCUMENT_PAGE._serialized_end=5698
  _DOCUMENT_PAGE_DIMENSION._serialized_start=2464
  _DOCUMENT_PAGE_DIMENSION._serialized_end=2541
  _DOCUMENT_PAGE_LAYOUT._serialized_start=2544
  _DOCUMENT_PAGE_LAYOUT._serialized_end=2981
  _DOCUMENT_PAGE_LAYOUT_ORIENTATION._serialized_start=2880
  _DOCUMENT_PAGE_LAYOUT_ORIENTATION._serialized_end=2981
  _DOCUMENT_PAGE_BLOCK._serialized_start=2984
  _DOCUMENT_PAGE_BLOCK._serialized_end=3182
  _DOCUMENT_PAGE_PARAGRAPH._serialized_start=3185
  _DOCUMENT_PAGE_PARAGRAPH._serialized_end=3387
  _DOCUMENT_PAGE_LINE._serialized_start=3390
  _DOCUMENT_PAGE_LINE._serialized_end=3587
  _DOCUMENT_PAGE_TOKEN._serialized_start=3590
  _DOCUMENT_PAGE_TOKEN._serialized_end=4075
  _DOCUMENT_PAGE_TOKEN_DETECTEDBREAK._serialized_start=3898
  _DOCUMENT_PAGE_TOKEN_DETECTEDBREAK._serialized_end=4075
  _DOCUMENT_PAGE_TOKEN_DETECTEDBREAK_TYPE._serialized_start=4008
  _DOCUMENT_PAGE_TOKEN_DETECTEDBREAK_TYPE._serialized_end=4075
  _DOCUMENT_PAGE_VISUALELEMENT._serialized_start=4078
  _DOCUMENT_PAGE_VISUALELEMENT._serialized_end=4304
  _DOCUMENT_PAGE_TABLE._serialized_start=4307
  _DOCUMENT_PAGE_TABLE._serialized_end=5050
  _DOCUMENT_PAGE_TABLE_TABLEROW._serialized_start=4695
  _DOCUMENT_PAGE_TABLE_TABLEROW._serialized_end=4791
  _DOCUMENT_PAGE_TABLE_TABLECELL._serialized_start=4794
  _DOCUMENT_PAGE_TABLE_TABLECELL._serialized_end=5050
  _DOCUMENT_PAGE_FORMFIELD._serialized_start=5053
  _DOCUMENT_PAGE_FORMFIELD._serialized_end=5609
  _DOCUMENT_PAGE_DETECTEDLANGUAGE._serialized_start=5611
  _DOCUMENT_PAGE_DETECTEDLANGUAGE._serialized_end=5698
  _DOCUMENT_ENTITY._serialized_start=5701
  _DOCUMENT_ENTITY._serialized_end=6158
  _DOCUMENT_ENTITYRELATION._serialized_start=6160
  _DOCUMENT_ENTITYRELATION._serialized_end=6264
  _DOCUMENT_TEXTANCHOR._serialized_start=6267
  _DOCUMENT_TEXTANCHOR._serialized_end=6459
  _DOCUMENT_TEXTANCHOR_TEXTSEGMENT._serialized_start=6384
  _DOCUMENT_TEXTANCHOR_TEXTSEGMENT._serialized_end=6459
  _DOCUMENT_PAGEANCHOR._serialized_start=6462
  _DOCUMENT_PAGEANCHOR._serialized_end=6888
  _DOCUMENT_PAGEANCHOR_PAGEREF._serialized_start=6568
  _DOCUMENT_PAGEANCHOR_PAGEREF._serialized_end=6888
  _DOCUMENT_PAGEANCHOR_PAGEREF_LAYOUTTYPE._serialized_start=6753
  _DOCUMENT_PAGEANCHOR_PAGEREF_LAYOUTTYPE._serialized_end=6888
# @@protoc_insertion_point(module_scope)
