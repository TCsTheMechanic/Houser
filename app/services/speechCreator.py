from gtts import gTTS
import os

def voice(speech):
  # Cria o mp3 com o texto indicado
  tts = gTTS(text=speech, lang='en')
  tts.save('assets/audios/voice.mp3')

  # Da o comando para o cmd executar o mp3
  os.system('cd assets/audios & voice.mp3')