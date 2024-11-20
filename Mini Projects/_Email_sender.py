from email.message import EmailMessage
import ssl
import smtplib

email_sender=input('Enter sender email address:')
email_password=input('Enter sender email password:')
email_receiver =input('Enter receiver email address:')
subject = "This is subject of mail"
body='''This is body of mail
This mail send by python programing'''

em = EmailMessage()
em['From']= email_sender
em['To']= email_receiver
em['subject']= subject
em.set_content(body)

try:
    context= ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context= context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
except Exception as e:
    print(e)
