# import statements
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class NotificationManager:

    def send_message(self, emails, message):
        """Sends user messages via email"""
        my_email = "ENTER YOUR EMAIL"
        my_password = "ENTER YOUR ADDED APP PASSWORD"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)

            # sending email to each user
            for email in emails:
                # sending email containing 'ascii' values
                msg = MIMEMultipart()
                msg['From'] = my_email
                msg['To'] = email
                msg["Subject"] = "New Low Price Flight!"

                # writing mail body
                body = MIMEText(message, 'plain', 'utf-8')

                # sending mail after attaching body to the email
                msg.attach(body)
                connection.send_message(msg)

            connection.close()
