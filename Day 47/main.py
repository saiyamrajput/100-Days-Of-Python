# import statements
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# storing url and headers
url = ("https://www.amazon.ca/Samsung-Galaxy-S24-5G-Nightography/dp/"
       "B0CQPPDV5P/ref=asc_df_B0CQPPDV5P")
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# generating price
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency.replace(',', ''))
title = soup.find(id="productTitle").get_text().strip()
print(f"{title}\n{price_as_float}")

# generating message
message = f"{title} is now {price_as_float}"

# sending mail
my_email = "ENTER YOUR EMAIL"
my_password = "ENTER YOUR ADDED APP PASSWORD"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)

    # sending email containing 'ascii' values
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = "ENTER RECEIVERS EMAIL"
    msg["Subject"] = "Amazon Price Alert!"

    # writing mail body
    body = MIMEText(message, 'plain', 'utf-8')

    # sending mail after attaching body to the email
    msg.attach(body)
    response = connection.send_message(msg)

    # printing status
    print(response)

    connection.close()
