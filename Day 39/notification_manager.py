# import statements
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class NotificationManager:

    def send_message(self, message):
        """Sends user messages via email"""
        my_email = "ENTER YOUR EMAIL"
        my_password = "ENTER YOUR ADDED APP PASSWORD"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)

            # sending email containing 'ascii' values
            msg = MIMEMultipart()
            msg['From'] = my_email
            msg['To'] = "ENTER RECEIVERS EMAIL"
            msg["Subject"] = "Cheap Flight Details"

            # writing mail body
            body = MIMEText(message, 'plain', 'utf-8')

            # sending mail after attaching body to the email
            msg.attach(body)
            response = connection.send_message(msg)

            # printing status
            print(response)

            connection.close()
