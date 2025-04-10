# ATB Bus Times

A Tidbyt app that displays real-time bus departures from ATB stops in Trondheim, Norway.

## Features

- Shows the next three departures from your selected bus stop
- Displays line numbers and departure times
- Updates in real-time
- Shows "Nå" when the bus is due to depart within the next minute

## Configuration

To use this app, you need to configure the following settings:

1. `stop_id`: The Entur ID for your bus stop (e.g., "NSR:StopPlace:42052" for Valøyvegen)
2. `quay_id`: The specific platform ID at your stop (e.g., "NSR:Quay:71981")
3. `stop_name`: The display name for your stop (e.g., "Valøyvegen")

You can find these IDs by:
1. Visiting [Entur's journey planner](https://entur.no)
2. Searching for your stop
3. Looking at the URL or using the browser's developer tools

## Default Values

If no configuration is provided, the app will show departures from Valøyvegen (stop ID: NSR:StopPlace:42052, quay ID: NSR:Quay:71981).

## Support

For support or to report issues, please visit the [GitHub repository](https://github.com/yourusername/atb-bus-times).