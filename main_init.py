
from google.cloud import texttospeech
import vlc
import time
import os
from def_fd import face_detect
from combined import *


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\admin\\Desktop\\Hackathon\\codeoverflow-08-10e832d41721.json'

client = texttospeech.TextToSpeechClient()
voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)




#from tts import texttospeech1
#from google.cloud.bigquery.client import Client

def texttospeech1(string, voice, audio_config, hello=None):
    # Set the text input to be synthesized
    sample=hello+string

    synthesis_input = texttospeech.types.SynthesisInput(text=sample)

    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('output1.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        #print('Audio content written to file "output.mp3"')
    playsound("output1.mp3")
    #player.stop()




flag=0

name,flag=face_detect()
#print(name)
if(flag==0):
    texttospeech1(name,voice,audio_config,hello="Hello")
    meta_detect()
else:
    print("Driving Restricted")




