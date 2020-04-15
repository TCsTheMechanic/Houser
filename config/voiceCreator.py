from gtts import gTTS
import os

def voice(connect):
  dialog_collection = connect.Dialog

  for dialog in dialog_collection.find():
    tts = gTTS(text=dialog['answer'], lang='en')
    tts.save('app/assets/audios/' + dialog['answer'] + '.mp3')