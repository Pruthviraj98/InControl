import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.MIMEText import MIMEText
 
 
fromaddr = "kunal.kc.chandiramani@gmail.com"
toaddr = "kdilip.chandiramani2016@vitstudent.ac.in"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "CAR ALERT"
 
body = "some inknown in your car"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "7666561900")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
