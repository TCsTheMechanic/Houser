from gtts import gTTS
import os

def voice(speech):
  tts = gTTS(text=speech, lang='en')
  tts.save('tmp/voice.mp3')

  os.system('cd tmp & voice.mp3')
  os.remove('tmp/voice.mp3')