import asyncio
from datetime import datetime, timedelta

from viam.app.viam_client import ViamClient
from viam.rpc.dial import DialOptions
from viam.utils import create_filter


async def test_export_tabular_data():
    """Test the export_tabular_data function with real data client."""
    print("Testing export_tabular_data function...")

    # Get credentials from environment variables
    api_key_id = "ebb16bb2-d90b-4d54-8c19-f413eecf0a9f"
    api_key = "dhjh680i33uagwpown4fy4g46pifk4jz"

    try:
        # Create ViamClient using API key
        dial_options = DialOptions.with_api_key(api_key, api_key_id)
        viam_client = await ViamClient.create_from_dial_options(dial_options, app_url="https://app.viam.dev")

        # Get data client from ViamClient
        data_client = viam_client.data_client

        # Set up test parameters
        part_id = "3380647d-127a-4fb8-aa7e-253ef7dbccc7"  # You may need to get a real part ID
        component_name = "sensor-1"
        component_type = "sensor"  # Use a common component type
        method = "DoCommand"
        start_time = datetime.now() - timedelta(days=1)
        end_time = datetime.now()

        print("Exporting tabular data for:")
        print(f"  Part ID: {part_id}")
        print(f"  Component: {component_name} ({component_type})")
        print(f"  Method: {method}")
        print(f"  Time range: {start_time} to {end_time}")

        # Call export_tabular_data
        try:
            tabular_data = await data_client.export_tabular_data(
                part_id=part_id,
                resource_name=component_name,
                resource_api=component_type,
                method_name=method,
                start_time=start_time,
                end_time=end_time,
                additional_params={"test_param": "test_value"}
            )

            print(f"Successfully exported {len(tabular_data)} tabular data records")

            # Print details of the first record if available
            if tabular_data:
                first_record = tabular_data[0]
                print("First record details:")
                print(f"  Part ID: {first_record.part_id}")
                print(f"  Resource name: {first_record.resource_name}")
                print(f"  Resource API: {first_record.resource_api}")
                print(f"  Time captured: {first_record.time_captured}")
                print(f"  Organization ID: {first_record.organization_id}")
                print(f"  Location ID: {first_record.location_id}")
                print(f"  Robot name: {first_record.robot_name}")
                print(f"  Robot ID: {first_record.robot_id}")
                print(f"  Part name: {first_record.part_name}")
                print(f"  Tags: {first_record.tags}")
                print(f"  Payload: {first_record.payload}")
                print(f"  Method parameters: {first_record.method_parameters}")
            else:
                print("No tabular data found for the specified parameters")

        except Exception as e:
            print(f"Error calling export_tabular_data: {e}")

        finally:
            viam_client.close()

    except Exception as e:
        print(f"Error setting up data client: {e}")


async def test_get_latest_tabular_data():
    """Test the get_latest_tabular_data function with real data client."""
    print("\nTesting get_latest_tabular_data function...")

    # Get credentials from environment variables
    api_key_id = "ebb16bb2-d90b-4d54-8c19-f413eecf0a9f"
    api_key = "dhjh680i33uagwpown4fy4g46pifk4jz"

    try:
        # Create ViamClient using API key
        dial_options = DialOptions.with_api_key(api_key, api_key_id)
        viam_client = await ViamClient.create_from_dial_options(dial_options, app_url="https://app.viam.dev")

        # Get data client from ViamClient
        data_client = viam_client.data_client

        # Set up test parameters
        part_id = "3380647d-127a-4fb8-aa7e-253ef7dbccc7"  # You may need to get a real part ID
        component_name = "sensor-1"
        component_type = "rdk:component:sensor"  # Use a common component type
        method = "DoCommand"
        additional_params = {"docommand_input": {"foo": "bar"}}

        print("Getting latest tabular data for:")
        print(f"  Part ID: {part_id}")
        print(f"  Component: {component_name} ({component_type})")
        print(f"  Method: {method}")

        # Call get_latest_tabular_data
        try:
            result = await data_client.get_latest_tabular_data(
                part_id=part_id,
                resource_name=component_name,
                resource_api=component_type,
                method_name=method,
                additional_params=additional_params,
            )

            if result:
                time_captured, time_synced, payload = result
                print("Successfully retrieved latest tabular data:")
                print(f"  Time captured: {time_captured}")
                print(f"  Time synced: {time_synced}")
                print(f"  Payload: {payload}")
            else:
                print("No latest tabular data found for the specified parameters")

        except Exception as e:
            print(f"Error calling get_latest_tabular_data: {e}")

        finally:
            viam_client.close()

    except Exception as e:
        print(f"Error setting up data client: {e}")


async def test_tabular_data_by_filter():
    """Test the tabular_data_by_filter function with real data client."""
    print("\nTesting tabular_data_by_filter function...")

    # Get credentials from environment variables
    api_key_id = "ebb16bb2-d90b-4d54-8c19-f413eecf0a9f"
    api_key = "dhjh680i33uagwpown4fy4g46pifk4jz"

    if not api_key_id or not api_key:
        print("Warning: VIAM_API_KEY_ID and VIAM_API_KEY environment variables not set. Skipping test.")
        return

    try:
        # Create ViamClient using API key
        dial_options = DialOptions.with_api_key(api_key_id, api_key)
        viam_client = await ViamClient.create_from_dial_options(dial_options, app_url="https://app.viam.dev")

        # Get data client from ViamClient
        data_client = viam_client.data_client

        # Create a filter for testing
        filter_obj = create_filter(
            component_type="sensor",
            method="DoCommand",
            start_time=datetime.now() - timedelta(days=7),
            end_time=datetime.now(),
            tags=["test"]
        )

        print("Querying tabular data with filter:")
        print(f"  Component type: {filter_obj.component_type}")
        print(f"  Method: {filter_obj.method}")
        print(f"  Time range: {filter_obj.interval.start.ToDatetime()} to {filter_obj.interval.end.ToDatetime()}")
        print(f"  Tags: {filter_obj.tags_filter.tags}")

        # Call tabular_data_by_filter
        try:
            tabular_data, count, last = await data_client.tabular_data_by_filter(
                filter=filter_obj,
                limit=10,
                count_only=False
            )

            print(f"Successfully retrieved {len(tabular_data)} tabular data records (total count: {count})")

            # Print details of the first record if available
            if tabular_data:
                first_record = tabular_data[0]
                print("First record details:")
                print(f"  Time captured: {first_record.time_requested}")
                print(f"  Time received: {first_record.time_received}")
                print(f"  Data: {first_record.data}")
                print(f"  Metadata: {first_record.metadata}")
            else:
                print("No tabular data found for the specified filter")

        except Exception as e:
            print(f"Error calling tabular_data_by_filter: {e}")

        finally:
            viam_client.close()

    except Exception as e:
        print(f"Error setting up data client: {e}")


async def main():
    """Run all data client tests."""
    print("Starting Data Client Integration Tests")
    print("=" * 50)

    # Run all tests
    await test_export_tabular_data()
    await test_get_latest_tabular_data()
    await test_tabular_data_by_filter()

    print("\n" + "=" * 50)
    print("Data Client Integration Tests completed")


if __name__ == "__main__":
    asyncio.run(main())
