from db.connection import connect
from app.services.recorder import listener

listener(connect())