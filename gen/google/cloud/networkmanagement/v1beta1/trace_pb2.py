# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/networkmanagement/v1beta1/trace.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/networkmanagement/v1beta1/trace.proto\x12&google.cloud.networkmanagement.v1beta1\x1a\x1cgoogle/api/annotations.proto\"\xa6\x01\n\x05Trace\x12Y\n\rendpoint_info\x18\x01 \x01(\x0b\x32\x34.google.cloud.networkmanagement.v1beta1.EndpointInfoR\x0c\x65ndpointInfo\x12\x42\n\x05steps\x18\x02 \x03(\x0b\x32,.google.cloud.networkmanagement.v1beta1.StepR\x05steps\"\x88\x10\n\x04Step\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12H\n\x05state\x18\x02 \x01(\x0e\x32\x32.google.cloud.networkmanagement.v1beta1.Step.StateR\x05state\x12\x1f\n\x0b\x63\x61uses_drop\x18\x03 \x01(\x08R\ncausesDrop\x12\x1d\n\nproject_id\x18\x04 \x01(\tR\tprojectId\x12R\n\x08instance\x18\x05 \x01(\x0b\x32\x34.google.cloud.networkmanagement.v1beta1.InstanceInfoH\x00R\x08instance\x12R\n\x08\x66irewall\x18\x06 \x01(\x0b\x32\x34.google.cloud.networkmanagement.v1beta1.FirewallInfoH\x00R\x08\x66irewall\x12I\n\x05route\x18\x07 \x01(\x0b\x32\x31.google.cloud.networkmanagement.v1beta1.RouteInfoH\x00R\x05route\x12R\n\x08\x65ndpoint\x18\x08 \x01(\x0b\x32\x34.google.cloud.networkmanagement.v1beta1.EndpointInfoH\x00R\x08\x65ndpoint\x12\x65\n\x0f\x66orwarding_rule\x18\t \x01(\x0b\x32:.google.cloud.networkmanagement.v1beta1.ForwardingRuleInfoH\x00R\x0e\x66orwardingRule\x12Y\n\x0bvpn_gateway\x18\n \x01(\x0b\x32\x36.google.cloud.networkmanagement.v1beta1.VpnGatewayInfoH\x00R\nvpnGateway\x12V\n\nvpn_tunnel\x18\x0b \x01(\x0b\x32\x35.google.cloud.networkmanagement.v1beta1.VpnTunnelInfoH\x00R\tvpnTunnel\x12O\n\x07\x64\x65liver\x18\x0c \x01(\x0b\x32\x33.google.cloud.networkmanagement.v1beta1.DeliverInfoH\x00R\x07\x64\x65liver\x12O\n\x07\x66orward\x18\r \x01(\x0b\x32\x33.google.cloud.networkmanagement.v1beta1.ForwardInfoH\x00R\x07\x66orward\x12I\n\x05\x61\x62ort\x18\x0e \x01(\x0b\x32\x31.google.cloud.networkmanagement.v1beta1.AbortInfoH\x00R\x05\x61\x62ort\x12\x46\n\x04\x64rop\x18\x0f \x01(\x0b\x32\x30.google.cloud.networkmanagement.v1beta1.DropInfoH\x00R\x04\x64rop\x12_\n\rload_balancer\x18\x10 \x01(\x0b\x32\x38.google.cloud.networkmanagement.v1beta1.LoadBalancerInfoH\x00R\x0cloadBalancer\x12O\n\x07network\x18\x11 \x01(\x0b\x32\x33.google.cloud.networkmanagement.v1beta1.NetworkInfoH\x00R\x07network\x12V\n\ngke_master\x18\x12 \x01(\x0b\x32\x35.google.cloud.networkmanagement.v1beta1.GKEMasterInfoH\x00R\tgkeMaster\x12l\n\x12\x63loud_sql_instance\x18\x13 \x01(\x0b\x32<.google.cloud.networkmanagement.v1beta1.CloudSQLInstanceInfoH\x00R\x10\x63loudSqlInstance\"\xb8\x04\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x17\n\x13START_FROM_INSTANCE\x10\x01\x12\x17\n\x13START_FROM_INTERNET\x10\x02\x12\x1e\n\x1aSTART_FROM_PRIVATE_NETWORK\x10\x03\x12\x19\n\x15START_FROM_GKE_MASTER\x10\x15\x12!\n\x1dSTART_FROM_CLOUD_SQL_INSTANCE\x10\x16\x12\x1f\n\x1b\x41PPLY_INGRESS_FIREWALL_RULE\x10\x04\x12\x1e\n\x1a\x41PPLY_EGRESS_FIREWALL_RULE\x10\x05\x12\x0f\n\x0b\x41PPLY_ROUTE\x10\x06\x12\x19\n\x15\x41PPLY_FORWARDING_RULE\x10\x07\x12\x15\n\x11SPOOFING_APPROVED\x10\x08\x12\x16\n\x12\x41RRIVE_AT_INSTANCE\x10\t\x12$\n ARRIVE_AT_INTERNAL_LOAD_BALANCER\x10\n\x12$\n ARRIVE_AT_EXTERNAL_LOAD_BALANCER\x10\x0b\x12\x19\n\x15\x41RRIVE_AT_VPN_GATEWAY\x10\x0c\x12\x18\n\x14\x41RRIVE_AT_VPN_TUNNEL\x10\r\x12\x07\n\x03NAT\x10\x0e\x12\x14\n\x10PROXY_CONNECTION\x10\x0f\x12\x0b\n\x07\x44\x45LIVER\x10\x10\x12\x08\n\x04\x44ROP\x10\x11\x12\x0b\n\x07\x46ORWARD\x10\x12\x12\t\n\x05\x41\x42ORT\x10\x13\x12\x1d\n\x19VIEWER_PERMISSION_MISSING\x10\x14\x42\x0b\n\tstep_info\"\x94\x02\n\x0cInstanceInfo\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12\x1c\n\tinterface\x18\x03 \x01(\tR\tinterface\x12\x1f\n\x0bnetwork_uri\x18\x04 \x01(\tR\nnetworkUri\x12\x1f\n\x0binternal_ip\x18\x05 \x01(\tR\ninternalIp\x12\x1f\n\x0b\x65xternal_ip\x18\x06 \x01(\tR\nexternalIp\x12!\n\x0cnetwork_tags\x18\x07 \x03(\tR\x0bnetworkTags\x12+\n\x0fservice_account\x18\x08 \x01(\tB\x02\x18\x01R\x0eserviceAccount\"l\n\x0bNetworkInfo\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12(\n\x10matched_ip_range\x18\x04 \x01(\tR\x0ematchedIpRange\"\xb2\x04\n\x0c\x46irewallInfo\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12\x1c\n\tdirection\x18\x03 \x01(\tR\tdirection\x12\x16\n\x06\x61\x63tion\x18\x04 \x01(\tR\x06\x61\x63tion\x12\x1a\n\x08priority\x18\x05 \x01(\x05R\x08priority\x12\x1f\n\x0bnetwork_uri\x18\x06 \x01(\tR\nnetworkUri\x12\x1f\n\x0btarget_tags\x18\x07 \x03(\tR\ntargetTags\x12\x36\n\x17target_service_accounts\x18\x08 \x03(\tR\x15targetServiceAccounts\x12\x16\n\x06policy\x18\t \x01(\tR\x06policy\x12s\n\x12\x66irewall_rule_type\x18\n \x01(\x0e\x32\x45.google.cloud.networkmanagement.v1beta1.FirewallInfo.FirewallRuleTypeR\x10\x66irewallRuleType\"\x93\x01\n\x10\x46irewallRuleType\x12\"\n\x1e\x46IREWALL_RULE_TYPE_UNSPECIFIED\x10\x00\x12%\n!HIERARCHICAL_FIREWALL_POLICY_RULE\x10\x01\x12\x15\n\x11VPC_FIREWALL_RULE\x10\x02\x12\x1d\n\x19IMPLIED_VPC_FIREWALL_RULE\x10\x03\"\xc6\x06\n\tRouteInfo\x12Z\n\nroute_type\x18\x08 \x01(\x0e\x32;.google.cloud.networkmanagement.v1beta1.RouteInfo.RouteTypeR\trouteType\x12\x61\n\rnext_hop_type\x18\t \x01(\x0e\x32=.google.cloud.networkmanagement.v1beta1.RouteInfo.NextHopTypeR\x0bnextHopType\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12\"\n\rdest_ip_range\x18\x03 \x01(\tR\x0b\x64\x65stIpRange\x12\x19\n\x08next_hop\x18\x04 \x01(\tR\x07nextHop\x12\x1f\n\x0bnetwork_uri\x18\x05 \x01(\tR\nnetworkUri\x12\x1a\n\x08priority\x18\x06 \x01(\x05R\x08priority\x12#\n\rinstance_tags\x18\x07 \x03(\tR\x0cinstanceTags\"\x89\x01\n\tRouteType\x12\x1a\n\x16ROUTE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06SUBNET\x10\x01\x12\n\n\x06STATIC\x10\x02\x12\x0b\n\x07\x44YNAMIC\x10\x03\x12\x12\n\x0ePEERING_SUBNET\x10\x04\x12\x12\n\x0ePEERING_STATIC\x10\x05\x12\x13\n\x0fPEERING_DYNAMIC\x10\x06\"\x97\x02\n\x0bNextHopType\x12\x1d\n\x19NEXT_HOP_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNEXT_HOP_IP\x10\x01\x12\x15\n\x11NEXT_HOP_INSTANCE\x10\x02\x12\x14\n\x10NEXT_HOP_NETWORK\x10\x03\x12\x14\n\x10NEXT_HOP_PEERING\x10\x04\x12\x19\n\x15NEXT_HOP_INTERCONNECT\x10\x05\x12\x17\n\x13NEXT_HOP_VPN_TUNNEL\x10\x06\x12\x18\n\x14NEXT_HOP_VPN_GATEWAY\x10\x07\x12\x1d\n\x19NEXT_HOP_INTERNET_GATEWAY\x10\x08\x12\x16\n\x12NEXT_HOP_BLACKHOLE\x10\t\x12\x10\n\x0cNEXT_HOP_ILB\x10\n\"\xed\x01\n\x12\x46orwardingRuleInfo\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12)\n\x10matched_protocol\x18\x03 \x01(\tR\x0fmatchedProtocol\x12,\n\x12matched_port_range\x18\x06 \x01(\tR\x10matchedPortRange\x12\x10\n\x03vip\x18\x04 \x01(\tR\x03vip\x12\x16\n\x06target\x18\x05 \x01(\tR\x06target\x12\x1f\n\x0bnetwork_uri\x18\x07 \x01(\tR\nnetworkUri\"\xfd\x04\n\x10LoadBalancerInfo\x12w\n\x12load_balancer_type\x18\x01 \x01(\x0e\x32I.google.cloud.networkmanagement.v1beta1.LoadBalancerInfo.LoadBalancerTypeR\x10loadBalancerType\x12(\n\x10health_check_uri\x18\x02 \x01(\tR\x0ehealthCheckUri\x12W\n\x08\x62\x61\x63kends\x18\x03 \x03(\x0b\x32;.google.cloud.networkmanagement.v1beta1.LoadBalancerBackendR\x08\x62\x61\x63kends\x12g\n\x0c\x62\x61\x63kend_type\x18\x04 \x01(\x0e\x32\x44.google.cloud.networkmanagement.v1beta1.LoadBalancerInfo.BackendTypeR\x0b\x62\x61\x63kendType\x12\x1f\n\x0b\x62\x61\x63kend_uri\x18\x05 \x01(\tR\nbackendUri\"\x8f\x01\n\x10LoadBalancerType\x12\"\n\x1eLOAD_BALANCER_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10INTERNAL_TCP_UDP\x10\x01\x12\x13\n\x0fNETWORK_TCP_UDP\x10\x02\x12\x0e\n\nHTTP_PROXY\x10\x03\x12\r\n\tTCP_PROXY\x10\x04\x12\r\n\tSSL_PROXY\x10\x05\"Q\n\x0b\x42\x61\x63kendType\x12\x1c\n\x18\x42\x41\x43KEND_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x42\x41\x43KEND_SERVICE\x10\x01\x12\x0f\n\x0bTARGET_POOL\x10\x02\"\xec\x03\n\x13LoadBalancerBackend\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12\x93\x01\n\x1bhealth_check_firewall_state\x18\x03 \x01(\x0e\x32T.google.cloud.networkmanagement.v1beta1.LoadBalancerBackend.HealthCheckFirewallStateR\x18healthCheckFirewallState\x12N\n$health_check_allowing_firewall_rules\x18\x04 \x03(\tR healthCheckAllowingFirewallRules\x12N\n$health_check_blocking_firewall_rules\x18\x05 \x03(\tR healthCheckBlockingFirewallRules\"j\n\x18HealthCheckFirewallState\x12+\n\'HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED\x10\x00\x12\x0e\n\nCONFIGURED\x10\x01\x12\x11\n\rMISCONFIGURED\x10\x02\"\xc3\x01\n\x0eVpnGatewayInfo\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12\x1f\n\x0bnetwork_uri\x18\x03 \x01(\tR\nnetworkUri\x12\x1d\n\nip_address\x18\x04 \x01(\tR\tipAddress\x12$\n\x0evpn_tunnel_uri\x18\x05 \x01(\tR\x0cvpnTunnelUri\x12\x16\n\x06region\x18\x06 \x01(\tR\x06region\"\xe6\x03\n\rVpnTunnelInfo\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12%\n\x0esource_gateway\x18\x03 \x01(\tR\rsourceGateway\x12%\n\x0eremote_gateway\x18\x04 \x01(\tR\rremoteGateway\x12*\n\x11remote_gateway_ip\x18\x05 \x01(\tR\x0fremoteGatewayIp\x12*\n\x11source_gateway_ip\x18\x06 \x01(\tR\x0fsourceGatewayIp\x12\x1f\n\x0bnetwork_uri\x18\x07 \x01(\tR\nnetworkUri\x12\x16\n\x06region\x18\x08 \x01(\tR\x06region\x12\x64\n\x0crouting_type\x18\t \x01(\x0e\x32\x41.google.cloud.networkmanagement.v1beta1.VpnTunnelInfo.RoutingTypeR\x0broutingType\"[\n\x0bRoutingType\x12\x1c\n\x18ROUTING_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bROUTE_BASED\x10\x01\x12\x10\n\x0cPOLICY_BASED\x10\x02\x12\x0b\n\x07\x44YNAMIC\x10\x03\"\xa0\x02\n\x0c\x45ndpointInfo\x12\x1b\n\tsource_ip\x18\x01 \x01(\tR\x08sourceIp\x12%\n\x0e\x64\x65stination_ip\x18\x02 \x01(\tR\rdestinationIp\x12\x1a\n\x08protocol\x18\x03 \x01(\tR\x08protocol\x12\x1f\n\x0bsource_port\x18\x04 \x01(\x05R\nsourcePort\x12)\n\x10\x64\x65stination_port\x18\x05 \x01(\x05R\x0f\x64\x65stinationPort\x12,\n\x12source_network_uri\x18\x06 \x01(\tR\x10sourceNetworkUri\x12\x36\n\x17\x64\x65stination_network_uri\x18\x07 \x01(\tR\x15\x64\x65stinationNetworkUri\"\xfa\x01\n\x0b\x44\x65liverInfo\x12R\n\x06target\x18\x01 \x01(\x0e\x32:.google.cloud.networkmanagement.v1beta1.DeliverInfo.TargetR\x06target\x12!\n\x0cresource_uri\x18\x02 \x01(\tR\x0bresourceUri\"t\n\x06Target\x12\x16\n\x12TARGET_UNSPECIFIED\x10\x00\x12\x0c\n\x08INSTANCE\x10\x01\x12\x0c\n\x08INTERNET\x10\x02\x12\x0e\n\nGOOGLE_API\x10\x03\x12\x0e\n\nGKE_MASTER\x10\x04\x12\x16\n\x12\x43LOUD_SQL_INSTANCE\x10\x05\"\xa7\x02\n\x0b\x46orwardInfo\x12R\n\x06target\x18\x01 \x01(\x0e\x32:.google.cloud.networkmanagement.v1beta1.ForwardInfo.TargetR\x06target\x12!\n\x0cresource_uri\x18\x02 \x01(\tR\x0bresourceUri\"\xa0\x01\n\x06Target\x12\x16\n\x12TARGET_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPEERING_VPC\x10\x01\x12\x0f\n\x0bVPN_GATEWAY\x10\x02\x12\x10\n\x0cINTERCONNECT\x10\x03\x12\x0e\n\nGKE_MASTER\x10\x04\x12\"\n\x1eIMPORTED_CUSTOM_ROUTE_NEXT_HOP\x10\x05\x12\x16\n\x12\x43LOUD_SQL_INSTANCE\x10\x06\"\xfb\x03\n\tAbortInfo\x12M\n\x05\x63\x61use\x18\x01 \x01(\x0e\x32\x37.google.cloud.networkmanagement.v1beta1.AbortInfo.CauseR\x05\x63\x61use\x12!\n\x0cresource_uri\x18\x02 \x01(\tR\x0bresourceUri\"\xfb\x02\n\x05\x43\x61use\x12\x15\n\x11\x43\x41USE_UNSPECIFIED\x10\x00\x12\x13\n\x0fUNKNOWN_NETWORK\x10\x01\x12\x0e\n\nUNKNOWN_IP\x10\x02\x12\x13\n\x0fUNKNOWN_PROJECT\x10\x03\x12\x15\n\x11PERMISSION_DENIED\x10\x04\x12\x16\n\x12NO_SOURCE_LOCATION\x10\x05\x12\x14\n\x10INVALID_ARGUMENT\x10\x06\x12\x12\n\x0eNO_EXTERNAL_IP\x10\x07\x12\x1a\n\x16UNINTENDED_DESTINATION\x10\x08\x12\x12\n\x0eTRACE_TOO_LONG\x10\t\x12\x12\n\x0eINTERNAL_ERROR\x10\n\x12\x1d\n\x19SOURCE_ENDPOINT_NOT_FOUND\x10\x0b\x12\x1d\n\x19MISMATCHED_SOURCE_NETWORK\x10\x0c\x12\"\n\x1e\x44\x45STINATION_ENDPOINT_NOT_FOUND\x10\r\x12\"\n\x1eMISMATCHED_DESTINATION_NETWORK\x10\x0e\"\xb3\x06\n\x08\x44ropInfo\x12L\n\x05\x63\x61use\x18\x01 \x01(\x0e\x32\x36.google.cloud.networkmanagement.v1beta1.DropInfo.CauseR\x05\x63\x61use\x12!\n\x0cresource_uri\x18\x02 \x01(\tR\x0bresourceUri\"\xb5\x05\n\x05\x43\x61use\x12\x15\n\x11\x43\x41USE_UNSPECIFIED\x10\x00\x12\x1c\n\x18UNKNOWN_EXTERNAL_ADDRESS\x10\x01\x12\x19\n\x15\x46OREIGN_IP_DISALLOWED\x10\x02\x12\x11\n\rFIREWALL_RULE\x10\x03\x12\x0c\n\x08NO_ROUTE\x10\x04\x12\x13\n\x0fROUTE_BLACKHOLE\x10\x05\x12\x17\n\x13ROUTE_WRONG_NETWORK\x10\x06\x12\x1f\n\x1bPRIVATE_TRAFFIC_TO_INTERNET\x10\x07\x12$\n PRIVATE_GOOGLE_ACCESS_DISALLOWED\x10\x08\x12\x17\n\x13NO_EXTERNAL_ADDRESS\x10\t\x12\x1c\n\x18UNKNOWN_INTERNAL_ADDRESS\x10\n\x12\x1c\n\x18\x46ORWARDING_RULE_MISMATCH\x10\x0b\x12 \n\x1c\x46ORWARDING_RULE_NO_INSTANCES\x10\x0c\x12\x38\n4FIREWALL_BLOCKING_LOAD_BALANCER_BACKEND_HEALTH_CHECK\x10\r\x12\x18\n\x14INSTANCE_NOT_RUNNING\x10\x0e\x12\x18\n\x14TRAFFIC_TYPE_BLOCKED\x10\x0f\x12\"\n\x1eGKE_MASTER_UNAUTHORIZED_ACCESS\x10\x10\x12*\n&CLOUD_SQL_INSTANCE_UNAUTHORIZED_ACCESS\x10\x11\x12\x1e\n\x1a\x44ROPPED_INSIDE_GKE_SERVICE\x10\x12\x12$\n DROPPED_INSIDE_CLOUD_SQL_SERVICE\x10\x13\x12%\n!GOOGLE_MANAGED_SERVICE_NO_PEERING\x10\x14\x12$\n CLOUD_SQL_INSTANCE_NO_IP_ADDRESS\x10\x15\"\xa2\x01\n\rGKEMasterInfo\x12\x1f\n\x0b\x63luster_uri\x18\x02 \x01(\tR\nclusterUri\x12.\n\x13\x63luster_network_uri\x18\x04 \x01(\tR\x11\x63lusterNetworkUri\x12\x1f\n\x0binternal_ip\x18\x05 \x01(\tR\ninternalIp\x12\x1f\n\x0b\x65xternal_ip\x18\x06 \x01(\tR\nexternalIp\"\xc6\x01\n\x14\x43loudSQLInstanceInfo\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12\x1f\n\x0bnetwork_uri\x18\x04 \x01(\tR\nnetworkUri\x12\x1f\n\x0binternal_ip\x18\x05 \x01(\tR\ninternalIp\x12\x1f\n\x0b\x65xternal_ip\x18\x06 \x01(\tR\nexternalIp\x12\x16\n\x06region\x18\x07 \x01(\tR\x06regionB\x91\x02\n*com.google.cloud.networkmanagement.v1beta1B\nTraceProtoP\x01ZWgoogle.golang.org/genproto/googleapis/cloud/networkmanagement/v1beta1;networkmanagement\xaa\x02&Google.Cloud.NetworkManagement.V1Beta1\xca\x02&Google\\Cloud\\NetworkManagement\\V1beta1\xea\x02)Google::Cloud::NetworkManagement::V1beta1b\x06proto3')



