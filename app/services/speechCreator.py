from gtts import gTTS
import os

def voice(text):
  # Cria o mp3 com o texto indicado
  tts = gTTS(text=text, lang="en")
  tts.save("voice.mp3")

  # Da o comando para o cmd executar o mp3
  os.system("cd assets/audios & voice.mp3")