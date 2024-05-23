# Day 36

- Check for Stock Price Movements
- Get the News Articles
- Send alert notifications

# Stocks News Monitoring

- The program generates stock price difference between yesterday and day before yesterday's closing price and if the 
  difference is more than the threshold (that is 5%) then we are generating the article consisting of news headline and 
  description of the company stocks we want (here the company is TESLA) and sending an email to us consisting of each 
  article as the separate messages.

# Note:

- You will need to enter your own email address and the added app password provided by the respective gmail service
  in "my_email" and "my_password" parameters and recipients email id in "msg['To']" parameter.
- If you want some other company stock price and news then you need to change the "STOCK_NAME" and "COMPANY_NAME"
  parameters.