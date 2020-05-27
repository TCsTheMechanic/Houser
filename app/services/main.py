from app.services.frequency import catcher
from db.connection import connect
from app.services import system

def __init__():
  pass

def start():
  dialog_collection = connect().Dialog

  while True:
    speech = system.listen()
    understood = False

    for dialog in dialog_collection.find():
      if (speech == dialog['command']):
        understood = dialog['command']

    if (understood != False):
      if (understood == 'goodbye Houser'):
        system.reply(understood)
        break
      elif (understood == 'add another person'):
        system.reply(understood)
        person_name = system.listen()
        catcher(person_name)
      else:
        system.reply(understood)

    if (speech != '' and understood != True):
      system.reply('command listening error')