# import statement
import requests

# adding sheety endpoint
sheety_endpoint = "https://api.sheety.co/******/flightDeals/users"


def post_new_row(first_name, last_name, email):
    """Adds new content to the sheet using API"""

    # adding body parameters
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    # posting via API
    response = requests.post(url=sheety_endpoint, json=body)
    response.raise_for_status()
    # printing response
    print(response.text)
