from viam.proto.app.data import Filter as ProtoFilter, CaptureInterval
from typing import List, Optional

class Filter:
    def __init__(
            self,
            component_name: Optional[str] = None,
            component_type: Optional[str] = None,
            component_model: Optional[str] = None,
            method: Optional[str] = None,
            robot_name: Optional[str] = None,
            robot_id: Optional[str] = None,
            part_name: Optional[str] = None,
            part_id: Optional[str] = None,
            location_ids: Optional[List[str]] = None,
            org_ids: Optional[List[str]] = None,
            capture_interval_start: Optional[int] = None,
            capture_interval_end: Optional[int] = None,
            bounding_box_labels: Optional[List[str]] = None,
            tags: Optional[List[str]] = None,
            ):
        self.component_name = component_name
        self.component_type = component_type
        self.component_model = component_model
        self.method = method
        self.robot_name = robot_name
        self.robot_id = robot_id
        self.part_name = part_name
        self.part_id = part_id
        self.location_ids = location_ids
        self.org_ids = org_ids
        self.capture_interval_start = capture_interval_start
        self.capture_interval_end = capture_interval_end
        self.bounding_box_labels = bounding_box_labels
        self.tags = tags

    def _to_proto_filter(self) -> ProtoFilter:
        filter = ProtoFilter()
        filter.component_name = self.component_name
        filter.component_type = self.component_type
        filter.component_model = self.component_model
        filter.method = self.method
        filter.robot_name = self.robot_name
        filter.robot_id = self.robot_id
        filter.part_name = self.part_name
        filter.part_id = self.part_id
        filter.location_ids = self.location_ids
        filter.org_ids = self.org_ids
        ## CR erodkin: this won't work, our version is just ints, we need more. probably just do a timestamp thing and convert under the hood?
        filter.interval = CaptureInterval(start=self.capture_interval_start, end=self.capture_interval_end)
        filter.bbox_labels = self.bounding_box_labels
        filter.tags_filter = self.tags
        return filter