_TRACE = DESCRIPTOR.message_types_by_name['Trace']
_STEP = DESCRIPTOR.message_types_by_name['Step']
_INSTANCEINFO = DESCRIPTOR.message_types_by_name['InstanceInfo']
_NETWORKINFO = DESCRIPTOR.message_types_by_name['NetworkInfo']
_FIREWALLINFO = DESCRIPTOR.message_types_by_name['FirewallInfo']
_ROUTEINFO = DESCRIPTOR.message_types_by_name['RouteInfo']
_FORWARDINGRULEINFO = DESCRIPTOR.message_types_by_name['ForwardingRuleInfo']
_LOADBALANCERINFO = DESCRIPTOR.message_types_by_name['LoadBalancerInfo']
_LOADBALANCERBACKEND = DESCRIPTOR.message_types_by_name['LoadBalancerBackend']
_VPNGATEWAYINFO = DESCRIPTOR.message_types_by_name['VpnGatewayInfo']
_VPNTUNNELINFO = DESCRIPTOR.message_types_by_name['VpnTunnelInfo']
_ENDPOINTINFO = DESCRIPTOR.message_types_by_name['EndpointInfo']
_DELIVERINFO = DESCRIPTOR.message_types_by_name['DeliverInfo']
_FORWARDINFO = DESCRIPTOR.message_types_by_name['ForwardInfo']
_ABORTINFO = DESCRIPTOR.message_types_by_name['AbortInfo']
_DROPINFO = DESCRIPTOR.message_types_by_name['DropInfo']
_GKEMASTERINFO = DESCRIPTOR.message_types_by_name['GKEMasterInfo']
_CLOUDSQLINSTANCEINFO = DESCRIPTOR.message_types_by_name['CloudSQLInstanceInfo']
_STEP_STATE = _STEP.enum_types_by_name['State']
_FIREWALLINFO_FIREWALLRULETYPE = _FIREWALLINFO.enum_types_by_name['FirewallRuleType']
_ROUTEINFO_ROUTETYPE = _ROUTEINFO.enum_types_by_name['RouteType']
_ROUTEINFO_NEXTHOPTYPE = _ROUTEINFO.enum_types_by_name['NextHopType']
_LOADBALANCERINFO_LOADBALANCERTYPE = _LOADBALANCERINFO.enum_types_by_name['LoadBalancerType']
_LOADBALANCERINFO_BACKENDTYPE = _LOADBALANCERINFO.enum_types_by_name['BackendType']
_LOADBALANCERBACKEND_HEALTHCHECKFIREWALLSTATE = _LOADBALANCERBACKEND.enum_types_by_name['HealthCheckFirewallState']
_VPNTUNNELINFO_ROUTINGTYPE = _VPNTUNNELINFO.enum_types_by_name['RoutingType']
_DELIVERINFO_TARGET = _DELIVERINFO.enum_types_by_name['Target']
_FORWARDINFO_TARGET = _FORWARDINFO.enum_types_by_name['Target']
_ABORTINFO_CAUSE = _ABORTINFO.enum_types_by_name['Cause']
_DROPINFO_CAUSE = _DROPINFO.enum_types_by_name['Cause']
Trace = _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), {
  'DESCRIPTOR' : _TRACE,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.Trace)
  })
