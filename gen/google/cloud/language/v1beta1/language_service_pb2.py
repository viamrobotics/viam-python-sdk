# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/language/v1beta1/language_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/language/v1beta1/language_service.proto\x12\x1dgoogle.cloud.language.v1beta1\x1a\x1cgoogle/api/annotations.proto\"\xf0\x01\n\x08\x44ocument\x12@\n\x04type\x18\x01 \x01(\x0e\x32,.google.cloud.language.v1beta1.Document.TypeR\x04type\x12\x1a\n\x07\x63ontent\x18\x02 \x01(\tH\x00R\x07\x63ontent\x12(\n\x0fgcs_content_uri\x18\x03 \x01(\tH\x00R\rgcsContentUri\x12\x1a\n\x08language\x18\x04 \x01(\tR\x08language\"6\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nPLAIN_TEXT\x10\x01\x12\x08\n\x04HTML\x10\x02\x42\x08\n\x06source\"\x8f\x01\n\x08Sentence\x12;\n\x04text\x18\x01 \x01(\x0b\x32\'.google.cloud.language.v1beta1.TextSpanR\x04text\x12\x46\n\tsentiment\x18\x02 \x01(\x0b\x32(.google.cloud.language.v1beta1.SentimentR\tsentiment\"\xcb\x03\n\x06\x45ntity\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12>\n\x04type\x18\x02 \x01(\x0e\x32*.google.cloud.language.v1beta1.Entity.TypeR\x04type\x12O\n\x08metadata\x18\x03 \x03(\x0b\x32\x33.google.cloud.language.v1beta1.Entity.MetadataEntryR\x08metadata\x12\x1a\n\x08salience\x18\x04 \x01(\x02R\x08salience\x12H\n\x08mentions\x18\x05 \x03(\x0b\x32,.google.cloud.language.v1beta1.EntityMentionR\x08mentions\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"y\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06PERSON\x10\x01\x12\x0c\n\x08LOCATION\x10\x02\x12\x10\n\x0cORGANIZATION\x10\x03\x12\t\n\x05\x45VENT\x10\x04\x12\x0f\n\x0bWORK_OF_ART\x10\x05\x12\x11\n\rCONSUMER_GOOD\x10\x06\x12\t\n\x05OTHER\x10\x07\"\x85\x02\n\x05Token\x12;\n\x04text\x18\x01 \x01(\x0b\x32\'.google.cloud.language.v1beta1.TextSpanR\x04text\x12Q\n\x0epart_of_speech\x18\x02 \x01(\x0b\x32+.google.cloud.language.v1beta1.PartOfSpeechR\x0cpartOfSpeech\x12V\n\x0f\x64\x65pendency_edge\x18\x03 \x01(\x0b\x32-.google.cloud.language.v1beta1.DependencyEdgeR\x0e\x64\x65pendencyEdge\x12\x14\n\x05lemma\x18\x04 \x01(\tR\x05lemma\"[\n\tSentiment\x12\x1a\n\x08polarity\x18\x01 \x01(\x02R\x08polarity\x12\x1c\n\tmagnitude\x18\x02 \x01(\x02R\tmagnitude\x12\x14\n\x05score\x18\x03 \x01(\x02R\x05score\"\xb9\x11\n\x0cPartOfSpeech\x12\x41\n\x03tag\x18\x01 \x01(\x0e\x32/.google.cloud.language.v1beta1.PartOfSpeech.TagR\x03tag\x12J\n\x06\x61spect\x18\x02 \x01(\x0e\x32\x32.google.cloud.language.v1beta1.PartOfSpeech.AspectR\x06\x61spect\x12\x44\n\x04\x63\x61se\x18\x03 \x01(\x0e\x32\x30.google.cloud.language.v1beta1.PartOfSpeech.CaseR\x04\x63\x61se\x12\x44\n\x04\x66orm\x18\x04 \x01(\x0e\x32\x30.google.cloud.language.v1beta1.PartOfSpeech.FormR\x04\x66orm\x12J\n\x06gender\x18\x05 \x01(\x0e\x32\x32.google.cloud.language.v1beta1.PartOfSpeech.GenderR\x06gender\x12\x44\n\x04mood\x18\x06 \x01(\x0e\x32\x30.google.cloud.language.v1beta1.PartOfSpeech.MoodR\x04mood\x12J\n\x06number\x18\x07 \x01(\x0e\x32\x32.google.cloud.language.v1beta1.PartOfSpeech.NumberR\x06number\x12J\n\x06person\x18\x08 \x01(\x0e\x32\x32.google.cloud.language.v1beta1.PartOfSpeech.PersonR\x06person\x12J\n\x06proper\x18\t \x01(\x0e\x32\x32.google.cloud.language.v1beta1.PartOfSpeech.ProperR\x06proper\x12Y\n\x0breciprocity\x18\n \x01(\x0e\x32\x37.google.cloud.language.v1beta1.PartOfSpeech.ReciprocityR\x0breciprocity\x12G\n\x05tense\x18\x0b \x01(\x0e\x32\x31.google.cloud.language.v1beta1.PartOfSpeech.TenseR\x05tense\x12G\n\x05voice\x18\x0c \x01(\x0e\x32\x31.google.cloud.language.v1beta1.PartOfSpeech.VoiceR\x05voice\"\x8d\x01\n\x03Tag\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41\x44J\x10\x01\x12\x07\n\x03\x41\x44P\x10\x02\x12\x07\n\x03\x41\x44V\x10\x03\x12\x08\n\x04\x43ONJ\x10\x04\x12\x07\n\x03\x44\x45T\x10\x05\x12\x08\n\x04NOUN\x10\x06\x12\x07\n\x03NUM\x10\x07\x12\x08\n\x04PRON\x10\x08\x12\x07\n\x03PRT\x10\t\x12\t\n\x05PUNCT\x10\n\x12\x08\n\x04VERB\x10\x0b\x12\x05\n\x01X\x10\x0c\x12\t\n\x05\x41\x46\x46IX\x10\r\"O\n\x06\x41spect\x12\x12\n\x0e\x41SPECT_UNKNOWN\x10\x00\x12\x0e\n\nPERFECTIVE\x10\x01\x12\x10\n\x0cIMPERFECTIVE\x10\x02\x12\x0f\n\x0bPROGRESSIVE\x10\x03\"\xf8\x01\n\x04\x43\x61se\x12\x10\n\x0c\x43\x41SE_UNKNOWN\x10\x00\x12\x0e\n\nACCUSATIVE\x10\x01\x12\r\n\tADVERBIAL\x10\x02\x12\x11\n\rCOMPLEMENTIVE\x10\x03\x12\n\n\x06\x44\x41TIVE\x10\x04\x12\x0c\n\x08GENITIVE\x10\x05\x12\x10\n\x0cINSTRUMENTAL\x10\x06\x12\x0c\n\x08LOCATIVE\x10\x07\x12\x0e\n\nNOMINATIVE\x10\x08\x12\x0b\n\x07OBLIQUE\x10\t\x12\r\n\tPARTITIVE\x10\n\x12\x11\n\rPREPOSITIONAL\x10\x0b\x12\x12\n\x0eREFLEXIVE_CASE\x10\x0c\x12\x11\n\rRELATIVE_CASE\x10\r\x12\x0c\n\x08VOCATIVE\x10\x0e\"\xaf\x01\n\x04\x46orm\x12\x10\n\x0c\x46ORM_UNKNOWN\x10\x00\x12\x0c\n\x08\x41\x44NOMIAL\x10\x01\x12\r\n\tAUXILIARY\x10\x02\x12\x12\n\x0e\x43OMPLEMENTIZER\x10\x03\x12\x10\n\x0c\x46INAL_ENDING\x10\x04\x12\n\n\x06GERUND\x10\x05\x12\n\n\x06REALIS\x10\x06\x12\x0c\n\x08IRREALIS\x10\x07\x12\t\n\x05SHORT\x10\x08\x12\x08\n\x04LONG\x10\t\x12\t\n\x05ORDER\x10\n\x12\x0c\n\x08SPECIFIC\x10\x0b\"E\n\x06Gender\x12\x12\n\x0eGENDER_UNKNOWN\x10\x00\x12\x0c\n\x08\x46\x45MININE\x10\x01\x12\r\n\tMASCULINE\x10\x02\x12\n\n\x06NEUTER\x10\x03\"\x7f\n\x04Mood\x12\x10\n\x0cMOOD_UNKNOWN\x10\x00\x12\x14\n\x10\x43ONDITIONAL_MOOD\x10\x01\x12\x0e\n\nIMPERATIVE\x10\x02\x12\x0e\n\nINDICATIVE\x10\x03\x12\x11\n\rINTERROGATIVE\x10\x04\x12\x0b\n\x07JUSSIVE\x10\x05\x12\x0f\n\x0bSUBJUNCTIVE\x10\x06\"@\n\x06Number\x12\x12\n\x0eNUMBER_UNKNOWN\x10\x00\x12\x0c\n\x08SINGULAR\x10\x01\x12\n\n\x06PLURAL\x10\x02\x12\x08\n\x04\x44UAL\x10\x03\"T\n\x06Person\x12\x12\n\x0ePERSON_UNKNOWN\x10\x00\x12\t\n\x05\x46IRST\x10\x01\x12\n\n\x06SECOND\x10\x02\x12\t\n\x05THIRD\x10\x03\x12\x14\n\x10REFLEXIVE_PERSON\x10\x04\"8\n\x06Proper\x12\x12\n\x0ePROPER_UNKNOWN\x10\x00\x12\n\n\x06PROPER\x10\x01\x12\x0e\n\nNOT_PROPER\x10\x02\"J\n\x0bReciprocity\x12\x17\n\x13RECIPROCITY_UNKNOWN\x10\x00\x12\x0e\n\nRECIPROCAL\x10\x01\x12\x12\n\x0eNON_RECIPROCAL\x10\x02\"s\n\x05Tense\x12\x11\n\rTENSE_UNKNOWN\x10\x00\x12\x15\n\x11\x43ONDITIONAL_TENSE\x10\x01\x12\n\n\x06\x46UTURE\x10\x02\x12\x08\n\x04PAST\x10\x03\x12\x0b\n\x07PRESENT\x10\x04\x12\r\n\tIMPERFECT\x10\x05\x12\x0e\n\nPLUPERFECT\x10\x06\"B\n\x05Voice\x12\x11\n\rVOICE_UNKNOWN\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\r\n\tCAUSATIVE\x10\x02\x12\x0b\n\x07PASSIVE\x10\x03\"\xf4\x07\n\x0e\x44\x65pendencyEdge\x12(\n\x10head_token_index\x18\x01 \x01(\x05R\x0eheadTokenIndex\x12I\n\x05label\x18\x02 \x01(\x0e\x32\x33.google.cloud.language.v1beta1.DependencyEdge.LabelR\x05label\"\xec\x06\n\x05Label\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x41\x42\x42REV\x10\x01\x12\t\n\x05\x41\x43OMP\x10\x02\x12\t\n\x05\x41\x44VCL\x10\x03\x12\n\n\x06\x41\x44VMOD\x10\x04\x12\x08\n\x04\x41MOD\x10\x05\x12\t\n\x05\x41PPOS\x10\x06\x12\x08\n\x04\x41TTR\x10\x07\x12\x07\n\x03\x41UX\x10\x08\x12\x0b\n\x07\x41UXPASS\x10\t\x12\x06\n\x02\x43\x43\x10\n\x12\t\n\x05\x43\x43OMP\x10\x0b\x12\x08\n\x04\x43ONJ\x10\x0c\x12\t\n\x05\x43SUBJ\x10\r\x12\r\n\tCSUBJPASS\x10\x0e\x12\x07\n\x03\x44\x45P\x10\x0f\x12\x07\n\x03\x44\x45T\x10\x10\x12\r\n\tDISCOURSE\x10\x11\x12\x08\n\x04\x44OBJ\x10\x12\x12\x08\n\x04\x45XPL\x10\x13\x12\x0c\n\x08GOESWITH\x10\x14\x12\x08\n\x04IOBJ\x10\x15\x12\x08\n\x04MARK\x10\x16\x12\x07\n\x03MWE\x10\x17\x12\x07\n\x03MWV\x10\x18\x12\x07\n\x03NEG\x10\x19\x12\x06\n\x02NN\x10\x1a\x12\x0c\n\x08NPADVMOD\x10\x1b\x12\t\n\x05NSUBJ\x10\x1c\x12\r\n\tNSUBJPASS\x10\x1d\x12\x07\n\x03NUM\x10\x1e\x12\n\n\x06NUMBER\x10\x1f\x12\x05\n\x01P\x10 \x12\r\n\tPARATAXIS\x10!\x12\x0b\n\x07PARTMOD\x10\"\x12\t\n\x05PCOMP\x10#\x12\x08\n\x04POBJ\x10$\x12\x08\n\x04POSS\x10%\x12\x0b\n\x07POSTNEG\x10&\x12\x0b\n\x07PRECOMP\x10\'\x12\x0b\n\x07PRECONJ\x10(\x12\n\n\x06PREDET\x10)\x12\x08\n\x04PREF\x10*\x12\x08\n\x04PREP\x10+\x12\t\n\x05PRONL\x10,\x12\x07\n\x03PRT\x10-\x12\x06\n\x02PS\x10.\x12\x0c\n\x08QUANTMOD\x10/\x12\t\n\x05RCMOD\x10\x30\x12\x0c\n\x08RCMODREL\x10\x31\x12\t\n\x05RDROP\x10\x32\x12\x07\n\x03REF\x10\x33\x12\x0b\n\x07REMNANT\x10\x34\x12\x0e\n\nREPARANDUM\x10\x35\x12\x08\n\x04ROOT\x10\x36\x12\x08\n\x04SNUM\x10\x37\x12\x08\n\x04SUFF\x10\x38\x12\x08\n\x04TMOD\x10\x39\x12\t\n\x05TOPIC\x10:\x12\x08\n\x04VMOD\x10;\x12\x0c\n\x08VOCATIVE\x10<\x12\t\n\x05XCOMP\x10=\x12\n\n\x06SUFFIX\x10>\x12\t\n\x05TITLE\x10?\x12\x0c\n\x08\x41\x44VPHMOD\x10@\x12\x0b\n\x07\x41UXCAUS\x10\x41\x12\t\n\x05\x41UXVV\x10\x42\x12\t\n\x05\x44TMOD\x10\x43\x12\x0b\n\x07\x46OREIGN\x10\x44\x12\x06\n\x02KW\x10\x45\x12\x08\n\x04LIST\x10\x46\x12\x08\n\x04NOMC\x10G\x12\x0c\n\x08NOMCSUBJ\x10H\x12\x10\n\x0cNOMCSUBJPASS\x10I\x12\x08\n\x04NUMC\x10J\x12\x07\n\x03\x43OP\x10K\x12\x0e\n\nDISLOCATED\x10L\"\xc5\x01\n\rEntityMention\x12;\n\x04text\x18\x01 \x01(\x0b\x32\'.google.cloud.language.v1beta1.TextSpanR\x04text\x12\x45\n\x04type\x18\x02 \x01(\x0e\x32\x31.google.cloud.language.v1beta1.EntityMention.TypeR\x04type\"0\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\n\n\x06PROPER\x10\x01\x12\n\n\x06\x43OMMON\x10\x02\"G\n\x08TextSpan\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\x12!\n\x0c\x62\x65gin_offset\x18\x02 \x01(\x05R\x0b\x62\x65ginOffset\"\xb0\x01\n\x17\x41nalyzeSentimentRequest\x12\x43\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\'.google.cloud.language.v1beta1.DocumentR\x08\x64ocument\x12P\n\rencoding_type\x18\x02 \x01(\x0e\x32+.google.cloud.language.v1beta1.EncodingTypeR\x0c\x65ncodingType\"\xd6\x01\n\x18\x41nalyzeSentimentResponse\x12W\n\x12\x64ocument_sentiment\x18\x01 \x01(\x0b\x32(.google.cloud.language.v1beta1.SentimentR\x11\x64ocumentSentiment\x12\x1a\n\x08language\x18\x02 \x01(\tR\x08language\x12\x45\n\tsentences\x18\x03 \x03(\x0b\x32\'.google.cloud.language.v1beta1.SentenceR\tsentences\"\xaf\x01\n\x16\x41nalyzeEntitiesRequest\x12\x43\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\'.google.cloud.language.v1beta1.DocumentR\x08\x64ocument\x12P\n\rencoding_type\x18\x02 \x01(\x0e\x32+.google.cloud.language.v1beta1.EncodingTypeR\x0c\x65ncodingType\"x\n\x17\x41nalyzeEntitiesResponse\x12\x41\n\x08\x65ntities\x18\x01 \x03(\x0b\x32%.google.cloud.language.v1beta1.EntityR\x08\x65ntities\x12\x1a\n\x08language\x18\x02 \x01(\tR\x08language\"\xad\x01\n\x14\x41nalyzeSyntaxRequest\x12\x43\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\'.google.cloud.language.v1beta1.DocumentR\x08\x64ocument\x12P\n\rencoding_type\x18\x02 \x01(\x0e\x32+.google.cloud.language.v1beta1.EncodingTypeR\x0c\x65ncodingType\"\xb8\x01\n\x15\x41nalyzeSyntaxResponse\x12\x45\n\tsentences\x18\x01 \x03(\x0b\x32\'.google.cloud.language.v1beta1.SentenceR\tsentences\x12<\n\x06tokens\x18\x02 \x03(\x0b\x32$.google.cloud.language.v1beta1.TokenR\x06tokens\x12\x1a\n\x08language\x18\x03 \x01(\tR\x08language\"\xa2\x03\n\x13\x41nnotateTextRequest\x12\x43\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\'.google.cloud.language.v1beta1.DocumentR\x08\x64ocument\x12W\n\x08\x66\x65\x61tures\x18\x02 \x01(\x0b\x32;.google.cloud.language.v1beta1.AnnotateTextRequest.FeaturesR\x08\x66\x65\x61tures\x12P\n\rencoding_type\x18\x03 \x01(\x0e\x32+.google.cloud.language.v1beta1.EncodingTypeR\x0c\x65ncodingType\x1a\x9a\x01\n\x08\x46\x65\x61tures\x12%\n\x0e\x65xtract_syntax\x18\x01 \x01(\x08R\rextractSyntax\x12)\n\x10\x65xtract_entities\x18\x02 \x01(\x08R\x0f\x65xtractEntities\x12<\n\x1a\x65xtract_document_sentiment\x18\x03 \x01(\x08R\x18\x65xtractDocumentSentiment\"\xd3\x02\n\x14\x41nnotateTextResponse\x12\x45\n\tsentences\x18\x01 \x03(\x0b\x32\'.google.cloud.language.v1beta1.SentenceR\tsentences\x12<\n\x06tokens\x18\x02 \x03(\x0b\x32$.google.cloud.language.v1beta1.TokenR\x06tokens\x12\x41\n\x08\x65ntities\x18\x03 \x03(\x0b\x32%.google.cloud.language.v1beta1.EntityR\x08\x65ntities\x12W\n\x12\x64ocument_sentiment\x18\x04 \x01(\x0b\x32(.google.cloud.language.v1beta1.SentimentR\x11\x64ocumentSentiment\x12\x1a\n\x08language\x18\x05 \x01(\tR\x08language*8\n\x0c\x45ncodingType\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04UTF8\x10\x01\x12\t\n\x05UTF16\x10\x02\x12\t\n\x05UTF32\x10\x03\x32\xc9\x05\n\x0fLanguageService\x12\xb3\x01\n\x10\x41nalyzeSentiment\x12\x36.google.cloud.language.v1beta1.AnalyzeSentimentRequest\x1a\x37.google.cloud.language.v1beta1.AnalyzeSentimentResponse\".\x82\xd3\xe4\x93\x02(\"#/v1beta1/documents:analyzeSentiment:\x01*\x12\xaf\x01\n\x0f\x41nalyzeEntities\x12\x35.google.cloud.language.v1beta1.AnalyzeEntitiesRequest\x1a\x36.google.cloud.language.v1beta1.AnalyzeEntitiesResponse\"-\x82\xd3\xe4\x93\x02\'\"\"/v1beta1/documents:analyzeEntities:\x01*\x12\xa7\x01\n\rAnalyzeSyntax\x12\x33.google.cloud.language.v1beta1.AnalyzeSyntaxRequest\x1a\x34.google.cloud.language.v1beta1.AnalyzeSyntaxResponse\"+\x82\xd3\xe4\x93\x02%\" /v1beta1/documents:analyzeSyntax:\x01*\x12\xa3\x01\n\x0c\x41nnotateText\x12\x32.google.cloud.language.v1beta1.AnnotateTextRequest\x1a\x33.google.cloud.language.v1beta1.AnnotateTextResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/v1beta1/documents:annotateText:\x01*B\x82\x01\n!com.google.cloud.language.v1beta1B\x14LanguageServiceProtoP\x01ZEgoogle.golang.org/genproto/googleapis/cloud/language/v1beta1;languageb\x06proto3')

