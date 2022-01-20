"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.tasks.v2beta3.target_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Queue(google.protobuf.message.Message):
    """A queue is a container of related tasks. Queues are configured to manage
    how those tasks are dispatched. Configurable properties include rate limits,
    retry options, queue types, and others.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _State:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        STATE_UNSPECIFIED: Queue.State.ValueType = ...  # 0
        """Unspecified state."""

        RUNNING: Queue.State.ValueType = ...  # 1
        """The queue is running. Tasks can be dispatched.

        If the queue was created using Cloud Tasks and the queue has
        had no activity (method calls or task dispatches) for 30 days,
        the queue may take a few minutes to re-activate. Some method
        calls may return [NOT_FOUND][google.rpc.Code.NOT_FOUND] and
        tasks may not be dispatched for a few minutes until the queue
        has been re-activated.
        """

        PAUSED: Queue.State.ValueType = ...  # 2
        """Tasks are paused by the user. If the queue is paused then Cloud
        Tasks will stop delivering tasks from it, but more tasks can
        still be added to it by the user.
        """

        DISABLED: Queue.State.ValueType = ...  # 3
        """The queue is disabled.

        A queue becomes `DISABLED` when
        [queue.yaml](https://cloud.google.com/appengine/docs/python/config/queueref)
        or
        [queue.xml](https://cloud.google.com/appengine/docs/standard/java/config/queueref)
        is uploaded which does not contain the queue. You cannot directly disable
        a queue.

        When a queue is disabled, tasks can still be added to a queue
        but the tasks are not dispatched.

        To permanently delete this queue and all of its tasks, call
        [DeleteQueue][google.cloud.tasks.v2beta3.CloudTasks.DeleteQueue].
        """

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """State of the queue."""
        pass

    STATE_UNSPECIFIED: Queue.State.ValueType = ...  # 0
    """Unspecified state."""

    RUNNING: Queue.State.ValueType = ...  # 1
    """The queue is running. Tasks can be dispatched.

    If the queue was created using Cloud Tasks and the queue has
    had no activity (method calls or task dispatches) for 30 days,
    the queue may take a few minutes to re-activate. Some method
    calls may return [NOT_FOUND][google.rpc.Code.NOT_FOUND] and
    tasks may not be dispatched for a few minutes until the queue
    has been re-activated.
    """

    PAUSED: Queue.State.ValueType = ...  # 2
    """Tasks are paused by the user. If the queue is paused then Cloud
    Tasks will stop delivering tasks from it, but more tasks can
    still be added to it by the user.
    """

    DISABLED: Queue.State.ValueType = ...  # 3
    """The queue is disabled.

    A queue becomes `DISABLED` when
    [queue.yaml](https://cloud.google.com/appengine/docs/python/config/queueref)
    or
    [queue.xml](https://cloud.google.com/appengine/docs/standard/java/config/queueref)
    is uploaded which does not contain the queue. You cannot directly disable
    a queue.

    When a queue is disabled, tasks can still be added to a queue
    but the tasks are not dispatched.

    To permanently delete this queue and all of its tasks, call
    [DeleteQueue][google.cloud.tasks.v2beta3.CloudTasks.DeleteQueue].
    """


    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TYPE_UNSPECIFIED: Queue.Type.ValueType = ...  # 0
        """Default value."""

        PULL: Queue.Type.ValueType = ...  # 1
        """A pull queue."""

        PUSH: Queue.Type.ValueType = ...  # 2
        """A push queue."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        """The type of the queue."""
        pass

    TYPE_UNSPECIFIED: Queue.Type.ValueType = ...  # 0
    """Default value."""

    PULL: Queue.Type.ValueType = ...  # 1
    """A pull queue."""

    PUSH: Queue.Type.ValueType = ...  # 2
    """A push queue."""


    NAME_FIELD_NUMBER: builtins.int
    APP_ENGINE_HTTP_QUEUE_FIELD_NUMBER: builtins.int
    RATE_LIMITS_FIELD_NUMBER: builtins.int
    RETRY_CONFIG_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    PURGE_TIME_FIELD_NUMBER: builtins.int
    TASK_TTL_FIELD_NUMBER: builtins.int
    TOMBSTONE_TTL_FIELD_NUMBER: builtins.int
    STACKDRIVER_LOGGING_CONFIG_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    STATS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Caller-specified and required in [CreateQueue][google.cloud.tasks.v2beta3.CloudTasks.CreateQueue],
    after which it becomes output only.

    The queue name.

    The queue name must have the following format:
    `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

    * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]),
       hyphens (-), colons (:), or periods (.).
       For more information, see
       [Identifying
       projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `LOCATION_ID` is the canonical ID for the queue's location.
       The list of available locations can be obtained by calling
       [ListLocations][google.cloud.location.Locations.ListLocations].
       For more information, see https://cloud.google.com/about/locations/.
    * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or
      hyphens (-). The maximum length is 100 characters.
    """

    @property
    def app_engine_http_queue(self) -> google.cloud.tasks.v2beta3.target_pb2.AppEngineHttpQueue:
        """[AppEngineHttpQueue][google.cloud.tasks.v2beta3.AppEngineHttpQueue] settings apply only to
        [App Engine tasks][google.cloud.tasks.v2beta3.AppEngineHttpRequest] in this queue.
        [Http tasks][google.cloud.tasks.v2beta3.HttpRequest] are not affected by this proto.
        """
        pass
    @property
    def rate_limits(self) -> global___RateLimits:
        """Rate limits for task dispatches.

        [rate_limits][google.cloud.tasks.v2beta3.Queue.rate_limits] and [retry_config][google.cloud.tasks.v2beta3.Queue.retry_config] are
        related because they both control task attempts. However they control task
        attempts in different ways:

        * [rate_limits][google.cloud.tasks.v2beta3.Queue.rate_limits] controls the total rate of
          dispatches from a queue (i.e. all traffic dispatched from the
          queue, regardless of whether the dispatch is from a first
          attempt or a retry).
        * [retry_config][google.cloud.tasks.v2beta3.Queue.retry_config] controls what happens to
          particular a task after its first attempt fails. That is,
          [retry_config][google.cloud.tasks.v2beta3.Queue.retry_config] controls task retries (the
          second attempt, third attempt, etc).

        The queue's actual dispatch rate is the result of:

        * Number of tasks in the queue
        * User-specified throttling: [rate_limits][google.cloud.tasks.v2beta3.Queue.rate_limits],
          [retry_config][google.cloud.tasks.v2beta3.Queue.retry_config], and the
          [queue's state][google.cloud.tasks.v2beta3.Queue.state].
        * System throttling due to `429` (Too Many Requests) or `503` (Service
          Unavailable) responses from the worker, high error rates, or to smooth
          sudden large traffic spikes.
        """
        pass
    @property
    def retry_config(self) -> global___RetryConfig:
        """Settings that determine the retry behavior.

        * For tasks created using Cloud Tasks: the queue-level retry settings
          apply to all tasks in the queue that were created using Cloud Tasks.
          Retry settings cannot be set on individual tasks.
        * For tasks created using the App Engine SDK: the queue-level retry
          settings apply to all tasks in the queue which do not have retry settings
          explicitly set on the task and were created by the App Engine SDK. See
          [App Engine
          documentation](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/retrying-tasks).
        """
        pass
    state: global___Queue.State.ValueType = ...
    """Output only. The state of the queue.

    `state` can only be changed by calling
    [PauseQueue][google.cloud.tasks.v2beta3.CloudTasks.PauseQueue],
    [ResumeQueue][google.cloud.tasks.v2beta3.CloudTasks.ResumeQueue], or uploading
    [queue.yaml/xml](https://cloud.google.com/appengine/docs/python/config/queueref).
    [UpdateQueue][google.cloud.tasks.v2beta3.CloudTasks.UpdateQueue] cannot be used to change `state`.
    """

    @property
    def purge_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The last time this queue was purged.

        All tasks that were [created][google.cloud.tasks.v2beta3.Task.create_time] before this time
        were purged.

        A queue can be purged using [PurgeQueue][google.cloud.tasks.v2beta3.CloudTasks.PurgeQueue], the
        [App Engine Task Queue SDK, or the Cloud
        Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue).

        Purge time will be truncated to the nearest microsecond. Purge
        time will be unset if the queue has never been purged.
        """
        pass
    @property
    def task_ttl(self) -> google.protobuf.duration_pb2.Duration:
        """The maximum amount of time that a task will be retained in
        this queue.

        Queues created by Cloud Tasks have a default `task_ttl` of 31 days.
        After a task has lived for `task_ttl`, the task will be deleted
        regardless of whether it was dispatched or not.

        The `task_ttl` for queues created via queue.yaml/xml is equal to the
        maximum duration because there is a
        [storage quota](https://cloud.google.com/appengine/quotas#Task_Queue) for
        these queues. To view the maximum valid duration, see the documentation for
        [Duration][google.protobuf.Duration].
        """
        pass
    @property
    def tombstone_ttl(self) -> google.protobuf.duration_pb2.Duration:
        """The task tombstone time to live (TTL).

        After a task is deleted or executed, the task's tombstone is
        retained for the length of time specified by `tombstone_ttl`.
        The tombstone is used by task de-duplication; another task with the same
        name can't be created until the tombstone has expired. For more information
        about task de-duplication, see the documentation for
        [CreateTaskRequest][google.cloud.tasks.v2beta3.CreateTaskRequest.task].

        Queues created by Cloud Tasks have a default `tombstone_ttl` of 1 hour.
        """
        pass
    @property
    def stackdriver_logging_config(self) -> global___StackdriverLoggingConfig:
        """Configuration options for writing logs to
        [Stackdriver Logging](https://cloud.google.com/logging/docs/). If this
        field is unset, then no logs are written.
        """
        pass
    type: global___Queue.Type.ValueType = ...
    """Immutable. The type of a queue (push or pull).

    `Queue.type` is an immutable property of the queue that is set at the queue
    creation time. When left unspecified, the default value of `PUSH` is
    selected.
    """

    @property
    def stats(self) -> global___QueueStats:
        """Output only. The realtime, informational statistics for a queue. In order
        to receive the statistics the caller should include this field in the
        FieldMask.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        app_engine_http_queue : typing.Optional[google.cloud.tasks.v2beta3.target_pb2.AppEngineHttpQueue] = ...,
        rate_limits : typing.Optional[global___RateLimits] = ...,
        retry_config : typing.Optional[global___RetryConfig] = ...,
        state : global___Queue.State.ValueType = ...,
        purge_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        task_ttl : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        tombstone_ttl : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        stackdriver_logging_config : typing.Optional[global___StackdriverLoggingConfig] = ...,
        type : global___Queue.Type.ValueType = ...,
        stats : typing.Optional[global___QueueStats] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["app_engine_http_queue",b"app_engine_http_queue","purge_time",b"purge_time","queue_type",b"queue_type","rate_limits",b"rate_limits","retry_config",b"retry_config","stackdriver_logging_config",b"stackdriver_logging_config","stats",b"stats","task_ttl",b"task_ttl","tombstone_ttl",b"tombstone_ttl"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_engine_http_queue",b"app_engine_http_queue","name",b"name","purge_time",b"purge_time","queue_type",b"queue_type","rate_limits",b"rate_limits","retry_config",b"retry_config","stackdriver_logging_config",b"stackdriver_logging_config","state",b"state","stats",b"stats","task_ttl",b"task_ttl","tombstone_ttl",b"tombstone_ttl","type",b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["queue_type",b"queue_type"]) -> typing.Optional[typing_extensions.Literal["app_engine_http_queue"]]: ...
global___Queue = Queue

class RateLimits(google.protobuf.message.Message):
    """Rate limits.

    This message determines the maximum rate that tasks can be dispatched by a
    queue, regardless of whether the dispatch is a first task attempt or a retry.

    Note: The debugging command, [RunTask][google.cloud.tasks.v2beta3.CloudTasks.RunTask], will run a task
    even if the queue has reached its [RateLimits][google.cloud.tasks.v2beta3.RateLimits].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MAX_DISPATCHES_PER_SECOND_FIELD_NUMBER: builtins.int
    MAX_BURST_SIZE_FIELD_NUMBER: builtins.int
    MAX_CONCURRENT_DISPATCHES_FIELD_NUMBER: builtins.int
    max_dispatches_per_second: builtins.float = ...
    """The maximum rate at which tasks are dispatched from this queue.

    If unspecified when the queue is created, Cloud Tasks will pick the
    default.

    * For [App Engine queues][google.cloud.tasks.v2beta3.AppEngineHttpQueue], the maximum allowed value
      is 500.


    This field has the same meaning as
    [rate in
    queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#rate).
    """

    max_burst_size: builtins.int = ...
    """The max burst size.

    Max burst size limits how fast tasks in queue are processed when
    many tasks are in the queue and the rate is high. This field
    allows the queue to have a high rate so processing starts shortly
    after a task is enqueued, but still limits resource usage when
    many tasks are enqueued in a short period of time.

    The [token bucket](https://wikipedia.org/wiki/Token_Bucket)
    algorithm is used to control the rate of task dispatches. Each
    queue has a token bucket that holds tokens, up to the maximum
    specified by `max_burst_size`. Each time a task is dispatched, a
    token is removed from the bucket. Tasks will be dispatched until
    the queue's bucket runs out of tokens. The bucket will be
    continuously refilled with new tokens based on
    [max_dispatches_per_second][google.cloud.tasks.v2beta3.RateLimits.max_dispatches_per_second].

    The default value of `max_burst_size` is picked by Cloud Tasks
    based on the value of
    [max_dispatches_per_second][google.cloud.tasks.v2beta3.RateLimits.max_dispatches_per_second].

    The maximum value of `max_burst_size` is 500.

    For App Engine queues that were created or updated using
    `queue.yaml/xml`, `max_burst_size` is equal to
    [bucket_size](https://cloud.google.com/appengine/docs/standard/python/config/queueref#bucket_size).
    If
    [UpdateQueue][google.cloud.tasks.v2beta3.CloudTasks.UpdateQueue] is called on a queue without
    explicitly setting a value for `max_burst_size`,
    `max_burst_size` value will get updated if
    [UpdateQueue][google.cloud.tasks.v2beta3.CloudTasks.UpdateQueue] is updating
    [max_dispatches_per_second][google.cloud.tasks.v2beta3.RateLimits.max_dispatches_per_second].
    """

    max_concurrent_dispatches: builtins.int = ...
    """The maximum number of concurrent tasks that Cloud Tasks allows
    to be dispatched for this queue. After this threshold has been
    reached, Cloud Tasks stops dispatching tasks until the number of
    concurrent requests decreases.

    If unspecified when the queue is created, Cloud Tasks will pick the
    default.


    The maximum allowed value is 5,000.


    This field has the same meaning as
    [max_concurrent_requests in
    queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#max_concurrent_requests).
    """

    def __init__(self,
        *,
        max_dispatches_per_second : builtins.float = ...,
        max_burst_size : builtins.int = ...,
        max_concurrent_dispatches : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_burst_size",b"max_burst_size","max_concurrent_dispatches",b"max_concurrent_dispatches","max_dispatches_per_second",b"max_dispatches_per_second"]) -> None: ...
global___RateLimits = RateLimits

class RetryConfig(google.protobuf.message.Message):
    """Retry config.

    These settings determine when a failed task attempt is retried.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MAX_ATTEMPTS_FIELD_NUMBER: builtins.int
    MAX_RETRY_DURATION_FIELD_NUMBER: builtins.int
    MIN_BACKOFF_FIELD_NUMBER: builtins.int
    MAX_BACKOFF_FIELD_NUMBER: builtins.int
    MAX_DOUBLINGS_FIELD_NUMBER: builtins.int
    max_attempts: builtins.int = ...
    """Number of attempts per task.

    Cloud Tasks will attempt the task `max_attempts` times (that is, if the
    first attempt fails, then there will be `max_attempts - 1` retries). Must
    be >= -1.

    If unspecified when the queue is created, Cloud Tasks will pick the
    default.

    -1 indicates unlimited attempts.

    This field has the same meaning as
    [task_retry_limit in
    queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).
    """

    @property
    def max_retry_duration(self) -> google.protobuf.duration_pb2.Duration:
        """If positive, `max_retry_duration` specifies the time limit for
        retrying a failed task, measured from when the task was first
        attempted. Once `max_retry_duration` time has passed *and* the
        task has been attempted [max_attempts][google.cloud.tasks.v2beta3.RetryConfig.max_attempts]
        times, no further attempts will be made and the task will be
        deleted.

        If zero, then the task age is unlimited.

        If unspecified when the queue is created, Cloud Tasks will pick the
        default.


        `max_retry_duration` will be truncated to the nearest second.

        This field has the same meaning as
        [task_age_limit in
        queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).
        """
        pass
    @property
    def min_backoff(self) -> google.protobuf.duration_pb2.Duration:
        """A task will be [scheduled][google.cloud.tasks.v2beta3.Task.schedule_time] for retry between
        [min_backoff][google.cloud.tasks.v2beta3.RetryConfig.min_backoff] and
        [max_backoff][google.cloud.tasks.v2beta3.RetryConfig.max_backoff] duration after it fails,
        if the queue's [RetryConfig][google.cloud.tasks.v2beta3.RetryConfig] specifies that the task should be
        retried.

        If unspecified when the queue is created, Cloud Tasks will pick the
        default.


        `min_backoff` will be truncated to the nearest second.

        This field has the same meaning as
        [min_backoff_seconds in
        queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).
        """
        pass
    @property
    def max_backoff(self) -> google.protobuf.duration_pb2.Duration:
        """A task will be [scheduled][google.cloud.tasks.v2beta3.Task.schedule_time] for retry between
        [min_backoff][google.cloud.tasks.v2beta3.RetryConfig.min_backoff] and
        [max_backoff][google.cloud.tasks.v2beta3.RetryConfig.max_backoff] duration after it fails,
        if the queue's [RetryConfig][google.cloud.tasks.v2beta3.RetryConfig] specifies that the task should be
        retried.

        If unspecified when the queue is created, Cloud Tasks will pick the
        default.


        `max_backoff` will be truncated to the nearest second.

        This field has the same meaning as
        [max_backoff_seconds in
        queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).
        """
        pass
    max_doublings: builtins.int = ...
    """The time between retries will double `max_doublings` times.

    A task's retry interval starts at
    [min_backoff][google.cloud.tasks.v2beta3.RetryConfig.min_backoff], then doubles
    `max_doublings` times, then increases linearly, and finally
    retries at intervals of
    [max_backoff][google.cloud.tasks.v2beta3.RetryConfig.max_backoff] up to
    [max_attempts][google.cloud.tasks.v2beta3.RetryConfig.max_attempts] times.

    For example, if [min_backoff][google.cloud.tasks.v2beta3.RetryConfig.min_backoff] is 10s,
    [max_backoff][google.cloud.tasks.v2beta3.RetryConfig.max_backoff] is 300s, and
    `max_doublings` is 3, then the a task will first be retried in
    10s. The retry interval will double three times, and then
    increase linearly by 2^3 * 10s.  Finally, the task will retry at
    intervals of [max_backoff][google.cloud.tasks.v2beta3.RetryConfig.max_backoff] until the
    task has been attempted [max_attempts][google.cloud.tasks.v2beta3.RetryConfig.max_attempts]
    times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s,
    240s, 300s, 300s, ....

    If unspecified when the queue is created, Cloud Tasks will pick the
    default.


    This field has the same meaning as
    [max_doublings in
    queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).
    """

    def __init__(self,
        *,
        max_attempts : builtins.int = ...,
        max_retry_duration : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        min_backoff : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        max_backoff : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        max_doublings : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["max_backoff",b"max_backoff","max_retry_duration",b"max_retry_duration","min_backoff",b"min_backoff"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_attempts",b"max_attempts","max_backoff",b"max_backoff","max_doublings",b"max_doublings","max_retry_duration",b"max_retry_duration","min_backoff",b"min_backoff"]) -> None: ...
global___RetryConfig = RetryConfig

class StackdriverLoggingConfig(google.protobuf.message.Message):
    """Configuration options for writing logs to
    [Stackdriver Logging](https://cloud.google.com/logging/docs/).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SAMPLING_RATIO_FIELD_NUMBER: builtins.int
    sampling_ratio: builtins.float = ...
    """Specifies the fraction of operations to write to
    [Stackdriver Logging](https://cloud.google.com/logging/docs/).
    This field may contain any value between 0.0 and 1.0, inclusive.
    0.0 is the default and means that no operations are logged.
    """

    def __init__(self,
        *,
        sampling_ratio : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sampling_ratio",b"sampling_ratio"]) -> None: ...
global___StackdriverLoggingConfig = StackdriverLoggingConfig

class QueueStats(google.protobuf.message.Message):
    """Statistics for a queue."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TASKS_COUNT_FIELD_NUMBER: builtins.int
    OLDEST_ESTIMATED_ARRIVAL_TIME_FIELD_NUMBER: builtins.int
    EXECUTED_LAST_MINUTE_COUNT_FIELD_NUMBER: builtins.int
    CONCURRENT_DISPATCHES_COUNT_FIELD_NUMBER: builtins.int
    EFFECTIVE_EXECUTION_RATE_FIELD_NUMBER: builtins.int
    tasks_count: builtins.int = ...
    """Output only. An estimation of the number of tasks in the queue, that is, the tasks in
    the queue that haven't been executed, the tasks in the queue which the
    queue has dispatched but has not yet received a reply for, and the failed
    tasks that the queue is retrying.
    """

    @property
    def oldest_estimated_arrival_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. An estimation of the nearest time in the future where a task in the queue
        is scheduled to be executed.
        """
        pass
    executed_last_minute_count: builtins.int = ...
    """Output only. The number of tasks that the queue has dispatched and received a reply for
    during the last minute. This variable counts both successful and
    non-successful executions.
    """

    concurrent_dispatches_count: builtins.int = ...
    """Output only. The number of requests that the queue has dispatched but has not received
    a reply for yet.
    """

    effective_execution_rate: builtins.float = ...
    """Output only. The current maximum number of tasks per second executed by the queue.
    The maximum value of this variable is controlled by the RateLimits of the
    Queue. However, this value could be less to avoid overloading the endpoints
    tasks in the queue are targeting.
    """

    def __init__(self,
        *,
        tasks_count : builtins.int = ...,
        oldest_estimated_arrival_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        executed_last_minute_count : builtins.int = ...,
        concurrent_dispatches_count : builtins.int = ...,
        effective_execution_rate : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["oldest_estimated_arrival_time",b"oldest_estimated_arrival_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["concurrent_dispatches_count",b"concurrent_dispatches_count","effective_execution_rate",b"effective_execution_rate","executed_last_minute_count",b"executed_last_minute_count","oldest_estimated_arrival_time",b"oldest_estimated_arrival_time","tasks_count",b"tasks_count"]) -> None: ...
global___QueueStats = QueueStats
