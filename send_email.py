# send_email.py
import os
import smtplib, ssl
from email.message import EmailMessage

def send_email(message: str, subject: str = "News digest"):
    sender = os.getenv("diju.sharon@gmail.com")             # e.g. youraddress@gmail.com
    app_pw = os.getenv("princesssbyju")     # app-specific password
    to = os.getenv("EMAIL_TO", sender)

    if not sender or not app_pw:
        raise RuntimeError("Set EMAIL_USER and EMAIL_APP_PASSWORD environment variables.")

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as s:
        s.login(sender, app_pw)
        s.send_message(msg)
