import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()
sheet_endpoint=os.environ["SHEET_ENDPOINT"]
user_endpoint=os.environ["USERS_ENDPOINT"]
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user=os.environ["USER"]
        self.password=os.environ["PASSWORD"]
        self.authorization=HTTPBasicAuth(self.user,self.password)
        self.destination_data={}
        self.customer_data={}

    def get_destination_data(self):
        response=requests.get(sheet_endpoint,auth=self.authorization)
        data=response.json()
        self.destination_data=data["prices"]
        return self.destination_data

    def update_lowest_price(self,row_id,new_price):
        new_data={
            "price":{
                "lowestPrice":new_price,
            }
        }
        requests.put(f"{sheet_endpoint}/{row_id}",json=new_data,auth=self.authorization)
    def get_customer_emails(self):
        response=requests.get(user_endpoint,auth=self.authorization)
        data=response.json()
        self.customer_data=data["users"]
        return self.customer_data