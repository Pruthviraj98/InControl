import speech_recognition as sr

import os

r=sr.Recognizer()
r.adjust_for_ambient_noise
r.energy_threshold = 10000
with sr.Microphone() as source:
    print('Say Something1')
    audio=r.listen(source)

try:

    print(r.recognize_google(audio))
    if(re.match("info",r.recognize_google(audio))):
       os.system("vlc-ctrl info")

except:
    pass
