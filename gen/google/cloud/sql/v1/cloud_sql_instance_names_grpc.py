# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/sql/v1/cloud_sql_instance_names.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.field_behavior_pb2
import google.api.client_pb2
import google.cloud.sql.v1.cloud_sql_instance_names_pb2


class SqlInstanceNamesServiceBase(abc.ABC):

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
        }


class SqlInstanceNamesServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
