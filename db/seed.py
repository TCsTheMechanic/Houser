from db.connection import connect

def __init__():
  pass

def dialog_seeder():

  connect().Dialog.insert_many([
    {
      'command': 'hello Houser',
      'answer': 'how can I help you?'
    },
    {
      'command': 'can you turn on the light',
      'answer': 'yes, please tell me the room'
    },
    {
      'command': 'goodbye Houser',
      'answer': 'goodbye'
    },
    {
      'command': 'add another person',
      'answer': 'alright, please, say hey houser three times'
    },
    {
      'command': 'who are you',
      'answer': "Hello, my name is Houser and I'm Eduardo Cerutti's final project, nice to meet you"
    },
    {
      'command': 'listening error',
      'answer': "sorry, I couldn't understand, can you please repeat?"
    }
  ])