_ENCODINGTYPE = DESCRIPTOR.enum_types_by_name['EncodingType']
EncodingType = enum_type_wrapper.EnumTypeWrapper(_ENCODINGTYPE)
NONE = 0
UTF8 = 1
UTF16 = 2
UTF32 = 3


_DOCUMENT = DESCRIPTOR.message_types_by_name['Document']
_SENTENCE = DESCRIPTOR.message_types_by_name['Sentence']
_ENTITY = DESCRIPTOR.message_types_by_name['Entity']
_ENTITY_METADATAENTRY = _ENTITY.nested_types_by_name['MetadataEntry']
_TOKEN = DESCRIPTOR.message_types_by_name['Token']
_SENTIMENT = DESCRIPTOR.message_types_by_name['Sentiment']
_PARTOFSPEECH = DESCRIPTOR.message_types_by_name['PartOfSpeech']
_DEPENDENCYEDGE = DESCRIPTOR.message_types_by_name['DependencyEdge']
_ENTITYMENTION = DESCRIPTOR.message_types_by_name['EntityMention']
_TEXTSPAN = DESCRIPTOR.message_types_by_name['TextSpan']
_ANALYZESENTIMENTREQUEST = DESCRIPTOR.message_types_by_name['AnalyzeSentimentRequest']
_ANALYZESENTIMENTRESPONSE = DESCRIPTOR.message_types_by_name['AnalyzeSentimentResponse']
_ANALYZEENTITIESREQUEST = DESCRIPTOR.message_types_by_name['AnalyzeEntitiesRequest']
_ANALYZEENTITIESRESPONSE = DESCRIPTOR.message_types_by_name['AnalyzeEntitiesResponse']
_ANALYZESYNTAXREQUEST = DESCRIPTOR.message_types_by_name['AnalyzeSyntaxRequest']
_ANALYZESYNTAXRESPONSE = DESCRIPTOR.message_types_by_name['AnalyzeSyntaxResponse']
_ANNOTATETEXTREQUEST = DESCRIPTOR.message_types_by_name['AnnotateTextRequest']
_ANNOTATETEXTREQUEST_FEATURES = _ANNOTATETEXTREQUEST.nested_types_by_name['Features']
_ANNOTATETEXTRESPONSE = DESCRIPTOR.message_types_by_name['AnnotateTextResponse']
_DOCUMENT_TYPE = _DOCUMENT.enum_types_by_name['Type']
_ENTITY_TYPE = _ENTITY.enum_types_by_name['Type']
_PARTOFSPEECH_TAG = _PARTOFSPEECH.enum_types_by_name['Tag']
_PARTOFSPEECH_ASPECT = _PARTOFSPEECH.enum_types_by_name['Aspect']
_PARTOFSPEECH_CASE = _PARTOFSPEECH.enum_types_by_name['Case']
_PARTOFSPEECH_FORM = _PARTOFSPEECH.enum_types_by_name['Form']
_PARTOFSPEECH_GENDER = _PARTOFSPEECH.enum_types_by_name['Gender']
_PARTOFSPEECH_MOOD = _PARTOFSPEECH.enum_types_by_name['Mood']
_PARTOFSPEECH_NUMBER = _PARTOFSPEECH.enum_types_by_name['Number']
_PARTOFSPEECH_PERSON = _PARTOFSPEECH.enum_types_by_name['Person']
_PARTOFSPEECH_PROPER = _PARTOFSPEECH.enum_types_by_name['Proper']
_PARTOFSPEECH_RECIPROCITY = _PARTOFSPEECH.enum_types_by_name['Reciprocity']
_PARTOFSPEECH_TENSE = _PARTOFSPEECH.enum_types_by_name['Tense']
_PARTOFSPEECH_VOICE = _PARTOFSPEECH.enum_types_by_name['Voice']
_DEPENDENCYEDGE_LABEL = _DEPENDENCYEDGE.enum_types_by_name['Label']
_ENTITYMENTION_TYPE = _ENTITYMENTION.enum_types_by_name['Type']
Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.Document)
  })
