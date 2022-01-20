"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CommandTask(google.protobuf.message.Message):
    """Describes a shell-style task to execute, suitable for providing as the Bots
    interface's `Lease.payload` field.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Inputs(google.protobuf.message.Message):
        """Describes the inputs to a shell-style task."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class EnvironmentVariable(google.protobuf.message.Message):
            """An environment variable required by this task."""
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            NAME_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            name: typing.Text = ...
            """The envvar name."""

            value: typing.Text = ...
            """The envvar value."""

            def __init__(self,
                *,
                name : typing.Text = ...,
                value : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["name",b"name","value",b"value"]) -> None: ...

        ARGUMENTS_FIELD_NUMBER: builtins.int
        FILES_FIELD_NUMBER: builtins.int
        INLINE_BLOBS_FIELD_NUMBER: builtins.int
        ENVIRONMENT_VARIABLES_FIELD_NUMBER: builtins.int
        WORKING_DIRECTORY_FIELD_NUMBER: builtins.int
        @property
        def arguments(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """The command itself to run (e.g., argv).

            This field should be passed directly to the underlying operating system,
            and so it must be sensible to that operating system. For example, on
            Windows, the first argument might be "C:\\Windows\\System32\\ping.exe" -
            that is, using drive letters and backslashes. A command for a *nix
            system, on the other hand, would use forward slashes.

            All other fields in the RWAPI must consistently use forward slashes,
            since those fields may be interpretted by both the service and the bot.
            """
            pass
        @property
        def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Digest]:
            """The input filesystem to be set up prior to the task beginning. The
            contents should be a repeated set of FileMetadata messages though other
            formats are allowed if better for the implementation (eg, a LUCI-style
            .isolated file).

            This field is repeated since implementations might want to cache the
            metadata, in which case it may be useful to break up portions of the
            filesystem that change frequently (eg, specific input files) from those
            that don't (eg, standard header files).
            """
            pass
        @property
        def inline_blobs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Blob]:
            """Inline contents for blobs expected to be needed by the bot to execute the
            task. For example, contents of entries in `files` or blobs that are
            indirectly referenced by an entry there.

            The bot should check against this list before downloading required task
            inputs to reduce the number of communications between itself and the
            remote CAS server.
            """
            pass
        @property
        def environment_variables(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CommandTask.Inputs.EnvironmentVariable]:
            """All environment variables required by the task."""
            pass
        working_directory: typing.Text = ...
        """Directory from which a command is executed. It is a relative directory
        with respect to the bot's working directory (i.e., "./"). If it is
        non-empty, then it must exist under "./". Otherwise, "./" will be used.
        """

        def __init__(self,
            *,
            arguments : typing.Optional[typing.Iterable[typing.Text]] = ...,
            files : typing.Optional[typing.Iterable[global___Digest]] = ...,
            inline_blobs : typing.Optional[typing.Iterable[global___Blob]] = ...,
            environment_variables : typing.Optional[typing.Iterable[global___CommandTask.Inputs.EnvironmentVariable]] = ...,
            working_directory : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["arguments",b"arguments","environment_variables",b"environment_variables","files",b"files","inline_blobs",b"inline_blobs","working_directory",b"working_directory"]) -> None: ...

    class Outputs(google.protobuf.message.Message):
        """Describes the expected outputs of the command."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        FILES_FIELD_NUMBER: builtins.int
        DIRECTORIES_FIELD_NUMBER: builtins.int
        STDOUT_DESTINATION_FIELD_NUMBER: builtins.int
        STDERR_DESTINATION_FIELD_NUMBER: builtins.int
        @property
        def files(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """A list of expected files, relative to the execution root. All paths
            MUST be delimited by forward slashes.
            """
            pass
        @property
        def directories(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """A list of expected directories, relative to the execution root. All paths
            MUST be delimited by forward slashes.
            """
            pass
        stdout_destination: typing.Text = ...
        """The destination to which any stdout should be sent. The method by which
        the bot should send the stream contents to that destination is not
        defined in this API. As examples, the destination could be a file
        referenced in the `files` field in this message, or it could be a URI
        that must be written via the ByteStream API.
        """

        stderr_destination: typing.Text = ...
        """The destination to which any stderr should be sent. The method by which
        the bot should send the stream contents to that destination is not
        defined in this API. As examples, the destination could be a file
        referenced in the `files` field in this message, or it could be a URI
        that must be written via the ByteStream API.
        """

        def __init__(self,
            *,
            files : typing.Optional[typing.Iterable[typing.Text]] = ...,
            directories : typing.Optional[typing.Iterable[typing.Text]] = ...,
            stdout_destination : typing.Text = ...,
            stderr_destination : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["directories",b"directories","files",b"files","stderr_destination",b"stderr_destination","stdout_destination",b"stdout_destination"]) -> None: ...

    class Timeouts(google.protobuf.message.Message):
        """Describes the timeouts associated with this task."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        EXECUTION_FIELD_NUMBER: builtins.int
        IDLE_FIELD_NUMBER: builtins.int
        SHUTDOWN_FIELD_NUMBER: builtins.int
        @property
        def execution(self) -> google.protobuf.duration_pb2.Duration:
            """This specifies the maximum time that the task can run, excluding the
            time required to download inputs or upload outputs. That is, the worker
            will terminate the task if it runs longer than this.
            """
            pass
        @property
        def idle(self) -> google.protobuf.duration_pb2.Duration:
            """This specifies the maximum amount of time the task can be idle - that is,
            go without generating some output in either stdout or stderr. If the
            process is silent for more than the specified time, the worker will
            terminate the task.
            """
            pass
        @property
        def shutdown(self) -> google.protobuf.duration_pb2.Duration:
            """If the execution or IO timeouts are exceeded, the worker will try to
            gracefully terminate the task and return any existing logs. However,
            tasks may be hard-frozen in which case this process will fail. This
            timeout specifies how long to wait for a terminated task to shut down
            gracefully (e.g. via SIGTERM) before we bring down the hammer (e.g.
            SIGKILL on *nix, CTRL_BREAK_EVENT on Windows).
            """
            pass
        def __init__(self,
            *,
            execution : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
            idle : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
            shutdown : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["execution",b"execution","idle",b"idle","shutdown",b"shutdown"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["execution",b"execution","idle",b"idle","shutdown",b"shutdown"]) -> None: ...

    INPUTS_FIELD_NUMBER: builtins.int
    EXPECTED_OUTPUTS_FIELD_NUMBER: builtins.int
    TIMEOUTS_FIELD_NUMBER: builtins.int
    @property
    def inputs(self) -> global___CommandTask.Inputs:
        """The inputs to the task."""
        pass
    @property
    def expected_outputs(self) -> global___CommandTask.Outputs:
        """The expected outputs from the task."""
        pass
    @property
    def timeouts(self) -> global___CommandTask.Timeouts:
        """The timeouts of this task."""
        pass
    def __init__(self,
        *,
        inputs : typing.Optional[global___CommandTask.Inputs] = ...,
        expected_outputs : typing.Optional[global___CommandTask.Outputs] = ...,
        timeouts : typing.Optional[global___CommandTask.Timeouts] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expected_outputs",b"expected_outputs","inputs",b"inputs","timeouts",b"timeouts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expected_outputs",b"expected_outputs","inputs",b"inputs","timeouts",b"timeouts"]) -> None: ...
global___CommandTask = CommandTask

class CommandOutputs(google.protobuf.message.Message):
    """DEPRECATED - use CommandResult instead.
    Describes the actual outputs from the task.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXIT_CODE_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    exit_code: builtins.int = ...
    """exit_code is only fully reliable if the status' code is OK. If the task
    exceeded its deadline or was cancelled, the process may still produce an
    exit code as it is cancelled, and this will be populated, but a successful
    (zero) is unlikely to be correct unless the status code is OK.
    """

    @property
    def outputs(self) -> global___Digest:
        """The output files. The blob referenced by the digest should contain
        one of the following (implementation-dependent):
           * A marshalled DirectoryMetadata of the returned filesystem
           * A LUCI-style .isolated file
        """
        pass
    def __init__(self,
        *,
        exit_code : builtins.int = ...,
        outputs : typing.Optional[global___Digest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["outputs",b"outputs"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["exit_code",b"exit_code","outputs",b"outputs"]) -> None: ...
global___CommandOutputs = CommandOutputs

class CommandOverhead(google.protobuf.message.Message):
    """DEPRECATED - use CommandResult instead.
    Can be used as part of CompleteRequest.metadata, or are part of a more
    sophisticated message.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DURATION_FIELD_NUMBER: builtins.int
    OVERHEAD_FIELD_NUMBER: builtins.int
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration:
        """The elapsed time between calling Accept and Complete. The server will also
        have its own idea of what this should be, but this excludes the overhead of
        the RPCs and the bot response time.
        """
        pass
    @property
    def overhead(self) -> google.protobuf.duration_pb2.Duration:
        """The amount of time *not* spent executing the command (ie
        uploading/downloading files).
        """
        pass
    def __init__(self,
        *,
        duration : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        overhead : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration",b"duration","overhead",b"overhead"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration",b"duration","overhead",b"overhead"]) -> None: ...
global___CommandOverhead = CommandOverhead

class CommandResult(google.protobuf.message.Message):
    """All information about the execution of a command, suitable for providing as
    the Bots interface's `Lease.result` field.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int
    EXIT_CODE_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    OVERHEAD_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    @property
    def status(self) -> google.rpc.status_pb2.Status:
        """An overall status for the command. For example, if the command timed out,
        this might have a code of DEADLINE_EXCEEDED; if it was killed by the OS for
        memory exhaustion, it might have a code of RESOURCE_EXHAUSTED.
        """
        pass
    exit_code: builtins.int = ...
    """The exit code of the process. An exit code of "0" should only be trusted if
    `status` has a code of OK (otherwise it may simply be unset).
    """

    @property
    def outputs(self) -> global___Digest:
        """The output files. The blob referenced by the digest should contain
        one of the following (implementation-dependent):
           * A marshalled DirectoryMetadata of the returned filesystem
           * A LUCI-style .isolated file
        """
        pass
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration:
        """The elapsed time between calling Accept and Complete. The server will also
        have its own idea of what this should be, but this excludes the overhead of
        the RPCs and the bot response time.
        """
        pass
    @property
    def overhead(self) -> google.protobuf.duration_pb2.Duration:
        """The amount of time *not* spent executing the command (ie
        uploading/downloading files).
        """
        pass
    @property
    def metadata(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """Implementation-dependent metadata about the task. Both servers and bots
        may define messages which can be encoded here; bots are free to provide
        metadata in multiple formats, and servers are free to choose one or more
        of the values to process and ignore others. In particular, it is *not*
        considered an error for the bot to provide the server with a field that it
        doesn't know about.
        """
        pass
    def __init__(self,
        *,
        status : typing.Optional[google.rpc.status_pb2.Status] = ...,
        exit_code : builtins.int = ...,
        outputs : typing.Optional[global___Digest] = ...,
        duration : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        overhead : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        metadata : typing.Optional[typing.Iterable[google.protobuf.any_pb2.Any]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration",b"duration","outputs",b"outputs","overhead",b"overhead","status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration",b"duration","exit_code",b"exit_code","metadata",b"metadata","outputs",b"outputs","overhead",b"overhead","status",b"status"]) -> None: ...
global___CommandResult = CommandResult

class FileMetadata(google.protobuf.message.Message):
    """The metadata for a file. Similar to the equivalent message in the Remote
    Execution API.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PATH_FIELD_NUMBER: builtins.int
    DIGEST_FIELD_NUMBER: builtins.int
    CONTENTS_FIELD_NUMBER: builtins.int
    IS_EXECUTABLE_FIELD_NUMBER: builtins.int
    path: typing.Text = ...
    """The path of this file. If this message is part of the
    CommandOutputs.outputs fields, the path is relative to the execution root
    and must correspond to an entry in CommandTask.outputs.files. If this
    message is part of a Directory message, then the path is relative to the
    root of that directory. All paths MUST be delimited by forward slashes.
    """

    @property
    def digest(self) -> global___Digest:
        """A pointer to the contents of the file. The method by which a client
        retrieves the contents from a CAS system is not defined here.
        """
        pass
    contents: builtins.bytes = ...
    """If the file is small enough, its contents may also or alternatively be
    listed here.
    """

    is_executable: builtins.bool = ...
    """Properties of the file"""

    def __init__(self,
        *,
        path : typing.Text = ...,
        digest : typing.Optional[global___Digest] = ...,
        contents : builtins.bytes = ...,
        is_executable : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["digest",b"digest"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["contents",b"contents","digest",b"digest","is_executable",b"is_executable","path",b"path"]) -> None: ...
global___FileMetadata = FileMetadata

class DirectoryMetadata(google.protobuf.message.Message):
    """The metadata for a directory. Similar to the equivalent message in the Remote
    Execution API.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PATH_FIELD_NUMBER: builtins.int
    DIGEST_FIELD_NUMBER: builtins.int
    path: typing.Text = ...
    """The path of the directory, as in
    [FileMetadata.path][google.devtools.remoteworkers.v1test2.FileMetadata.path].
    """

    @property
    def digest(self) -> global___Digest:
        """A pointer to the contents of the directory, in the form of a marshalled
        Directory message.
        """
        pass
    def __init__(self,
        *,
        path : typing.Text = ...,
        digest : typing.Optional[global___Digest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["digest",b"digest"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["digest",b"digest","path",b"path"]) -> None: ...
global___DirectoryMetadata = DirectoryMetadata

class Digest(google.protobuf.message.Message):
    """The CommandTask and CommandResult messages assume the existence of a service
    that can serve blobs of content, identified by a hash and size known as a
    "digest." The method by which these blobs may be retrieved is not specified
    here, but a model implementation is in the Remote Execution API's
    "ContentAddressibleStorage" interface.

    In the context of the RWAPI, a Digest will virtually always refer to the
    contents of a file or a directory. The latter is represented by the
    byte-encoded Directory message.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HASH_FIELD_NUMBER: builtins.int
    SIZE_BYTES_FIELD_NUMBER: builtins.int
    hash: typing.Text = ...
    """A string-encoded hash (eg "1a2b3c", not the byte array [0x1a, 0x2b, 0x3c])
    using an implementation-defined hash algorithm (eg SHA-256).
    """

    size_bytes: builtins.int = ...
    """The size of the contents. While this is not strictly required as part of an
    identifier (after all, any given hash will have exactly one canonical
    size), it's useful in almost all cases when one might want to send or
    retrieve blobs of content and is included here for this reason.
    """

    def __init__(self,
        *,
        hash : typing.Text = ...,
        size_bytes : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hash",b"hash","size_bytes",b"size_bytes"]) -> None: ...
global___Digest = Digest

class Blob(google.protobuf.message.Message):
    """Describes a blob of binary content with its digest."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DIGEST_FIELD_NUMBER: builtins.int
    CONTENTS_FIELD_NUMBER: builtins.int
    @property
    def digest(self) -> global___Digest:
        """The digest of the blob. This should be verified by the receiver."""
        pass
    contents: builtins.bytes = ...
    """The contents of the blob."""

    def __init__(self,
        *,
        digest : typing.Optional[global___Digest] = ...,
        contents : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["digest",b"digest"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["contents",b"contents","digest",b"digest"]) -> None: ...
global___Blob = Blob

class Directory(google.protobuf.message.Message):
    """The contents of a directory. Similar to the equivalent message in the Remote
    Execution API.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FILES_FIELD_NUMBER: builtins.int
    DIRECTORIES_FIELD_NUMBER: builtins.int
    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FileMetadata]:
        """The files in this directory"""
        pass
    @property
    def directories(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DirectoryMetadata]:
        """Any subdirectories"""
        pass
    def __init__(self,
        *,
        files : typing.Optional[typing.Iterable[global___FileMetadata]] = ...,
        directories : typing.Optional[typing.Iterable[global___DirectoryMetadata]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["directories",b"directories","files",b"files"]) -> None: ...
global___Directory = Directory
