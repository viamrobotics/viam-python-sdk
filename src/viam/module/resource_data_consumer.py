import datetime
import os
from typing import Any, Dict, List

from viam.app.viam_client import ViamClient


class ResourceDataConsumer:
    """Client for retrieving historical module data from app.

    Inherit from this class in a module to get access to historical module data.
    """

    @classmethod
    async def query_tabular_data(cls, resource_name: str, time_back: datetime.timedelta, **kwargs) -> List[Dict[str, Any]]:
        """Return historical data for this module, queried with MQL."""
        viam_client = await ViamClient.create_from_env_vars()

        org_id = os.environ["VIAM_PRIMARY_ORG_ID"]
        part_id = os.environ["VIAM_MACHINE_PART_ID"]

        query = [
            {
                "$match": {
                    "part_id": part_id,
                    "component_name": resource_name,
                    "time_received": {"$gte": datetime.datetime.now() - time_back},
                }
            }
        ]

        return await viam_client.data_client.tabular_data_by_mql(org_id, query)
