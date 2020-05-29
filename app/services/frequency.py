from app.services.system import reply
from db.connection import connect
import pyaudio
import struct
import time

def __init__():
  pass

def catcher(user_name):
  person_collection = connect().Person

  CHUNK = 2048

  houser = pyaudio.PyAudio()

  stream = houser.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
  )

  reply('command say houser 3 times')
  time.sleep(5)

  for index in range(3):
    reply('command ask frequency ' + str(index))
    time.sleep(1)

    record_timeout = time.time() + 3

    print('----------Start----------')

    while (time.time() < record_timeout):
      data = stream.read(CHUNK)
      data_list = struct.unpack(str(2 * CHUNK) + 'B', data)

    print('----recording is over----')

    person_collection.insert_one(
      {
        'sample': index,
        'name': user_name,
        'frequency': data_list
      }
    )

  reply('command nice to meet you')