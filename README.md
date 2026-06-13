# Analytics
A simple analytics dashboard with WebSocket data updates and CSV export.

## Usage
1. Create a `UserEngagement` object with active users, session duration, and conversion funnels.
2. Create a `WebSocket` object and send the `UserEngagement` data using `send_data`.
3. Get the updated data using `get_data`.
4. Export the data to CSV using `export_to_csv`.
