import config
# Import modules
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
### Add new subclass for adding attachments
from email.mime.application import MIMEApplication
## The pandas library is only for generating the current date, which is not necessary for sending emails
import pandas as pd
import calendar
from datetime import date

curr_date = date.today()
today_date = calendar.day_name[curr_date.weekday()]
# Define the HTML document
# Add an image element
##############################################################
html = '''
    <html>
        <body>
            <h1>Daily timesheet report</h1>
            <p>Hello, bot just added 8 hours to the timesheet</p>
            <img src='cid:myimageid' width="700">
        </body>
    </html>
    '''


htmlM = '''
    <html>
        <body>
            <h1>Daily timesheet report</h1>
            <p>Hello, bot just created a new week and added 8 hours to the timesheet</p>
            <img src='cid:myimageid' width="700">
        </body>
    </html>
    '''


htmlF = '''
    <html>
        <body>
            <h1>Daily timesheet report</h1>
            <p>Hello, bot just added 8 hours to the timesheet. Timesheet saved and submitted</p>
            <img src='cid:myimageid' width="700">
        </body>
    </html>
    '''
htmlW = f'''
    <html>
        <body>
            <h1>Weekend timesheet report</h1>
            <p>Hello, bot just check timesheet. Timesheet status is pending</p>
            <img src='cid:myimageid' width="700">
        </body>
    </html>
    '''


##############################################################

# Define a function to attach files as MIMEApplication to the email
    ## Add another input extra_headers default to None
##############################################################
def attach_file_to_email(email_message, filename, extra_headers=None):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Set up the input extra_headers for img
      ## Default is None: since for regular file attachments, it's not needed
      ## When given a value: the following code will run
         ### Used to set the cid for image
    if extra_headers is not None:
        for name, value in extra_headers.items():
            file_attachment.add_header(name, value)
    # Attach the file to the message
    email_message.attach(file_attachment)
##############################################################    

# Set up the email addresses and password. Please replace below with your email address and password
email_from = config.email_origen
password = config.gmail_password
email_to = config.email_end


# Generate today's date to be included in the email Subject
date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Report email - {date_str}'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
#email_message.attach(MIMEText(html, "html"))
if calendar.day_name[curr_date.weekday()] == "Monday":
    email_message.attach(MIMEText(htmlM, "html"))
elif calendar.day_name[curr_date.weekday()] == "Friday":
    email_message.attach(MIMEText(htmlF, "html"))
elif calendar.day_name[curr_date.weekday()] == "Sunday":
    email_message.attach(MIMEText(htmlW, "html"))
else:
    email_message.attach(MIMEText(html, "html"))

# Attach more (documents)
## Apply function with extra_header on chart.png. This will render chart.png in the html content
##############################################################
attach_file_to_email(email_message, f'{today_date}.png', {'Content-ID': '<myimageid>'})
##############################################################
attach_file_to_email(email_message, f'{today_date}.png')
#attach_file_to_email(email_message, 'fpdf_pdf_report.pdf') multiple attachment if required 

# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_from, password)
    server.sendmail(email_from, [email_to], email_string) 
    print('Mail Sent')
















""" import email
import config
import ssl
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

email_sender = 'groupprinterad@gmail.com'
email_password = config.gmail
email_reciver = 'iorijvc@gmail.com'

subject = 'test test test'
body = """
#This is a test email from myself
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] =  email_reciver
em['Subject'] =subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciver,em.as_string())

print("email send")
 """