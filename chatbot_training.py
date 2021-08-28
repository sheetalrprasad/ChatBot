from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

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

directory = 'training_data'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        print('\n Chatbot training with '+os.path.join(directory, filename)+' file')
        training_data = open(os.path.join(directory, filename)).read().splitlines()
        trainer = ListTrainer(py_bot)
        trainer.train(training_data)
    else:
        continue

decision = input('Train chatbot with English corpus data? (Y/N): ')

if decision == 'Y':
    print('\n Chatbot training with English corpus data')

    trainer_corpus = ChatterBotCorpusTrainer(py_bot)
    trainer_corpus.train('chatterbot.corpus.english')
