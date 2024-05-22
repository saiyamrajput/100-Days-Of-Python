# import statement
import requests

# creating questions criteria parameter
parameter = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

# generating data
response = requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()

# getting data in json format
data = response.json()

# storing data in question
questions = data["results"]
