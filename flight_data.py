class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date,stops,air_line,
                 flight_number,stop_list_airline,stop_list_number):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops
        self.airline =air_line
        self.flight_number=flight_number
        self.airline_list=stop_list_airline
        self.number_list=stop_list_number

def find_cheapest_flight(data, return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A",
                          "N/A", "N/A","N/A",
                          "N/A","N/A","N/A",)





    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    first_flight = all_flights[0]
    lowest_price=first_flight["price"]
    origin=first_flight["flights"][0]["departure_airport"]["id"]
    destination=first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date=first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
    nr_stops=len(first_flight["flights"])-1
    air_line=first_flight["flights"][0]["airline"]
    flight_number=first_flight["flights"][0]["flight_number"]

    stop_list_airline=[]
    stop_list_number=[]
    if nr_stops>0:
        for i in range(nr_stops+1):
            stop_list_airline.append(first_flight["flights"][i]["airline"])
            stop_list_number.append(first_flight["flights"][i]["flight_number"])

    cheapest_flight=FlightData(lowest_price, origin, destination, out_date, return_date,
                               nr_stops,air_line,flight_number,stop_list_airline,stop_list_number)

    for flight in all_flights:

        try:
            price = flight["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue
        if price < lowest_price:
            lowest_price = price
            origin = flight["flights"][0]["departure_airport"]["id"]
            destination = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            nr_stops = len(flight["flights"]) - 1
            air_line=flight["flights"][0]["airline"]
            flight_number=flight["flights"][0]["flight_number"]

            stop_list_airline = []
            stop_list_number = []
            if nr_stops > 0:
                for i in range(nr_stops+1):
                    stop_list_airline.append(flight["flights"][i]["airline"])
                    stop_list_number.append(flight["flights"][i]["flight_number"])

            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date,nr_stops,
                                         air_line,flight_number,stop_list_airline,stop_list_number)


    return cheapest_flight
