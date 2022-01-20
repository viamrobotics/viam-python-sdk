# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/study.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/aiplatform/v1/study.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xf5\x03\n\x05Study\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\'\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0b\x64isplayName\x12J\n\nstudy_spec\x18\x03 \x01(\x0b\x32%.google.cloud.aiplatform.v1.StudySpecB\x04\xe2\x41\x01\x02R\tstudySpec\x12\x43\n\x05state\x18\x04 \x01(\x0e\x32\'.google.cloud.aiplatform.v1.Study.StateB\x04\xe2\x41\x01\x03R\x05state\x12\x41\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12-\n\x0finactive_reason\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03R\x0einactiveReason\"G\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\x12\r\n\tCOMPLETED\x10\x03:]\xea\x41Z\n\x1f\x61iplatform.googleapis.com/Study\x12\x37projects/{project}/locations/{location}/studies/{study}\"\x85\t\n\x05Trial\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\x14\n\x02id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x02id\x12\x43\n\x05state\x18\x03 \x01(\x0e\x32\'.google.cloud.aiplatform.v1.Trial.StateB\x04\xe2\x41\x01\x03R\x05state\x12Q\n\nparameters\x18\x04 \x03(\x0b\x32+.google.cloud.aiplatform.v1.Trial.ParameterB\x04\xe2\x41\x01\x03R\nparameters\x12Z\n\x11\x66inal_measurement\x18\x05 \x01(\x0b\x32\'.google.cloud.aiplatform.v1.MeasurementB\x04\xe2\x41\x01\x03R\x10\x66inalMeasurement\x12Q\n\x0cmeasurements\x18\x06 \x03(\x0b\x32\'.google.cloud.aiplatform.v1.MeasurementB\x04\xe2\x41\x01\x03R\x0cmeasurements\x12?\n\nstart_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\tstartTime\x12;\n\x08\x65nd_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x07\x65ndTime\x12!\n\tclient_id\x18\t \x01(\tB\x04\xe2\x41\x01\x03R\x08\x63lientId\x12\x31\n\x11infeasible_reason\x18\n \x01(\tB\x04\xe2\x41\x01\x03R\x10infeasibleReason\x12K\n\ncustom_job\x18\x0b \x01(\tB,\xe2\x41\x01\x03\xfa\x41%\n#aiplatform.googleapis.com/CustomJobR\tcustomJob\x12\x62\n\x0fweb_access_uris\x18\x0c \x03(\x0b\x32\x34.google.cloud.aiplatform.v1.Trial.WebAccessUrisEntryB\x04\xe2\x41\x01\x03R\rwebAccessUris\x1ah\n\tParameter\x12\'\n\x0cparameter_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x0bparameterId\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueB\x04\xe2\x41\x01\x03R\x05value\x1a@\n\x12WebAccessUrisEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"f\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tREQUESTED\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08STOPPING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\x0e\n\nINFEASIBLE\x10\x05:l\xea\x41i\n\x1f\x61iplatform.googleapis.com/Trial\x12\x46projects/{project}/locations/{location}/studies/{study}/trials/{trial}\"\xc5\x1c\n\tStudySpec\x12\x82\x01\n\x19\x64\x65\x63\x61y_curve_stopping_spec\x18\x04 \x01(\x0b\x32\x45.google.cloud.aiplatform.v1.StudySpec.DecayCurveAutomatedStoppingSpecH\x00R\x16\x64\x65\x63\x61yCurveStoppingSpec\x12\x88\x01\n\x1emedian_automated_stopping_spec\x18\x05 \x01(\x0b\x32\x41.google.cloud.aiplatform.v1.StudySpec.MedianAutomatedStoppingSpecH\x00R\x1bmedianAutomatedStoppingSpec\x12P\n\x07metrics\x18\x01 \x03(\x0b\x32\x30.google.cloud.aiplatform.v1.StudySpec.MetricSpecB\x04\xe2\x41\x01\x02R\x07metrics\x12Y\n\nparameters\x18\x02 \x03(\x0b\x32\x33.google.cloud.aiplatform.v1.StudySpec.ParameterSpecB\x04\xe2\x41\x01\x02R\nparameters\x12M\n\talgorithm\x18\x03 \x01(\x0e\x32/.google.cloud.aiplatform.v1.StudySpec.AlgorithmR\talgorithm\x12\x63\n\x11observation_noise\x18\x06 \x01(\x0e\x32\x36.google.cloud.aiplatform.v1.StudySpec.ObservationNoiseR\x10observationNoise\x12|\n\x1ameasurement_selection_type\x18\x07 \x01(\x0e\x32>.google.cloud.aiplatform.v1.StudySpec.MeasurementSelectionTypeR\x18measurementSelectionType\x1a\xc7\x01\n\nMetricSpec\x12!\n\tmetric_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08metricId\x12S\n\x04goal\x18\x02 \x01(\x0e\x32\x39.google.cloud.aiplatform.v1.StudySpec.MetricSpec.GoalTypeB\x04\xe2\x41\x01\x02R\x04goal\"A\n\x08GoalType\x12\x19\n\x15GOAL_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08MAXIMIZE\x10\x01\x12\x0c\n\x08MINIMIZE\x10\x02\x1a\xb3\x11\n\rParameterSpec\x12q\n\x11\x64ouble_value_spec\x18\x02 \x01(\x0b\x32\x43.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DoubleValueSpecH\x00R\x0f\x64oubleValueSpec\x12t\n\x12integer_value_spec\x18\x03 \x01(\x0b\x32\x44.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.IntegerValueSpecH\x00R\x10integerValueSpec\x12\x80\x01\n\x16\x63\x61tegorical_value_spec\x18\x04 \x01(\x0b\x32H.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.CategoricalValueSpecH\x00R\x14\x63\x61tegoricalValueSpec\x12w\n\x13\x64iscrete_value_spec\x18\x05 \x01(\x0b\x32\x45.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DiscreteValueSpecH\x00R\x11\x64iscreteValueSpec\x12\'\n\x0cparameter_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0bparameterId\x12\\\n\nscale_type\x18\x06 \x01(\x0e\x32=.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ScaleTypeR\tscaleType\x12\x8c\x01\n\x1b\x63onditional_parameter_specs\x18\n \x03(\x0b\x32L.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpecR\x19\x63onditionalParameterSpecs\x1a\x93\x01\n\x0f\x44oubleValueSpec\x12!\n\tmin_value\x18\x01 \x01(\x01\x42\x04\xe2\x41\x01\x02R\x08minValue\x12!\n\tmax_value\x18\x02 \x01(\x01\x42\x04\xe2\x41\x01\x02R\x08maxValue\x12(\n\rdefault_value\x18\x04 \x01(\x01H\x00R\x0c\x64\x65\x66\x61ultValue\x88\x01\x01\x42\x10\n\x0e_default_value\x1a\x94\x01\n\x10IntegerValueSpec\x12!\n\tmin_value\x18\x01 \x01(\x03\x42\x04\xe2\x41\x01\x02R\x08minValue\x12!\n\tmax_value\x18\x02 \x01(\x03\x42\x04\xe2\x41\x01\x02R\x08maxValue\x12(\n\rdefault_value\x18\x04 \x01(\x03H\x00R\x0c\x64\x65\x66\x61ultValue\x88\x01\x01\x42\x10\n\x0e_default_value\x1ap\n\x14\x43\x61tegoricalValueSpec\x12\x1c\n\x06values\x18\x01 \x03(\tB\x04\xe2\x41\x01\x02R\x06values\x12(\n\rdefault_value\x18\x03 \x01(\tH\x00R\x0c\x64\x65\x66\x61ultValue\x88\x01\x01\x42\x10\n\x0e_default_value\x1am\n\x11\x44iscreteValueSpec\x12\x1c\n\x06values\x18\x01 \x03(\x01\x42\x04\xe2\x41\x01\x02R\x06values\x12(\n\rdefault_value\x18\x03 \x01(\x01H\x00R\x0c\x64\x65\x66\x61ultValue\x88\x01\x01\x42\x10\n\x0e_default_value\x1a\x90\x06\n\x18\x43onditionalParameterSpec\x12\x9b\x01\n\x16parent_discrete_values\x18\x02 \x01(\x0b\x32\x63.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.DiscreteValueConditionH\x00R\x14parentDiscreteValues\x12\x8c\x01\n\x11parent_int_values\x18\x03 \x01(\x0b\x32^.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.IntValueConditionH\x00R\x0fparentIntValues\x12\xa4\x01\n\x19parent_categorical_values\x18\x04 \x01(\x0b\x32\x66.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.CategoricalValueConditionH\x00R\x17parentCategoricalValues\x12`\n\x0eparameter_spec\x18\x01 \x01(\x0b\x32\x33.google.cloud.aiplatform.v1.StudySpec.ParameterSpecB\x04\xe2\x41\x01\x02R\rparameterSpec\x1a\x36\n\x16\x44iscreteValueCondition\x12\x1c\n\x06values\x18\x01 \x03(\x01\x42\x04\xe2\x41\x01\x02R\x06values\x1a\x31\n\x11IntValueCondition\x12\x1c\n\x06values\x18\x01 \x03(\x03\x42\x04\xe2\x41\x01\x02R\x06values\x1a\x39\n\x19\x43\x61tegoricalValueCondition\x12\x1c\n\x06values\x18\x01 \x03(\tB\x04\xe2\x41\x01\x02R\x06valuesB\x18\n\x16parent_value_condition\"n\n\tScaleType\x12\x1a\n\x16SCALE_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11UNIT_LINEAR_SCALE\x10\x01\x12\x12\n\x0eUNIT_LOG_SCALE\x10\x02\x12\x1a\n\x16UNIT_REVERSE_LOG_SCALE\x10\x03\x42\x16\n\x14parameter_value_spec\x1aS\n\x1f\x44\x65\x63\x61yCurveAutomatedStoppingSpec\x12\x30\n\x14use_elapsed_duration\x18\x01 \x01(\x08R\x12useElapsedDuration\x1aO\n\x1bMedianAutomatedStoppingSpec\x12\x30\n\x14use_elapsed_duration\x18\x01 \x01(\x08R\x12useElapsedDuration\"J\n\tAlgorithm\x12\x19\n\x15\x41LGORITHM_UNSPECIFIED\x10\x00\x12\x0f\n\x0bGRID_SEARCH\x10\x02\x12\x11\n\rRANDOM_SEARCH\x10\x03\"H\n\x10ObservationNoise\x12!\n\x1dOBSERVATION_NOISE_UNSPECIFIED\x10\x00\x12\x07\n\x03LOW\x10\x01\x12\x08\n\x04HIGH\x10\x02\"r\n\x18MeasurementSelectionType\x12*\n&MEASUREMENT_SELECTION_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10LAST_MEASUREMENT\x10\x01\x12\x14\n\x10\x42\x45ST_MEASUREMENT\x10\x02\x42\x19\n\x17\x61utomated_stopping_spec\"\x97\x02\n\x0bMeasurement\x12J\n\x10\x65lapsed_duration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe2\x41\x01\x03R\x0f\x65lapsedDuration\x12#\n\nstep_count\x18\x02 \x01(\x03\x42\x04\xe2\x41\x01\x03R\tstepCount\x12N\n\x07metrics\x18\x03 \x03(\x0b\x32..google.cloud.aiplatform.v1.Measurement.MetricB\x04\xe2\x41\x01\x03R\x07metrics\x1aG\n\x06Metric\x12!\n\tmetric_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x08metricId\x12\x1a\n\x05value\x18\x02 \x01(\x01\x42\x04\xe2\x41\x01\x03R\x05valueB\xce\x01\n\x1e\x63om.google.cloud.aiplatform.v1B\nStudyProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')



