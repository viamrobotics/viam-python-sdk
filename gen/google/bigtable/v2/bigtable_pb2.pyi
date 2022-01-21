"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.bigtable.v2.data_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ReadRowsRequest(google.protobuf.message.Message):
    """Request message for Bigtable.ReadRows."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TABLE_NAME_FIELD_NUMBER: builtins.int
    APP_PROFILE_ID_FIELD_NUMBER: builtins.int
    ROWS_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ROWS_LIMIT_FIELD_NUMBER: builtins.int
    table_name: typing.Text = ...
    """Required. The unique name of the table from which to read.
    Values are of the form
    `projects/<project>/instances/<instance>/tables/<table>`.
    """

    app_profile_id: typing.Text = ...
    """This value specifies routing for replication. If not specified, the
    "default" application profile will be used.
    """

    @property
    def rows(self) -> google.bigtable.v2.data_pb2.RowSet:
        """The row keys and/or ranges to read sequentially. If not specified, reads
        from all rows.
        """
        pass
    @property
    def filter(self) -> google.bigtable.v2.data_pb2.RowFilter:
        """The filter to apply to the contents of the specified row(s). If unset,
        reads the entirety of each row.
        """
        pass
    rows_limit: builtins.int = ...
    """The read will stop after committing to N rows' worth of results. The
    default (zero) is to return all results.
    """

    def __init__(self,
        *,
        table_name : typing.Text = ...,
        app_profile_id : typing.Text = ...,
        rows : typing.Optional[google.bigtable.v2.data_pb2.RowSet] = ...,
        filter : typing.Optional[google.bigtable.v2.data_pb2.RowFilter] = ...,
        rows_limit : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter",b"filter","rows",b"rows"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_profile_id",b"app_profile_id","filter",b"filter","rows",b"rows","rows_limit",b"rows_limit","table_name",b"table_name"]) -> None: ...
global___ReadRowsRequest = ReadRowsRequest

class ReadRowsResponse(google.protobuf.message.Message):
    """Response message for Bigtable.ReadRows."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class CellChunk(google.protobuf.message.Message):
        """Specifies a piece of a row's contents returned as part of the read
        response stream.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        ROW_KEY_FIELD_NUMBER: builtins.int
        FAMILY_NAME_FIELD_NUMBER: builtins.int
        QUALIFIER_FIELD_NUMBER: builtins.int
        TIMESTAMP_MICROS_FIELD_NUMBER: builtins.int
        LABELS_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        VALUE_SIZE_FIELD_NUMBER: builtins.int
        RESET_ROW_FIELD_NUMBER: builtins.int
        COMMIT_ROW_FIELD_NUMBER: builtins.int
        row_key: builtins.bytes = ...
        """The row key for this chunk of data.  If the row key is empty,
        this CellChunk is a continuation of the same row as the previous
        CellChunk in the response stream, even if that CellChunk was in a
        previous ReadRowsResponse message.
        """

        @property
        def family_name(self) -> google.protobuf.wrappers_pb2.StringValue:
            """The column family name for this chunk of data.  If this message
            is not present this CellChunk is a continuation of the same column
            family as the previous CellChunk.  The empty string can occur as a
            column family name in a response so clients must check
            explicitly for the presence of this message, not just for
            `family_name.value` being non-empty.
            """
            pass
        @property
        def qualifier(self) -> google.protobuf.wrappers_pb2.BytesValue:
            """The column qualifier for this chunk of data.  If this message
            is not present, this CellChunk is a continuation of the same column
            as the previous CellChunk.  Column qualifiers may be empty so
            clients must check for the presence of this message, not just
            for `qualifier.value` being non-empty.
            """
            pass
        timestamp_micros: builtins.int = ...
        """The cell's stored timestamp, which also uniquely identifies it
        within its column.  Values are always expressed in
        microseconds, but individual tables may set a coarser
        granularity to further restrict the allowed values. For
        example, a table which specifies millisecond granularity will
        only allow values of `timestamp_micros` which are multiples of
        1000.  Timestamps are only set in the first CellChunk per cell
        (for cells split into multiple chunks).
        """

        @property
        def labels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """Labels applied to the cell by a
            [RowFilter][google.bigtable.v2.RowFilter].  Labels are only set
            on the first CellChunk per cell.
            """
            pass
        value: builtins.bytes = ...
        """The value stored in the cell.  Cell values can be split across
        multiple CellChunks.  In that case only the value field will be
        set in CellChunks after the first: the timestamp and labels
        will only be present in the first CellChunk, even if the first
        CellChunk came in a previous ReadRowsResponse.
        """

        value_size: builtins.int = ...
        """If this CellChunk is part of a chunked cell value and this is
        not the final chunk of that cell, value_size will be set to the
        total length of the cell value.  The client can use this size
        to pre-allocate memory to hold the full cell value.
        """

        reset_row: builtins.bool = ...
        """Indicates that the client should drop all previous chunks for
        `row_key`, as it will be re-read from the beginning.
        """

        commit_row: builtins.bool = ...
        """Indicates that the client can safely process all previous chunks for
        `row_key`, as its data has been fully read.
        """

        def __init__(self,
            *,
            row_key : builtins.bytes = ...,
            family_name : typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
            qualifier : typing.Optional[google.protobuf.wrappers_pb2.BytesValue] = ...,
            timestamp_micros : builtins.int = ...,
            labels : typing.Optional[typing.Iterable[typing.Text]] = ...,
            value : builtins.bytes = ...,
            value_size : builtins.int = ...,
            reset_row : builtins.bool = ...,
            commit_row : builtins.bool = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["commit_row",b"commit_row","family_name",b"family_name","qualifier",b"qualifier","reset_row",b"reset_row","row_status",b"row_status"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["commit_row",b"commit_row","family_name",b"family_name","labels",b"labels","qualifier",b"qualifier","reset_row",b"reset_row","row_key",b"row_key","row_status",b"row_status","timestamp_micros",b"timestamp_micros","value",b"value","value_size",b"value_size"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["row_status",b"row_status"]) -> typing.Optional[typing_extensions.Literal["reset_row","commit_row"]]: ...

    CHUNKS_FIELD_NUMBER: builtins.int
    LAST_SCANNED_ROW_KEY_FIELD_NUMBER: builtins.int
    @property
    def chunks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ReadRowsResponse.CellChunk]:
        """A collection of a row's contents as part of the read request."""
        pass
    last_scanned_row_key: builtins.bytes = ...
    """Optionally the server might return the row key of the last row it
    has scanned.  The client can use this to construct a more
    efficient retry request if needed: any row keys or portions of
    ranges less than this row key can be dropped from the request.
    This is primarily useful for cases where the server has read a
    lot of data that was filtered out since the last committed row
    key, allowing the client to skip that work on a retry.
    """

    def __init__(self,
        *,
        chunks : typing.Optional[typing.Iterable[global___ReadRowsResponse.CellChunk]] = ...,
        last_scanned_row_key : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chunks",b"chunks","last_scanned_row_key",b"last_scanned_row_key"]) -> None: ...
global___ReadRowsResponse = ReadRowsResponse

class SampleRowKeysRequest(google.protobuf.message.Message):
    """Request message for Bigtable.SampleRowKeys."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TABLE_NAME_FIELD_NUMBER: builtins.int
    APP_PROFILE_ID_FIELD_NUMBER: builtins.int
    table_name: typing.Text = ...
    """Required. The unique name of the table from which to sample row keys.
    Values are of the form
    `projects/<project>/instances/<instance>/tables/<table>`.
    """

    app_profile_id: typing.Text = ...
    """This value specifies routing for replication. If not specified, the
    "default" application profile will be used.
    """

    def __init__(self,
        *,
        table_name : typing.Text = ...,
        app_profile_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_profile_id",b"app_profile_id","table_name",b"table_name"]) -> None: ...
global___SampleRowKeysRequest = SampleRowKeysRequest

class SampleRowKeysResponse(google.protobuf.message.Message):
    """Response message for Bigtable.SampleRowKeys."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ROW_KEY_FIELD_NUMBER: builtins.int
    OFFSET_BYTES_FIELD_NUMBER: builtins.int
    row_key: builtins.bytes = ...
    """Sorted streamed sequence of sample row keys in the table. The table might
    have contents before the first row key in the list and after the last one,
    but a key containing the empty string indicates "end of table" and will be
    the last response given, if present.
    Note that row keys in this list may not have ever been written to or read
    from, and users should therefore not make any assumptions about the row key
    structure that are specific to their use case.
    """

    offset_bytes: builtins.int = ...
    """Approximate total storage space used by all rows in the table which precede
    `row_key`. Buffering the contents of all rows between two subsequent
    samples would require space roughly equal to the difference in their
    `offset_bytes` fields.
    """

    def __init__(self,
        *,
        row_key : builtins.bytes = ...,
        offset_bytes : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["offset_bytes",b"offset_bytes","row_key",b"row_key"]) -> None: ...
global___SampleRowKeysResponse = SampleRowKeysResponse

class MutateRowRequest(google.protobuf.message.Message):
    """Request message for Bigtable.MutateRow."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TABLE_NAME_FIELD_NUMBER: builtins.int
    APP_PROFILE_ID_FIELD_NUMBER: builtins.int
    ROW_KEY_FIELD_NUMBER: builtins.int
    MUTATIONS_FIELD_NUMBER: builtins.int
    table_name: typing.Text = ...
    """Required. The unique name of the table to which the mutation should be applied.
    Values are of the form
    `projects/<project>/instances/<instance>/tables/<table>`.
    """

    app_profile_id: typing.Text = ...
    """This value specifies routing for replication. If not specified, the
    "default" application profile will be used.
    """

    row_key: builtins.bytes = ...
    """Required. The key of the row to which the mutation should be applied."""

    @property
    def mutations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.bigtable.v2.data_pb2.Mutation]:
        """Required. Changes to be atomically applied to the specified row. Entries are applied
        in order, meaning that earlier mutations can be masked by later ones.
        Must contain at least one entry and at most 100000.
        """
        pass
    def __init__(self,
        *,
        table_name : typing.Text = ...,
        app_profile_id : typing.Text = ...,
        row_key : builtins.bytes = ...,
        mutations : typing.Optional[typing.Iterable[google.bigtable.v2.data_pb2.Mutation]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_profile_id",b"app_profile_id","mutations",b"mutations","row_key",b"row_key","table_name",b"table_name"]) -> None: ...
global___MutateRowRequest = MutateRowRequest

class MutateRowResponse(google.protobuf.message.Message):
    """Response message for Bigtable.MutateRow."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MutateRowResponse = MutateRowResponse

class MutateRowsRequest(google.protobuf.message.Message):
    """Request message for BigtableService.MutateRows."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Entry(google.protobuf.message.Message):
        """A mutation for a given row."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        ROW_KEY_FIELD_NUMBER: builtins.int
        MUTATIONS_FIELD_NUMBER: builtins.int
        row_key: builtins.bytes = ...
        """The key of the row to which the `mutations` should be applied."""

        @property
        def mutations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.bigtable.v2.data_pb2.Mutation]:
            """Required. Changes to be atomically applied to the specified row. Mutations are
            applied in order, meaning that earlier mutations can be masked by
            later ones.
            You must specify at least one mutation.
            """
            pass
        def __init__(self,
            *,
            row_key : builtins.bytes = ...,
            mutations : typing.Optional[typing.Iterable[google.bigtable.v2.data_pb2.Mutation]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["mutations",b"mutations","row_key",b"row_key"]) -> None: ...

    TABLE_NAME_FIELD_NUMBER: builtins.int
    APP_PROFILE_ID_FIELD_NUMBER: builtins.int
    ENTRIES_FIELD_NUMBER: builtins.int
    table_name: typing.Text = ...
    """Required. The unique name of the table to which the mutations should be applied."""

    app_profile_id: typing.Text = ...
    """This value specifies routing for replication. If not specified, the
    "default" application profile will be used.
    """

    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MutateRowsRequest.Entry]:
        """Required. The row keys and corresponding mutations to be applied in bulk.
        Each entry is applied as an atomic mutation, but the entries may be
        applied in arbitrary order (even between entries for the same row).
        At least one entry must be specified, and in total the entries can
        contain at most 100000 mutations.
        """
        pass
    def __init__(self,
        *,
        table_name : typing.Text = ...,
        app_profile_id : typing.Text = ...,
        entries : typing.Optional[typing.Iterable[global___MutateRowsRequest.Entry]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_profile_id",b"app_profile_id","entries",b"entries","table_name",b"table_name"]) -> None: ...
global___MutateRowsRequest = MutateRowsRequest

class MutateRowsResponse(google.protobuf.message.Message):
    """Response message for BigtableService.MutateRows."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Entry(google.protobuf.message.Message):
        """The result of applying a passed mutation in the original request."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        INDEX_FIELD_NUMBER: builtins.int
        STATUS_FIELD_NUMBER: builtins.int
        index: builtins.int = ...
        """The index into the original request's `entries` list of the Entry
        for which a result is being reported.
        """

        @property
        def status(self) -> google.rpc.status_pb2.Status:
            """The result of the request Entry identified by `index`.
            Depending on how requests are batched during execution, it is possible
            for one Entry to fail due to an error with another Entry. In the event
            that this occurs, the same error will be reported for both entries.
            """
            pass
        def __init__(self,
            *,
            index : builtins.int = ...,
            status : typing.Optional[google.rpc.status_pb2.Status] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["status",b"status"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["index",b"index","status",b"status"]) -> None: ...

    ENTRIES_FIELD_NUMBER: builtins.int
    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MutateRowsResponse.Entry]:
        """One or more results for Entries from the batch request."""
        pass
    def __init__(self,
        *,
        entries : typing.Optional[typing.Iterable[global___MutateRowsResponse.Entry]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entries",b"entries"]) -> None: ...
global___MutateRowsResponse = MutateRowsResponse

class CheckAndMutateRowRequest(google.protobuf.message.Message):
    """Request message for Bigtable.CheckAndMutateRow."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TABLE_NAME_FIELD_NUMBER: builtins.int
    APP_PROFILE_ID_FIELD_NUMBER: builtins.int
    ROW_KEY_FIELD_NUMBER: builtins.int
    PREDICATE_FILTER_FIELD_NUMBER: builtins.int
    TRUE_MUTATIONS_FIELD_NUMBER: builtins.int
    FALSE_MUTATIONS_FIELD_NUMBER: builtins.int
    table_name: typing.Text = ...
    """Required. The unique name of the table to which the conditional mutation should be
    applied.
    Values are of the form
    `projects/<project>/instances/<instance>/tables/<table>`.
    """

    app_profile_id: typing.Text = ...
    """This value specifies routing for replication. If not specified, the
    "default" application profile will be used.
    """

    row_key: builtins.bytes = ...
    """Required. The key of the row to which the conditional mutation should be applied."""

    @property
    def predicate_filter(self) -> google.bigtable.v2.data_pb2.RowFilter:
        """The filter to be applied to the contents of the specified row. Depending
        on whether or not any results are yielded, either `true_mutations` or
        `false_mutations` will be executed. If unset, checks that the row contains
        any values at all.
        """
        pass
    @property
    def true_mutations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.bigtable.v2.data_pb2.Mutation]:
        """Changes to be atomically applied to the specified row if `predicate_filter`
        yields at least one cell when applied to `row_key`. Entries are applied in
        order, meaning that earlier mutations can be masked by later ones.
        Must contain at least one entry if `false_mutations` is empty, and at most
        100000.
        """
        pass
    @property
    def false_mutations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.bigtable.v2.data_pb2.Mutation]:
        """Changes to be atomically applied to the specified row if `predicate_filter`
        does not yield any cells when applied to `row_key`. Entries are applied in
        order, meaning that earlier mutations can be masked by later ones.
        Must contain at least one entry if `true_mutations` is empty, and at most
        100000.
        """
        pass
    def __init__(self,
        *,
        table_name : typing.Text = ...,
        app_profile_id : typing.Text = ...,
        row_key : builtins.bytes = ...,
        predicate_filter : typing.Optional[google.bigtable.v2.data_pb2.RowFilter] = ...,
        true_mutations : typing.Optional[typing.Iterable[google.bigtable.v2.data_pb2.Mutation]] = ...,
        false_mutations : typing.Optional[typing.Iterable[google.bigtable.v2.data_pb2.Mutation]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["predicate_filter",b"predicate_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_profile_id",b"app_profile_id","false_mutations",b"false_mutations","predicate_filter",b"predicate_filter","row_key",b"row_key","table_name",b"table_name","true_mutations",b"true_mutations"]) -> None: ...
global___CheckAndMutateRowRequest = CheckAndMutateRowRequest

class CheckAndMutateRowResponse(google.protobuf.message.Message):
    """Response message for Bigtable.CheckAndMutateRow."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PREDICATE_MATCHED_FIELD_NUMBER: builtins.int
    predicate_matched: builtins.bool = ...
    """Whether or not the request's `predicate_filter` yielded any results for
    the specified row.
    """

    def __init__(self,
        *,
        predicate_matched : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["predicate_matched",b"predicate_matched"]) -> None: ...
global___CheckAndMutateRowResponse = CheckAndMutateRowResponse

class ReadModifyWriteRowRequest(google.protobuf.message.Message):
    """Request message for Bigtable.ReadModifyWriteRow."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TABLE_NAME_FIELD_NUMBER: builtins.int
    APP_PROFILE_ID_FIELD_NUMBER: builtins.int
    ROW_KEY_FIELD_NUMBER: builtins.int
    RULES_FIELD_NUMBER: builtins.int
    table_name: typing.Text = ...
    """Required. The unique name of the table to which the read/modify/write rules should be
    applied.
    Values are of the form
    `projects/<project>/instances/<instance>/tables/<table>`.
    """

    app_profile_id: typing.Text = ...
    """This value specifies routing for replication. If not specified, the
    "default" application profile will be used.
    """

    row_key: builtins.bytes = ...
    """Required. The key of the row to which the read/modify/write rules should be applied."""

    @property
    def rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.bigtable.v2.data_pb2.ReadModifyWriteRule]:
        """Required. Rules specifying how the specified row's contents are to be transformed
        into writes. Entries are applied in order, meaning that earlier rules will
        affect the results of later ones.
        """
        pass
    def __init__(self,
        *,
        table_name : typing.Text = ...,
        app_profile_id : typing.Text = ...,
        row_key : builtins.bytes = ...,
        rules : typing.Optional[typing.Iterable[google.bigtable.v2.data_pb2.ReadModifyWriteRule]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_profile_id",b"app_profile_id","row_key",b"row_key","rules",b"rules","table_name",b"table_name"]) -> None: ...
global___ReadModifyWriteRowRequest = ReadModifyWriteRowRequest

class ReadModifyWriteRowResponse(google.protobuf.message.Message):
    """Response message for Bigtable.ReadModifyWriteRow."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ROW_FIELD_NUMBER: builtins.int
    @property
    def row(self) -> google.bigtable.v2.data_pb2.Row:
        """A Row containing the new contents of all cells modified by the request."""
        pass
    def __init__(self,
        *,
        row : typing.Optional[google.bigtable.v2.data_pb2.Row] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["row",b"row"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["row",b"row"]) -> None: ...
global___ReadModifyWriteRowResponse = ReadModifyWriteRowResponse
