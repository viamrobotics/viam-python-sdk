"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from ...app.packages.v1 import packages_pb2 as app_dot_packages_dot_v1_dot_packages__pb2
from ...common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from ...tagger.v1 import tagger_pb2 as tagger_dot_v1_dot_tagger__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10app/v1/app.proto\x12\x0bviam.app.v1\x1a\x1eapp/packages/v1/packages.proto\x1a\x16common/v1/common.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16tagger/v1/tagger.proto"\xec\x02\n\x05Robot\x123\n\x02id\x18\x01 \x01(\tB#\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"R\x02id\x120\n\x04name\x18\x02 \x01(\tB\x1c\x9a\x84\x9e\x03\x17bson:"name" json:"name"R\x04name\x12@\n\x08location\x18\x03 \x01(\tB$\x9a\x84\x9e\x03\x1fbson:"location" json:"location"R\x08location\x12g\n\x0blast_access\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB*\x9a\x84\x9e\x03%bson:"last_access" json:"last_access"R\nlastAccess\x12Q\n\ncreated_on\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x16\x9a\x84\x9e\x03\x11bson:"created_on"R\tcreatedOn"\xd3\x07\n\tRobotPart\x123\n\x02id\x18\x01 \x01(\tB#\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"R\x02id\x120\n\x04name\x18\x02 \x01(\tB\x1c\x9a\x84\x9e\x03\x17bson:"name" json:"name"R\x04name\x12?\n\x08dns_name\x18\n \x01(\tB$\x9a\x84\x9e\x03\x1fbson:"dns_name" json:"dns_name"R\x07dnsName\x12B\n\x06secret\x18\x03 \x01(\tB*\x9a\x84\x9e\x03%bson:"secret" json:"secret,omitempty"R\x06secret\x124\n\x05robot\x18\x04 \x01(\tB\x1e\x9a\x84\x9e\x03\x19bson:"robot" json:"robot"R\x05robot\x12A\n\x0blocation_id\x18\x0c \x01(\tB \x9a\x84\x9e\x03\x1bbson:"location_id" json:"-"R\nlocationId\x12b\n\x0crobot_config\x18\x05 \x01(\x0b2\x17.google.protobuf.StructB&\x9a\x84\x9e\x03!bson:"config" json:"robot_config"R\x0brobotConfig\x12g\n\x0blast_access\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB*\x9a\x84\x9e\x03%bson:"last_access" json:"last_access"R\nlastAccess\x12\x7f\n\x12user_supplied_info\x18\x07 \x01(\x0b2\x17.google.protobuf.StructB8\x9a\x84\x9e\x033bson:"user_supplied_info" json:"user_supplied_info"R\x10userSuppliedInfo\x12C\n\tmain_part\x18\x08 \x01(\x08B&\x9a\x84\x9e\x03!bson:"main_part" json:"main_part"R\x08mainPart\x12\x12\n\x04fqdn\x18\t \x01(\tR\x04fqdn\x12\x1d\n\nlocal_fqdn\x18\x0b \x01(\tR\tlocalFqdn\x12Q\n\ncreated_on\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x16\x9a\x84\x9e\x03\x11bson:"created_on"R\tcreatedOn\x12H\n\x07secrets\x18\x0e \x03(\x0b2\x19.viam.app.v1.SharedSecretB\x13\x9a\x84\x9e\x03\x0ebson:"secrets"R\x07secrets"\x93\x02\n\x15RobotPartHistoryEntry\x120\n\x04part\x18\x01 \x01(\tB\x1c\x9a\x84\x9e\x03\x17bson:"part" json:"part"R\x04part\x124\n\x05robot\x18\x02 \x01(\tB\x1e\x9a\x84\x9e\x03\x19bson:"robot" json:"robot"R\x05robot\x12L\n\x04when\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\x9a\x84\x9e\x03\x17bson:"when" json:"when"R\x04when\x12D\n\x03old\x18\x04 \x01(\x0b2\x16.viam.app.v1.RobotPartB\x1a\x9a\x84\x9e\x03\x15bson:"old" json:"old"R\x03old"\x1a\n\x18ListOrganizationsRequest"\xde\x01\n\x0cOrganization\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x129\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedOn\x12)\n\x10public_namespace\x18\x04 \x01(\tR\x0fpublicNamespace\x12%\n\x0edefault_region\x18\x05 \x01(\tR\rdefaultRegion\x12\x15\n\x03cid\x18\x06 \x01(\tH\x00R\x03cid\x88\x01\x01B\x06\n\x04_cid"\xcf\x01\n\x12OrganizationMember\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x16\n\x06emails\x18\x02 \x03(\tR\x06emails\x129\n\ndate_added\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tdateAdded\x12>\n\nlast_login\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\tlastLogin\x88\x01\x01B\r\n\x0b_last_login"\\\n\x19ListOrganizationsResponse\x12?\n\rorganizations\x18\x01 \x03(\x0b2\x19.viam.app.v1.OrganizationR\rorganizations"\xd2\x01\n\x12OrganizationInvite\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x14\n\x05email\x18\x02 \x01(\tR\x05email\x129\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedOn\x12B\n\x0eauthorizations\x18\x04 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x0eauthorizations"/\n\x19CreateOrganizationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"[\n\x1aCreateOrganizationResponse\x12=\n\x0corganization\x18\x01 \x01(\x0b2\x19.viam.app.v1.OrganizationR\x0corganization"A\n\x16GetOrganizationRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId"X\n\x17GetOrganizationResponse\x12=\n\x0corganization\x18\x01 \x01(\x0b2\x19.viam.app.v1.OrganizationR\x0corganization"X\n+GetOrganizationNamespaceAvailabilityRequest\x12)\n\x10public_namespace\x18\x01 \x01(\tR\x0fpublicNamespace"L\n,GetOrganizationNamespaceAvailabilityResponse\x12\x1c\n\tavailable\x18\x01 \x01(\x08R\tavailable"\xf2\x01\n\x19UpdateOrganizationRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x12.\n\x10public_namespace\x18\x03 \x01(\tH\x01R\x0fpublicNamespace\x88\x01\x01\x12\x1b\n\x06region\x18\x04 \x01(\tH\x02R\x06region\x88\x01\x01\x12\x15\n\x03cid\x18\x05 \x01(\tH\x03R\x03cid\x88\x01\x01B\x07\n\x05_nameB\x13\n\x11_public_namespaceB\t\n\x07_regionB\x06\n\x04_cid"[\n\x1aUpdateOrganizationResponse\x12=\n\x0corganization\x18\x01 \x01(\x0b2\x19.viam.app.v1.OrganizationR\x0corganization"D\n\x19DeleteOrganizationRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId"\x1c\n\x1aDeleteOrganizationResponse"I\n\x1eListOrganizationMembersRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId"\xc0\x01\n\x1fListOrganizationMembersResponse\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x129\n\x07members\x18\x02 \x03(\x0b2\x1f.viam.app.v1.OrganizationMemberR\x07members\x129\n\x07invites\x18\x03 \x03(\x0b2\x1f.viam.app.v1.OrganizationInviteR\x07invites"\xa4\x01\n\x1fCreateOrganizationInviteRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x14\n\x05email\x18\x02 \x01(\tR\x05email\x12B\n\x0eauthorizations\x18\x03 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x0eauthorizations"[\n CreateOrganizationInviteResponse\x127\n\x06invite\x18\x01 \x01(\x0b2\x1f.viam.app.v1.OrganizationInviteR\x06invite"\x8a\x02\n-UpdateOrganizationInviteAuthorizationsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x14\n\x05email\x18\x02 \x01(\tR\x05email\x12I\n\x12add_authorizations\x18\x03 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x11addAuthorizations\x12O\n\x15remove_authorizations\x18\x04 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x14removeAuthorizations"i\n.UpdateOrganizationInviteAuthorizationsResponse\x127\n\x06invite\x18\x01 \x01(\x0b2\x1f.viam.app.v1.OrganizationInviteR\x06invite"`\n\x1fDeleteOrganizationInviteRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x14\n\x05email\x18\x02 \x01(\tR\x05email""\n DeleteOrganizationInviteResponse"`\n\x1fResendOrganizationInviteRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x14\n\x05email\x18\x02 \x01(\tR\x05email"[\n ResendOrganizationInviteResponse\x127\n\x06invite\x18\x01 \x01(\x0b2\x1f.viam.app.v1.OrganizationInviteR\x06invite"c\n\x1fDeleteOrganizationMemberRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId""\n DeleteOrganizationMemberResponse":\n\x14OrganizationIdentity\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"Y\n\x14LocationOrganization\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x18\n\x07primary\x18\x02 \x01(\x08R\x07primary"\x80\x01\n\x0cLocationAuth\x12\x1a\n\x06secret\x18\x01 \x01(\tB\x02\x18\x01R\x06secret\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId\x123\n\x07secrets\x18\x03 \x03(\x0b2\x19.viam.app.v1.SharedSecretR\x07secrets"\'\n\rStorageConfig\x12\x16\n\x06region\x18\x01 \x01(\tR\x06region"\xe4\x02\n\x08Location\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12,\n\x12parent_location_id\x18\x04 \x01(\tR\x10parentLocationId\x12-\n\x04auth\x18\x05 \x01(\x0b2\x19.viam.app.v1.LocationAuthR\x04auth\x12G\n\rorganizations\x18\x06 \x03(\x0b2!.viam.app.v1.LocationOrganizationR\rorganizations\x129\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedOn\x12\x1f\n\x0brobot_count\x18\x07 \x01(\x05R\nrobotCount\x122\n\x06config\x18\x08 \x01(\x0b2\x1a.viam.app.v1.StorageConfigR\x06config"\xd0\x02\n\x0cSharedSecret\x12\x1e\n\x02id\x18\x01 \x01(\tB\x0e\x9a\x84\x9e\x03\tbson:"id"R\x02id\x12*\n\x06secret\x18\x02 \x01(\tB\x12\x9a\x84\x9e\x03\rbson:"secret"R\x06secret\x12c\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB(\x9a\x84\x9e\x03#bson:"created_on" json:"created_on"R\tcreatedOn\x12H\n\x05state\x18\x04 \x01(\x0e2\x1f.viam.app.v1.SharedSecret.StateB\x11\x9a\x84\x9e\x03\x0cbson:"state"R\x05state"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x11\n\rSTATE_ENABLED\x10\x01\x12\x12\n\x0eSTATE_DISABLED\x10\x02"\x9e\x01\n\x15CreateLocationRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x121\n\x12parent_location_id\x18\x03 \x01(\tH\x00R\x10parentLocationId\x88\x01\x01B\x15\n\x13_parent_location_id"K\n\x16CreateLocationResponse\x121\n\x08location\x18\x01 \x01(\x0b2\x15.viam.app.v1.LocationR\x08location"5\n\x12GetLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"H\n\x13GetLocationResponse\x121\n\x08location\x18\x01 \x01(\x0b2\x15.viam.app.v1.LocationR\x08location"\xcc\x01\n\x15UpdateLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x121\n\x12parent_location_id\x18\x03 \x01(\tH\x01R\x10parentLocationId\x88\x01\x01\x12\x1b\n\x06region\x18\x04 \x01(\tH\x02R\x06region\x88\x01\x01B\x07\n\x05_nameB\x15\n\x13_parent_location_idB\t\n\x07_region"K\n\x16UpdateLocationResponse\x121\n\x08location\x18\x01 \x01(\x0b2\x15.viam.app.v1.LocationR\x08location"8\n\x15DeleteLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"\x18\n\x16DeleteLocationResponse"N\n+GetOrganizationsWithAccessToLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"\x8a\x01\n,GetOrganizationsWithAccessToLocationResponse\x12Z\n\x17organization_identities\x18\x01 \x03(\x0b2!.viam.app.v1.OrganizationIdentityR\x16organizationIdentities"?\n\x14ListLocationsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId"`\n\x14ShareLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId"\x17\n\x15ShareLocationResponse"b\n\x16UnshareLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId"\x19\n\x17UnshareLocationResponse"L\n\x15ListLocationsResponse\x123\n\tlocations\x18\x01 \x03(\x0b2\x15.viam.app.v1.LocationR\tlocations">\n\x1bCreateLocationSecretRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"M\n\x1cCreateLocationSecretResponse\x12-\n\x04auth\x18\x01 \x01(\x0b2\x19.viam.app.v1.LocationAuthR\x04auth"[\n\x1bDeleteLocationSecretRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId\x12\x1b\n\tsecret_id\x18\x02 \x01(\tR\x08secretId"\x1e\n\x1cDeleteLocationSecretResponse"6\n\x13LocationAuthRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"E\n\x14LocationAuthResponse\x12-\n\x04auth\x18\x01 \x01(\x0b2\x19.viam.app.v1.LocationAuthR\x04auth"!\n\x0fGetRobotRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"4\n\x1bGetRoverRentalRobotsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\x9a\x01\n\x10RoverRentalRobot\x12\x19\n\x08robot_id\x18\x01 \x01(\tR\x07robotId\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId\x12\x1d\n\nrobot_name\x18\x03 \x01(\tR\trobotName\x12+\n\x12robot_main_part_id\x18\x04 \x01(\tR\x0frobotMainPartId"U\n\x1cGetRoverRentalRobotsResponse\x125\n\x06robots\x18\x01 \x03(\x0b2\x1d.viam.app.v1.RoverRentalRobotR\x06robots"<\n\x10GetRobotResponse\x12(\n\x05robot\x18\x01 \x01(\x0b2\x12.viam.app.v1.RobotR\x05robot"1\n\x14GetRobotPartsRequest\x12\x19\n\x08robot_id\x18\x01 \x01(\tR\x07robotId"E\n\x15GetRobotPartsResponse\x12,\n\x05parts\x18\x01 \x03(\x0b2\x16.viam.app.v1.RobotPartR\x05parts"%\n\x13GetRobotPartRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"c\n\x14GetRobotPartResponse\x12*\n\x04part\x18\x01 \x01(\x0b2\x16.viam.app.v1.RobotPartR\x04part\x12\x1f\n\x0bconfig_json\x18\x02 \x01(\tR\nconfigJson"\xc1\x01\n\x17GetRobotPartLogsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12#\n\x0berrors_only\x18\x02 \x01(\x08B\x02\x18\x01R\nerrorsOnly\x12\x1b\n\x06filter\x18\x03 \x01(\tH\x00R\x06filter\x88\x01\x01\x12"\n\npage_token\x18\x04 \x01(\tH\x01R\tpageToken\x88\x01\x01\x12\x16\n\x06levels\x18\x05 \x03(\tR\x06levelsB\t\n\x07_filterB\r\n\x0b_page_token"p\n\x18GetRobotPartLogsResponse\x12,\n\x04logs\x18\x01 \x03(\x0b2\x18.viam.common.v1.LogEntryR\x04logs\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken"s\n\x18TailRobotPartLogsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1f\n\x0berrors_only\x18\x02 \x01(\x08R\nerrorsOnly\x12\x1b\n\x06filter\x18\x03 \x01(\tH\x00R\x06filter\x88\x01\x01B\t\n\x07_filter"I\n\x19TailRobotPartLogsResponse\x12,\n\x04logs\x18\x01 \x03(\x0b2\x18.viam.common.v1.LogEntryR\x04logs",\n\x1aGetRobotPartHistoryRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"[\n\x1bGetRobotPartHistoryResponse\x12<\n\x07history\x18\x01 \x03(\x0b2".viam.app.v1.RobotPartHistoryEntryR\x07history"x\n\x16UpdateRobotPartRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12:\n\x0crobot_config\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x0brobotConfig"E\n\x17UpdateRobotPartResponse\x12*\n\x04part\x18\x01 \x01(\x0b2\x16.viam.app.v1.RobotPartR\x04part"M\n\x13NewRobotPartRequest\x12\x19\n\x08robot_id\x18\x01 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x02 \x01(\tR\x08partName"/\n\x14NewRobotPartResponse\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId"1\n\x16DeleteRobotPartRequest\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId"3\n\x16GetRobotAPIKeysRequest\x12\x19\n\x08robot_id\x18\x01 \x01(\tR\x07robotId"y\n\x06APIKey\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x129\n\ncreated_on\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedOn"[\n\x17GetRobotAPIKeysResponse\x12@\n\x08api_keys\x18\x01 \x03(\x0b2%.viam.app.v1.APIKeyWithAuthorizationsR\x07apiKeys"\x19\n\x17DeleteRobotPartResponse"\xe8\x04\n\x08Fragment\x123\n\x02id\x18\x01 \x01(\tB#\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"R\x02id\x120\n\x04name\x18\x02 \x01(\tB\x1c\x9a\x84\x9e\x03\x17bson:"name" json:"name"R\x04name\x12Y\n\x08fragment\x18\x03 \x01(\x0b2\x17.google.protobuf.StructB$\x9a\x84\x9e\x03\x1fbson:"fragment" json:"fragment"R\x08fragment\x12Z\n\x12organization_owner\x18\x04 \x01(\tB+\x9a\x84\x9e\x03&bson:"organization_owner" json:"owner"R\x11organizationOwner\x128\n\x06public\x18\x05 \x01(\x08B \x9a\x84\x9e\x03\x1bbson:"public" json:"public"R\x06public\x12Q\n\ncreated_on\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x16\x9a\x84\x9e\x03\x11bson:"created_on"R\tcreatedOn\x12+\n\x11organization_name\x18\x07 \x01(\tR\x10organizationName\x12(\n\x10robot_part_count\x18\t \x01(\x05R\x0erobotPartCount\x12-\n\x12organization_count\x18\n \x01(\x05R\x11organizationCount\x12+\n\x12only_used_by_owner\x18\x0b \x01(\x08R\x0fonlyUsedByOwner"`\n\x14ListFragmentsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x1f\n\x0bshow_public\x18\x02 \x01(\x08R\nshowPublic"L\n\x15ListFragmentsResponse\x123\n\tfragments\x18\x01 \x03(\x0b2\x15.viam.app.v1.FragmentR\tfragments"$\n\x12GetFragmentRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"H\n\x13GetFragmentResponse\x121\n\x08fragment\x18\x01 \x01(\x0b2\x15.viam.app.v1.FragmentR\x08fragment"\x85\x01\n\x15CreateFragmentRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12/\n\x06config\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x06config\x12\'\n\x0forganization_id\x18\x03 \x01(\tR\x0eorganizationId"K\n\x16CreateFragmentResponse\x121\n\x08fragment\x18\x01 \x01(\x0b2\x15.viam.app.v1.FragmentR\x08fragment"\x94\x01\n\x15UpdateFragmentRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12/\n\x06config\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x06config\x12\x1b\n\x06public\x18\x04 \x01(\x08H\x00R\x06public\x88\x01\x01B\t\n\x07_public"K\n\x16UpdateFragmentResponse\x121\n\x08fragment\x18\x01 \x01(\x0b2\x15.viam.app.v1.FragmentR\x08fragment"\'\n\x15DeleteFragmentRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x18\n\x16DeleteFragmentResponse"4\n\x11ListRobotsRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"@\n\x12ListRobotsResponse\x12*\n\x06robots\x18\x01 \x03(\x0b2\x12.viam.app.v1.RobotR\x06robots"A\n\x0fNewRobotRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1a\n\x08location\x18\x02 \x01(\tR\x08location""\n\x10NewRobotResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"T\n\x12UpdateRobotRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1a\n\x08location\x18\x03 \x01(\tR\x08location"?\n\x13UpdateRobotResponse\x12(\n\x05robot\x18\x01 \x01(\x0b2\x12.viam.app.v1.RobotR\x05robot"$\n\x12DeleteRobotRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x15\n\x13DeleteRobotResponse"0\n\x15MarkPartAsMainRequest\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId"\x18\n\x16MarkPartAsMainResponse"4\n\x19MarkPartForRestartRequest\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId"\x1c\n\x1aMarkPartForRestartResponse"7\n\x1cCreateRobotPartSecretRequest\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId"K\n\x1dCreateRobotPartSecretResponse\x12*\n\x04part\x18\x01 \x01(\x0b2\x16.viam.app.v1.RobotPartR\x04part"T\n\x1cDeleteRobotPartSecretRequest\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId\x12\x1b\n\tsecret_id\x18\x02 \x01(\tR\x08secretId"\x1f\n\x1dDeleteRobotPartSecretResponse"\x9e\x02\n\rAuthorization\x12-\n\x12authorization_type\x18\x01 \x01(\tR\x11authorizationType\x12)\n\x10authorization_id\x18\x02 \x01(\tR\x0fauthorizationId\x12#\n\rresource_type\x18\x03 \x01(\tR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x04 \x01(\tR\nresourceId\x12\x1f\n\x0bidentity_id\x18\x05 \x01(\tR\nidentityId\x12\'\n\x0forganization_id\x18\x06 \x01(\tR\x0eorganizationId\x12#\n\ridentity_type\x18\x07 \x01(\tR\x0cidentityType"R\n\x0eAddRoleRequest\x12@\n\rauthorization\x18\x01 \x01(\x0b2\x1a.viam.app.v1.AuthorizationR\rauthorization"\x11\n\x0fAddRoleResponse"U\n\x11RemoveRoleRequest\x12@\n\rauthorization\x18\x01 \x01(\x0b2\x1a.viam.app.v1.AuthorizationR\rauthorization"\x14\n\x12RemoveRoleResponse"\xa5\x01\n\x11ChangeRoleRequest\x12G\n\x11old_authorization\x18\x01 \x01(\x0b2\x1a.viam.app.v1.AuthorizationR\x10oldAuthorization\x12G\n\x11new_authorization\x18\x02 \x01(\x0b2\x1a.viam.app.v1.AuthorizationR\x10newAuthorization"\x14\n\x12ChangeRoleResponse"g\n\x19ListAuthorizationsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12!\n\x0cresource_ids\x18\x02 \x03(\tR\x0bresourceIds"`\n\x1aListAuthorizationsResponse\x12B\n\x0eauthorizations\x18\x01 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x0eauthorizations"_\n\x17CheckPermissionsRequest\x12D\n\x0bpermissions\x18\x01 \x03(\x0b2".viam.app.v1.AuthorizedPermissionsR\x0bpermissions"\x7f\n\x15AuthorizedPermissions\x12#\n\rresource_type\x18\x01 \x01(\tR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12 \n\x0bpermissions\x18\x03 \x03(\tR\x0bpermissions"u\n\x18CheckPermissionsResponse\x12Y\n\x16authorized_permissions\x18\x01 \x03(\x0b2".viam.app.v1.AuthorizedPermissionsR\x15authorizedPermissions"\xa1\x01\n\rModuleVersion\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12*\n\x05files\x18\x02 \x03(\x0b2\x14.viam.app.v1.UploadsR\x05files\x12*\n\x06models\x18\x03 \x03(\x0b2\x12.viam.app.v1.ModelR\x06models\x12\x1e\n\nentrypoint\x18\x04 \x01(\tR\nentrypoint"\x94\x01\n\x0eModuleMetadata\x12*\n\x06models\x18\x01 \x03(\x0b2\x12.viam.app.v1.ModelR\x06models\x126\n\x08versions\x18\x02 \x03(\x0b2\x1a.viam.app.v1.ModuleVersionR\x08versions\x12\x1e\n\nentrypoint\x18\x03 \x01(\tR\nentrypoint"-\n\x0fMLModelMetadata\x12\x1a\n\x08versions\x18\x01 \x03(\tR\x08versions"\xb7\x06\n\x0cRegistryItem\x12\x17\n\x07item_id\x18\x01 \x01(\tR\x06itemId\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId\x12)\n\x10public_namespace\x18\x03 \x01(\tR\x0fpublicNamespace\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x125\n\x04type\x18\x05 \x01(\x0e2!.viam.app.packages.v1.PackageTypeR\x04type\x127\n\nvisibility\x18\x06 \x01(\x0e2\x17.viam.app.v1.VisibilityR\nvisibility\x12\x10\n\x03url\x18\x07 \x01(\tR\x03url\x12 \n\x0bdescription\x18\x08 \x01(\tR\x0bdescription\x12*\n\x11total_robot_usage\x18\t \x01(\x03R\x0ftotalRobotUsage\x12;\n\x1atotal_external_robot_usage\x18\r \x01(\x03R\x17totalExternalRobotUsage\x128\n\x18total_organization_usage\x18\n \x01(\x03R\x16totalOrganizationUsage\x12I\n!total_external_organization_usage\x18\x0e \x01(\x03R\x1etotalExternalOrganizationUsage\x12F\n\x0fmodule_metadata\x18\x0b \x01(\x0b2\x1b.viam.app.v1.ModuleMetadataH\x00R\x0emoduleMetadata\x12J\n\x11ml_model_metadata\x18\x0c \x01(\x0b2\x1c.viam.app.v1.MLModelMetadataH\x00R\x0fmlModelMetadata\x129\n\ncreated_at\x18\x0f \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAtB\n\n\x08metadata"1\n\x16GetRegistryItemRequest\x12\x17\n\x07item_id\x18\x01 \x01(\tR\x06itemId"H\n\x17GetRegistryItemResponse\x12-\n\x04item\x18\x01 \x01(\x0b2\x19.viam.app.v1.RegistryItemR\x04item"\x8f\x01\n\x19CreateRegistryItemRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x125\n\x04type\x18\x03 \x01(\x0e2!.viam.app.packages.v1.PackageTypeR\x04type"\x1c\n\x1aCreateRegistryItemResponse"\xc6\x01\n\x19UpdateRegistryItemRequest\x12\x17\n\x07item_id\x18\x01 \x01(\tR\x06itemId\x125\n\x04type\x18\x02 \x01(\x0e2!.viam.app.packages.v1.PackageTypeR\x04type\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x127\n\nvisibility\x18\x04 \x01(\x0e2\x17.viam.app.v1.VisibilityR\nvisibility"\x1c\n\x1aUpdateRegistryItemResponse"\x96\x03\n\x18ListRegistryItemsRequest\x12,\n\x0forganization_id\x18\x01 \x01(\tH\x00R\x0eorganizationId\x88\x01\x01\x127\n\x05types\x18\x02 \x03(\x0e2!.viam.app.packages.v1.PackageTypeR\x05types\x12;\n\x0cvisibilities\x18\x03 \x03(\x0e2\x17.viam.app.v1.VisibilityR\x0cvisibilities\x12\x1c\n\tplatforms\x18\x04 \x03(\tR\tplatforms\x12;\n\x08statuses\x18\x05 \x03(\x0e2\x1f.viam.app.v1.RegistryItemStatusR\x08statuses\x12$\n\x0bsearch_term\x18\x06 \x01(\tH\x01R\nsearchTerm\x88\x01\x01\x12"\n\npage_token\x18\x07 \x01(\tH\x02R\tpageToken\x88\x01\x01B\x12\n\x10_organization_idB\x0e\n\x0c_search_termB\r\n\x0b_page_token"L\n\x19ListRegistryItemsResponse\x12/\n\x05items\x18\x01 \x03(\x0b2\x19.viam.app.v1.RegistryItemR\x05items"4\n\x19DeleteRegistryItemRequest\x12\x17\n\x07item_id\x18\x01 \x01(\tR\x06itemId"\x1c\n\x1aDeleteRegistryItemResponse"R\n\x13CreateModuleRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"E\n\x14CreateModuleResponse\x12\x1b\n\tmodule_id\x18\x01 \x01(\tR\x08moduleId\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url"\xeb\x01\n\x13UpdateModuleRequest\x12\x1b\n\tmodule_id\x18\x01 \x01(\tR\x08moduleId\x127\n\nvisibility\x18\x02 \x01(\x0e2\x17.viam.app.v1.VisibilityR\nvisibility\x12\x10\n\x03url\x18\x03 \x01(\tR\x03url\x12 \n\x0bdescription\x18\x04 \x01(\tR\x0bdescription\x12*\n\x06models\x18\x05 \x03(\x0b2\x12.viam.app.v1.ModelR\x06models\x12\x1e\n\nentrypoint\x18\x06 \x01(\tR\nentrypoint"(\n\x14UpdateModuleResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url"/\n\x05Model\x12\x10\n\x03api\x18\x01 \x01(\tR\x03api\x12\x14\n\x05model\x18\x02 \x01(\tR\x05model"c\n\x0eModuleFileInfo\x12\x1b\n\tmodule_id\x18\x01 \x01(\tR\x08moduleId\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12\x1a\n\x08platform\x18\x03 \x01(\tR\x08platform"\x87\x01\n\x17UploadModuleFileRequest\x12G\n\x10module_file_info\x18\x01 \x01(\x0b2\x1b.viam.app.v1.ModuleFileInfoH\x00R\x0emoduleFileInfo\x12\x14\n\x04file\x18\x02 \x01(\x0cH\x00R\x04fileB\r\n\x0bmodule_file",\n\x18UploadModuleFileResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url"/\n\x10GetModuleRequest\x12\x1b\n\tmodule_id\x18\x01 \x01(\tR\x08moduleId"@\n\x11GetModuleResponse\x12+\n\x06module\x18\x01 \x01(\x0b2\x13.viam.app.v1.ModuleR\x06module"\xe5\x03\n\x06Module\x12\x1b\n\tmodule_id\x18\x01 \x01(\tR\x08moduleId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x127\n\nvisibility\x18\x03 \x01(\x0e2\x17.viam.app.v1.VisibilityR\nvisibility\x127\n\x08versions\x18\x04 \x03(\x0b2\x1b.viam.app.v1.VersionHistoryR\x08versions\x12\x10\n\x03url\x18\x05 \x01(\tR\x03url\x12 \n\x0bdescription\x18\x06 \x01(\tR\x0bdescription\x12*\n\x06models\x18\x07 \x03(\x0b2\x12.viam.app.v1.ModelR\x06models\x12*\n\x11total_robot_usage\x18\x08 \x01(\x03R\x0ftotalRobotUsage\x128\n\x18total_organization_usage\x18\t \x01(\x03R\x16totalOrganizationUsage\x12\'\n\x0forganization_id\x18\n \x01(\tR\x0eorganizationId\x12\x1e\n\nentrypoint\x18\x0b \x01(\tR\nentrypoint\x12)\n\x10public_namespace\x18\x0c \x01(\tR\x0fpublicNamespace"\xa2\x01\n\x0eVersionHistory\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12*\n\x05files\x18\x02 \x03(\x0b2\x14.viam.app.v1.UploadsR\x05files\x12*\n\x06models\x18\x03 \x03(\x0b2\x12.viam.app.v1.ModelR\x06models\x12\x1e\n\nentrypoint\x18\x04 \x01(\tR\nentrypoint"b\n\x07Uploads\x12\x1a\n\x08platform\x18\x01 \x01(\tR\x08platform\x12;\n\x0buploaded_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\nuploadedAt"V\n\x12ListModulesRequest\x12,\n\x0forganization_id\x18\x01 \x01(\tH\x00R\x0eorganizationId\x88\x01\x01B\x12\n\x10_organization_id"D\n\x13ListModulesResponse\x12-\n\x07modules\x18\x01 \x03(\x0b2\x13.viam.app.v1.ModuleR\x07modules"/\n\x17GetUserIDByEmailRequest\x12\x14\n\x05email\x18\x01 \x01(\tR\x05email"3\n\x18GetUserIDByEmailResponse\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId"9\n\x1eListOrganizationsByUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId">\n\nOrgDetails\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x19\n\x08org_name\x18\x02 \x01(\tR\x07orgName"N\n\x1fListOrganizationsByUserResponse\x12+\n\x04orgs\x18\x01 \x03(\x0b2\x17.viam.app.v1.OrgDetailsR\x04orgs"j\n\x10CreateKeyRequest\x12B\n\x0eauthorizations\x18\x01 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x0eauthorizations\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"5\n\x11CreateKeyResponse\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id""\n\x10DeleteKeyRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x13\n\x11DeleteKeyResponse"\xcd\x01\n\x14AuthorizationDetails\x12-\n\x12authorization_type\x18\x01 \x01(\tR\x11authorizationType\x12)\n\x10authorization_id\x18\x02 \x01(\tR\x0fauthorizationId\x12#\n\rresource_type\x18\x03 \x01(\tR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x04 \x01(\tR\nresourceId\x12\x15\n\x06org_id\x18\x05 \x01(\tR\x05orgId"\x93\x01\n\x18APIKeyWithAuthorizations\x12,\n\x07api_key\x18\x01 \x01(\x0b2\x13.viam.app.v1.APIKeyR\x06apiKey\x12I\n\x0eauthorizations\x18\x02 \x03(\x0b2!.viam.app.v1.AuthorizationDetailsR\x0eauthorizations"(\n\x0fListKeysRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"T\n\x10ListKeysResponse\x12@\n\x08api_keys\x18\x01 \x03(\x0b2%.viam.app.v1.APIKeyWithAuthorizationsR\x07apiKeys""\n\x10RotateKeyRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"5\n\x11RotateKeyResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key"?\n-CreateKeyFromExistingKeyAuthorizationsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"R\n.CreateKeyFromExistingKeyAuthorizationsResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key*\x87\x01\n\x12RegistryItemStatus\x12$\n REGISTRY_ITEM_STATUS_UNSPECIFIED\x10\x00\x12"\n\x1eREGISTRY_ITEM_STATUS_PUBLISHED\x10\x01\x12\'\n#REGISTRY_ITEM_STATUS_IN_DEVELOPMENT\x10\x02*W\n\nVisibility\x12\x1a\n\x16VISIBILITY_UNSPECIFIED\x10\x00\x12\x16\n\x12VISIBILITY_PRIVATE\x10\x01\x12\x15\n\x11VISIBILITY_PUBLIC\x10\x022\xef4\n\nAppService\x12_\n\x10GetUserIDByEmail\x12$.viam.app.v1.GetUserIDByEmailRequest\x1a%.viam.app.v1.GetUserIDByEmailResponse\x12e\n\x12CreateOrganization\x12&.viam.app.v1.CreateOrganizationRequest\x1a\'.viam.app.v1.CreateOrganizationResponse\x12b\n\x11ListOrganizations\x12%.viam.app.v1.ListOrganizationsRequest\x1a&.viam.app.v1.ListOrganizationsResponse\x12\x9b\x01\n$GetOrganizationsWithAccessToLocation\x128.viam.app.v1.GetOrganizationsWithAccessToLocationRequest\x1a9.viam.app.v1.GetOrganizationsWithAccessToLocationResponse\x12t\n\x17ListOrganizationsByUser\x12+.viam.app.v1.ListOrganizationsByUserRequest\x1a,.viam.app.v1.ListOrganizationsByUserResponse\x12\\\n\x0fGetOrganization\x12#.viam.app.v1.GetOrganizationRequest\x1a$.viam.app.v1.GetOrganizationResponse\x12\x9b\x01\n$GetOrganizationNamespaceAvailability\x128.viam.app.v1.GetOrganizationNamespaceAvailabilityRequest\x1a9.viam.app.v1.GetOrganizationNamespaceAvailabilityResponse\x12e\n\x12UpdateOrganization\x12&.viam.app.v1.UpdateOrganizationRequest\x1a\'.viam.app.v1.UpdateOrganizationResponse\x12e\n\x12DeleteOrganization\x12&.viam.app.v1.DeleteOrganizationRequest\x1a\'.viam.app.v1.DeleteOrganizationResponse\x12t\n\x17ListOrganizationMembers\x12+.viam.app.v1.ListOrganizationMembersRequest\x1a,.viam.app.v1.ListOrganizationMembersResponse\x12w\n\x18CreateOrganizationInvite\x12,.viam.app.v1.CreateOrganizationInviteRequest\x1a-.viam.app.v1.CreateOrganizationInviteResponse\x12\xa1\x01\n&UpdateOrganizationInviteAuthorizations\x12:.viam.app.v1.UpdateOrganizationInviteAuthorizationsRequest\x1a;.viam.app.v1.UpdateOrganizationInviteAuthorizationsResponse\x12w\n\x18DeleteOrganizationMember\x12,.viam.app.v1.DeleteOrganizationMemberRequest\x1a-.viam.app.v1.DeleteOrganizationMemberResponse\x12w\n\x18DeleteOrganizationInvite\x12,.viam.app.v1.DeleteOrganizationInviteRequest\x1a-.viam.app.v1.DeleteOrganizationInviteResponse\x12w\n\x18ResendOrganizationInvite\x12,.viam.app.v1.ResendOrganizationInviteRequest\x1a-.viam.app.v1.ResendOrganizationInviteResponse\x12Y\n\x0eCreateLocation\x12".viam.app.v1.CreateLocationRequest\x1a#.viam.app.v1.CreateLocationResponse\x12P\n\x0bGetLocation\x12\x1f.viam.app.v1.GetLocationRequest\x1a .viam.app.v1.GetLocationResponse\x12Y\n\x0eUpdateLocation\x12".viam.app.v1.UpdateLocationRequest\x1a#.viam.app.v1.UpdateLocationResponse\x12Y\n\x0eDeleteLocation\x12".viam.app.v1.DeleteLocationRequest\x1a#.viam.app.v1.DeleteLocationResponse\x12V\n\rListLocations\x12!.viam.app.v1.ListLocationsRequest\x1a".viam.app.v1.ListLocationsResponse\x12V\n\rShareLocation\x12!.viam.app.v1.ShareLocationRequest\x1a".viam.app.v1.ShareLocationResponse\x12\\\n\x0fUnshareLocation\x12#.viam.app.v1.UnshareLocationRequest\x1a$.viam.app.v1.UnshareLocationResponse\x12S\n\x0cLocationAuth\x12 .viam.app.v1.LocationAuthRequest\x1a!.viam.app.v1.LocationAuthResponse\x12k\n\x14CreateLocationSecret\x12(.viam.app.v1.CreateLocationSecretRequest\x1a).viam.app.v1.CreateLocationSecretResponse\x12k\n\x14DeleteLocationSecret\x12(.viam.app.v1.DeleteLocationSecretRequest\x1a).viam.app.v1.DeleteLocationSecretResponse\x12G\n\x08GetRobot\x12\x1c.viam.app.v1.GetRobotRequest\x1a\x1d.viam.app.v1.GetRobotResponse\x12k\n\x14GetRoverRentalRobots\x12(.viam.app.v1.GetRoverRentalRobotsRequest\x1a).viam.app.v1.GetRoverRentalRobotsResponse\x12V\n\rGetRobotParts\x12!.viam.app.v1.GetRobotPartsRequest\x1a".viam.app.v1.GetRobotPartsResponse\x12S\n\x0cGetRobotPart\x12 .viam.app.v1.GetRobotPartRequest\x1a!.viam.app.v1.GetRobotPartResponse\x12_\n\x10GetRobotPartLogs\x12$.viam.app.v1.GetRobotPartLogsRequest\x1a%.viam.app.v1.GetRobotPartLogsResponse\x12d\n\x11TailRobotPartLogs\x12%.viam.app.v1.TailRobotPartLogsRequest\x1a&.viam.app.v1.TailRobotPartLogsResponse0\x01\x12h\n\x13GetRobotPartHistory\x12\'.viam.app.v1.GetRobotPartHistoryRequest\x1a(.viam.app.v1.GetRobotPartHistoryResponse\x12\\\n\x0fUpdateRobotPart\x12#.viam.app.v1.UpdateRobotPartRequest\x1a$.viam.app.v1.UpdateRobotPartResponse\x12S\n\x0cNewRobotPart\x12 .viam.app.v1.NewRobotPartRequest\x1a!.viam.app.v1.NewRobotPartResponse\x12\\\n\x0fDeleteRobotPart\x12#.viam.app.v1.DeleteRobotPartRequest\x1a$.viam.app.v1.DeleteRobotPartResponse\x12\\\n\x0fGetRobotAPIKeys\x12#.viam.app.v1.GetRobotAPIKeysRequest\x1a$.viam.app.v1.GetRobotAPIKeysResponse\x12Y\n\x0eMarkPartAsMain\x12".viam.app.v1.MarkPartAsMainRequest\x1a#.viam.app.v1.MarkPartAsMainResponse\x12e\n\x12MarkPartForRestart\x12&.viam.app.v1.MarkPartForRestartRequest\x1a\'.viam.app.v1.MarkPartForRestartResponse\x12n\n\x15CreateRobotPartSecret\x12).viam.app.v1.CreateRobotPartSecretRequest\x1a*.viam.app.v1.CreateRobotPartSecretResponse\x12n\n\x15DeleteRobotPartSecret\x12).viam.app.v1.DeleteRobotPartSecretRequest\x1a*.viam.app.v1.DeleteRobotPartSecretResponse\x12M\n\nListRobots\x12\x1e.viam.app.v1.ListRobotsRequest\x1a\x1f.viam.app.v1.ListRobotsResponse\x12G\n\x08NewRobot\x12\x1c.viam.app.v1.NewRobotRequest\x1a\x1d.viam.app.v1.NewRobotResponse\x12P\n\x0bUpdateRobot\x12\x1f.viam.app.v1.UpdateRobotRequest\x1a .viam.app.v1.UpdateRobotResponse\x12P\n\x0bDeleteRobot\x12\x1f.viam.app.v1.DeleteRobotRequest\x1a .viam.app.v1.DeleteRobotResponse\x12V\n\rListFragments\x12!.viam.app.v1.ListFragmentsRequest\x1a".viam.app.v1.ListFragmentsResponse\x12P\n\x0bGetFragment\x12\x1f.viam.app.v1.GetFragmentRequest\x1a .viam.app.v1.GetFragmentResponse\x12Y\n\x0eCreateFragment\x12".viam.app.v1.CreateFragmentRequest\x1a#.viam.app.v1.CreateFragmentResponse\x12Y\n\x0eUpdateFragment\x12".viam.app.v1.UpdateFragmentRequest\x1a#.viam.app.v1.UpdateFragmentResponse\x12Y\n\x0eDeleteFragment\x12".viam.app.v1.DeleteFragmentRequest\x1a#.viam.app.v1.DeleteFragmentResponse\x12D\n\x07AddRole\x12\x1b.viam.app.v1.AddRoleRequest\x1a\x1c.viam.app.v1.AddRoleResponse\x12M\n\nRemoveRole\x12\x1e.viam.app.v1.RemoveRoleRequest\x1a\x1f.viam.app.v1.RemoveRoleResponse\x12M\n\nChangeRole\x12\x1e.viam.app.v1.ChangeRoleRequest\x1a\x1f.viam.app.v1.ChangeRoleResponse\x12e\n\x12ListAuthorizations\x12&.viam.app.v1.ListAuthorizationsRequest\x1a\'.viam.app.v1.ListAuthorizationsResponse\x12_\n\x10CheckPermissions\x12$.viam.app.v1.CheckPermissionsRequest\x1a%.viam.app.v1.CheckPermissionsResponse\x12\\\n\x0fGetRegistryItem\x12#.viam.app.v1.GetRegistryItemRequest\x1a$.viam.app.v1.GetRegistryItemResponse\x12e\n\x12CreateRegistryItem\x12&.viam.app.v1.CreateRegistryItemRequest\x1a\'.viam.app.v1.CreateRegistryItemResponse\x12e\n\x12UpdateRegistryItem\x12&.viam.app.v1.UpdateRegistryItemRequest\x1a\'.viam.app.v1.UpdateRegistryItemResponse\x12b\n\x11ListRegistryItems\x12%.viam.app.v1.ListRegistryItemsRequest\x1a&.viam.app.v1.ListRegistryItemsResponse\x12e\n\x12DeleteRegistryItem\x12&.viam.app.v1.DeleteRegistryItemRequest\x1a\'.viam.app.v1.DeleteRegistryItemResponse\x12S\n\x0cCreateModule\x12 .viam.app.v1.CreateModuleRequest\x1a!.viam.app.v1.CreateModuleResponse\x12S\n\x0cUpdateModule\x12 .viam.app.v1.UpdateModuleRequest\x1a!.viam.app.v1.UpdateModuleResponse\x12a\n\x10UploadModuleFile\x12$.viam.app.v1.UploadModuleFileRequest\x1a%.viam.app.v1.UploadModuleFileResponse(\x01\x12J\n\tGetModule\x12\x1d.viam.app.v1.GetModuleRequest\x1a\x1e.viam.app.v1.GetModuleResponse\x12P\n\x0bListModules\x12\x1f.viam.app.v1.ListModulesRequest\x1a .viam.app.v1.ListModulesResponse\x12J\n\tCreateKey\x12\x1d.viam.app.v1.CreateKeyRequest\x1a\x1e.viam.app.v1.CreateKeyResponse\x12J\n\tDeleteKey\x12\x1d.viam.app.v1.DeleteKeyRequest\x1a\x1e.viam.app.v1.DeleteKeyResponse\x12G\n\x08ListKeys\x12\x1c.viam.app.v1.ListKeysRequest\x1a\x1d.viam.app.v1.ListKeysResponse\x12J\n\tRotateKey\x12\x1d.viam.app.v1.RotateKeyRequest\x1a\x1e.viam.app.v1.RotateKeyResponse\x12\xa1\x01\n&CreateKeyFromExistingKeyAuthorizations\x12:.viam.app.v1.CreateKeyFromExistingKeyAuthorizationsRequest\x1a;.viam.app.v1.CreateKeyFromExistingKeyAuthorizationsResponseB\x18Z\x16go.viam.com/api/app/v1b\x06proto3'
)
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "app.v1.app_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z\x16go.viam.com/api/app/v1"
    _ROBOT.fields_by_name["id"]._options = None
    _ROBOT.fields_by_name[
        "id"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"'
    _ROBOT.fields_by_name["name"]._options = None
    _ROBOT.fields_by_name[
        "name"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"name" json:"name"'
    _ROBOT.fields_by_name["location"]._options = None
    _ROBOT.fields_by_name[
        "location"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"location" json:"location"'
    _ROBOT.fields_by_name["last_access"]._options = None
    _ROBOT.fields_by_name[
        "last_access"
    ]._serialized_options = b'\x9a\x84\x9e\x03%bson:"last_access" json:"last_access"'
    _ROBOT.fields_by_name["created_on"]._options = None
    _ROBOT.fields_by_name[
        "created_on"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x11bson:"created_on"'
    _ROBOTPART.fields_by_name["id"]._options = None
    _ROBOTPART.fields_by_name[
        "id"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"'
    _ROBOTPART.fields_by_name["name"]._options = None
    _ROBOTPART.fields_by_name[
        "name"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"name" json:"name"'
    _ROBOTPART.fields_by_name["dns_name"]._options = None
    _ROBOTPART.fields_by_name[
        "dns_name"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"dns_name" json:"dns_name"'
    _ROBOTPART.fields_by_name["secret"]._options = None
    _ROBOTPART.fields_by_name[
        "secret"
    ]._serialized_options = b'\x9a\x84\x9e\x03%bson:"secret" json:"secret,omitempty"'
    _ROBOTPART.fields_by_name["robot"]._options = None
    _ROBOTPART.fields_by_name[
        "robot"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x19bson:"robot" json:"robot"'
    _ROBOTPART.fields_by_name["location_id"]._options = None
    _ROBOTPART.fields_by_name[
        "location_id"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x1bbson:"location_id" json:"-"'
    _ROBOTPART.fields_by_name["robot_config"]._options = None
    _ROBOTPART.fields_by_name[
        "robot_config"
    ]._serialized_options = b'\x9a\x84\x9e\x03!bson:"config" json:"robot_config"'
    _ROBOTPART.fields_by_name["last_access"]._options = None
    _ROBOTPART.fields_by_name[
        "last_access"
    ]._serialized_options = b'\x9a\x84\x9e\x03%bson:"last_access" json:"last_access"'
    _ROBOTPART.fields_by_name["user_supplied_info"]._options = None
    _ROBOTPART.fields_by_name[
        "user_supplied_info"
    ]._serialized_options = (
        b'\x9a\x84\x9e\x033bson:"user_supplied_info" json:"user_supplied_info"'
    )
    _ROBOTPART.fields_by_name["main_part"]._options = None
    _ROBOTPART.fields_by_name[
        "main_part"
    ]._serialized_options = b'\x9a\x84\x9e\x03!bson:"main_part" json:"main_part"'
    _ROBOTPART.fields_by_name["created_on"]._options = None
    _ROBOTPART.fields_by_name[
        "created_on"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x11bson:"created_on"'
    _ROBOTPART.fields_by_name["secrets"]._options = None
    _ROBOTPART.fields_by_name[
        "secrets"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x0ebson:"secrets"'
    _ROBOTPARTHISTORYENTRY.fields_by_name["part"]._options = None
    _ROBOTPARTHISTORYENTRY.fields_by_name[
        "part"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"part" json:"part"'
    _ROBOTPARTHISTORYENTRY.fields_by_name["robot"]._options = None
    _ROBOTPARTHISTORYENTRY.fields_by_name[
        "robot"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x19bson:"robot" json:"robot"'
    _ROBOTPARTHISTORYENTRY.fields_by_name["when"]._options = None
    _ROBOTPARTHISTORYENTRY.fields_by_name[
        "when"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"when" json:"when"'
    _ROBOTPARTHISTORYENTRY.fields_by_name["old"]._options = None
    _ROBOTPARTHISTORYENTRY.fields_by_name[
        "old"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x15bson:"old" json:"old"'
    _LOCATIONAUTH.fields_by_name["secret"]._options = None
    _LOCATIONAUTH.fields_by_name["secret"]._serialized_options = b"\x18\x01"
    _SHAREDSECRET.fields_by_name["id"]._options = None
    _SHAREDSECRET.fields_by_name[
        "id"
    ]._serialized_options = b'\x9a\x84\x9e\x03\tbson:"id"'
    _SHAREDSECRET.fields_by_name["secret"]._options = None
    _SHAREDSECRET.fields_by_name[
        "secret"
    ]._serialized_options = b'\x9a\x84\x9e\x03\rbson:"secret"'
    _SHAREDSECRET.fields_by_name["created_on"]._options = None
    _SHAREDSECRET.fields_by_name[
        "created_on"
    ]._serialized_options = b'\x9a\x84\x9e\x03#bson:"created_on" json:"created_on"'
    _SHAREDSECRET.fields_by_name["state"]._options = None
    _SHAREDSECRET.fields_by_name[
        "state"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x0cbson:"state"'
    _GETROBOTPARTLOGSREQUEST.fields_by_name["errors_only"]._options = None
    _GETROBOTPARTLOGSREQUEST.fields_by_name[
        "errors_only"
    ]._serialized_options = b"\x18\x01"
    _FRAGMENT.fields_by_name["id"]._options = None
    _FRAGMENT.fields_by_name[
        "id"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"'
    _FRAGMENT.fields_by_name["name"]._options = None
    _FRAGMENT.fields_by_name[
        "name"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"name" json:"name"'
    _FRAGMENT.fields_by_name["fragment"]._options = None
    _FRAGMENT.fields_by_name[
        "fragment"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"fragment" json:"fragment"'
    _FRAGMENT.fields_by_name["organization_owner"]._options = None
    _FRAGMENT.fields_by_name[
        "organization_owner"
    ]._serialized_options = b'\x9a\x84\x9e\x03&bson:"organization_owner" json:"owner"'
    _FRAGMENT.fields_by_name["public"]._options = None
    _FRAGMENT.fields_by_name[
        "public"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x1bbson:"public" json:"public"'
    _FRAGMENT.fields_by_name["created_on"]._options = None
    _FRAGMENT.fields_by_name[
        "created_on"
    ]._serialized_options = b'\x9a\x84\x9e\x03\x11bson:"created_on"'
    _REGISTRYITEMSTATUS._serialized_start = 18417
    _REGISTRYITEMSTATUS._serialized_end = 18552
    _VISIBILITY._serialized_start = 18554
    _VISIBILITY._serialized_end = 18641
    _ROBOT._serialized_start = 177
    _ROBOT._serialized_end = 541
    _ROBOTPART._serialized_start = 544
    _ROBOTPART._serialized_end = 1523
    _ROBOTPARTHISTORYENTRY._serialized_start = 1526
    _ROBOTPARTHISTORYENTRY._serialized_end = 1801
    _LISTORGANIZATIONSREQUEST._serialized_start = 1803
    _LISTORGANIZATIONSREQUEST._serialized_end = 1829
    _ORGANIZATION._serialized_start = 1832
    _ORGANIZATION._serialized_end = 2054
    _ORGANIZATIONMEMBER._serialized_start = 2057
    _ORGANIZATIONMEMBER._serialized_end = 2264
    _LISTORGANIZATIONSRESPONSE._serialized_start = 2266
    _LISTORGANIZATIONSRESPONSE._serialized_end = 2358
    _ORGANIZATIONINVITE._serialized_start = 2361
    _ORGANIZATIONINVITE._serialized_end = 2571
    _CREATEORGANIZATIONREQUEST._serialized_start = 2573
    _CREATEORGANIZATIONREQUEST._serialized_end = 2620
    _CREATEORGANIZATIONRESPONSE._serialized_start = 2622
    _CREATEORGANIZATIONRESPONSE._serialized_end = 2713
    _GETORGANIZATIONREQUEST._serialized_start = 2715
    _GETORGANIZATIONREQUEST._serialized_end = 2780
    _GETORGANIZATIONRESPONSE._serialized_start = 2782
    _GETORGANIZATIONRESPONSE._serialized_end = 2870
    _GETORGANIZATIONNAMESPACEAVAILABILITYREQUEST._serialized_start = 2872
    _GETORGANIZATIONNAMESPACEAVAILABILITYREQUEST._serialized_end = 2960
    _GETORGANIZATIONNAMESPACEAVAILABILITYRESPONSE._serialized_start = 2962
    _GETORGANIZATIONNAMESPACEAVAILABILITYRESPONSE._serialized_end = 3038
    _UPDATEORGANIZATIONREQUEST._serialized_start = 3041
    _UPDATEORGANIZATIONREQUEST._serialized_end = 3283
    _UPDATEORGANIZATIONRESPONSE._serialized_start = 3285
    _UPDATEORGANIZATIONRESPONSE._serialized_end = 3376
    _DELETEORGANIZATIONREQUEST._serialized_start = 3378
    _DELETEORGANIZATIONREQUEST._serialized_end = 3446
    _DELETEORGANIZATIONRESPONSE._serialized_start = 3448
    _DELETEORGANIZATIONRESPONSE._serialized_end = 3476
    _LISTORGANIZATIONMEMBERSREQUEST._serialized_start = 3478
    _LISTORGANIZATIONMEMBERSREQUEST._serialized_end = 3551
    _LISTORGANIZATIONMEMBERSRESPONSE._serialized_start = 3554
    _LISTORGANIZATIONMEMBERSRESPONSE._serialized_end = 3746
    _CREATEORGANIZATIONINVITEREQUEST._serialized_start = 3749
    _CREATEORGANIZATIONINVITEREQUEST._serialized_end = 3913
    _CREATEORGANIZATIONINVITERESPONSE._serialized_start = 3915
    _CREATEORGANIZATIONINVITERESPONSE._serialized_end = 4006
    _UPDATEORGANIZATIONINVITEAUTHORIZATIONSREQUEST._serialized_start = 4009
    _UPDATEORGANIZATIONINVITEAUTHORIZATIONSREQUEST._serialized_end = 4275
    _UPDATEORGANIZATIONINVITEAUTHORIZATIONSRESPONSE._serialized_start = 4277
    _UPDATEORGANIZATIONINVITEAUTHORIZATIONSRESPONSE._serialized_end = 4382
    _DELETEORGANIZATIONINVITEREQUEST._serialized_start = 4384
    _DELETEORGANIZATIONINVITEREQUEST._serialized_end = 4480
    _DELETEORGANIZATIONINVITERESPONSE._serialized_start = 4482
    _DELETEORGANIZATIONINVITERESPONSE._serialized_end = 4516
    _RESENDORGANIZATIONINVITEREQUEST._serialized_start = 4518
    _RESENDORGANIZATIONINVITEREQUEST._serialized_end = 4614
    _RESENDORGANIZATIONINVITERESPONSE._serialized_start = 4616
    _RESENDORGANIZATIONINVITERESPONSE._serialized_end = 4707
    _DELETEORGANIZATIONMEMBERREQUEST._serialized_start = 4709
    _DELETEORGANIZATIONMEMBERREQUEST._serialized_end = 4808
    _DELETEORGANIZATIONMEMBERRESPONSE._serialized_start = 4810
    _DELETEORGANIZATIONMEMBERRESPONSE._serialized_end = 4844
    _ORGANIZATIONIDENTITY._serialized_start = 4846
    _ORGANIZATIONIDENTITY._serialized_end = 4904
    _LOCATIONORGANIZATION._serialized_start = 4906
    _LOCATIONORGANIZATION._serialized_end = 4995
    _LOCATIONAUTH._serialized_start = 4998
    _LOCATIONAUTH._serialized_end = 5126
    _STORAGECONFIG._serialized_start = 5128
    _STORAGECONFIG._serialized_end = 5167
    _LOCATION._serialized_start = 5170
    _LOCATION._serialized_end = 5526
    _SHAREDSECRET._serialized_start = 5529
    _SHAREDSECRET._serialized_end = 5865
    _SHAREDSECRET_STATE._serialized_start = 5796
    _SHAREDSECRET_STATE._serialized_end = 5865
    _CREATELOCATIONREQUEST._serialized_start = 5868
    _CREATELOCATIONREQUEST._serialized_end = 6026
    _CREATELOCATIONRESPONSE._serialized_start = 6028
    _CREATELOCATIONRESPONSE._serialized_end = 6103
    _GETLOCATIONREQUEST._serialized_start = 6105
    _GETLOCATIONREQUEST._serialized_end = 6158
    _GETLOCATIONRESPONSE._serialized_start = 6160
    _GETLOCATIONRESPONSE._serialized_end = 6232
    _UPDATELOCATIONREQUEST._serialized_start = 6235
    _UPDATELOCATIONREQUEST._serialized_end = 6439
    _UPDATELOCATIONRESPONSE._serialized_start = 6441
    _UPDATELOCATIONRESPONSE._serialized_end = 6516
    _DELETELOCATIONREQUEST._serialized_start = 6518
    _DELETELOCATIONREQUEST._serialized_end = 6574
    _DELETELOCATIONRESPONSE._serialized_start = 6576
    _DELETELOCATIONRESPONSE._serialized_end = 6600
    _GETORGANIZATIONSWITHACCESSTOLOCATIONREQUEST._serialized_start = 6602
    _GETORGANIZATIONSWITHACCESSTOLOCATIONREQUEST._serialized_end = 6680
    _GETORGANIZATIONSWITHACCESSTOLOCATIONRESPONSE._serialized_start = 6683
    _GETORGANIZATIONSWITHACCESSTOLOCATIONRESPONSE._serialized_end = 6821
    _LISTLOCATIONSREQUEST._serialized_start = 6823
    _LISTLOCATIONSREQUEST._serialized_end = 6886
    _SHARELOCATIONREQUEST._serialized_start = 6888
    _SHARELOCATIONREQUEST._serialized_end = 6984
    _SHARELOCATIONRESPONSE._serialized_start = 6986
    _SHARELOCATIONRESPONSE._serialized_end = 7009
    _UNSHARELOCATIONREQUEST._serialized_start = 7011
    _UNSHARELOCATIONREQUEST._serialized_end = 7109
    _UNSHARELOCATIONRESPONSE._serialized_start = 7111
    _UNSHARELOCATIONRESPONSE._serialized_end = 7136
    _LISTLOCATIONSRESPONSE._serialized_start = 7138
    _LISTLOCATIONSRESPONSE._serialized_end = 7214
    _CREATELOCATIONSECRETREQUEST._serialized_start = 7216
    _CREATELOCATIONSECRETREQUEST._serialized_end = 7278
    _CREATELOCATIONSECRETRESPONSE._serialized_start = 7280
    _CREATELOCATIONSECRETRESPONSE._serialized_end = 7357
    _DELETELOCATIONSECRETREQUEST._serialized_start = 7359
    _DELETELOCATIONSECRETREQUEST._serialized_end = 7450
    _DELETELOCATIONSECRETRESPONSE._serialized_start = 7452
    _DELETELOCATIONSECRETRESPONSE._serialized_end = 7482
    _LOCATIONAUTHREQUEST._serialized_start = 7484
    _LOCATIONAUTHREQUEST._serialized_end = 7538
    _LOCATIONAUTHRESPONSE._serialized_start = 7540
    _LOCATIONAUTHRESPONSE._serialized_end = 7609
    _GETROBOTREQUEST._serialized_start = 7611
    _GETROBOTREQUEST._serialized_end = 7644
    _GETROVERRENTALROBOTSREQUEST._serialized_start = 7646
    _GETROVERRENTALROBOTSREQUEST._serialized_end = 7698
    _ROVERRENTALROBOT._serialized_start = 7701
    _ROVERRENTALROBOT._serialized_end = 7855
    _GETROVERRENTALROBOTSRESPONSE._serialized_start = 7857
    _GETROVERRENTALROBOTSRESPONSE._serialized_end = 7942
    _GETROBOTRESPONSE._serialized_start = 7944
    _GETROBOTRESPONSE._serialized_end = 8004
    _GETROBOTPARTSREQUEST._serialized_start = 8006
    _GETROBOTPARTSREQUEST._serialized_end = 8055
    _GETROBOTPARTSRESPONSE._serialized_start = 8057
    _GETROBOTPARTSRESPONSE._serialized_end = 8126
    _GETROBOTPARTREQUEST._serialized_start = 8128
    _GETROBOTPARTREQUEST._serialized_end = 8165
    _GETROBOTPARTRESPONSE._serialized_start = 8167
    _GETROBOTPARTRESPONSE._serialized_end = 8266
    _GETROBOTPARTLOGSREQUEST._serialized_start = 8269
    _GETROBOTPARTLOGSREQUEST._serialized_end = 8462
    _GETROBOTPARTLOGSRESPONSE._serialized_start = 8464
    _GETROBOTPARTLOGSRESPONSE._serialized_end = 8576
    _TAILROBOTPARTLOGSREQUEST._serialized_start = 8578
    _TAILROBOTPARTLOGSREQUEST._serialized_end = 8693
    _TAILROBOTPARTLOGSRESPONSE._serialized_start = 8695
    _TAILROBOTPARTLOGSRESPONSE._serialized_end = 8768
    _GETROBOTPARTHISTORYREQUEST._serialized_start = 8770
    _GETROBOTPARTHISTORYREQUEST._serialized_end = 8814
    _GETROBOTPARTHISTORYRESPONSE._serialized_start = 8816
    _GETROBOTPARTHISTORYRESPONSE._serialized_end = 8907
    _UPDATEROBOTPARTREQUEST._serialized_start = 8909
    _UPDATEROBOTPARTREQUEST._serialized_end = 9029
    _UPDATEROBOTPARTRESPONSE._serialized_start = 9031
    _UPDATEROBOTPARTRESPONSE._serialized_end = 9100
    _NEWROBOTPARTREQUEST._serialized_start = 9102
    _NEWROBOTPARTREQUEST._serialized_end = 9179
    _NEWROBOTPARTRESPONSE._serialized_start = 9181
    _NEWROBOTPARTRESPONSE._serialized_end = 9228
    _DELETEROBOTPARTREQUEST._serialized_start = 9230
    _DELETEROBOTPARTREQUEST._serialized_end = 9279
    _GETROBOTAPIKEYSREQUEST._serialized_start = 9281
    _GETROBOTAPIKEYSREQUEST._serialized_end = 9332
    _APIKEY._serialized_start = 9334
    _APIKEY._serialized_end = 9455
    _GETROBOTAPIKEYSRESPONSE._serialized_start = 9457
    _GETROBOTAPIKEYSRESPONSE._serialized_end = 9548
    _DELETEROBOTPARTRESPONSE._serialized_start = 9550
    _DELETEROBOTPARTRESPONSE._serialized_end = 9575
    _FRAGMENT._serialized_start = 9578
    _FRAGMENT._serialized_end = 10194
    _LISTFRAGMENTSREQUEST._serialized_start = 10196
    _LISTFRAGMENTSREQUEST._serialized_end = 10292
    _LISTFRAGMENTSRESPONSE._serialized_start = 10294
    _LISTFRAGMENTSRESPONSE._serialized_end = 10370
    _GETFRAGMENTREQUEST._serialized_start = 10372
    _GETFRAGMENTREQUEST._serialized_end = 10408
    _GETFRAGMENTRESPONSE._serialized_start = 10410
    _GETFRAGMENTRESPONSE._serialized_end = 10482
    _CREATEFRAGMENTREQUEST._serialized_start = 10485
    _CREATEFRAGMENTREQUEST._serialized_end = 10618
    _CREATEFRAGMENTRESPONSE._serialized_start = 10620
    _CREATEFRAGMENTRESPONSE._serialized_end = 10695
    _UPDATEFRAGMENTREQUEST._serialized_start = 10698
    _UPDATEFRAGMENTREQUEST._serialized_end = 10846
    _UPDATEFRAGMENTRESPONSE._serialized_start = 10848
    _UPDATEFRAGMENTRESPONSE._serialized_end = 10923
    _DELETEFRAGMENTREQUEST._serialized_start = 10925
    _DELETEFRAGMENTREQUEST._serialized_end = 10964
    _DELETEFRAGMENTRESPONSE._serialized_start = 10966
    _DELETEFRAGMENTRESPONSE._serialized_end = 10990
    _LISTROBOTSREQUEST._serialized_start = 10992
    _LISTROBOTSREQUEST._serialized_end = 11044
    _LISTROBOTSRESPONSE._serialized_start = 11046
    _LISTROBOTSRESPONSE._serialized_end = 11110
    _NEWROBOTREQUEST._serialized_start = 11112
    _NEWROBOTREQUEST._serialized_end = 11177
    _NEWROBOTRESPONSE._serialized_start = 11179
    _NEWROBOTRESPONSE._serialized_end = 11213
    _UPDATEROBOTREQUEST._serialized_start = 11215
    _UPDATEROBOTREQUEST._serialized_end = 11299
    _UPDATEROBOTRESPONSE._serialized_start = 11301
    _UPDATEROBOTRESPONSE._serialized_end = 11364
    _DELETEROBOTREQUEST._serialized_start = 11366
    _DELETEROBOTREQUEST._serialized_end = 11402
    _DELETEROBOTRESPONSE._serialized_start = 11404
    _DELETEROBOTRESPONSE._serialized_end = 11425
    _MARKPARTASMAINREQUEST._serialized_start = 11427
    _MARKPARTASMAINREQUEST._serialized_end = 11475
    _MARKPARTASMAINRESPONSE._serialized_start = 11477
    _MARKPARTASMAINRESPONSE._serialized_end = 11501
    _MARKPARTFORRESTARTREQUEST._serialized_start = 11503
    _MARKPARTFORRESTARTREQUEST._serialized_end = 11555
    _MARKPARTFORRESTARTRESPONSE._serialized_start = 11557
    _MARKPARTFORRESTARTRESPONSE._serialized_end = 11585
    _CREATEROBOTPARTSECRETREQUEST._serialized_start = 11587
    _CREATEROBOTPARTSECRETREQUEST._serialized_end = 11642
    _CREATEROBOTPARTSECRETRESPONSE._serialized_start = 11644
    _CREATEROBOTPARTSECRETRESPONSE._serialized_end = 11719
    _DELETEROBOTPARTSECRETREQUEST._serialized_start = 11721
    _DELETEROBOTPARTSECRETREQUEST._serialized_end = 11805
    _DELETEROBOTPARTSECRETRESPONSE._serialized_start = 11807
    _DELETEROBOTPARTSECRETRESPONSE._serialized_end = 11838
    _AUTHORIZATION._serialized_start = 11841
    _AUTHORIZATION._serialized_end = 12127
    _ADDROLEREQUEST._serialized_start = 12129
    _ADDROLEREQUEST._serialized_end = 12211
    _ADDROLERESPONSE._serialized_start = 12213
    _ADDROLERESPONSE._serialized_end = 12230
    _REMOVEROLEREQUEST._serialized_start = 12232
    _REMOVEROLEREQUEST._serialized_end = 12317
    _REMOVEROLERESPONSE._serialized_start = 12319
    _REMOVEROLERESPONSE._serialized_end = 12339
    _CHANGEROLEREQUEST._serialized_start = 12342
    _CHANGEROLEREQUEST._serialized_end = 12507
    _CHANGEROLERESPONSE._serialized_start = 12509
    _CHANGEROLERESPONSE._serialized_end = 12529
    _LISTAUTHORIZATIONSREQUEST._serialized_start = 12531
    _LISTAUTHORIZATIONSREQUEST._serialized_end = 12634
    _LISTAUTHORIZATIONSRESPONSE._serialized_start = 12636
    _LISTAUTHORIZATIONSRESPONSE._serialized_end = 12732
    _CHECKPERMISSIONSREQUEST._serialized_start = 12734
    _CHECKPERMISSIONSREQUEST._serialized_end = 12829
    _AUTHORIZEDPERMISSIONS._serialized_start = 12831
    _AUTHORIZEDPERMISSIONS._serialized_end = 12958
    _CHECKPERMISSIONSRESPONSE._serialized_start = 12960
    _CHECKPERMISSIONSRESPONSE._serialized_end = 13077
    _MODULEVERSION._serialized_start = 13080
    _MODULEVERSION._serialized_end = 13241
    _MODULEMETADATA._serialized_start = 13244
    _MODULEMETADATA._serialized_end = 13392
    _MLMODELMETADATA._serialized_start = 13394
    _MLMODELMETADATA._serialized_end = 13439
    _REGISTRYITEM._serialized_start = 13442
    _REGISTRYITEM._serialized_end = 14265
    _GETREGISTRYITEMREQUEST._serialized_start = 14267
    _GETREGISTRYITEMREQUEST._serialized_end = 14316
    _GETREGISTRYITEMRESPONSE._serialized_start = 14318
    _GETREGISTRYITEMRESPONSE._serialized_end = 14390
    _CREATEREGISTRYITEMREQUEST._serialized_start = 14393
    _CREATEREGISTRYITEMREQUEST._serialized_end = 14536
    _CREATEREGISTRYITEMRESPONSE._serialized_start = 14538
    _CREATEREGISTRYITEMRESPONSE._serialized_end = 14566
    _UPDATEREGISTRYITEMREQUEST._serialized_start = 14569
    _UPDATEREGISTRYITEMREQUEST._serialized_end = 14767
    _UPDATEREGISTRYITEMRESPONSE._serialized_start = 14769
    _UPDATEREGISTRYITEMRESPONSE._serialized_end = 14797
    _LISTREGISTRYITEMSREQUEST._serialized_start = 14800
    _LISTREGISTRYITEMSREQUEST._serialized_end = 15206
    _LISTREGISTRYITEMSRESPONSE._serialized_start = 15208
    _LISTREGISTRYITEMSRESPONSE._serialized_end = 15284
    _DELETEREGISTRYITEMREQUEST._serialized_start = 15286
    _DELETEREGISTRYITEMREQUEST._serialized_end = 15338
    _DELETEREGISTRYITEMRESPONSE._serialized_start = 15340
    _DELETEREGISTRYITEMRESPONSE._serialized_end = 15368
    _CREATEMODULEREQUEST._serialized_start = 15370
    _CREATEMODULEREQUEST._serialized_end = 15452
    _CREATEMODULERESPONSE._serialized_start = 15454
    _CREATEMODULERESPONSE._serialized_end = 15523
    _UPDATEMODULEREQUEST._serialized_start = 15526
    _UPDATEMODULEREQUEST._serialized_end = 15761
    _UPDATEMODULERESPONSE._serialized_start = 15763
    _UPDATEMODULERESPONSE._serialized_end = 15803
    _MODEL._serialized_start = 15805
    _MODEL._serialized_end = 15852
    _MODULEFILEINFO._serialized_start = 15854
    _MODULEFILEINFO._serialized_end = 15953
    _UPLOADMODULEFILEREQUEST._serialized_start = 15956
    _UPLOADMODULEFILEREQUEST._serialized_end = 16091
    _UPLOADMODULEFILERESPONSE._serialized_start = 16093
    _UPLOADMODULEFILERESPONSE._serialized_end = 16137
    _GETMODULEREQUEST._serialized_start = 16139
    _GETMODULEREQUEST._serialized_end = 16186
    _GETMODULERESPONSE._serialized_start = 16188
    _GETMODULERESPONSE._serialized_end = 16252
    _MODULE._serialized_start = 16255
    _MODULE._serialized_end = 16740
    _VERSIONHISTORY._serialized_start = 16743
    _VERSIONHISTORY._serialized_end = 16905
    _UPLOADS._serialized_start = 16907
    _UPLOADS._serialized_end = 17005
    _LISTMODULESREQUEST._serialized_start = 17007
    _LISTMODULESREQUEST._serialized_end = 17093
    _LISTMODULESRESPONSE._serialized_start = 17095
    _LISTMODULESRESPONSE._serialized_end = 17163
    _GETUSERIDBYEMAILREQUEST._serialized_start = 17165
    _GETUSERIDBYEMAILREQUEST._serialized_end = 17212
    _GETUSERIDBYEMAILRESPONSE._serialized_start = 17214
    _GETUSERIDBYEMAILRESPONSE._serialized_end = 17265
    _LISTORGANIZATIONSBYUSERREQUEST._serialized_start = 17267
    _LISTORGANIZATIONSBYUSERREQUEST._serialized_end = 17324
    _ORGDETAILS._serialized_start = 17326
    _ORGDETAILS._serialized_end = 17388
    _LISTORGANIZATIONSBYUSERRESPONSE._serialized_start = 17390
    _LISTORGANIZATIONSBYUSERRESPONSE._serialized_end = 17468
    _CREATEKEYREQUEST._serialized_start = 17470
    _CREATEKEYREQUEST._serialized_end = 17576
    _CREATEKEYRESPONSE._serialized_start = 17578
    _CREATEKEYRESPONSE._serialized_end = 17631
    _DELETEKEYREQUEST._serialized_start = 17633
    _DELETEKEYREQUEST._serialized_end = 17667
    _DELETEKEYRESPONSE._serialized_start = 17669
    _DELETEKEYRESPONSE._serialized_end = 17688
    _AUTHORIZATIONDETAILS._serialized_start = 17691
    _AUTHORIZATIONDETAILS._serialized_end = 17896
    _APIKEYWITHAUTHORIZATIONS._serialized_start = 17899
    _APIKEYWITHAUTHORIZATIONS._serialized_end = 18046
    _LISTKEYSREQUEST._serialized_start = 18048
    _LISTKEYSREQUEST._serialized_end = 18088
    _LISTKEYSRESPONSE._serialized_start = 18090
    _LISTKEYSRESPONSE._serialized_end = 18174
    _ROTATEKEYREQUEST._serialized_start = 18176
    _ROTATEKEYREQUEST._serialized_end = 18210
    _ROTATEKEYRESPONSE._serialized_start = 18212
    _ROTATEKEYRESPONSE._serialized_end = 18265
    _CREATEKEYFROMEXISTINGKEYAUTHORIZATIONSREQUEST._serialized_start = 18267
    _CREATEKEYFROMEXISTINGKEYAUTHORIZATIONSREQUEST._serialized_end = 18330
    _CREATEKEYFROMEXISTINGKEYAUTHORIZATIONSRESPONSE._serialized_start = 18332
    _CREATEKEYFROMEXISTINGKEYAUTHORIZATIONSRESPONSE._serialized_end = 18414
    _APPSERVICE._serialized_start = 18644
    _APPSERVICE._serialized_end = 25411
