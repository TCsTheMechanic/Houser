from pymongo import MongoClient

def connect():
  try:
    connect = MongoClient()
    print('Database Connected!!')
    return connect.Houser
  except:
    print('Database MIA!!')