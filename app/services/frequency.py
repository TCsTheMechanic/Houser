from app.services import system
from db.connection import connect
import time

def __init__():
  pass

def catcher(user_name):
  person_collection = connect().Person

  system.reply('command say houser 3 times')
  time.sleep(5)

  for index in range(3):
    system.reply('command ask frequency ' + str(index))
    time.sleep(1)

    timeout = 3
    data_list = system.listen_frequency(timeout)

    person_collection.insert_one(
      {
        'sample': index,
        'name': user_name,
        'frequency': data_list
      }
    )

  system.reply('command nice to meet you')