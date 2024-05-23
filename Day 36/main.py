# import statements
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# please enter your own email id and password
my_email = ""
my_password = ""

# stocks name and company's name
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# stock and news API reference
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# storing stock API and news API
STOCK_API_KEY = "X9608TGNJWOZ8AKT"
NEWS_API_KEY = "0327baa157d34ac8bb1c0a51d6af9f1c"

# setting stock and news parameter to get proper data from the API
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
news_parameters = {
    "apikey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}

# getting data from the API
request = requests.get(STOCK_ENDPOINT, params=stock_parameters)
request.raise_for_status()

# converting data to json format
data = request.json()["Time Series (Daily)"]

# converting data to list
data = [value for (key, value) in data.items()]

# getting yesterdays data and day before yesterday's data
yesterday_data = data[0]
yesterday_data_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data["4. close"]

# generating difference between the price of stock
diff = (float(yesterday_data_closing_price) -
        float(day_before_yesterday_data_closing_price))

# updown stores whether stock went up or down
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# calculating percentage difference
diff_percentage = round((diff / float(yesterday_data_closing_price)) * 100)

# If percentage is greater than 5 then get news from news API
if abs(diff_percentage) > 5:
    # getting data from the API
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()

    # getting data in json format
    news_data = news_response.json()["articles"]

    # generating first three articles
    three_articles = news_data[:3]

    # creating new list of first three articles
    articles = [(f"{STOCK_NAME}: {up_down}{diff_percentage}%\n"
                 f"Headline: {article['title']}. "
                 f"\nBrief: {article['description']}")
                for article in three_articles]

    # connecting to gmail server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)

        # sending three articles separately
        for article in articles:
            # sending email containing 'ascii' values
            msg = MIMEMultipart()
            msg['From'] = my_email
            msg['To'] = ""
            msg["Subject"] = f"{COMPANY_NAME} Stock News"

            # writing mail body
            body = MIMEText(article, 'plain', 'utf-8')

            # sending mail after attaching body to the email
            msg.attach(body)
            connection.send_message(msg)

        connection.close()
