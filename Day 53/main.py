# import statements
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# creating header arguments
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

load_dotenv(".env")
URL = os.getenv("URL")

# chrome_options keeps the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# opening the browser
driver = webdriver.Chrome(options=chrome_options)

# getting information from the API
response = requests.get(url=URL, headers=header)

# getting html format using beautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# selecting all anchor elements with the class "list-card-top"
all_link_elements = soup.select(".list-card-top a")

# all_links stores all urls of zillow website
all_links = []
for link in all_link_elements:
    href = link["href"]
    # checking if the href is a full URL, if not, prepend the base URL
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

# selecting all address elements with the class "list-card-info" and store only
#   text in all_addresses
all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1]
                 for address in all_address_elements]

# select all heading elements with the class "list-card-heading"
all_price_elements = soup.select(".list-card-heading")
all_prices = []

# stores prices of each element
for element in all_price_elements:
    price = ""
    # getting the prices. Single and multiple listings have
    #   different tag & class structures
    try:
        # Price with only one listing
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        # Price with multiple listings
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)

# looping through each link to fill out the Google form
for n in range(len(all_links)):
    # connecting to the site and opening the Google form
    Google_sheet = os.getenv("GOOGLE_SHEET")
    driver.get(Google_sheet)

    # finding and filling the address, price and link field
    time.sleep(2)
    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/'
                                        'div[1]/div/div/div[2]/div/div[1]/div/'
                                        'div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/'
                                      'div[2]/div/div/div[2]/div/div[1]/div/'
                                      'div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/'
                                     'div[3]/div/div/div[2]/div/div[1]/div/'
                                     'div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/'
                                              'div[3]/div[1]/div[1]/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
