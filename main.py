#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from flight_data import find_cheapest_flight
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch

from datetime import datetime, timedelta


# tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
# sixs_month_from_today=(datetime.today()+timedelta(days=181.6)).strftime("%Y-%m-%d")
#you can input ur own date
from_day=datetime(2026,6,17).strftime("%Y-%m-%d")
till_day=datetime(2026,6,22).strftime("%Y-%m-%d")

data_manager=DataManager()
sheet_data=data_manager.get_destination_data()
#pprint(sheet_data)

users_data=data_manager.get_customer_emails()
customer_emails=[row["whatIsYourEmail"] for row in users_data]

flight_search=FlightSearch()
for loc in sheet_data:
    print(f"Flights for {loc["city"]}...")
    flight=flight_search.check_flights("BLR",loc["iataCode"],from_day,till_day)
    #pprint(flight)

    cheap_flight=find_cheapest_flight(data=flight,return_date=till_day)
    pprint(f"{loc['city']}: INR {cheap_flight.price}")

    if cheap_flight.price == "N/A":
        print(f"Falling back to check indirect flights for {loc['city']}...")
        flight = flight_search.check_flights("BLR", loc["iataCode"], from_day, till_day,False)
        # pprint(flight)
        cheap_flight = find_cheapest_flight(data=flight, return_date=till_day)
        pprint(f"cheapest indirect flight: INR {cheap_flight.price}")
        print(cheap_flight.stops)
    if cheap_flight.price != "N/A" and cheap_flight.price < loc['lowestPrice']:
        data_manager.update_lowest_price(row_id=loc["id"], new_price=cheap_flight.price)
        notification = NotificationManager(cheap_flight.price,"BLR",loc["iataCode"],
                                               cheap_flight.out_date,cheap_flight.return_date,cheap_flight.stops,
                                               customer_emails,cheap_flight.airline,cheap_flight.flight_number,
                                           cheap_flight.airline_list,cheap_flight.number_list)


