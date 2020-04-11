import os
import speech_recognition as sr
from speechCreator import voice
from db.connection import connect

database = connect()
dialog_collection = database.Dialog

houser = sr.Recognizer()
speech = ''

while(speech != 'goodbye Houser'):
  with sr.Microphone() as source:
    print('----------Start----------')
    audio = houser.listen(source)
    print('----recording is over----')

  try:
    speech = '' + houser.recognize_google(audio)
    print('Person said: ' + speech)
    if(speech == 'ask from mongo'):
      voice('answer from mongo')
  except:
    pass