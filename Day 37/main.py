# import statements
import requests
from datetime import datetime


# enter the username you want, your own generated token and own graph id
USERNAME = "YOUR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

# storing API
pixela_endpoint = "https://pixe.la/v1/users"

# adding User configuration parameters
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # posting to pixela via API
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# adding graph API
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# creating graph configuration parameters
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# creating header
headers = {
    "X-USER-TOKEN": TOKEN
}

# # Sending a POST request to create/update a graph with provided configuration
# #     and headers
# response = requests.post(url=graph_endpoint, json=graph_config,
#                          headers=headers)
# print(response.text)

# creating endpoint having graph id
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# generating today's date
today = datetime.now()

# stores users data
pixel_data = {
    "date": today.strftime("%Y%m%d"),   # stores date in YYYY-MM-DD format
    "quantity": input("How many kilometers did you cycle today? "),
}

# posting the data
response = requests.post(url=pixel_creation_endpoint, json=pixel_data,
                         headers=headers)
print(response.text)

# updating the endpoint with time
update_endpoint = (f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"
                   f"{today.strftime('%Y%m%d')}")

# new_pixel_data variables is an example variable to update the data
new_pixel_data = {
    "quantity": "4.5"
}

# # updating the data
# response = requests.put(url=update_endpoint, json=new_pixel_data,
#                         headers=headers)
# print(response.text)

# creating delete endpoint
delete_endpoint = (f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"
                   f"{today.strftime('%Y%m%d')}")


# # DELETES the data for the day you want
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
