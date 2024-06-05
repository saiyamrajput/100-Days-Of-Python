# import statements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def cancel_application():
    """Cancels the application"""
    # close Button
    close_button = driver.find_element(by=By.CLASS_NAME,
                                       value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME,
                                          value="artdeco-modal__confirm-"
                                                "dialog-btn")[1]
    discard_button.click()


# enter your email, password and phone number
EMAIL = "YOUR EMAIL"
PASSWORD = 'YOUR PASSWORD'
PHONE_NUMBER = "YOUR PHONE NUMBER"

# chrome_options keeps the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# connecting to the website
driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0")

# clicking reject cookies button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR,
                                    value='button[action-type="DENY"]')
reject_button.click()

# clicking sign in button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# signing in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

# generating all job listing
time.sleep(5)
all_job_listings = driver.find_elements(by=By.CSS_SELECTOR,
                                        value=".job-card-container--clickable")

# applying for Jobs in all_job_listing
for listing in all_job_listings:
    # clicking on a single job listing
    listing.click()
    time.sleep(2)

    # handling exceptions
    try:
        # locating the apply button
        time.sleep(5)
        apply_button = driver.find_element(by=By.CSS_SELECTOR,
                                           value=".jobs-s-apply button")
        apply_button.click()

        # checking if application requires phone number and the field is empty,
        #   then filling in the number.
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR,
                                    value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE_NUMBER)

        # submitting the application
        submit_button = driver.find_element(by=By.CSS_SELECTOR,
                                            value="footer button")

        # checking if the application requires additional fields to enter then
        #   discarding the application, else submitting the application
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            cancel_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)

        # closing the application
        shut_button = driver.find_element(by=By.CLASS_NAME,
                                          value="artdeco-modal__dismiss")
        shut_button.click()
    except NoSuchElementException:
        cancel_application()
        print("No application button, skipped.")
        continue

print("\nWork Completed")
time.sleep(5)
driver.quit()
