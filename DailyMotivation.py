import smtplib
from email.mime.multipart import MIMEMultipart
from datetime import datetime, date, time, timedelta
import random

#Random Number
random_number = random.randint(0,3)

#Motivational Quotes
quotes = [
    'Nothing is impossible, the word itself says "Im possible"! -- Audrey Hepburn',
    'Ive learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. -- Maya Angelou',
    'Whether you think you can or you think you cant, youre right. -- Henry Ford'
    ]

#Get Todays Date
today = date.today()
#Gmail User Details
gmail_user = 'emails@luigi-marino.com'
gmail_password = ''
sent_from = gmail_user
to = ['emails@luigi-marino.com']

#Email Title
msg = str(today) + "\n" + quotes[random_number]

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg)
    server.close

    print ('Email Sent!')
except:
    print ('Something went wrong')