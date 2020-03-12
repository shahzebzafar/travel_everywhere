import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from traveleverywhere.models import Question, Answer

def populate():
    questions = [
        {'title' : 'Where is the best place to go in September?',
        'body' : 'Hello, I am planning a big trip this autumn and would love to give me some advice on where.',
        'replies': 37},
        {'title' : 'Best place to see the Northen lights?',
        'body' : 'I want to ask fellow travellers where to go to see the Northern lights this year.',
        'replies' : 20},
    ]

def add_question(title,body, replies=0):
    q = Question.get_or_create(title=title)[0]
    q.body = body
    q.replies = replies
    q.save()
    return q

def add_answer(quest, text):
    a = Answer.get_or_create(question=quest)[0]
    a.text = text
    a.save()
    return a

if __name__ == '__main__':
    print('Starting population script...')
    populate()
