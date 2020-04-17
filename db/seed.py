def dialog_seeder(connect):

  connect.Dialog.insert_many([
    {
      'question': 'hello Houser',
      'answer': 'how can I help you?'
    },
    {
      'question': 'can you turn on the light',
      'answer': 'yes, please tell me the room'
    },
    {
      'question': 'goodbye Houser',
      'answer': 'goodbye'
    },
    {
      'question': 'introduction',
      'answer': "Hello, my name is Houser and I'm Eduardo Cerutti's final project, nice to meet you"
    },
    {
      'question': 'listening error',
      'answer': "sorry, I couldn't understand, can you please repeat?"
    }
  ])