_sym_db.RegisterMessage(Trace)

Step = _reflection.GeneratedProtocolMessageType('Step', (_message.Message,), {
  'DESCRIPTOR' : _STEP,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.Step)
  })
_sym_db.RegisterMessage(Step)

InstanceInfo = _reflection.GeneratedProtocolMessageType('InstanceInfo', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCEINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.InstanceInfo)
  })
_sym_db.RegisterMessage(InstanceInfo)

NetworkInfo = _reflection.GeneratedProtocolMessageType('NetworkInfo', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.NetworkInfo)
  })
_sym_db.RegisterMessage(NetworkInfo)

FirewallInfo = _reflection.GeneratedProtocolMessageType('FirewallInfo', (_message.Message,), {
  'DESCRIPTOR' : _FIREWALLINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.FirewallInfo)
  })
_sym_db.RegisterMessage(FirewallInfo)

RouteInfo = _reflection.GeneratedProtocolMessageType('RouteInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.RouteInfo)
  })
_sym_db.RegisterMessage(RouteInfo)

ForwardingRuleInfo = _reflection.GeneratedProtocolMessageType('ForwardingRuleInfo', (_message.Message,), {
  'DESCRIPTOR' : _FORWARDINGRULEINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.ForwardingRuleInfo)
  })
