from db.connection import connect
import speech_recognition as sr
import numpy as np
import pyaudio
import struct
import time
import os

def listen_speech():
  houser = sr.Recognizer()

  try:
    with sr.Microphone() as source:
      print('----------Start----------')
      audio = houser.listen(source)
      print('----recording is over----')

    speech = '' + houser.recognize_google(audio)
    print('Person said: ' + speech)
    return speech

  except:
    pass

def listen_frequency(timeout):
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

  record_timeout = time.time() + timeout
  frequency_list = []

  print('----------Start----------')

  while (time.time() < record_timeout):
    frequency = stream.read(CHUNK)
    frequency_list.extend(struct.unpack(str(2 * CHUNK) + 'B', frequency))

  print('----recording is over----')

  return frequency_list

def reply(audio):
  os.system('cd app/assets/audios & "' + audio + '.mp3"')

def voice_recon():
  pass