from config.speechCreator import voice
from db.seed import dialog_seeder
from db.connection import connect

#dialog_seeder(connect())
voice(connect())