_STUDY = DESCRIPTOR.message_types_by_name['Study']
_TRIAL = DESCRIPTOR.message_types_by_name['Trial']
_TRIAL_PARAMETER = _TRIAL.nested_types_by_name['Parameter']
_TRIAL_WEBACCESSURISENTRY = _TRIAL.nested_types_by_name['WebAccessUrisEntry']
_STUDYSPEC = DESCRIPTOR.message_types_by_name['StudySpec']
_STUDYSPEC_METRICSPEC = _STUDYSPEC.nested_types_by_name['MetricSpec']
_STUDYSPEC_PARAMETERSPEC = _STUDYSPEC.nested_types_by_name['ParameterSpec']
_STUDYSPEC_PARAMETERSPEC_DOUBLEVALUESPEC = _STUDYSPEC_PARAMETERSPEC.nested_types_by_name['DoubleValueSpec']
_STUDYSPEC_PARAMETERSPEC_INTEGERVALUESPEC = _STUDYSPEC_PARAMETERSPEC.nested_types_by_name['IntegerValueSpec']
_STUDYSPEC_PARAMETERSPEC_CATEGORICALVALUESPEC = _STUDYSPEC_PARAMETERSPEC.nested_types_by_name['CategoricalValueSpec']
_STUDYSPEC_PARAMETERSPEC_DISCRETEVALUESPEC = _STUDYSPEC_PARAMETERSPEC.nested_types_by_name['DiscreteValueSpec']
_STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC = _STUDYSPEC_PARAMETERSPEC.nested_types_by_name['ConditionalParameterSpec']
_STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_DISCRETEVALUECONDITION = _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC.nested_types_by_name['DiscreteValueCondition']
_STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_INTVALUECONDITION = _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC.nested_types_by_name['IntValueCondition']
_STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_CATEGORICALVALUECONDITION = _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC.nested_types_by_name['CategoricalValueCondition']
_STUDYSPEC_DECAYCURVEAUTOMATEDSTOPPINGSPEC = _STUDYSPEC.nested_types_by_name['DecayCurveAutomatedStoppingSpec']
_STUDYSPEC_MEDIANAUTOMATEDSTOPPINGSPEC = _STUDYSPEC.nested_types_by_name['MedianAutomatedStoppingSpec']
_MEASUREMENT = DESCRIPTOR.message_types_by_name['Measurement']
_MEASUREMENT_METRIC = _MEASUREMENT.nested_types_by_name['Metric']
_STUDY_STATE = _STUDY.enum_types_by_name['State']
_TRIAL_STATE = _TRIAL.enum_types_by_name['State']
_STUDYSPEC_METRICSPEC_GOALTYPE = _STUDYSPEC_METRICSPEC.enum_types_by_name['GoalType']
_STUDYSPEC_PARAMETERSPEC_SCALETYPE = _STUDYSPEC_PARAMETERSPEC.enum_types_by_name['ScaleType']
_STUDYSPEC_ALGORITHM = _STUDYSPEC.enum_types_by_name['Algorithm']
_STUDYSPEC_OBSERVATIONNOISE = _STUDYSPEC.enum_types_by_name['ObservationNoise']
_STUDYSPEC_MEASUREMENTSELECTIONTYPE = _STUDYSPEC.enum_types_by_name['MeasurementSelectionType']
Study = _reflection.GeneratedProtocolMessageType('Study', (_message.Message,), {
  'DESCRIPTOR' : _STUDY,
  '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.Study)
  })
