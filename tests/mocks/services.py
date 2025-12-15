# In MockApp.__init__, add a new attribute to store the tracing config
self.robot_config_tracing: Optional[Dict[str, Any]] = None

# In MockApp.UpdateRobotPart, after `self.last_known_update = request.last_known_update`:
# Extract the tracing config from the request.robot_config
robot_config_dict = struct_to_dict(request.robot_config)
if "tracing" in robot_config_dict:
    self.robot_config_tracing = robot_config_dict["tracing"]

# When constructing the RobotPart response, ensure the robot_config includes the tracing field.
# The existing self.robot_part already has a robot_config field. We need to update it.
# Create a mutable version of the robot_config from self.robot_part
updated_robot_config_proto = self.robot_part.robot_config
if self.robot_config_tracing:
    from viam.proto.app.robot import TracingConfig
    tracing_config_proto = TracingConfig(
        enabled=self.robot_config_tracing.get("enabled", False),
        disk=self.robot_config_tracing.get("disk", False),
        stdout=self.robot_config_tracing.get("stdout", False),
        otlp_endpoint=self.robot_config_tracing.get("otlp_endpoint", "")
    )
    updated_robot_config_proto.tracing.CopyFrom(tracing_config_proto)

# Ensure the response uses this updated config
response_robot_part = RobotPart(
    id=self.robot_part.id,
    name=self.robot_part.name,
    dns_name=self.robot_part.dns_name,
    secret=self.robot_part.secret,
    robot=self.robot_part.robot,
    location_id=self.robot_part.location_id,
    robot_config=updated_robot_config_proto, # Use the updated config
    last_access=self.robot_part.last_access,
    user_supplied_info=self.robot_part.user_supplied_info,
    main_part=self.robot_part.main_part,
    fqdn=self.robot_part.fqdn,
    local_fqdn=self.robot_part.local_fqdn,
    created_on=self.robot_part.created_on,
    secrets=self.robot_part.secrets,
    last_updated=self.robot_part.last_updated,
)
await stream.send_message(UpdateRobotPartResponse(part=response_robot_part))
```
```python
# In MockApp.__init__, add a new attribute to store the tracing config
self.robot_config_tracing: Optional[Dict[str, Any]] = None

# In MockApp.UpdateRobotPart, after `self.last_known_update = request.last_known_update`:
# Extract the tracing config from the request.robot_config
robot_config_dict = struct_to_dict(request.robot_config)
if "tracing" in robot_config_dict:
    self.robot_config_tracing = robot_config_dict["tracing"]

# When constructing the RobotPart response, ensure the robot_config includes the tracing field.
# The existing self.robot_part already has a robot_config field. We need to update it.
# Create a mutable version of the robot_config from self.robot_part
updated_robot_config_proto = self.robot_part.robot_config
if self.robot_config_tracing:
    from viam.proto.app.robot import TracingConfig
    tracing_config_proto = TracingConfig(
        enabled=self.robot_config_tracing.get("enabled", False),
        disk=self.robot_config_tracing.get("disk", False),
        stdout=self.robot_config_tracing.get("stdout", False),
        otlp_endpoint=self.robot_config_tracing.get("otlp_endpoint", "")
    )
    updated_robot_config_proto.tracing.CopyFrom(tracing_config_proto)

# Ensure the response uses this updated config
response_robot_part = RobotPart(
    id=self.robot_part.id,
    name=self.robot_part.name,
    dns_name=self.robot_part.dns_name,
    secret=self.robot_part.secret,
    robot=self.robot_part.robot,
    location_id=self.robot_part.location_id,
    robot_config=updated_robot_config_proto, # Use the updated config
    last_access=self.robot_part.last_access,
    user_supplied_info=self.robot_part.user_supplied_info,
    main_part=self.robot_part.main_part,
    fqdn=self.robot_part.fqdn,
    local_fqdn=self.robot_part.local_fqdn,
    created_on=self.robot_part.created_on,
    secrets=self.robot_part.secrets,
    last_updated=self.robot_part.last_updated,
)
await stream.send_message(UpdateRobotPartResponse(part=response_robot_part))