_sym_db.RegisterMessage(ForwardingRuleInfo)

LoadBalancerInfo = _reflection.GeneratedProtocolMessageType('LoadBalancerInfo', (_message.Message,), {
  'DESCRIPTOR' : _LOADBALANCERINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.LoadBalancerInfo)
  })
_sym_db.RegisterMessage(LoadBalancerInfo)

LoadBalancerBackend = _reflection.GeneratedProtocolMessageType('LoadBalancerBackend', (_message.Message,), {
  'DESCRIPTOR' : _LOADBALANCERBACKEND,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.LoadBalancerBackend)
  })
_sym_db.RegisterMessage(LoadBalancerBackend)

VpnGatewayInfo = _reflection.GeneratedProtocolMessageType('VpnGatewayInfo', (_message.Message,), {
  'DESCRIPTOR' : _VPNGATEWAYINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.VpnGatewayInfo)
  })
_sym_db.RegisterMessage(VpnGatewayInfo)

VpnTunnelInfo = _reflection.GeneratedProtocolMessageType('VpnTunnelInfo', (_message.Message,), {
  'DESCRIPTOR' : _VPNTUNNELINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.VpnTunnelInfo)
  })
_sym_db.RegisterMessage(VpnTunnelInfo)

EndpointInfo = _reflection.GeneratedProtocolMessageType('EndpointInfo', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.EndpointInfo)
  })
