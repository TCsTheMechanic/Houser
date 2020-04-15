def dialog_seeder(connect):

  connect.Dialog.insert_many([
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
  ])