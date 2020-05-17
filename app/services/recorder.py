from db.connection import connect
from frequency import catcher
import speech_recognition as sr
import os

def __init__():
  pass

def listener():
  dialog_collection = connect().Dialog

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
      understood = False
      for dialog in dialog_collection.find():
        if (speech == dialog['command']):
          understood = dialog['command']
      if (understood != False):
        if (understood == 'add another person'):
          os.system('cd app/assets/audios & "command as person name.mp3"')
          person_name = ''
          catcher(person_name)
        else:
          os.system('cd app/assets/audios & "' + understood + '.mp3"')
      else:
        os.system('cd app/assets/audios & "listening error.mp3"')
    except:
      pass