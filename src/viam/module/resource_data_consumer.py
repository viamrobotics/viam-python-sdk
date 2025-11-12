import datetime
import os
from typing import Any, Dict, List, Optional

from viam.app.viam_client import ViamClient


class ResourceDataConsumer:
    """Client for retrieving historical module data from app.

    Inherit from this class in a module to get access to historical module data.
    """

    @classmethod
    def construct_query(cls, part_id: str, resource_name: str, time_back: datetime.timedelta) -> List[Dict[str, Any]]:
        return [
            {
                "$match": {
                    "part_id": part_id,
                    "component_name": resource_name,
                    "time_received": {"$gte": datetime.datetime.now() - time_back},
                }
            }
        ]

    @classmethod
    async def query_tabular_data(
        cls, resource_name: str, time_back: datetime.timedelta, additional_stages: Optional[List[Dict[str, Any]]] = None, **kwargs
    ) -> List[Dict[str, Any]]:
        """Return historical data for this module, queried with MQL."""
        viam_client = await ViamClient.create_from_env_vars()

        org_id = os.environ["VIAM_PRIMARY_ORG_ID"]
        part_id = os.environ["VIAM_MACHINE_PART_ID"]

        query = cls.construct_query(part_id=part_id, resource_name=resource_name, time_back=time_back)

        if additional_stages is not None:
            query += additional_stages

        return await viam_client.data_client.tabular_data_by_mql(org_id, query)