_sym_db.RegisterMessage(Study)

Trial = _reflection.GeneratedProtocolMessageType('Trial', (_message.Message,), {

  'Parameter' : _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), {
    'DESCRIPTOR' : _TRIAL_PARAMETER,
    '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.Trial.Parameter)
    })
  ,

  'WebAccessUrisEntry' : _reflection.GeneratedProtocolMessageType('WebAccessUrisEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRIAL_WEBACCESSURISENTRY,
    '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.Trial.WebAccessUrisEntry)
    })
  ,
  'DESCRIPTOR' : _TRIAL,
  '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.Trial)
  })
_sym_db.RegisterMessage(Trial)
_sym_db.RegisterMessage(Trial.Parameter)
_sym_db.RegisterMessage(Trial.WebAccessUrisEntry)

StudySpec = _reflection.GeneratedProtocolMessageType('StudySpec', (_message.Message,), {

  'MetricSpec' : _reflection.GeneratedProtocolMessageType('MetricSpec', (_message.Message,), {
    'DESCRIPTOR' : _STUDYSPEC_METRICSPEC,
    '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.MetricSpec)
    })
  ,

  'ParameterSpec' : _reflection.GeneratedProtocolMessageType('ParameterSpec', (_message.Message,), {

    'DoubleValueSpec' : _reflection.GeneratedProtocolMessageType('DoubleValueSpec', (_message.Message,), {
      'DESCRIPTOR' : _STUDYSPEC_PARAMETERSPEC_DOUBLEVALUESPEC,
      '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DoubleValueSpec)
      })
    ,

    'IntegerValueSpec' : _reflection.GeneratedProtocolMessageType('IntegerValueSpec', (_message.Message,), {
      'DESCRIPTOR' : _STUDYSPEC_PARAMETERSPEC_INTEGERVALUESPEC,
      '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.ParameterSpec.IntegerValueSpec)
      })
    ,

    'CategoricalValueSpec' : _reflection.GeneratedProtocolMessageType('CategoricalValueSpec', (_message.Message,), {
      'DESCRIPTOR' : _STUDYSPEC_PARAMETERSPEC_CATEGORICALVALUESPEC,
      '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.ParameterSpec.CategoricalValueSpec)
      })
    ,

    'DiscreteValueSpec' : _reflection.GeneratedProtocolMessageType('DiscreteValueSpec', (_message.Message,), {
      'DESCRIPTOR' : _STUDYSPEC_PARAMETERSPEC_DISCRETEVALUESPEC,
      '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DiscreteValueSpec)
      })
    ,

    'ConditionalParameterSpec' : _reflection.GeneratedProtocolMessageType('ConditionalParameterSpec', (_message.Message,), {

      'DiscreteValueCondition' : _reflection.GeneratedProtocolMessageType('DiscreteValueCondition', (_message.Message,), {
        'DESCRIPTOR' : _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_DISCRETEVALUECONDITION,
        '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.DiscreteValueCondition)
        })
      ,

      'IntValueCondition' : _reflection.GeneratedProtocolMessageType('IntValueCondition', (_message.Message,), {
        'DESCRIPTOR' : _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_INTVALUECONDITION,
        '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.IntValueCondition)
        })
      ,

      'CategoricalValueCondition' : _reflection.GeneratedProtocolMessageType('CategoricalValueCondition', (_message.Message,), {
        'DESCRIPTOR' : _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_CATEGORICALVALUECONDITION,
        '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
        # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.CategoricalValueCondition)
        })
      ,
      'DESCRIPTOR' : _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC,
      '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec)
      })
    ,
    'DESCRIPTOR' : _STUDYSPEC_PARAMETERSPEC,
    '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.ParameterSpec)
    })
  ,

  'DecayCurveAutomatedStoppingSpec' : _reflection.GeneratedProtocolMessageType('DecayCurveAutomatedStoppingSpec', (_message.Message,), {
    'DESCRIPTOR' : _STUDYSPEC_DECAYCURVEAUTOMATEDSTOPPINGSPEC,
    '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.DecayCurveAutomatedStoppingSpec)
    })
  ,

  'MedianAutomatedStoppingSpec' : _reflection.GeneratedProtocolMessageType('MedianAutomatedStoppingSpec', (_message.Message,), {
    'DESCRIPTOR' : _STUDYSPEC_MEDIANAUTOMATEDSTOPPINGSPEC,
    '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec.MedianAutomatedStoppingSpec)
    })
  ,
  'DESCRIPTOR' : _STUDYSPEC,
  '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StudySpec)
  })
