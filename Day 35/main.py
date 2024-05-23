# import statements
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# enter your own longitude, latitude and API key
MY_LAT = 43.469860
MY_LONG = -80.538391
api_key = ""

# add your email and added app password below
my_email = ""
my_password = ""

# adding parameters for url
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

# generating data
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                        params=parameters)
response.raise_for_status()

# storing data in json format
weather_data = response.json()

# will_rain checks if it will rain or not
will_rain = False

# checking weather condition for next 12 hours
for hour in weather_data["list"]:
    weather_code = hour["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True

# informing user by email
if will_rain:
    message = "☂️☔It's going to rain today, bring an umbrella with you."
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)

        # sending the mail
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = ""
        msg["Subject"] = "Weather Report"

        # writing mail body
        body = MIMEText(message, 'plain', 'utf-8')

        # sending mail after attaching body to the email
        msg.attach(body)
        connection.send_message(msg)

        connection.close()
