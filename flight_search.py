import os
import requests
from dotenv import load_dotenv
load_dotenv()
flight_endpoint=os.environ["FLIGHT_ENDPOINT"]
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key=os.environ["SERPAPI_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time,is_direct=True):
        params = {
          "engine": "google_flights",
          "departure_id": origin_city_code,
          "arrival_id": destination_city_code,
          "outbound_date": from_time,
          "return_date": to_time,
          "type": "1",
          "adults": "1",
          "currency": "INR",
          "api_key": self.api_key,
        }
        if is_direct:
            params["stops"]="1"


        response1=requests.get(flight_endpoint, params=params)
        if response1.status_code != 200:
            print(f"check_flights() response code: {response1.status_code}")
            return None
        data1 = response1.json()
        if "error" in data1:
            print(f"API error: {data1['error']}")
            return None
        return data1

