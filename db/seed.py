from db.connection import connect

def dialog_seeder():

  connect().Dialog.insert_many([
    {
      'command': 'hello Houser',
      'answer': 'how can I help you?'
    },
    {
      'command': 'can you turn on the bedroom light',
      'answer': 'alright, badroom light is on'
    },
    {
      'command': 'can you turn on the bathroom light',
      'answer': 'alright, bathroom light is on'
    },
    {
      'command': 'can you turn on the kitchen light',
      'answer': 'alright, kitchen light is on'
    },
    {
      'command': 'can you turn on the livingroom light',
      'answer': 'alright, livingroom light is on'
    },
    {
      'command': 'can you turn off the bedroom light',
      'answer': 'alright, badroom light is off'
    },
    {
      'command': 'can you turn off the bathroom light',
      'answer': 'alright, bathroom light is off'
    },
    {
      'command': 'can you turn off the kitchen light',
      'answer': 'alright, kitchen light is off'
    },
    {
      'command': 'can you turn off the livingroom light',
      'answer': 'alright, livingroom light is off'
    },
    {
      'command': 'goodbye Houser',
      'answer': 'goodbye'
    },
    {
      'command': 'add another person',
      'answer': "what's the person's name?"
    },
    {
      'command': 'who are you',
      'answer': "Hello, my name is Houser and I'm Eduardo Cerutti's final project, nice to meet you"
    },
    {
      'command': 'thank you',
      'answer': "you're welcome"
    },
    {
      'command': 'command say houser 3 times',
      'answer': 'alright, please, when I ask you will say hello Houser three times'
    },
    {
      'command': 'command ask frequency 0',
      'answer': 'say the first time please'
    },
    {
      'command': 'command ask frequency 1',
      'answer': 'the second'
    },
    {
      'command': 'command ask frequency 2',
      'answer': 'and the last one'
    },
    {
      'command': 'command nice to meet you',
      'answer': 'nice to meet you'
    },
    {
      'command': 'command thanks',
      'answer': 'thank you'
    },
    {
      'command': 'command listening error',
      'answer': "sorry, I couldn't understand, can you please repeat?"
    }
  ])