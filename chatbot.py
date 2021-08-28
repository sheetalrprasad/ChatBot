from chatterbot import ChatBot

py_bot = ChatBot(name='PyBuddy', readOnly=True,
                    logic_adapter=[{
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'I am unable to understand your query. Please try to Google this.',
                        'maximum_similarity_threshold':0.90

                    }],
                    preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html',
                        'chatterbot.preprocessors.convert_to_ascii']
                )
name = input('Enter Your Name: ')
print ('Welcome to PyBot Service! Let me know how can I help you')

while True:

    request = input(name+': ')

    if request=="Bye" or request=='bye':
        print('Bot: Bye!!!')
        break
    else:
        response=py_bot.get_response(request)
        print('Bot: ', response)