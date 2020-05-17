from db.connection import connect
import numpy as np
import pyaudio
import struct
import os

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

  os.system('cd app/assets/audios & "add another person.mp3"')

  for index in range(3):
    os.system('cd app/assets/audios & "ask frequency ' + index + '.mp3"')
    data_array = []
    data = stream.read(CHUNK)
    data_integer = struct.unpack(str(2 * CHUNK) + 'B', data)
    data_array << np.array(data_integer, dtype = 'b')[::2]
    person_collection.inser_one(
      {
        'name': user_name,
        'sample': index,
        'frequency': data_array
      }
    )

  os.system('cd app/assets/audios & "command nice to meet you.mp3"'')