_sym_db.RegisterMessage(Document)

Sentence = _reflection.GeneratedProtocolMessageType('Sentence', (_message.Message,), {
  'DESCRIPTOR' : _SENTENCE,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.Sentence)
  })
_sym_db.RegisterMessage(Sentence)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENTITY_METADATAENTRY,
    '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.Entity.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.Entity)
  })
_sym_db.RegisterMessage(Entity)
_sym_db.RegisterMessage(Entity.MetadataEntry)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.Token)
  })
_sym_db.RegisterMessage(Token)

Sentiment = _reflection.GeneratedProtocolMessageType('Sentiment', (_message.Message,), {
  'DESCRIPTOR' : _SENTIMENT,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.Sentiment)
  })
_sym_db.RegisterMessage(Sentiment)

PartOfSpeech = _reflection.GeneratedProtocolMessageType('PartOfSpeech', (_message.Message,), {
  'DESCRIPTOR' : _PARTOFSPEECH,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.PartOfSpeech)
  })
_sym_db.RegisterMessage(PartOfSpeech)

DependencyEdge = _reflection.GeneratedProtocolMessageType('DependencyEdge', (_message.Message,), {
  'DESCRIPTOR' : _DEPENDENCYEDGE,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.DependencyEdge)
  })
_sym_db.RegisterMessage(DependencyEdge)

