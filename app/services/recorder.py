from app.services.frequency import catcher
from db.connection import connect
import speech_recognition as sr
import os

def __init__():
  pass

def start():
  dialog_collection = connect().Dialog

  houser = sr.Recognizer()
  speech = ''

  while(speech != 'goodbye Houser'):
    try:
      speech = listener(houser)
      print('Person said: ' + speech)
      understood = False
      for dialog in dialog_collection.find():
        if (speech == dialog['command']):
          understood = dialog['command']
      if (understood != False):
        if (understood == 'add another person'):
          os.system('cd app/assets/audios & "command as person name.mp3"')
          person_name = listener(houser)
          catcher(person_name)
        else:
          os.system('cd app/assets/audios & "' + understood + '.mp3"')
      else:
        os.system('cd app/assets/audios & "listening error.mp3"')
    except:
      pass

def listener(houser):
  with sr.Microphone() as source:
    print('----------Start----------')
    audio = houser.listen(source)
    print('----recording is over----')
    return '' + houser.recognize_google(audio)