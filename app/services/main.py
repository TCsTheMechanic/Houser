from app.services import frequency
from db.connection import connect
from app.services import system
import time

def __init__():
  pass

def start():
  dialog_collection = connect().Dialog

  while True:
    speech = system.listen_speech()
    understood = False

    for dialog in dialog_collection.find():
      if (speech == dialog['command']):
        understood = dialog['command']

    if (understood != False and speech is not None):
      if (understood == 'goodbye Houser'):
        system.reply(understood)
        break
      elif (understood == 'add another person'):
        system.reply(understood)
        time.sleep(2)
        person_name = system.listen_speech()
        frequency.catcher(person_name)
      else:
        system.reply(understood)