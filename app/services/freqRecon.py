import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as matplot

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

