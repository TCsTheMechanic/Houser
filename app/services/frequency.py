import numpy as np
import pyaudio
import struct

def __init__():
  pass

def catcher(user_name, database):
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

  for index in range(3):
    data_array = []
    data = stream.read(CHUNK)
    data_integer = struct.unpack(str(2 * CHUNK) + 'B', data)
    data_array << np.array(data_integer, dtype = 'b')[::2]
    database.Person.inser_one(
      {
        'name': user_name,
        'sample': index,
        'frequency': data_array
      }
    )