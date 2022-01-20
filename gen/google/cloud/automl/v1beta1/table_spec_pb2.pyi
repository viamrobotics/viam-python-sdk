"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.automl.v1beta1.io_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TableSpec(google.protobuf.message.Message):
    """A specification of a relational table.
    The table's schema is represented via its child column specs. It is
    pre-populated as part of ImportData by schema inference algorithm, the
    version of which is a required parameter of ImportData InputConfig.
    Note: While working with a table, at times the schema may be
    inconsistent with the data in the table (e.g. string in a FLOAT64 column).
    The consistency validation is done upon creation of a model.
    Used by:
      *   Tables
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    TIME_COLUMN_SPEC_ID_FIELD_NUMBER: builtins.int
    ROW_COUNT_FIELD_NUMBER: builtins.int
    VALID_ROW_COUNT_FIELD_NUMBER: builtins.int
    COLUMN_COUNT_FIELD_NUMBER: builtins.int
    INPUT_CONFIGS_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The resource name of the table spec.
    Form:

    `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/tableSpecs/{table_spec_id}`
    """

    time_column_spec_id: typing.Text = ...
    """column_spec_id of the time column. Only used if the parent dataset's
    ml_use_column_spec_id is not set. Used to split rows into TRAIN, VALIDATE
    and TEST sets such that oldest rows go to TRAIN set, newest to TEST, and
    those in between to VALIDATE.
    Required type: TIMESTAMP.
    If both this column and ml_use_column are not set, then ML use of all rows
    will be assigned by AutoML. NOTE: Updates of this field will instantly
    affect any other users concurrently working with the dataset.
    """

    row_count: builtins.int = ...
    """Output only. The number of rows (i.e. examples) in the table."""

    valid_row_count: builtins.int = ...
    """Output only. The number of valid rows (i.e. without values that don't match
    DataType-s of their columns).
    """

    column_count: builtins.int = ...
    """Output only. The number of columns of the table. That is, the number of
    child ColumnSpec-s.
    """

    @property
    def input_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.automl.v1beta1.io_pb2.InputConfig]:
        """Output only. Input configs via which data currently residing in the table
        had been imported.
        """
        pass
    etag: typing.Text = ...
    """Used to perform consistent read-modify-write updates. If not set, a blind
    "overwrite" update happens.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        time_column_spec_id : typing.Text = ...,
        row_count : builtins.int = ...,
        valid_row_count : builtins.int = ...,
        column_count : builtins.int = ...,
        input_configs : typing.Optional[typing.Iterable[google.cloud.automl.v1beta1.io_pb2.InputConfig]] = ...,
        etag : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["column_count",b"column_count","etag",b"etag","input_configs",b"input_configs","name",b"name","row_count",b"row_count","time_column_spec_id",b"time_column_spec_id","valid_row_count",b"valid_row_count"]) -> None: ...
global___TableSpec = TableSpec
