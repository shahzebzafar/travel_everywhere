import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_everywhere.settings')

import django
django.setup()
from traveleverywhere.models import Question, Answer, Blog, Airline, Agency, BookingWebsite, User

def populate():
    answers_q1 = [
        {'text' : 'I think the best place you could go in September depends on what you aim to do. Last year I went to Canarian islands and do not regret it but the year before that I was in Turkey and this was also a great experience.'},
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

    airlines = [
        {'name': 'Ryanair', 'link' : 'https://www.ryanair.com/', 'rating' : 90},
        {'name':'EasyJet', 'link':'https://www.easyjet.com/', 'rating':80},
        {'name': 'Qatar', 'link':'https://www.qatarairways.com/', 'rating': 56},
        {'name': 'British Airways', 'link':'https://www.britishairways.com/', 'rating':40},
    ]

    agencies = [
        {'name': 'LoveHolidays', 'link' : 'https://www.loveholidays.com/', 'rating' : 55},
        {'name':'FlightCenter', 'link':'https://www.flightcentre.co.uk/', 'rating':46},
        {'name': 'AppleHouseTravel', 'link':'https://www.applehousetravel.co.uk/', 'rating': 40},
        {'name': 'Tui', 'link':'https://www.tui.co.uk/', 'rating':25},
    ]

    websites = [
        {'name': 'Trivago', 'link' : 'https://www.trivago.co.uk/', 'rating' : 60},
        {'name':'Expedia', 'link':'https://www.expedia.co.uk/', 'rating':49},
        {'name': 'Booking', 'link':'https://www.booking.com/', 'rating': 40},
        {'name': 'AirBnB', 'link':'https://www.airbnb.co.uk/', 'rating':36},
    ]

    for quest, quest_data in questions.items():
        q = add_question(quest, quest_data['body'], quest_data['replies'])
        for answ in quest_data['answers']:
            add_answer(q, answ['text'])
    
    for air in airlines:
        add_airline(air['name'],air['link'],air['rating'])

    for agency in agencies:
        add_agency(agency['name'],agency['link'],agency['rating'])

    for web in websites:
        add_website(web['name'],web['link'],web['rating'])

    for q in Question.objects.all():
        for a in Answer.objects.filter(question=q):
            print(f'- {q}: {a}')
    for air in Airline.objects.all():
        print(f'-{air}')
    for age in Agency.objects.all():
        print(f'-{age}')
    for web in BookingWebsite.objects.all():
        print(f'-{web}')
    

def add_question(title,body, replies=0):
    q = Question.objects.get_or_create(title=title, body=body, replies=replies)[0]
    q.save()
    return q

def add_answer(quest, text):
    a = Answer.objects.get_or_create(question=quest, text=text)[0]
    a.save()
    return a

def add_airline(name,link,rating=0):
    air=Airline.objects.get_or_create(name=name, link=link, rating=rating)[0]
    air.save()
    return air

def add_agency(name,link,rating=0):
    agency=Agency.objects.get_or_create(name=name, link=link, rating=rating)[0]
    agency.save()
    return agency

def add_website(name,link,rating=0):
    website=BookingWebsite.objects.get_or_create(name=name, link=link,rating=rating)[0]
    website.save()
    return website

if __name__ == '__main__':
    print('Starting population script...')
    populate()
