import asyncio
from datetime import datetime, timedelta

from viam.app.viam_client import ViamClient
from viam.rpc.dial import DialOptions
from viam.utils import create_filter

async def test_rename_data_pipeline():
    """Test the rename_data_pipeline function with real data client."""
    print("\nTesting rename_data_pipeline function...")

    # Get credentials from environment variables
    api_key_id = "ebb16bb2-d90b-4d54-8c19-f413eecf0a9f"
    api_key = "dhjh680i33uagwpown4fy4g46pifk4jz"

    try:
        # Create ViamClient using API key
        dial_options = DialOptions.with_api_key(api_key, api_key_id)
        viam_client = await ViamClient.create_from_dial_options(dial_options, app_url="https://pr-9261-appmain-bplesliplq-uc.a.run.app/")

        # Get data client from ViamClient
        data_client = viam_client.data_client

        # get all data pipelines
        data_pipelines = await data_client.list_data_pipelines(organization_id="880d1411-1608-4ac8-bbd3-b4ca8a74372d")
        print(f"Data pipelines: {data_pipelines}")

        # Set up test parameters
        pipeline_id = "93a9318d-2944-4175-9668-43418857ce04"
        new_name = "rename-test-pipeline"

        print("Renaming data pipeline:")
        print(f"  Pipeline ID: {pipeline_id}")
        print(f"  New name: {new_name}")

        # Call rename_data_pipeline
        try:
            await data_client.rename_data_pipeline(id=pipeline_id, name=new_name)
            print("Successfully renamed data pipeline")
        except Exception as e:
            print(f"Error calling rename_data_pipeline: {e}")

        # test empty name
        try:
            await data_client.rename_data_pipeline(id=pipeline_id, name="")
            print("Successfully renamed data pipeline")
        except Exception as e:
            print(f"Error calling rename_data_pipeline: {e}")

        # test name that already exists
        try:
            await data_client.rename_data_pipeline(id=pipeline_id, name=new_name)
            print("Successfully renamed data pipeline")
        except Exception as e:
            print(f"Error calling rename_data_pipeline: {e}")

        finally:
            viam_client.close()


    except Exception as e:
        print(f"Error setting up data client: {e}")


async def main():
    """Run all data client tests."""
    print("Starting Data Client Integration Tests")
    print("=" * 50)

    # Run all tests
    # await test_export_tabular_data()
    # await test_get_latest_tabular_data()
    # await test_tabular_data_by_filter()
    await test_rename_data_pipeline()
    print("\n" + "=" * 50)
    print("Data Client Integration Tests completed")


if __name__ == "__main__":
    asyncio.run(main())
