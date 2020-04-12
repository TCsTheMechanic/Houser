from connection import connect

db = connect()

collection = db.Dialog

documents = [
  {
    'question': 'hey houser',
    'answer': 'how can I help you?'
  },
  {
    'question': 'can you turn on the light?',
    'answer': 'yes, please tell me the room'
  },
  {
    'question': 'goodbye Houser',
    'answer': 'goodbye'
  }
]

collection.insert_many(documents)