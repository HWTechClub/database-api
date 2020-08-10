import smtplib
from socket import gaierror

port = 587
smtp_server = "smtp.migadu.com"
login = "hasan@hwtech.club" 
password = "QA7YNTNmpjwMBkn" 

sender = "hasan@hwtech.club"
receiver = "akilan@hwtech.club"

message = f"""\
Subject: Hi
To: {receiver}
From: {sender}

hello, how are you."""

try:
    with smtplib.SMTP("smtp.migadu.com", 587) as server:
        server.connect("smtp.migadu.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("hasan@hwtech.club", "QA7YNTNmpjwMBkn")
        server.sendmail(sender, receiver, message)
except (gaierror, ConnectionRefusedError):
  print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
  print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
  print('SMTP error occurred: ' + str(e))
else:
  print('Sent')
