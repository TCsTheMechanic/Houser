from gtts import gTTS
import os

# Cria o mp3 com o texto indicado
tts = gTTS(text="I'm fine, but I think you should make me think", lang="en")
tts.save("fineThink.mp3")

# Da o comando para o cmd executar o mp3
os.system("fineThink.mp3")