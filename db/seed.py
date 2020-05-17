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
      'answer': 'alright, please, when I ask you will say hey houser three times'
    },
    {
      'command': 'who are you',
      'answer': "Hello, my name is Houser and I'm Eduardo Cerutti's final project, nice to meet you"
    },
    {
      'command': 'ask frequency 1',
      'answer': 'say the first time please'
    },
    {
      'command': 'ask frequency 2',
      'answer': 'the second'
    },
    {
      'command': 'ask frequency 3',
      'answer': 'and the last one'
    },
    {
      'command': 'thank you',
      'answer': "you're welcome"
    },
    {
      'command': 'command nice to meet you',
      'answer': 'nice to meet you'
    },
    {
      'command': 'command ask person name',
      'answer': "what's the person's name?"
    },
    {
      'command': 'command thanks',
      'answer': 'thank you'
    },
    {
      'command': 'listening error',
      'answer': "sorry, I couldn't understand, can you please repeat?"
    }
  ])