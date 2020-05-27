import speech_recognition as sr
import os

def __init__():
  pass

def listen():
  houser = sr.Recognizer()

  try:
    with sr.Microphone() as source:
      print('----------Start----------')
      audio = houser.listen(source)
      print('----recording is over----')

    speech = '' + houser.recognize_google(audio)
    print('Person said: ' + speech)
    return speech

  except:
      pass

def reply(audio):
  os.system('cd app/assets/audios & "' + audio + '.mp3"')

def voice_recon():
  pass