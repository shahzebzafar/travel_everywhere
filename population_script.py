import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_everywhere.settings')

import django
django.setup()
from traveleverywhere.models import Question, Answer, Blog, Airline, Agency, BookingWebsite, User_Profile
from django.contrib.auth.models import User

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
        'body' : 'Hello, I am planning a big trip this autumn and would love to give me some advice on where.'},
        'Best place to see the Northen lights?': {'answers' : answers_q2,
        'body' : 'I want to ask fellow travellers where to go to see the Northern lights this year.'},
    }
    
    blog1 = {
        'title' : 'Mini Vacation At Dubai International Airport',
        'country' : 'UAE',
        'city' : 'Dubai',
        'place' : 'Dubai International Airport',
        'body': 'Picture this: You have a connecting flight from the UK to the other side of the world. You’re traveling via Emirates and have just gotten through a long 8+ hour flight and the hassle of going through security before you’re finally allowed to roam the behemoth that is Dubai International Airport while waiting for your next flight.\nNow normally, this would only be 2 or 3 hour affair max. You go in; check the timing of your next flight; find a nice place to sit down at; grab a coffee or a sandwich or both; and pass the time listening to that new audio book you purchased. Life’s good.\nBut what if it wasn’t a 2-3 hour wait and was instead a whopping 10 hour stay at the airport? Well then it’s time for your dream getaway at an airport.\nThe experience at Dubai international can wary depending on which terminal you get stuck at. If you’re at terminal 1 or 2 – you’re in luck. You’ll have a wide range of restaurants, fast food joints, and bars to eat at along with the massive duty free. If you’re the poor shmuck at terminal 3 like I was, you’ll have the choice between Costa, Costa, Costa and the one McDonald’s tucked away in a far, remote corner of the terminal.\nIt wasn’t all too bad, minus the excruciatingly long walk to McDonald’s for a decent meal – oh the irony. There was also a bar where I was able to have a pint while watching some live sports. Here I mingled with some of my fellow travellers. We swapped stories, made friendly wagers on the game, and generally had a good time.\nThough even after all of that, I had plenty of time to kill so I shopped around the duty free for small gifts and trinkets for my friends and family back home. It was incredibly overpriced mind you, but there was a little something for everyone so an hour later I was laden with bags and my wallet was painfully light. They’d better appreciate what I got for them, I thought venomously at the time.\nIt was only then that I realised my folly. I was beginning to get tired and since there were still a few hours until my flight, I wished to take a short power nap. But, I was now carrying around quite a few valuables which could easily be stolen at such a busy airport whilst catching some shuteye and I was not about to pay an exorbitant amount of money just to gain access to the VIP lounge for a few hours.\nAs luck would have it, there were about a dozen or so Costas around me so I went to one and drank a couple of lattes to keep myself awake and energized. I never felt so disgusted in my life.\nMy flight could not depart any sooner and once I was safely aboard the plane, I thought to myself:\n“Next time I’m flying with Etihad.”\n',
    }

    blog2 = {
        'title' : 'Glasgow – Former Murder Capital of Europe Today',
        'country' : 'UK',
        'city' : 'Glasgow',
        'place' : '',
        'body' : 'Not many people these days are aware of Glasgow’s infamous reputation as one of the most dangerous cities in the world where crime and violence were at an all-time high, gangs reigned supreme and knifing was a daily occurrence.\nFast forward to today and you’ll find that the city’s gone through a metamorphosis – putting much of its dark past behind it and becoming one of the more attractive places to live in the UK, provided of course you don’t linger around to seedier parts of the city after dark.\nSo what does this once-dangerous city offer to visitors? Quite a lot really. Divided into two halves by the River Clyde, Glasgow is a city with a blend of modern and classic Victorian architecture with many great spots for tourists to visit and enjoy.\nFor this little blog, I’ll focus mainly on the City Centre since that’s where you’ll spend a significant portion of your time. Fancy a shopping spree? There’s plenty of shopping centres and plazas with every possible store imaginable. Want a great dining experience? You’ll be hard pressed to not find a restaurant to suit your palate. Want to go on a romantic stroll with your significant other? An evening walk along the River Clyde is a breath-taking experience. Simply want a nice pint of the finest brew? We’ve got more pubs and bars than the number of people living here. Seriously, it feels like that sometimes.\nSo where to begin? You can start off by taking a train from where you’re staying to Glasgow Central. While a bus or a taxi are also good, I feel every visitor to Glasgow should visit the station at least once. There you’ll find yourself in the heart of the City Centre. Go north on Renfield Street for an amazing dining and theatre experience or west on Gordon Street and enter Buchanan Street for an excellent range of stores and the ever-popular Buchanan Galleries.\nYou can also south on Union Street and link up with Argyle Street which opens up even more avenue for you to explore. If you’re feeling lucky, you can visit one of the many casino’s which dot the City Centre and win big. But do try to not go broke since you still need to pay to go back home. Or if you’d rather just laze about and relax, there are many parks and gardens scattered around and anyone of them will fulfil your needs.\nMost importantly though, if you’re new to the UK and Glasgow is your first time ever in a British city, you have to indulge in a hot sausage roll at Greggs for they are divine and refusing to do so is akin to a crime against the crown. I’m not joking. We have special police to make sure you partake in such a divine delicacy. There’s a vegan option as well for those non-meat eating aliens among us.\nThat should cover the basics. If you have any questions, you can post them in the forum and I’ll do my best to answer them if you do your best and try to visit this reformed city that I’ve come to love.\n',
    }

    blog3 = {
        'title' : 'Cycling in the Ardennes',
        'country' : 'France',
        'city' : '',
        'place' : 'Ardennes',
        'body' : 'La Meuse is a winding river which meanders its way through the French Ardennes and on into Belgium. It’s a haven for cyclists, especially if you enjoy cycling on the flat. A cycle path follows the Meuse for over 50 kms with incredibly scenic views on either side of the river where hills descend sometimes gently and sometimes steeply down to the river. There is also a railway which follows the route from Charleville-Mezieres to Givet near the Belgium border so it is possible to put your cycle on the train and cycle back.\nThe other advantage is that the French Ardennes are not too far from Calais and one can drive there in 3-4 hours. If you want to explore just a little further afield then Reims and the Champagne district are not much further. La Meuse is easily accessible and very scenic too, approached through dense rolling forests that seem to go on for miles. A brochure advertises the Ardennes as a place to ‘changez de rythme, adoptez la slow attitude’ with massive forests, deep rivers and exceptional panoramas. A good description.\nThe Lac des Vielles Forges is a beautiful site to stay at, with walks by the lake where the early morning mists descend. In early September temperatures can be quite chilly first thing in the morning. In the town of Fumay it’s a lovely ride by the Meuse with a stop at the nearby village of Haybes where the small mairie is decked with flowers and has a lovely fountain. On the corner is a café and just along the road a boulangerie. Sitting in the sun in the small square with coffee and croissants provides one of those very French, special moments.\nNot far away is the unusual small fortress town of Rocroy, ‘ville etoile’ as roads and fortifications spread outwards from the centre forming the shape of a five pointed star. Begun in 1555, the ramparts were rebuilt in 1691 by Sébastien Le Prestre de Vauban, Louis XIV’s military engineer. The duc d’Enghien (later called the Great Condé) defeated the Spaniards near Rocroi in 1643. There are easy walks round the outskirts of the town along the fortifications with good views.\nThere are many villages along the Meuse worth a visit. Montherme is very pretty and a scenic cycling expedition is possible along a river leading off the Meuse called Le Semoy. Climb the steep hill behind Montherme (not for the faint hearted by bike) to visit la Roche la Tor, a collection of high rocks with scenic views over the countryside. There are other good vantage points above Bogny-sur- Meuse where a statue of the Knight Dardennor guards the valley from Roc du hermitage. It stands on the edge of a rock, looking out to the monument of the Four Aymon Brothers across the river Meuse. On his shield is a depiction of a boar’s head, the boar is the symbol of the Ardennes. The name ‘Dardennor’ is derived from ‘d’Ardenne’.\nYou’re unlikely to cross hordes of tourists in this area, which is scarcely known to the British. Belgian and Dutch visitors were more evident.\nCharleville-Mezieres is the main town on the Meuse and well worth visiting. It has a notable square called La Place Ducale which is known as the twin sister to the Place des Vosges in Paris with similar impressive colonnades surrounding the square.\nThis quiet unspoilt area of France is perfect for nature lovers has plenty of history and culture and is easily accessible from the UK.\n',
    }    
        
    airlines = [
        {'name': 'Ryanair', 'link' : 'https://www.ryanair.com/'},
        {'name':'EasyJet', 'link':'https://www.easyjet.com/'},
        {'name': 'Qatar', 'link':'https://www.qatarairways.com/'},
        {'name': 'British Airways', 'link':'https://www.britishairways.com/'},
        {'name': 'Jet2', 'link':'https://www.jet2.com/'},
        {'name': 'KLM', 'link':'https://www.klm.com/'},
        {'name':'Lufthansa', 'link':'https://www.lufthansa.com/'},
        {'name': 'Virgin Atlantic', 'link':'https://www.virginatlantic.com/'},
        {'name': 'Turkish Airline', 'link':'https://www.turkishairlines.com/'},
        {'name':'Wizzair', 'link':'https://wizzair.com/'},
    ]

    agencies = [
        {'name': 'LoveHolidays', 'link' : 'https://www.loveholidays.com/'},
        {'name':'FlightCenter', 'link':'https://www.flightcentre.co.uk/'},
        {'name': 'AppleHouseTravel', 'link':'https://www.applehousetravel.co.uk/'},
        {'name': 'Tui', 'link':'https://www.tui.co.uk/'},
        {'name':'Kayak', 'link':'https://www.kayak.co.uk/'},
        {'name':'Dream World Travel', 'link':'https://dreamworldtravel.co.uk/'},
        {'name':'BookIt', 'link':'https://bookit.com/'},
        {'name':'HotelPlanner','link':'https://www.hotelplanner.com/'},
        {'name':'CheapOAir', 'link':'https://www.cheapoair.com/'},
        {'name':'Global Work And Trave', 'link':'https://globalworkandtravel.com/'},
    ]

    websites = [
        {'name': 'Trivago', 'link' : 'https://www.trivago.co.uk/'},
        {'name':'Expedia', 'link':'https://www.expedia.co.uk/'},
        {'name': 'Booking', 'link':'https://www.booking.com/'},
        {'name': 'AirBnB', 'link':'https://www.airbnb.co.uk/'},
        {'name':'Hotels.com', 'link':'https://uk.hotels.com/'},
        {'name':'Tripadvisor', 'link':'https://www.tripadvisor.co.uk/'},
        {'name':'Pricelne', 'link':'https://www.priceline.com/'},
        {'name':'OrbitZ', 'link':'https://www.orbitz.com/'},
        {'name':'Hotwire', 'link':'https://www.hotwire.com/'},
        {'name':'Agoda', 'link':'https://www.agoda.com/'},
    ]

    user1 = add_user('zdravko','travel123')
    user2 = add_user('john', 'winner')
    user3 = add_user('paul', 'hello123')
    
    
    for quest, quest_data in questions.items():
        q = add_question(quest, quest_data['body'],user1)
        for answ in quest_data['answers']:
            add_answer(q, answ['text'],user2)
    
    for air in airlines:
        add_airline(air['name'],air['link'])

    for agency in agencies:
        add_agency(agency['name'],agency['link'])

    for web in websites:
        add_website(web['name'],web['link'])

    for q in Question.objects.all():
        for a in Answer.objects.filter(question=q):
            print(f'- {q}: {a}')
    for air in Airline.objects.all():
        print(f'-{air}')
    for age in Agency.objects.all():
        print(f'-{age}')
    for web in BookingWebsite.objects.all():
        print(f'-{web}')
    
    add_blog(blog1['title'], blog1['body'], blog1['body'][:200] + "...", blog1['country'], blog1['city'], blog1['place'], user1)
    add_blog(blog2['title'], blog2['body'], blog2['body'][:200] + "...", blog2['country'], blog2['city'], blog2['place'], user2)
    add_blog(blog3['title'], blog3['body'], blog3['body'][:200] + "...", blog3['country'], blog3['city'], blog3['place'], user3)
    
def add_user(username, password):
    user = User.objects.get_or_create(username=username, password=password)[0]
    user.save()
    return user

def add_question(title,body,user):
    q = Question.objects.get_or_create(title=title, body=body)[0]
    q.user = user
    q.save()
    return q

def add_answer(quest, text, user):
    a = Answer.objects.get_or_create(question=quest, text=text)[0]
    a.user = user
    a.save()
    return a

def add_airline(name,link):
    air=Airline.objects.get_or_create(name=name, link=link)[0]
    air.save()
    return air

def add_agency(name,link):
    agency=Agency.objects.get_or_create(name=name, link=link)[0]
    agency.save()
    return agency

def add_website(name,link):
    website=BookingWebsite.objects.get_or_create(name=name, link=link)[0]
    website.save()
    return website
    
def add_blog(title, body, bodySummary, location_country, location_city, location_place, user):
    b = Blog.objects.get_or_create(title=title, body=body, bodySummary = bodySummary, location_country=location_country, location_city=location_city, location_place=location_place)[0]
    b.user = user
    b.save
    return b

if __name__ == '__main__':
    print('Starting population script...')
    populate()
