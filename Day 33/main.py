# import statements
import requests
from datetime import datetime
import smtplib
import time

# please enter your own latitude and longitude below
MY_LAT = 43.469860
MY_LONG = -80.538391

# add your email and added app password below
my_email = ""
my_password = ""


def is_iss_overhead():
    """Returns true if ISS is near our position or not"""
    # getting data from the api
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # storing latitude and longitude from the data we got from the url
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
            MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True  # returning true


def night():
    """Returns true if it is nighttime"""
    # creating parameters dictionary containing formatting, and latitude and
    #   longitude
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # getting data from the api
    response = requests.get("https://api.sunrise-sunset.org/json",
                            params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # checking for nighttime
    if time_now >= sunset or time_now <= sunrise:
        return True  # returning true


# runs the loop after running every 2 minute
while True:
    time.sleep(120)
    # sending email to us if iss is overhead
    if is_iss_overhead() and night():
        # connecting to server
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg="Subject:Look Up\n\nThe ISS is above you in "
                                "the sky")

        # closing the connection
        connection.close()
