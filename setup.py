from config.voice_creator import voice
from db.seed import dialog_seeder
import os 

if (os.path.isdir('app/assets') == False):
  os.makedirs('app/assets/audios')

dialog_seeder()
voice()