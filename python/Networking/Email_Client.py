import smtplib
from email.mime.text import MIMEText

body = "This is test email How are you"
msg = MIMEText(body)
msg['From']  = "maazshaikh7020@gmail.com"
msg['To'] = "maazshaikh7020@gmail.com"
msg['Subject'] = "Test"

server = smtplib.SMTP("smtp.gmail.com", 587)  # port
server.starttls()
server.login("maazshaikh7020@gmail.com","Maaz")
server.send_message(msg)
print("mail send")
server.quit()