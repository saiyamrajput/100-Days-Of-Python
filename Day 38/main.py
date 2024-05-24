# import statements
import requests
from datetime import datetime

# enter your own API KEY and APP ID
API_KEY = "YOUR API KEY"
APP_ID = "YOUR APP ID"

# enter your own gender, height, weight, age
GENDER = "YOUR GENDER"
WEIGHT_KG = "YOUR WEIGHT"
HEIGHT_CM = "YOUR HEIGHT"
AGE = "YOUR AGE"


# creating endpoint connection
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "YOUR ENDPOINT"

# asking user for the input
exercise_text = input("Tell me which exercises you did: ")

# creating headers
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# creating parameters to post
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# posting the
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# generating today's date and time
date = datetime.now().strftime("%d%m%Y")  # date format: DD-MM-YYYY
today_time = datetime.now().strftime("%X")  # time format: 24 hours (TT:MM:SS)

# extracting data from result and posting in spreadsheet
for exercise in result["exercises"]:

    # creating sheet input
    sheet = {
        "workout": {
            "date": date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # posting
    sheet_response = requests.post(sheety_endpoint, json=sheet)