_sym_db.RegisterMessage(EndpointInfo)

DeliverInfo = _reflection.GeneratedProtocolMessageType('DeliverInfo', (_message.Message,), {
  'DESCRIPTOR' : _DELIVERINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.DeliverInfo)
  })
_sym_db.RegisterMessage(DeliverInfo)

ForwardInfo = _reflection.GeneratedProtocolMessageType('ForwardInfo', (_message.Message,), {
  'DESCRIPTOR' : _FORWARDINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.ForwardInfo)
  })
_sym_db.RegisterMessage(ForwardInfo)

AbortInfo = _reflection.GeneratedProtocolMessageType('AbortInfo', (_message.Message,), {
  'DESCRIPTOR' : _ABORTINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.AbortInfo)
  })
_sym_db.RegisterMessage(AbortInfo)

DropInfo = _reflection.GeneratedProtocolMessageType('DropInfo', (_message.Message,), {
  'DESCRIPTOR' : _DROPINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.DropInfo)
  })
_sym_db.RegisterMessage(DropInfo)

GKEMasterInfo = _reflection.GeneratedProtocolMessageType('GKEMasterInfo', (_message.Message,), {
  'DESCRIPTOR' : _GKEMASTERINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.GKEMasterInfo)
  })
_sym_db.RegisterMessage(GKEMasterInfo)

