import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,price,departure_airport,arrival_airport,out_date,in_date,stop,emails,airlines,
                 flight_number,stop_list_airline,stop_list_number):
        self.price=price
        self.departure_airport=departure_airport
        self.arrival_airport=arrival_airport
        self.out_date=out_date
        self.in_date=in_date
        self.stop=stop
        self.emails=emails
        self.airlines=airlines
        self.flight_number=flight_number
        self.airline_list=stop_list_airline
        self.number_list=stop_list_number

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.environ["MY_EMAIL"],password=os.environ["PASSS"])
            if self.stop==0:

                for email in self.emails:

                    connection.sendmail(from_addr=os.environ["MY_EMAIL"],to_addrs=email,
                                    msg=f"Subject: Flight Update \n\n "
                                    f"Low Price Alert! Only \u20B9{self.price} to fly from {self.departure_airport} "
                                        f"with {self.stop} stop(s) to {self.arrival_airport},"
                                    f" departing on {self.out_date} and returning on {self.in_date}\n\n"
                                    f"Air-lines:{airlines}, Flight Number: {flight_number}\n"
                                    f"For further detail visit Google Flights")

            else:
                msg=""
                for i in range(self.stop+1):
                    msg+=f"\n Air-lines:{self.airline_list[i]}, Flight Number: {self.number_list[i]}"

                for email in self.emails:
                    connection.sendmail(from_addr=os.environ["MY_EMAIL"], to_addrs=email,
                                        msg=f"Subject: Flight Update \n\n "
                                            f"Low Price Alert! Only \u20B9{self.price} to fly from {self.departure_airport} "
                                            f"with {self.stop} stop(s) to {self.arrival_airport},"
                                            f" departing on {self.out_date} and returning on {self.in_date}\n"
                                            f"{msg}\n"
                                            f"For further detail visit Google Flights")
