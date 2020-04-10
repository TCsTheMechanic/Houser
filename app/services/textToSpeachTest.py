import os
import speech_recognition as sr
from speechCreator import voice

houser = sr.Recognizer()

speech = ""

while(speech != "goodbye Houser"):
  with sr.Microphone() as source:
    print("----------Start----------")
    audio = houser.listen(source)
    print("----recording is over----")

  try:
    speech = "" + houser.recognize_google(audio)
    print("Person said: " + speech)
    if(speech == "data from mongo"):
      voice(speech)
  except:
    pass
