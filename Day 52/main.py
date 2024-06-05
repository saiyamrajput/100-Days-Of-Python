# import statements
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# enter your username and password
SIMILAR_ACCOUNT = "********"  # Change this to an account of your choice
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"

# chrome_options keeps the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        # connecting to the website and logging in
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(6)

        # entering username and password
        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)

        # clicking "Not now" and ignoring Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH,
                                                     value="//div[contains"
                                                           "(text(), 'Not now')"
                                                           "]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(5)

        # clicking "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH,
                                                        value="//button["
                                                              "contains(text(),"
                                                              " 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        time.sleep(5)

        # connecting to the site
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
                        f"followers")

        time.sleep(5)

        modal = self.driver.find_element(by=By.XPATH,
                                         value="/html/body/div[4]/div/div/"
                                               "div[2]")
        for i in range(5):
            # executing java script
            self.driver.execute_script("arguments[0].scrollTop = "
                                       "arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,
                                                value='li button')

        # following the users
        for button in all_buttons:
            # handling exception
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH,
                                                         value="//button["
                                                               "contains(text()"
                                                               ", 'Cancel')]")
                cancel_button.click()


telegram_bot = InstaFollower()
telegram_bot.login()
telegram_bot.find_followers()
telegram_bot.follow()
