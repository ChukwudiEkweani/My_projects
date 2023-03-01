# Importing neede libraries

import requests # For requesting url's API
from datetime import datetime # For checking current time
import smtplib # For sending the email alert
import time

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "yourpassword"
MY_LAT = 9.081999 # Your latitude
MY_LONG = 8.675277 # Your longitude

# Getting response from endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # Creating exceptions in case the page encounters an issue loading
data = response.json()  # Extracting the json data

iss_latitude = float(data["iss_position"]["latitude"]) # Extracting the latitude value from the json file
iss_longitude = float(data["iss_position"]["longitude"]) # Extracting the longitude from the json file

#Your position is within +5 or -5 degrees of the ISS position.
def iss_overhead():
    diff_lat = MY_LAT - iss_latitude
    diff_lng = MY_LONG - iss_longitude

    if diff_lat in range(-5, 5) and diff_lng in range(-5,5):
        return True
    
def is_night():
    if time_now >= sunset or time_now <= sunrise: # This condition ensures the program alerts us when the environment is dark enough the see the iss 
        return True

# Setting up parameters for the sunrise-sunset api
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Creating response
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status() # Ceating exceptions
data = response.json() # Extracting the json fromat
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) # Extracting the sunrise time from the json
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) # Extracting the sunset time from the json

time_now = int(datetime.now().hour) # Generating the current time in nearest hour


while True:
    time.sleep(60) # This runs the code every 60 seconds
    if iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg= "Subject:Look Up👆\n\nThe ISS is above you in the sky"
        )





