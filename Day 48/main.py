# import statements
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_upgrade_prices():
    """Generates upgrade prices"""
    global item_prices

    # gets all upgrade <b> tags
    all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")

    # Convert <b> text into an integer price.
    for price in all_prices:
        element_text = price.text
        if element_text != "":
            item_prices.append(int(element_text.split("-")
                                   [1].strip().replace(",", "")))


# setting browser and its options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# setting the url
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# gets cookie to click on
cookie = driver.find_element(by=By.ID, value="cookie")

# gets upgrade item ids
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
item_ids.pop()

# setting time
timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

# item_prices stores prices of the items
item_prices = []

# generating price
get_upgrade_prices()

# creating dictionary of store items and prices
cookie_upgrades = {}
for n in range(len(item_prices)):
    cookie_upgrades[item_prices[n]] = item_ids[n]

# Running the bot
while True:
    cookie.click()

    # checking every 5 second
    if time.time() > timeout:

        # getting current cookie count
        cookie_made = driver.find_element(by=By.ID, value="money").text
        if "," in cookie_made:
            cookie_made = cookie_made.replace(",", "")

        # storing the cookie made in cookie count
        cookie_count = int(cookie_made)

        # finding upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, upgrade_id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = upgrade_id

        # purchasing the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)

        # creating purchase id and clicking the button
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stopping the bot and checking the cookies per second
    #   count.
    if time.time() > five_min:
        # printing the total number of cookies/second that were being made
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

# exiting the browser
driver.quit()
