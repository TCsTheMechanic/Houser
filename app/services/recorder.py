import speech_recognition as sr
import os

def listener(connect):
  dialog_collection = connect.Dialog

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
        if (speech == dialog['question']):
          understood = dialog['question']
      if (understood != False):
        os.system('cd app/assets/audios & "' + understood + '.mp3"')
      else:
        os.system('cd app/assets/audios & "listening error.mp3"')
    except:
      pass