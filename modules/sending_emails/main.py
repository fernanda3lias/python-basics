# Sending SMTP e-mails 
# SMTP, or Simple Mail Transfer Protocol
# Is a standard network protocol for sending email. 
import os
import pathlib
from string import Template
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

# HTML file path
HTML_PATH = pathlib.Path(__file__).parent / 'email.html'

# Sender and recipient data
sender = os.getenv('FROM_EMAIL', '')
recipient = sender

# SMTP settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('email_password', '')

# Text message
with open(HTML_PATH, 'r') as file:
    file_text = file.read()
    template = Template(file_text)
    email_text = template.substitute(name='John')

# Transforming message in MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = recipient
mime_multipart['subject'] = 'E-mail subject'

email_body = MIMEText(email_text, 'html', 'utf-8')
mime_multipart.attach(email_body)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail sended successfully')