import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("kunal.kc.chandiramani@gmail.com", "7666561900")
 
msg = "A stranger has entered your car!"
server.sendmail("kunal.kc.chandiramani@gmail.com", "kunal.kc.chandiramani@gmail.com", msg)
server.quit()