EntityMention = _reflection.GeneratedProtocolMessageType('EntityMention', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYMENTION,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.EntityMention)
  })
_sym_db.RegisterMessage(EntityMention)

TextSpan = _reflection.GeneratedProtocolMessageType('TextSpan', (_message.Message,), {
  'DESCRIPTOR' : _TEXTSPAN,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.TextSpan)
  })
_sym_db.RegisterMessage(TextSpan)

AnalyzeSentimentRequest = _reflection.GeneratedProtocolMessageType('AnalyzeSentimentRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZESENTIMENTREQUEST,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.AnalyzeSentimentRequest)
  })
_sym_db.RegisterMessage(AnalyzeSentimentRequest)

AnalyzeSentimentResponse = _reflection.GeneratedProtocolMessageType('AnalyzeSentimentResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZESENTIMENTRESPONSE,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.AnalyzeSentimentResponse)
  })
_sym_db.RegisterMessage(AnalyzeSentimentResponse)

AnalyzeEntitiesRequest = _reflection.GeneratedProtocolMessageType('AnalyzeEntitiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZEENTITIESREQUEST,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.AnalyzeEntitiesRequest)
  })
_sym_db.RegisterMessage(AnalyzeEntitiesRequest)

AnalyzeEntitiesResponse = _reflection.GeneratedProtocolMessageType('AnalyzeEntitiesResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZEENTITIESRESPONSE,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.AnalyzeEntitiesResponse)
  })
