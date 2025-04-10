import requests
import json
from datetime import datetime

# Entur API endpoint for real-time departures
ENTUR_API_URL = "https://api.entur.io/journey-planner/v3/graphql"

# Headers required by Entur API
HEADERS = {
    "ET-Client-Name": "atb-tidbyt-display",
    "Content-Type": "application/json"
}

def get_departures():
    # GraphQL query for departures
    query = """
    {
      stopPlace(id: "NSR:StopPlace:42052") {
        id
        name
        estimatedCalls(timeRange: 72000, numberOfDepartures: 10) {
          realtime
          aimedDepartureTime
          expectedDepartureTime
          destinationDisplay {
            frontText
          }
          serviceJourney {
            line {
              publicCode
            }
          }
        }
      }
    }
    """

    try:
        # Make the request to Entur API
        response = requests.post(
            ENTUR_API_URL,
            json={'query': query},
            headers=HEADERS
        )
        
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text[:200]}...")  # Print first 200 chars
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            if 'data' in data and 'stopPlace' in data['data']:
                stop_place = data['data']['stopPlace']
                print(f"\nStop: {stop_place['name']}")
                
                if 'estimatedCalls' in stop_place:
                    print("\nUpcoming Departures:")
                    for call in stop_place['estimatedCalls']:
                        line = call['serviceJourney']['line']['publicCode']
                        destination = call['destinationDisplay']['frontText']
                        departure_time = call['expectedDepartureTime'] or call['aimedDepartureTime']
                        
                        # Convert the time to a more readable format
                        try:
                            departure_time = datetime.fromisoformat(departure_time.replace('Z', '+00:00'))
                            formatted_time = departure_time.strftime("%H:%M")
                        except:
                            formatted_time = departure_time
                        
                        print(f"Line {line} to {destination} at {formatted_time}")
            else:
                print("No departure information found in the response")
                print("Response structure:", json.dumps(data, indent=2))
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("Testing Entur API for real-time departures...")
    get_departures() 