_sym_db.RegisterMessage(StudySpec)
_sym_db.RegisterMessage(StudySpec.MetricSpec)
_sym_db.RegisterMessage(StudySpec.ParameterSpec)
_sym_db.RegisterMessage(StudySpec.ParameterSpec.DoubleValueSpec)
_sym_db.RegisterMessage(StudySpec.ParameterSpec.IntegerValueSpec)
_sym_db.RegisterMessage(StudySpec.ParameterSpec.CategoricalValueSpec)
_sym_db.RegisterMessage(StudySpec.ParameterSpec.DiscreteValueSpec)
_sym_db.RegisterMessage(StudySpec.ParameterSpec.ConditionalParameterSpec)
_sym_db.RegisterMessage(StudySpec.ParameterSpec.ConditionalParameterSpec.DiscreteValueCondition)
_sym_db.RegisterMessage(StudySpec.ParameterSpec.ConditionalParameterSpec.IntValueCondition)
_sym_db.RegisterMessage(StudySpec.ParameterSpec.ConditionalParameterSpec.CategoricalValueCondition)
_sym_db.RegisterMessage(StudySpec.DecayCurveAutomatedStoppingSpec)
_sym_db.RegisterMessage(StudySpec.MedianAutomatedStoppingSpec)

Measurement = _reflection.GeneratedProtocolMessageType('Measurement', (_message.Message,), {

  'Metric' : _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
    'DESCRIPTOR' : _MEASUREMENT_METRIC,
    '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.Measurement.Metric)
    })
  ,
  'DESCRIPTOR' : _MEASUREMENT,
  '__module__' : 'google.cloud.aiplatform.v1.study_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.Measurement)
  })
