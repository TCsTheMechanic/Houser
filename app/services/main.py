from app.services.frequency import catcher
from db.connection import connect
from app.services import system

def __init__():
  pass

def start():
  dialog_collection = connect().Dialog

  while True:
    speech = system.listen
    understood = False

    if (speech == 'goodbye Houser'):
      system.reply('goodbye Houser')
      break

    for dialog in dialog_collection.find():
      if (speech == dialog['command']):
        understood = dialog['command']

    if (understood != False):
      if (understood == 'add another person'):
        system.reply('command ask person name')
        person_name = system.listen()
        catcher(person_name)
      else:
        system.reply(understood)

    if (speech != '' and understood != True):
      system.reply('listening error')