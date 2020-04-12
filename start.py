from db.connection import connect
from app.services.recorder import listener
from app.services.speechCreator import voice

listener(connect(), voice)