_sym_db.RegisterMessage(AnalyzeEntitiesResponse)

AnalyzeSyntaxRequest = _reflection.GeneratedProtocolMessageType('AnalyzeSyntaxRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZESYNTAXREQUEST,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.AnalyzeSyntaxRequest)
  })
_sym_db.RegisterMessage(AnalyzeSyntaxRequest)

AnalyzeSyntaxResponse = _reflection.GeneratedProtocolMessageType('AnalyzeSyntaxResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZESYNTAXRESPONSE,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.AnalyzeSyntaxResponse)
  })
_sym_db.RegisterMessage(AnalyzeSyntaxResponse)

AnnotateTextRequest = _reflection.GeneratedProtocolMessageType('AnnotateTextRequest', (_message.Message,), {

  'Features' : _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), {
    'DESCRIPTOR' : _ANNOTATETEXTREQUEST_FEATURES,
    '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.AnnotateTextRequest.Features)
    })
  ,
  'DESCRIPTOR' : _ANNOTATETEXTREQUEST,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.AnnotateTextRequest)
  })
_sym_db.RegisterMessage(AnnotateTextRequest)
_sym_db.RegisterMessage(AnnotateTextRequest.Features)

AnnotateTextResponse = _reflection.GeneratedProtocolMessageType('AnnotateTextResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANNOTATETEXTRESPONSE,
  '__module__' : 'google.cloud.language.v1beta1.language_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.language.v1beta1.AnnotateTextResponse)
  })
