# ATB Bus Times for Tidbyt

This app displays real-time bus departures from ATB stops in Trondheim, Norway on your Tidbyt display.

## Features

- Shows upcoming bus departures from your selected stop
- Displays line number, destination, and minutes until departure
- Updates every minute with real-time information
- Default stop is Valøyvegen (northbound) (NSR:StopPlace:5843)
- Includes a test mode for previewing the display

## Configuration

You can configure the app by setting the following parameters in your Tidbyt app settings:

- `stop_id`: The Entur stop ID (default: NSR:StopPlace:5843 for Valøyvegen)
- `test_mode`: Set to `true` to use test data instead of real-time data

## Testing

To test the app before publishing:

1. Install the Tidbyt CLI
2. Run the following command to test the app locally:
   ```bash
   tidbyt apps run atb_bus_times.star --config '{"test_mode": true}'
   ```
3. The app will display test data showing how it will look on your Tidbyt

## Finding Your Stop ID

1. Go to [Entur Journey Planner](https://entur.no)
2. Search for your bus stop
3. Click on the stop to see its details
4. The stop ID will be in the URL or you can find it in the page source

## Publishing

To publish this app to your Tidbyt:

1. Make sure you have the Tidbyt CLI installed
2. Run `tidbyt apps push` in this directory
3. The app will be available in your Tidbyt's app list

## Support

If you have any issues or questions, please open an issue in this repository.