_sym_db.RegisterMessage(Measurement)
_sym_db.RegisterMessage(Measurement.Metric)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.google.cloud.aiplatform.v1B\nStudyProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\252\002\032Google.Cloud.AIPlatform.V1\312\002\032Google\\Cloud\\AIPlatform\\V1\352\002\035Google::Cloud::AIPlatform::V1'
  _STUDY.fields_by_name['name']._options = None
  _STUDY.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _STUDY.fields_by_name['display_name']._options = None
  _STUDY.fields_by_name['display_name']._serialized_options = b'\342A\001\002'
  _STUDY.fields_by_name['study_spec']._options = None
  _STUDY.fields_by_name['study_spec']._serialized_options = b'\342A\001\002'
  _STUDY.fields_by_name['state']._options = None
  _STUDY.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _STUDY.fields_by_name['create_time']._options = None
  _STUDY.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _STUDY.fields_by_name['inactive_reason']._options = None
  _STUDY.fields_by_name['inactive_reason']._serialized_options = b'\342A\001\003'
  _STUDY._options = None
  _STUDY._serialized_options = b'\352AZ\n\037aiplatform.googleapis.com/Study\0227projects/{project}/locations/{location}/studies/{study}'
  _TRIAL_PARAMETER.fields_by_name['parameter_id']._options = None
  _TRIAL_PARAMETER.fields_by_name['parameter_id']._serialized_options = b'\342A\001\003'
  _TRIAL_PARAMETER.fields_by_name['value']._options = None
  _TRIAL_PARAMETER.fields_by_name['value']._serialized_options = b'\342A\001\003'
  _TRIAL_WEBACCESSURISENTRY._options = None
  _TRIAL_WEBACCESSURISENTRY._serialized_options = b'8\001'
  _TRIAL.fields_by_name['name']._options = None
  _TRIAL.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _TRIAL.fields_by_name['id']._options = None
  _TRIAL.fields_by_name['id']._serialized_options = b'\342A\001\003'
  _TRIAL.fields_by_name['state']._options = None
  _TRIAL.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _TRIAL.fields_by_name['parameters']._options = None
  _TRIAL.fields_by_name['parameters']._serialized_options = b'\342A\001\003'
  _TRIAL.fields_by_name['final_measurement']._options = None
  _TRIAL.fields_by_name['final_measurement']._serialized_options = b'\342A\001\003'
  _TRIAL.fields_by_name['measurements']._options = None
  _TRIAL.fields_by_name['measurements']._serialized_options = b'\342A\001\003'
  _TRIAL.fields_by_name['start_time']._options = None
  _TRIAL.fields_by_name['start_time']._serialized_options = b'\342A\001\003'
  _TRIAL.fields_by_name['end_time']._options = None
  _TRIAL.fields_by_name['end_time']._serialized_options = b'\342A\001\003'
  _TRIAL.fields_by_name['client_id']._options = None
  _TRIAL.fields_by_name['client_id']._serialized_options = b'\342A\001\003'
  _TRIAL.fields_by_name['infeasible_reason']._options = None
  _TRIAL.fields_by_name['infeasible_reason']._serialized_options = b'\342A\001\003'
  _TRIAL.fields_by_name['custom_job']._options = None
  _TRIAL.fields_by_name['custom_job']._serialized_options = b'\342A\001\003\372A%\n#aiplatform.googleapis.com/CustomJob'
  _TRIAL.fields_by_name['web_access_uris']._options = None
  _TRIAL.fields_by_name['web_access_uris']._serialized_options = b'\342A\001\003'
  _TRIAL._options = None
  _TRIAL._serialized_options = b'\352Ai\n\037aiplatform.googleapis.com/Trial\022Fprojects/{project}/locations/{location}/studies/{study}/trials/{trial}'
  _STUDYSPEC_METRICSPEC.fields_by_name['metric_id']._options = None
  _STUDYSPEC_METRICSPEC.fields_by_name['metric_id']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_METRICSPEC.fields_by_name['goal']._options = None
  _STUDYSPEC_METRICSPEC.fields_by_name['goal']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC_DOUBLEVALUESPEC.fields_by_name['min_value']._options = None
  _STUDYSPEC_PARAMETERSPEC_DOUBLEVALUESPEC.fields_by_name['min_value']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC_DOUBLEVALUESPEC.fields_by_name['max_value']._options = None
  _STUDYSPEC_PARAMETERSPEC_DOUBLEVALUESPEC.fields_by_name['max_value']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC_INTEGERVALUESPEC.fields_by_name['min_value']._options = None
  _STUDYSPEC_PARAMETERSPEC_INTEGERVALUESPEC.fields_by_name['min_value']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC_INTEGERVALUESPEC.fields_by_name['max_value']._options = None
  _STUDYSPEC_PARAMETERSPEC_INTEGERVALUESPEC.fields_by_name['max_value']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC_CATEGORICALVALUESPEC.fields_by_name['values']._options = None
  _STUDYSPEC_PARAMETERSPEC_CATEGORICALVALUESPEC.fields_by_name['values']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC_DISCRETEVALUESPEC.fields_by_name['values']._options = None
  _STUDYSPEC_PARAMETERSPEC_DISCRETEVALUESPEC.fields_by_name['values']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_DISCRETEVALUECONDITION.fields_by_name['values']._options = None
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_DISCRETEVALUECONDITION.fields_by_name['values']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_INTVALUECONDITION.fields_by_name['values']._options = None
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_INTVALUECONDITION.fields_by_name['values']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_CATEGORICALVALUECONDITION.fields_by_name['values']._options = None
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_CATEGORICALVALUECONDITION.fields_by_name['values']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC.fields_by_name['parameter_spec']._options = None
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC.fields_by_name['parameter_spec']._serialized_options = b'\342A\001\002'
  _STUDYSPEC_PARAMETERSPEC.fields_by_name['parameter_id']._options = None
  _STUDYSPEC_PARAMETERSPEC.fields_by_name['parameter_id']._serialized_options = b'\342A\001\002'
  _STUDYSPEC.fields_by_name['metrics']._options = None
  _STUDYSPEC.fields_by_name['metrics']._serialized_options = b'\342A\001\002'
  _STUDYSPEC.fields_by_name['parameters']._options = None
  _STUDYSPEC.fields_by_name['parameters']._serialized_options = b'\342A\001\002'
  _MEASUREMENT_METRIC.fields_by_name['metric_id']._options = None
  _MEASUREMENT_METRIC.fields_by_name['metric_id']._serialized_options = b'\342A\001\003'
  _MEASUREMENT_METRIC.fields_by_name['value']._options = None
  _MEASUREMENT_METRIC.fields_by_name['value']._serialized_options = b'\342A\001\003'
  _MEASUREMENT.fields_by_name['elapsed_duration']._options = None
  _MEASUREMENT.fields_by_name['elapsed_duration']._serialized_options = b'\342A\001\003'
  _MEASUREMENT.fields_by_name['step_count']._options = None
  _MEASUREMENT.fields_by_name['step_count']._serialized_options = b'\342A\001\003'
  _MEASUREMENT.fields_by_name['metrics']._options = None
  _MEASUREMENT.fields_by_name['metrics']._serialized_options = b'\342A\001\003'
  _STUDY._serialized_start=256
  _STUDY._serialized_end=757
  _STUDY_STATE._serialized_start=591
  _STUDY_STATE._serialized_end=662
  _TRIAL._serialized_start=760
  _TRIAL._serialized_end=1917
  _TRIAL_PARAMETER._serialized_start=1533
  _TRIAL_PARAMETER._serialized_end=1637
  _TRIAL_WEBACCESSURISENTRY._serialized_start=1639
  _TRIAL_WEBACCESSURISENTRY._serialized_end=1703
  _TRIAL_STATE._serialized_start=1705
  _TRIAL_STATE._serialized_end=1807
  _STUDYSPEC._serialized_start=1920
  _STUDYSPEC._serialized_end=5573
  _STUDYSPEC_METRICSPEC._serialized_start=2685
  _STUDYSPEC_METRICSPEC._serialized_end=2884
  _STUDYSPEC_METRICSPEC_GOALTYPE._serialized_start=2819
  _STUDYSPEC_METRICSPEC_GOALTYPE._serialized_end=2884
  _STUDYSPEC_PARAMETERSPEC._serialized_start=2887
  _STUDYSPEC_PARAMETERSPEC._serialized_end=5114
  _STUDYSPEC_PARAMETERSPEC_DOUBLEVALUESPEC._serialized_start=3668
  _STUDYSPEC_PARAMETERSPEC_DOUBLEVALUESPEC._serialized_end=3815
  _STUDYSPEC_PARAMETERSPEC_INTEGERVALUESPEC._serialized_start=3818
  _STUDYSPEC_PARAMETERSPEC_INTEGERVALUESPEC._serialized_end=3966
  _STUDYSPEC_PARAMETERSPEC_CATEGORICALVALUESPEC._serialized_start=3968
  _STUDYSPEC_PARAMETERSPEC_CATEGORICALVALUESPEC._serialized_end=4080
  _STUDYSPEC_PARAMETERSPEC_DISCRETEVALUESPEC._serialized_start=4082
  _STUDYSPEC_PARAMETERSPEC_DISCRETEVALUESPEC._serialized_end=4191
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC._serialized_start=4194
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC._serialized_end=4978
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_DISCRETEVALUECONDITION._serialized_start=4788
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_DISCRETEVALUECONDITION._serialized_end=4842
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_INTVALUECONDITION._serialized_start=4844
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_INTVALUECONDITION._serialized_end=4893
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_CATEGORICALVALUECONDITION._serialized_start=4895
  _STUDYSPEC_PARAMETERSPEC_CONDITIONALPARAMETERSPEC_CATEGORICALVALUECONDITION._serialized_end=4952
  _STUDYSPEC_PARAMETERSPEC_SCALETYPE._serialized_start=4980
  _STUDYSPEC_PARAMETERSPEC_SCALETYPE._serialized_end=5090
  _STUDYSPEC_DECAYCURVEAUTOMATEDSTOPPINGSPEC._serialized_start=5116
  _STUDYSPEC_DECAYCURVEAUTOMATEDSTOPPINGSPEC._serialized_end=5199
  _STUDYSPEC_MEDIANAUTOMATEDSTOPPINGSPEC._serialized_start=5201
  _STUDYSPEC_MEDIANAUTOMATEDSTOPPINGSPEC._serialized_end=5280
  _STUDYSPEC_ALGORITHM._serialized_start=5282
  _STUDYSPEC_ALGORITHM._serialized_end=5356
  _STUDYSPEC_OBSERVATIONNOISE._serialized_start=5358
  _STUDYSPEC_OBSERVATIONNOISE._serialized_end=5430
  _STUDYSPEC_MEASUREMENTSELECTIONTYPE._serialized_start=5432
  _STUDYSPEC_MEASUREMENTSELECTIONTYPE._serialized_end=5546
  _MEASUREMENT._serialized_start=5576
  _MEASUREMENT._serialized_end=5855
  _MEASUREMENT_METRIC._serialized_start=5784
  _MEASUREMENT_METRIC._serialized_end=5855
# @@protoc_insertion_point(module_scope)