_sym_db.RegisterMessage(AnnotateTextResponse)

_LANGUAGESERVICE = DESCRIPTOR.services_by_name['LanguageService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.cloud.language.v1beta1B\024LanguageServiceProtoP\001ZEgoogle.golang.org/genproto/googleapis/cloud/language/v1beta1;language'
  _ENTITY_METADATAENTRY._options = None
  _ENTITY_METADATAENTRY._serialized_options = b'8\001'
  _LANGUAGESERVICE.methods_by_name['AnalyzeSentiment']._options = None
  _LANGUAGESERVICE.methods_by_name['AnalyzeSentiment']._serialized_options = b'\202\323\344\223\002(\"#/v1beta1/documents:analyzeSentiment:\001*'
  _LANGUAGESERVICE.methods_by_name['AnalyzeEntities']._options = None
  _LANGUAGESERVICE.methods_by_name['AnalyzeEntities']._serialized_options = b'\202\323\344\223\002\'\"\"/v1beta1/documents:analyzeEntities:\001*'
  _LANGUAGESERVICE.methods_by_name['AnalyzeSyntax']._options = None
  _LANGUAGESERVICE.methods_by_name['AnalyzeSyntax']._serialized_options = b'\202\323\344\223\002%\" /v1beta1/documents:analyzeSyntax:\001*'
  _LANGUAGESERVICE.methods_by_name['AnnotateText']._options = None
  _LANGUAGESERVICE.methods_by_name['AnnotateText']._serialized_options = b'\202\323\344\223\002$\"\037/v1beta1/documents:annotateText:\001*'
  _ENCODINGTYPE._serialized_start=6671
  _ENCODINGTYPE._serialized_end=6727
  _DOCUMENT._serialized_start=118
  _DOCUMENT._serialized_end=358
  _DOCUMENT_TYPE._serialized_start=294
  _DOCUMENT_TYPE._serialized_end=348
  _SENTENCE._serialized_start=361
  _SENTENCE._serialized_end=504
  _ENTITY._serialized_start=507
  _ENTITY._serialized_end=966
  _ENTITY_METADATAENTRY._serialized_start=784
  _ENTITY_METADATAENTRY._serialized_end=843
  _ENTITY_TYPE._serialized_start=845
  _ENTITY_TYPE._serialized_end=966
  _TOKEN._serialized_start=969
  _TOKEN._serialized_end=1230
  _SENTIMENT._serialized_start=1232
  _SENTIMENT._serialized_end=1323
  _PARTOFSPEECH._serialized_start=1326
  _PARTOFSPEECH._serialized_end=3559
  _PARTOFSPEECH_TAG._serialized_start=2237
  _PARTOFSPEECH_TAG._serialized_end=2378
  _PARTOFSPEECH_ASPECT._serialized_start=2380
  _PARTOFSPEECH_ASPECT._serialized_end=2459
  _PARTOFSPEECH_CASE._serialized_start=2462
  _PARTOFSPEECH_CASE._serialized_end=2710
  _PARTOFSPEECH_FORM._serialized_start=2713
  _PARTOFSPEECH_FORM._serialized_end=2888
  _PARTOFSPEECH_GENDER._serialized_start=2890
  _PARTOFSPEECH_GENDER._serialized_end=2959
  _PARTOFSPEECH_MOOD._serialized_start=2961
  _PARTOFSPEECH_MOOD._serialized_end=3088
  _PARTOFSPEECH_NUMBER._serialized_start=3090
  _PARTOFSPEECH_NUMBER._serialized_end=3154
  _PARTOFSPEECH_PERSON._serialized_start=3156
  _PARTOFSPEECH_PERSON._serialized_end=3240
  _PARTOFSPEECH_PROPER._serialized_start=3242
  _PARTOFSPEECH_PROPER._serialized_end=3298
  _PARTOFSPEECH_RECIPROCITY._serialized_start=3300
  _PARTOFSPEECH_RECIPROCITY._serialized_end=3374
  _PARTOFSPEECH_TENSE._serialized_start=3376
  _PARTOFSPEECH_TENSE._serialized_end=3491
  _PARTOFSPEECH_VOICE._serialized_start=3493
  _PARTOFSPEECH_VOICE._serialized_end=3559
  _DEPENDENCYEDGE._serialized_start=3562
  _DEPENDENCYEDGE._serialized_end=4574
  _DEPENDENCYEDGE_LABEL._serialized_start=3698
  _DEPENDENCYEDGE_LABEL._serialized_end=4574
  _ENTITYMENTION._serialized_start=4577
  _ENTITYMENTION._serialized_end=4774
  _ENTITYMENTION_TYPE._serialized_start=4726
  _ENTITYMENTION_TYPE._serialized_end=4774
  _TEXTSPAN._serialized_start=4776
  _TEXTSPAN._serialized_end=4847
  _ANALYZESENTIMENTREQUEST._serialized_start=4850
  _ANALYZESENTIMENTREQUEST._serialized_end=5026
  _ANALYZESENTIMENTRESPONSE._serialized_start=5029
  _ANALYZESENTIMENTRESPONSE._serialized_end=5243
  _ANALYZEENTITIESREQUEST._serialized_start=5246
  _ANALYZEENTITIESREQUEST._serialized_end=5421
  _ANALYZEENTITIESRESPONSE._serialized_start=5423
  _ANALYZEENTITIESRESPONSE._serialized_end=5543
  _ANALYZESYNTAXREQUEST._serialized_start=5546
  _ANALYZESYNTAXREQUEST._serialized_end=5719
  _ANALYZESYNTAXRESPONSE._serialized_start=5722
  _ANALYZESYNTAXRESPONSE._serialized_end=5906
  _ANNOTATETEXTREQUEST._serialized_start=5909
  _ANNOTATETEXTREQUEST._serialized_end=6327
  _ANNOTATETEXTREQUEST_FEATURES._serialized_start=6173
  _ANNOTATETEXTREQUEST_FEATURES._serialized_end=6327
  _ANNOTATETEXTRESPONSE._serialized_start=6330
  _ANNOTATETEXTRESPONSE._serialized_end=6669
  _LANGUAGESERVICE._serialized_start=6730
  _LANGUAGESERVICE._serialized_end=7443
# @@protoc_insertion_point(module_scope)