CloudSQLInstanceInfo = _reflection.GeneratedProtocolMessageType('CloudSQLInstanceInfo', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDSQLINSTANCEINFO,
  '__module__' : 'google.cloud.networkmanagement.v1beta1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.networkmanagement.v1beta1.CloudSQLInstanceInfo)
  })
_sym_db.RegisterMessage(CloudSQLInstanceInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n*com.google.cloud.networkmanagement.v1beta1B\nTraceProtoP\001ZWgoogle.golang.org/genproto/googleapis/cloud/networkmanagement/v1beta1;networkmanagement\252\002&Google.Cloud.NetworkManagement.V1Beta1\312\002&Google\\Cloud\\NetworkManagement\\V1beta1\352\002)Google::Cloud::NetworkManagement::V1beta1'
  _INSTANCEINFO.fields_by_name['service_account']._options = None
  _INSTANCEINFO.fields_by_name['service_account']._serialized_options = b'\030\001'
  _TRACE._serialized_start=125
  _TRACE._serialized_end=291
  _STEP._serialized_start=294
  _STEP._serialized_end=2350
  _STEP_STATE._serialized_start=1769
  _STEP_STATE._serialized_end=2337
  _INSTANCEINFO._serialized_start=2353
  _INSTANCEINFO._serialized_end=2629
  _NETWORKINFO._serialized_start=2631
  _NETWORKINFO._serialized_end=2739
  _FIREWALLINFO._serialized_start=2742
  _FIREWALLINFO._serialized_end=3304
  _FIREWALLINFO_FIREWALLRULETYPE._serialized_start=3157
  _FIREWALLINFO_FIREWALLRULETYPE._serialized_end=3304
  _ROUTEINFO._serialized_start=3307
  _ROUTEINFO._serialized_end=4145
  _ROUTEINFO_ROUTETYPE._serialized_start=3726
  _ROUTEINFO_ROUTETYPE._serialized_end=3863
  _ROUTEINFO_NEXTHOPTYPE._serialized_start=3866
  _ROUTEINFO_NEXTHOPTYPE._serialized_end=4145
  _FORWARDINGRULEINFO._serialized_start=4148
  _FORWARDINGRULEINFO._serialized_end=4385
  _LOADBALANCERINFO._serialized_start=4388
  _LOADBALANCERINFO._serialized_end=5025
  _LOADBALANCERINFO_LOADBALANCERTYPE._serialized_start=4799
  _LOADBALANCERINFO_LOADBALANCERTYPE._serialized_end=4942
  _LOADBALANCERINFO_BACKENDTYPE._serialized_start=4944
  _LOADBALANCERINFO_BACKENDTYPE._serialized_end=5025
  _LOADBALANCERBACKEND._serialized_start=5028
  _LOADBALANCERBACKEND._serialized_end=5520
  _LOADBALANCERBACKEND_HEALTHCHECKFIREWALLSTATE._serialized_start=5414
  _LOADBALANCERBACKEND_HEALTHCHECKFIREWALLSTATE._serialized_end=5520
  _VPNGATEWAYINFO._serialized_start=5523
  _VPNGATEWAYINFO._serialized_end=5718
  _VPNTUNNELINFO._serialized_start=5721
  _VPNTUNNELINFO._serialized_end=6207
  _VPNTUNNELINFO_ROUTINGTYPE._serialized_start=6116
  _VPNTUNNELINFO_ROUTINGTYPE._serialized_end=6207
  _ENDPOINTINFO._serialized_start=6210
  _ENDPOINTINFO._serialized_end=6498
  _DELIVERINFO._serialized_start=6501
  _DELIVERINFO._serialized_end=6751
  _DELIVERINFO_TARGET._serialized_start=6635
  _DELIVERINFO_TARGET._serialized_end=6751
  _FORWARDINFO._serialized_start=6754
  _FORWARDINFO._serialized_end=7049
  _FORWARDINFO_TARGET._serialized_start=6889
  _FORWARDINFO_TARGET._serialized_end=7049
  _ABORTINFO._serialized_start=7052
  _ABORTINFO._serialized_end=7559
  _ABORTINFO_CAUSE._serialized_start=7180
  _ABORTINFO_CAUSE._serialized_end=7559
  _DROPINFO._serialized_start=7562
  _DROPINFO._serialized_end=8381
  _DROPINFO_CAUSE._serialized_start=7688
  _DROPINFO_CAUSE._serialized_end=8381
  _GKEMASTERINFO._serialized_start=8384
  _GKEMASTERINFO._serialized_end=8546
  _CLOUDSQLINSTANCEINFO._serialized_start=8549
  _CLOUDSQLINSTANCEINFO._serialized_end=8747
# @@protoc_insertion_point(module_scope)
