from email.message import EmailMessage
import ssl              #secure socket layer
import smtplib          # simple mail transfer protocol(smtp)

email_reciver='sarthakpalde5@gmail.com'
email_sender="ninadkawade25@gmail.com"
email_password=' '

subject="email processing part"

body="""
email is being proceed 
"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_reciver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
  smtp.login(email_sender,email_password)
  smtp.sendmail(email_sender,email_reciver,em.as_string())