"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.common.simulation_pb2
import google.ads.googleads.v9.enums.simulation_modification_method_pb2
import google.ads.googleads.v9.enums.simulation_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CampaignSimulation(google.protobuf.message.Message):
    """Proto file describing the campaign simulation resource.

    A campaign simulation. Supported combinations of advertising
    channel type, simulation type and simulation modification
    method is detailed below respectively.

    SEARCH - CPC_BID - UNIFORM
    SEARCH - CPC_BID - SCALING
    SEARCH - TARGET_CPA - UNIFORM
    SEARCH - TARGET_CPA - SCALING
    SEARCH - TARGET_ROAS - UNIFORM
    SEARCH - TARGET_IMPRESSION_SHARE - UNIFORM
    SEARCH - BUDGET - UNIFORM
    SHOPPING - BUDGET - UNIFORM
    SHOPPING - TARGET_ROAS - UNIFORM
    MULTIPLE - TARGET_CPA - UNIFORM
    OWNED_AND_OPERATED - TARGET_CPA - DEFAULT
    DISPLAY - TARGET_CPA - UNIFORM
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CAMPAIGN_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    MODIFICATION_METHOD_FIELD_NUMBER: builtins.int
    START_DATE_FIELD_NUMBER: builtins.int
    END_DATE_FIELD_NUMBER: builtins.int
    CPC_BID_POINT_LIST_FIELD_NUMBER: builtins.int
    TARGET_CPA_POINT_LIST_FIELD_NUMBER: builtins.int
    TARGET_ROAS_POINT_LIST_FIELD_NUMBER: builtins.int
    TARGET_IMPRESSION_SHARE_POINT_LIST_FIELD_NUMBER: builtins.int
    BUDGET_POINT_LIST_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Output only. The resource name of the campaign simulation.
    Campaign simulation resource names have the form:

    `customers/{customer_id}/campaignSimulations/{campaign_id}~{type}~{modification_method}~{start_date}~{end_date}`
    """

    campaign_id: builtins.int = ...
    """Output only. Campaign id of the simulation."""

    type: google.ads.googleads.v9.enums.simulation_type_pb2.SimulationTypeEnum.SimulationType.ValueType = ...
    """Output only. The field that the simulation modifies."""

    modification_method: google.ads.googleads.v9.enums.simulation_modification_method_pb2.SimulationModificationMethodEnum.SimulationModificationMethod.ValueType = ...
    """Output only. How the simulation modifies the field."""

    start_date: typing.Text = ...
    """Output only. First day on which the simulation is based, in YYYY-MM-DD format."""

    end_date: typing.Text = ...
    """Output only. Last day on which the simulation is based, in YYYY-MM-DD format"""

    @property
    def cpc_bid_point_list(self) -> google.ads.googleads.v9.common.simulation_pb2.CpcBidSimulationPointList:
        """Output only. Simulation points if the simulation type is CPC_BID."""
        pass
    @property
    def target_cpa_point_list(self) -> google.ads.googleads.v9.common.simulation_pb2.TargetCpaSimulationPointList:
        """Output only. Simulation points if the simulation type is TARGET_CPA."""
        pass
    @property
    def target_roas_point_list(self) -> google.ads.googleads.v9.common.simulation_pb2.TargetRoasSimulationPointList:
        """Output only. Simulation points if the simulation type is TARGET_ROAS."""
        pass
    @property
    def target_impression_share_point_list(self) -> google.ads.googleads.v9.common.simulation_pb2.TargetImpressionShareSimulationPointList:
        """Output only. Simulation points if the simulation type is TARGET_IMPRESSION_SHARE."""
        pass
    @property
    def budget_point_list(self) -> google.ads.googleads.v9.common.simulation_pb2.BudgetSimulationPointList:
        """Output only. Simulation points if the simulation type is BUDGET."""
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        campaign_id : builtins.int = ...,
        type : google.ads.googleads.v9.enums.simulation_type_pb2.SimulationTypeEnum.SimulationType.ValueType = ...,
        modification_method : google.ads.googleads.v9.enums.simulation_modification_method_pb2.SimulationModificationMethodEnum.SimulationModificationMethod.ValueType = ...,
        start_date : typing.Text = ...,
        end_date : typing.Text = ...,
        cpc_bid_point_list : typing.Optional[google.ads.googleads.v9.common.simulation_pb2.CpcBidSimulationPointList] = ...,
        target_cpa_point_list : typing.Optional[google.ads.googleads.v9.common.simulation_pb2.TargetCpaSimulationPointList] = ...,
        target_roas_point_list : typing.Optional[google.ads.googleads.v9.common.simulation_pb2.TargetRoasSimulationPointList] = ...,
        target_impression_share_point_list : typing.Optional[google.ads.googleads.v9.common.simulation_pb2.TargetImpressionShareSimulationPointList] = ...,
        budget_point_list : typing.Optional[google.ads.googleads.v9.common.simulation_pb2.BudgetSimulationPointList] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["budget_point_list",b"budget_point_list","cpc_bid_point_list",b"cpc_bid_point_list","point_list",b"point_list","target_cpa_point_list",b"target_cpa_point_list","target_impression_share_point_list",b"target_impression_share_point_list","target_roas_point_list",b"target_roas_point_list"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["budget_point_list",b"budget_point_list","campaign_id",b"campaign_id","cpc_bid_point_list",b"cpc_bid_point_list","end_date",b"end_date","modification_method",b"modification_method","point_list",b"point_list","resource_name",b"resource_name","start_date",b"start_date","target_cpa_point_list",b"target_cpa_point_list","target_impression_share_point_list",b"target_impression_share_point_list","target_roas_point_list",b"target_roas_point_list","type",b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["point_list",b"point_list"]) -> typing.Optional[typing_extensions.Literal["cpc_bid_point_list","target_cpa_point_list","target_roas_point_list","target_impression_share_point_list","budget_point_list"]]: ...
global___CampaignSimulation = CampaignSimulation
