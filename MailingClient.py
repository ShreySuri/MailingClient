import smptlib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smptlib.SMPT("smpt.gmail.com", 25)

server.ehlo()

with open("password.txt", "r") as f:
	password = f.read()

server.login("throwaway.boi5808@gmail.com", password)

msg = MIMEMultipart()
msg["from"] = "Shrey Suri"
msg["to"] = "shrey.suri5@gmail.com"
msg["Subject"] = "Just a test"

with open("message.txt", "r") as g:
	message = g.read()

message.attach(MIMEText(message, "plain"))

