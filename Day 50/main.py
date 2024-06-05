from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (NoSuchElementException,
                                        ElementClickInterceptedException)
from time import sleep

# enter your email, password
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

# chrome_options keeps the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# connecting to the website
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.tinder.com")

# logging in
sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()
sleep(2)
fb_login = driver.find_element(By.XPATH,
                               value='//*[@id="modal-manager"]/div/div/div[1]/'
                                     'div/div[3]/span/div[2]/button')
fb_login.click()
sleep(2)

# switching to facebook window and logging via facebook
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# signing in
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# switching back to Tinder Window
driver.switch_to.window(base_window)

sleep(5)

# allowing permissions
allow_location_button = driver.find_element(By.XPATH,
                                            value='//*[@id="modal-manager"]/'
                                                  'div/div/div/div/div[3]/'
                                                  'button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH,
                                           value='//*[@id="modal-manager"]/div/'
                                                 'div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH,
                              value='//*[@id="content"]/div/div[2]/div/div/div'
                                    '[1]/button')
cookies.click()

# tinder free tier only allows 100 "Likes" per day
for n in range(100):
    sleep(1)

    # handling exceptions
    try:
        print("called")

        # like button
        like_button = driver.find_element(By.XPATH,
                                          value='//*[@id="content"]/div/div[1]/'
                                                'div/main/div[1]/div/div/div[1]'
                                                '/div/div[2]/div[4]/button')
        like_button.click()

    # catches the cases where there is a "Matched" pop-up in front of the
    #   "Like" button:
    except ElementClickInterceptedException:
        try:
            # clicking on match pop up
            match_popup = driver.find_element(By.CSS_SELECTOR,
                                              value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded,
        #   so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

# closing the browser
driver.quit()
