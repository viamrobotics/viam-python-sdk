"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/client.proto')
_sym_db = _symbol_database.Default()
from ...google.api import launch_stage_pb2 as google_dot_api_dot_launch__stage__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17google/api/client.proto\x12\ngoogle.api\x1a\x1dgoogle/api/launch_stage.proto\x1a google/protobuf/descriptor.proto\x1a\x1egoogle/protobuf/duration.proto"\xf8\x01\n\x16CommonLanguageSettings\x120\n\x12reference_docs_uri\x18\x01 \x01(\tB\x02\x18\x01R\x10referenceDocsUri\x12H\n\x0cdestinations\x18\x02 \x03(\x0e2$.google.api.ClientLibraryDestinationR\x0cdestinations\x12b\n\x1aselective_gapic_generation\x18\x03 \x01(\x0b2$.google.api.SelectiveGapicGenerationR\x18selectiveGapicGeneration"\x93\x05\n\x15ClientLibrarySettings\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12:\n\x0claunch_stage\x18\x02 \x01(\x0e2\x17.google.api.LaunchStageR\x0blaunchStage\x12,\n\x12rest_numeric_enums\x18\x03 \x01(\x08R\x10restNumericEnums\x12=\n\rjava_settings\x18\x15 \x01(\x0b2\x18.google.api.JavaSettingsR\x0cjavaSettings\x12:\n\x0ccpp_settings\x18\x16 \x01(\x0b2\x17.google.api.CppSettingsR\x0bcppSettings\x12:\n\x0cphp_settings\x18\x17 \x01(\x0b2\x17.google.api.PhpSettingsR\x0bphpSettings\x12C\n\x0fpython_settings\x18\x18 \x01(\x0b2\x1a.google.api.PythonSettingsR\x0epythonSettings\x12=\n\rnode_settings\x18\x19 \x01(\x0b2\x18.google.api.NodeSettingsR\x0cnodeSettings\x12C\n\x0fdotnet_settings\x18\x1a \x01(\x0b2\x1a.google.api.DotnetSettingsR\x0edotnetSettings\x12=\n\rruby_settings\x18\x1b \x01(\x0b2\x18.google.api.RubySettingsR\x0crubySettings\x127\n\x0bgo_settings\x18\x1c \x01(\x0b2\x16.google.api.GoSettingsR\ngoSettings"\xf4\x04\n\nPublishing\x12C\n\x0fmethod_settings\x18\x02 \x03(\x0b2\x1a.google.api.MethodSettingsR\x0emethodSettings\x12"\n\rnew_issue_uri\x18e \x01(\tR\x0bnewIssueUri\x12+\n\x11documentation_uri\x18f \x01(\tR\x10documentationUri\x12$\n\x0eapi_short_name\x18g \x01(\tR\x0capiShortName\x12!\n\x0cgithub_label\x18h \x01(\tR\x0bgithubLabel\x124\n\x16codeowner_github_teams\x18i \x03(\tR\x14codeownerGithubTeams\x12$\n\x0edoc_tag_prefix\x18j \x01(\tR\x0cdocTagPrefix\x12I\n\x0corganization\x18k \x01(\x0e2%.google.api.ClientLibraryOrganizationR\x0corganization\x12L\n\x10library_settings\x18m \x03(\x0b2!.google.api.ClientLibrarySettingsR\x0flibrarySettings\x12I\n!proto_reference_documentation_uri\x18n \x01(\tR\x1eprotoReferenceDocumentationUri\x12G\n rest_reference_documentation_uri\x18o \x01(\tR\x1drestReferenceDocumentationUri"\x9a\x02\n\x0cJavaSettings\x12\'\n\x0flibrary_package\x18\x01 \x01(\tR\x0elibraryPackage\x12_\n\x13service_class_names\x18\x02 \x03(\x0b2/.google.api.JavaSettings.ServiceClassNamesEntryR\x11serviceClassNames\x12:\n\x06common\x18\x03 \x01(\x0b2".google.api.CommonLanguageSettingsR\x06common\x1aD\n\x16ServiceClassNamesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"I\n\x0bCppSettings\x12:\n\x06common\x18\x01 \x01(\x0b2".google.api.CommonLanguageSettingsR\x06common"I\n\x0bPhpSettings\x12:\n\x06common\x18\x01 \x01(\x0b2".google.api.CommonLanguageSettingsR\x06common"\x87\x03\n\x0ePythonSettings\x12:\n\x06common\x18\x01 \x01(\x0b2".google.api.CommonLanguageSettingsR\x06common\x12d\n\x15experimental_features\x18\x02 \x01(\x0b2/.google.api.PythonSettings.ExperimentalFeaturesR\x14experimentalFeatures\x1a\xd2\x01\n\x14ExperimentalFeatures\x121\n\x15rest_async_io_enabled\x18\x01 \x01(\x08R\x12restAsyncIoEnabled\x12E\n\x1fprotobuf_pythonic_types_enabled\x18\x02 \x01(\x08R\x1cprotobufPythonicTypesEnabled\x12@\n\x1cunversioned_package_disabled\x18\x03 \x01(\x08R\x1aunversionedPackageDisabled"J\n\x0cNodeSettings\x12:\n\x06common\x18\x01 \x01(\x0b2".google.api.CommonLanguageSettingsR\x06common"\xae\x04\n\x0eDotnetSettings\x12:\n\x06common\x18\x01 \x01(\x0b2".google.api.CommonLanguageSettingsR\x06common\x12Z\n\x10renamed_services\x18\x02 \x03(\x0b2/.google.api.DotnetSettings.RenamedServicesEntryR\x0frenamedServices\x12]\n\x11renamed_resources\x18\x03 \x03(\x0b20.google.api.DotnetSettings.RenamedResourcesEntryR\x10renamedResources\x12+\n\x11ignored_resources\x18\x04 \x03(\tR\x10ignoredResources\x128\n\x18forced_namespace_aliases\x18\x05 \x03(\tR\x16forcedNamespaceAliases\x125\n\x16handwritten_signatures\x18\x06 \x03(\tR\x15handwrittenSignatures\x1aB\n\x14RenamedServicesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01\x1aC\n\x15RenamedResourcesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"J\n\x0cRubySettings\x12:\n\x06common\x18\x01 \x01(\x0b2".google.api.CommonLanguageSettingsR\x06common"\xe4\x01\n\nGoSettings\x12:\n\x06common\x18\x01 \x01(\x0b2".google.api.CommonLanguageSettingsR\x06common\x12V\n\x10renamed_services\x18\x02 \x03(\x0b2+.google.api.GoSettings.RenamedServicesEntryR\x0frenamedServices\x1aB\n\x14RenamedServicesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\xc2\x03\n\x0eMethodSettings\x12\x1a\n\x08selector\x18\x01 \x01(\tR\x08selector\x12I\n\x0clong_running\x18\x02 \x01(\x0b2&.google.api.MethodSettings.LongRunningR\x0blongRunning\x122\n\x15auto_populated_fields\x18\x03 \x03(\tR\x13autoPopulatedFields\x1a\x94\x02\n\x0bLongRunning\x12G\n\x12initial_poll_delay\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationR\x10initialPollDelay\x122\n\x15poll_delay_multiplier\x18\x02 \x01(\x02R\x13pollDelayMultiplier\x12?\n\x0emax_poll_delay\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationR\x0cmaxPollDelay\x12G\n\x12total_poll_timeout\x18\x04 \x01(\x0b2\x19.google.protobuf.DurationR\x10totalPollTimeout"u\n\x18SelectiveGapicGeneration\x12\x18\n\x07methods\x18\x01 \x03(\tR\x07methods\x12?\n\x1cgenerate_omitted_as_internal\x18\x02 \x01(\x08R\x19generateOmittedAsInternal*\xa3\x01\n\x19ClientLibraryOrganization\x12+\n\'CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED\x10\x00\x12\t\n\x05CLOUD\x10\x01\x12\x07\n\x03ADS\x10\x02\x12\n\n\x06PHOTOS\x10\x03\x12\x0f\n\x0bSTREET_VIEW\x10\x04\x12\x0c\n\x08SHOPPING\x10\x05\x12\x07\n\x03GEO\x10\x06\x12\x11\n\rGENERATIVE_AI\x10\x07*g\n\x18ClientLibraryDestination\x12*\n&CLIENT_LIBRARY_DESTINATION_UNSPECIFIED\x10\x00\x12\n\n\x06GITHUB\x10\n\x12\x13\n\x0fPACKAGE_MANAGER\x10\x14:J\n\x10method_signature\x12\x1e.google.protobuf.MethodOptions\x18\x9b\x08 \x03(\tR\x0fmethodSignature:C\n\x0cdefault_host\x12\x1f.google.protobuf.ServiceOptions\x18\x99\x08 \x01(\tR\x0bdefaultHost:C\n\x0coauth_scopes\x12\x1f.google.protobuf.ServiceOptions\x18\x9a\x08 \x01(\tR\x0boauthScopes:D\n\x0bapi_version\x12\x1f.google.protobuf.ServiceOptions\x18\xc1\xba\xab\xfa\x01 \x01(\tR\napiVersionBi\n\x0ecom.google.apiB\x0bClientProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.client_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x0bClientProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPI'
    _globals['_COMMONLANGUAGESETTINGS'].fields_by_name['reference_docs_uri']._loaded_options = None
    _globals['_COMMONLANGUAGESETTINGS'].fields_by_name['reference_docs_uri']._serialized_options = b'\x18\x01'
    _globals['_JAVASETTINGS_SERVICECLASSNAMESENTRY']._loaded_options = None
    _globals['_JAVASETTINGS_SERVICECLASSNAMESENTRY']._serialized_options = b'8\x01'
    _globals['_DOTNETSETTINGS_RENAMEDSERVICESENTRY']._loaded_options = None
    _globals['_DOTNETSETTINGS_RENAMEDSERVICESENTRY']._serialized_options = b'8\x01'
    _globals['_DOTNETSETTINGS_RENAMEDRESOURCESENTRY']._loaded_options = None
    _globals['_DOTNETSETTINGS_RENAMEDRESOURCESENTRY']._serialized_options = b'8\x01'
    _globals['_GOSETTINGS_RENAMEDSERVICESENTRY']._loaded_options = None
    _globals['_GOSETTINGS_RENAMEDSERVICESENTRY']._serialized_options = b'8\x01'
    _globals['_CLIENTLIBRARYORGANIZATION']._serialized_start = 4026
    _globals['_CLIENTLIBRARYORGANIZATION']._serialized_end = 4189
    _globals['_CLIENTLIBRARYDESTINATION']._serialized_start = 4191
    _globals['_CLIENTLIBRARYDESTINATION']._serialized_end = 4294
    _globals['_COMMONLANGUAGESETTINGS']._serialized_start = 137
    _globals['_COMMONLANGUAGESETTINGS']._serialized_end = 385
    _globals['_CLIENTLIBRARYSETTINGS']._serialized_start = 388
    _globals['_CLIENTLIBRARYSETTINGS']._serialized_end = 1047
    _globals['_PUBLISHING']._serialized_start = 1050
    _globals['_PUBLISHING']._serialized_end = 1678
    _globals['_JAVASETTINGS']._serialized_start = 1681
    _globals['_JAVASETTINGS']._serialized_end = 1963
    _globals['_JAVASETTINGS_SERVICECLASSNAMESENTRY']._serialized_start = 1895
    _globals['_JAVASETTINGS_SERVICECLASSNAMESENTRY']._serialized_end = 1963
    _globals['_CPPSETTINGS']._serialized_start = 1965
    _globals['_CPPSETTINGS']._serialized_end = 2038
    _globals['_PHPSETTINGS']._serialized_start = 2040
    _globals['_PHPSETTINGS']._serialized_end = 2113
    _globals['_PYTHONSETTINGS']._serialized_start = 2116
    _globals['_PYTHONSETTINGS']._serialized_end = 2507
    _globals['_PYTHONSETTINGS_EXPERIMENTALFEATURES']._serialized_start = 2297
    _globals['_PYTHONSETTINGS_EXPERIMENTALFEATURES']._serialized_end = 2507
    _globals['_NODESETTINGS']._serialized_start = 2509
    _globals['_NODESETTINGS']._serialized_end = 2583
    _globals['_DOTNETSETTINGS']._serialized_start = 2586
    _globals['_DOTNETSETTINGS']._serialized_end = 3144
    _globals['_DOTNETSETTINGS_RENAMEDSERVICESENTRY']._serialized_start = 3009
    _globals['_DOTNETSETTINGS_RENAMEDSERVICESENTRY']._serialized_end = 3075
    _globals['_DOTNETSETTINGS_RENAMEDRESOURCESENTRY']._serialized_start = 3077
    _globals['_DOTNETSETTINGS_RENAMEDRESOURCESENTRY']._serialized_end = 3144
    _globals['_RUBYSETTINGS']._serialized_start = 3146
    _globals['_RUBYSETTINGS']._serialized_end = 3220
    _globals['_GOSETTINGS']._serialized_start = 3223
    _globals['_GOSETTINGS']._serialized_end = 3451
    _globals['_GOSETTINGS_RENAMEDSERVICESENTRY']._serialized_start = 3009
    _globals['_GOSETTINGS_RENAMEDSERVICESENTRY']._serialized_end = 3075
    _globals['_METHODSETTINGS']._serialized_start = 3454
    _globals['_METHODSETTINGS']._serialized_end = 3904
    _globals['_METHODSETTINGS_LONGRUNNING']._serialized_start = 3628
    _globals['_METHODSETTINGS_LONGRUNNING']._serialized_end = 3904
    _globals['_SELECTIVEGAPICGENERATION']._serialized_start = 3906
    _globals['_SELECTIVEGAPICGENERATION']._serialized_end = 4023