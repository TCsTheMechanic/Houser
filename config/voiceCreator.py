from gtts import gTTS
import os

def voice(connect):
  dialog_collection = connect.Dialog

  for dialog in dialog_collection.find():
    if (os.path.isfile('app/assets/audios/' + dialog['question'] + '.mp3') == False):
      tts = gTTS(text=dialog['answer'], lang='en')
      # I chose to name the audio by question bc question never have special char
      tts.save('app/assets/audios/' + dialog['question'] + '.mp3')