# import statements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# setting parameters
PROMISED_DOWN = 250
PROMISED_UP = 100
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

# chrome_options keeps the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # connecting to the site
        self.driver.get("https://www.speedtest.net/")

        # checking internet speed
        time.sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR,
                                             value=".start-button a")
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH,
                                           value='//*[@id="container"]/div/div'
                                                 '[3]/div/div/div/div[2]/div[3]'
                                                 '/div[3]/div/div[3]/div/div/'
                                                 'div[2]/div[1]/div[2]/div/div'
                                                 '[2]/span').text
        self.down = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/'
                                                   'div[3]/div/div/div/div[2]/'
                                                   'div[3]/div[3]/div/div[3]/'
                                                   'div/div/div[2]/div[1]/'
                                                   'div[3]/div/div[2]/'
                                                   'span').text

        print(f"Download Speed: {self.down} Mbps")
        print(f"Upload Speed: {self.up} Mbps")
        time.sleep(2)

    def tweet_at_provider(self):
        # connecting to the site
        self.driver.get("https://twitter.com/login")

        # signing in
        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         value='//*[@id="react-root"]/div'
                                               '/div/div[2]/main/div/div/'
                                               'div[1]/form/div/div[1]/label/'
                                               'div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH,
                                            value='//*[@id="react-root"]/'
                                                  'div/div/div[2]/main/div/'
                                                  'div/div[1]/form/div/div[2]/'
                                                  'label/div/div[2]/div/input')

        email.send_keys(EMAIL)
        time.sleep(3)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        # tweeting to the internet service provider
        time.sleep(10)
        tweet = self.driver.find_element(By.XPATH,
                                         value='//*[@id="react-root"]/'
                                               'div/div/div[2]/main/div'
                                               '/div/div/div/div/div[2]'
                                               '/div/div[2]/div[1]/div/'
                                               'div/div/div[2]/div[1]/'
                                               'div/div/div/div/div/div'
                                               '/div/div/div/div[1]/div'
                                               '/div/div/div[2]/div/div'
                                               '/div/div')

        tweet.send_keys(f"Hey Internet Provider, why is my internet speed "
                        f"{self.down} Mbps down/{self.up} Mbps up when I pay "
                        f"for {PROMISED_DOWN} Mbps down/{PROMISED_UP} Mbps up?")
        time.sleep(3)

        # clicking on tweet button
        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/'
                                                      'div/div/div[2]/main/div'
                                                      '/div/div/div/div/div[2]'
                                                      '/div/div[2]/div[1]/div/'
                                                      'div/div/div[2]/div[4]/'
                                                      'div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
