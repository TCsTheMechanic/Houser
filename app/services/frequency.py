from app.services.system import reply
from db.connection import connect
import numpy as np
import pyaudio
import struct

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

  for index in range(3):
    reply('command ask frequency ' + index)
    
    data_array = []
    print('----------Start----------')
    data = stream.read(CHUNK)
    print('----recording is over----')

    data_integer = struct.unpack(str(2 * CHUNK) + 'B', data)
    data_array << np.array(data_integer, dtype = 'b')[::2]
    person_collection.inser_one(
      {
        'name': user_name,
        'sample': index,
        'frequency': data_array
      }
    )

  reply('command nice to meet you')