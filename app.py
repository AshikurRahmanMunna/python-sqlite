"""send email python"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Your Name"
message["to"] = "yourrecipient@example.com"
message["subject"] = "Test email."
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("yourEmail@example.com", "yourpassword")
    smtp.send_message(message)
    print('Sent...')
