import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as matplot

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

while True:
  data = stream.read(CHUNK)
  data_integer = struct.unpack(str(2 * CHUNK) + 'B', data)
  data_array = np.array(data_integer, dtype = 'b')[::2]
  print(data_array)