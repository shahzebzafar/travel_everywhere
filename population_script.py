import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_everywhere.settings')

import django
django.setup()
from traveleverywhere.models import Question, Answer, Blog, Airline, Agency, BookingWebsite

def populate():
    answers_q1 = [
        {'text' : 'I think the best place you could go in September depends on what you aim to do. Last year I went to Canarian islands and do not regret it but the year before that I was in Turkey and this was also a great experience'},
        {'text' : 'I would suggest you go somewhere popular because in September the tourists will not be that many.'},
    ]

    answers_q2 = [
        {'text': 'Right now the tickets to Iceland are really cheap so if I were you, I would go wathc them there.'},
    ]

    questions = {
        'Where is the best place to go in September?': {'answers': answers_q1,
        'body' : 'Hello, I am planning a big trip this autumn and would love to give me some advice on where.',
        'replies': 37},
        'Best place to see the Northen lights?': {'answers' : answers_q2,
        'body' : 'I want to ask fellow travellers where to go to see the Northern lights this year.',
        'replies' : 20},
    }

    for quest, quest_data in questions.items():
        q = add_question(quest, quest_data['body'], quest_data['replies'])
        for answ in quest_data['answers']:
            add_answer(q, answ['text'])

    for q in Question.objects.all():
        for a in Answer.objects.filter(question=q):
            print(f'- {q}: {a}')

def add_question(title,body, replies=0):
    q = Question.objects.get_or_create(title=title, body=body, replies=replies)[0]
    q.save()
    return q

def add_answer(quest, text):
    a = Answer.objects.get_or_create(question=quest, text=text)[0]
    a.save()
    return a

if __name__ == '__main__':
    print('Starting population script...')
    populate()
