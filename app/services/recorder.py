import os
import speech_recognition as sr

def listener(connect, voice):
  database = connect
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
      for dialog in dialog_collection.find():
        if(speech == dialog['question']):
          voice(dialog['answer'])
        else:
          voice("sorry, I couldn't understand, can you please repeat?")
    except:
      pass