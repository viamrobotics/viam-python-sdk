import asyncio

from viam.app.viam_client import ViamClient
from viam.rpc.dial import Credentials, DialOptions

MY_ORG_ID = "79211bf0-597e-42fa-9f51-0291f2fdbb16"
MY_LOCATION_ID = "c9qlaevgys"
MY_ROBOT_ID = "495bfd7a-e070-4b07-9fe1-2863bdad9c82"
MY_ROBOT_PART_ID = "bf0db9cb-abac-49c0-9a52-c8aa6ddd6d18"

NAVEED_USER_ID = "4ab2f69b-77d3-4d80-af95-15a0a90410d4"
JULIE_USER_ID = "a14096d2-114c-43d4-9b1a-cd17b294da0f"
BASHAR_USER_ID = "871de11d-81f1-490f-b237-90df0ea68e32"
ETHAN_USER_ID = "26bd69d2-b29f-430b-9a8c-c4358b5d81b6"

MODULE_ID = "bashar-org:new-test-module"
MODULE_URL = "https://app.viam.com/module/bashar-org/new-test-module"


async def main():
    dial_opts = DialOptions(
        auth_entity="rover-main.c9qlaevgys.viam.cloud",
        credentials=Credentials(type="robot-location-secret", payload="4gjbqdsv39how2mm8fdzorynpkvc7ot7tkyki6w433o5ojjw"),
        allow_insecure_downgrade=True,
    )
    viam_client = await ViamClient.create_from_dial_options(dial_opts)
    client = viam_client.app_client

    logs_stream = await client.tail_robot_part_logs(robot_part_id=MY_ROBOT_PART_ID, errors_only=False, filter="")

    async for logs in logs_stream:
        for log in logs:
            print(f"{log.message}\n")

    viam_client.close()


if __name__ == "__main__":
    asyncio.run(main())
