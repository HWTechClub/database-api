import csv
import smtplib
from socket import gaierror

port = 587
smtp_server = "smtp.migadu.com"
login = "hasan@hwtech.club" 
password = "QA7YNTNmpjwMBkn" 

sender = "hasan@hwtech.club"

message = """Subject: Whatsapp web
To: {recipient}
From: {sender}
Hi {name}, bye bye"""

try:
    with smtplib.SMTP("smtp.migadu.com", 587) as server:
        server.connect("smtp.migadu.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("hasan@hwtech.club", "QA7YNTNmpjwMBkn")
        with open("contact.csv") as file:
         reader = csv.reader(file)
         next(reader)  # it skips the header row
         for name, email in reader:
           server.sendmail(
           sender,
           email,
           message.format(name=name, recipient=email, sender=sender),
          )
        
except (gaierror, ConnectionRefusedError):
  print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
  print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
  print('SMTP error occurred: ' + str(e))
else:
  print(f'Sent to {name}')
