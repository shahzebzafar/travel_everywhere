from django.test import TestCase
from traveleverywhere.models import Question, Blog, Answer, Airline, Agency, BookingWebsite, User, AirlineLike, AirlineDislike, AgencyLike, AgencyDislike, WebsiteLike, WebsiteDislike
from django.urls import reverse


class QuestionModelTests(TestCase):
    
    def test_question_slug_creation(self):
        """
        Checks to make sure when a question is created,
        an approriate slug is created as well.
        For example, "Slug should have dashes" should look like
        "slug-should-have-dashes".
        """
        question = Question(title="Slug should have dashes")
        question.save()

        self.assertEqual(question.slug, "slug-should-have-dashes")

class BlogModelTests(TestCase):

    def test_blog_slug_creation(self):
        """
        Checks to make sure when a blog is created,
        an approriate slug is created as well.
        For example, "Slug should have dashes" should look like
        "slug-should-have-dashes".
        """
        blog = Blog(title="Slug should have dashes")
        blog.save()

        self.assertEqual(blog.slug, "slug-should-have-dashes")

def add_question(title):
    question = Question.objects.get_or_create(title=title)[0]
    question.save()
    return question

def add_answer(text,question):
    answer = Answer.objects.get_or_create(text=text, question=question)[0]
    answer.save()
    return answer

class ForumViewTests(TestCase):

    def test_forum_view_with_no_questions(self):
        """ 
        If no questions exist, the appropriate message should be displayed.
        """ 
        response = self.client.get(reverse('traveleverywhere:forum'))
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 'There are no questions present.') 
        self.assertQuerysetEqual(response.context['questions'], [])
    
    def test_forum_view_with_questions(self):
        """
        Checks whether questions are displayed correctly when present.
        """
        add_question('How to travel to Ibiza?')
        add_question('When is the best time to go hikig to Ben Nevis?')

        response = self.client.get(reverse('traveleverywhere:forum'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'How to travel to Ibiza?')
        self.assertContains(response, 'When is the best time to go hikig to Ben Nevis?')
        num_questions = len(response.context['questions'])
        self.assertEquals(num_questions, 2)

    def test_forum_view_for_answers_number(self):
        """
        Checks whether the number of answers for each question are correctly displayed.
        """
        question = add_question('How to travel to Ibiza?')
        add_answer('You could go with WizzAir.', question)
        add_answer('Check in Skyscanner.', question)

        response = self.client.get(reverse('traveleverywhere:forum'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'How to travel to Ibiza?')
        self.assertEquals(response.context['questions'][0][1], 2)

def add_airline(name,link):
    airline = Airline.objects.get_or_create(name=name, link=link)[0]
    airline.save()
    return airline

def add_agency(name,link):
    agency = Agency.objects.get_or_create(name=name, link=link)[0]
    agency.save()
    return agency

def add_website(name,link):
    website = BookingWebsite.objects.get_or_create(name=name, link=link)[0]
    website.save()
    return website

def add_user(username, password):
    user = User.objects.get_or_create(username=username, password=password)[0]
    user.save()
    return user

def add_airline_like(airline, user):
    airline_like = AirlineLike.objects.get_or_create(airline=airline, user=user)[0]
    airline_like.save()
    return airline_like

def add_agency_like(agency, user):
    agency_like = AgencyLike.objects.get_or_create(agency=agency, user=user)[0]
    agency_like.save()
    return agency_like

def add_website_like(website, user):
    website_like = WebsiteLike.objects.get_or_create(website=website, user=user)[0]
    website_like.save()
    return website_like

def add_airline_dislike(airline, user):
    airline_dislike = AirlineDislike.objects.get_or_create(airline=airline, user=user)[0]
    airline_dislike.save()
    return airline_dislike

def add_agency_dislike(agency, user):
    agency_dislike = AgencyDislike.objects.get_or_create(agency=agency, user=user)[0]
    agency_dislike.save()
    return agency_dislike

def add_website_dislike(website, user):
    website_dislike = WebsiteDislike.objects.get_or_create(website=website, user=user)[0]
    website_dislike.save()
    return website_dislike



class TravelViewTests(TestCase):

    def test_travel_view_with_no_airlines(self):
        """
        Checks that if no airlines exist, the appropriate message is displayed.
        """
        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 'There are no airlines to show.') 
        self.assertQuerysetEqual(response.context['airlines'], [])

    def test_travel_view_with_no_agencies(self):
        """
        Checks that if no agencies exist, the appropriate message is displayed.
        """
        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 'There are no agencies to show.') 
        self.assertQuerysetEqual(response.context['agencies'], [])
    
    def test_travel_view_with_no_websites(self):
        """
        Checks that if no websites exist, the appropriate message is displayed.
        """
        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 'There are no websites to show.') 
        self.assertQuerysetEqual(response.context['websites'], [])

    def test_travel_view_with_airlines(self):
        """
        Checks whether airlines are displayed correctly when present.
        """
        add_airline('Ryanair', 'https://www.ryanair.com/')
        add_airline('EasyJet', 'https://www.easyjet.com/')

        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ryanair')
        self.assertContains(response, 'EasyJet')
        num_airlines = len(response.context['airlines'])
        self.assertEquals(num_airlines, 2)

    def test_travel_view_with_agencies(self):
        """
        Checks whether agencies are displayed correctly when present.
        """
        add_agency('LoveHolidays', 'https://www.loveholidays.com/')
        add_agency('FlightCenter', 'https://www.flightcentre.co.uk/')

        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LoveHolidays')
        self.assertContains(response, 'FlightCenter')
        num_agencies = len(response.context['agencies'])
        self.assertEquals(num_agencies, 2)

    def test_travel_view_with_websites(self):
        """
        Checks whether websites are displayed correctly when present.
        """
        add_website('Trivago', 'https://www.trivago.co.uk/')
        add_website('Expedia', 'https://www.expedia.co.uk/')

        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Trivago')
        self.assertContains(response, 'Expedia')
        num_websites = len(response.context['websites'])
        self.assertEquals(num_websites, 2)

    def test_travel_view_for_airline_rating_display(self):
        """
        Checks whether the rating is computed and displayed properly.
        """
        airline = add_airline('Ryanair', 'https://www.ryanair.com/')
        user1 = add_user('john', 'travel123')
        user2 = add_user('gregory', 'gr1234')
        user3 = add_user('zack','win56')
        user4 = add_user('amy', 'lovej')
        airline_like1 = add_airline_like(airline, user1)
        airline_like2 = add_airline_like(airline, user2)
        airline_like3 = add_airline_like(airline, user3)
        airline_dislike1 = add_airline_dislike(airline, user4)
        
        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ryanair')
        rating = response.context['airlines'][0][1]
        self.assertEquals(rating, 3.75)

    def test_travel_view_for_agency_rating_display(self):
        """
        Checks whether the rating is computed and displayed properly.
        """
        agency = add_agency('LoveHolidays', 'https://www.loveholidays.com/')
        user1 = add_user('john', 'travel123')
        user2 = add_user('gregory', 'gr1234')
        user3 = add_user('zack','win56')
        user4 = add_user('amy', 'lovej')
        agency_like1 = add_agency_like(agency, user1)
        agency_like2 = add_agency_like(agency, user2)
        agency_like3 = add_agency_like(agency, user3)
        agency_dislike1 = add_agency_dislike(agency, user4)
        
        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LoveHolidays')
        rating = response.context['agencies'][0][1]
        self.assertEquals(rating, 3.75)

    def test_travel_view_for_website_rating_display(self):
        """
        Checks whether the rating is computed and displayed properly.
        """
        website = add_website('Trivago', 'https://www.trivago.co.uk/')
        user1 = add_user('john', 'travel123')
        user2 = add_user('gregory', 'gr1234')
        user3 = add_user('zack','win56')
        user4 = add_user('amy', 'lovej')
        website_like1 = add_website_like(website, user1)
        website_like2 = add_website_like(website, user2)
        website_like3 = add_website_like(website, user3)
        website_dislike1 = add_website_dislike(website, user4)
        
        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Trivago')
        rating = response.context['websites'][0][1]
        self.assertEquals(rating, 3.75)

    def test_travel_view_sorted_airlines_by_rating(self):
        """
        Checks whether the airlines are sorted by rating in ascending order.
        """
        airline1 = add_airline('Ryanair', 'https://www.ryanair.com/')
        airline2 = add_airline('EasyJet', 'https://www.easyjet.com/')
        user1 = add_user('john', 'travel123')
        user2 = add_user('gregory', 'gr1234')
        user3 = add_user('zack','win56')
        user4 = add_user('amy', 'lovej')
        airline1_like1 = add_airline_like(airline1, user1)
        airline1_like2 = add_airline_like(airline1, user2)
        airline1_like3 = add_airline_like(airline1, user3)
        airline2_like1 = add_airline_like(airline2, user4)
        airline2_dislike1 = add_airline_dislike(airline2, user1)

        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ryanair')
        self.assertContains(response, 'EasyJet')
        self.assertTrue(response.context['airlines'][0][1] <= response.context['airlines'][1][1])

    def test_travel_view_sorted_agencies_by_rating(self):
        """
        Checks whether the agencies are sorted by rating in ascending order.
        """
        agency1 = add_agency('LoveHolidays', 'https://www.loveholidays.com/')
        agency2 = add_agency('FlightCenter', 'https://www.flightcentre.co.uk/')
        user1 = add_user('john', 'travel123')
        user2 = add_user('gregory', 'gr1234')
        user3 = add_user('zack','win56')
        user4 = add_user('amy', 'lovej')
        agency1_like1 = add_agency_like(agency1, user1)
        agency1_like2 = add_agency_like(agency1, user2)
        agency1_like3 = add_agency_like(agency1, user3)
        agency2_like1 = add_agency_like(agency2, user4)
        agency2_dislike1 = add_agency_dislike(agency2, user1)

        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LoveHolidays')
        self.assertContains(response, 'FlightCenter')
        self.assertTrue(response.context['agencies'][0][1] <= response.context['agencies'][1][1])

    def test_travel_view_sorted_websites_by_rating(self):
        """
        Checks whether the websites are sorted by rating in ascending order.
        """
        website1 = add_website('Trivago', 'https://www.trivago.co.uk/')
        website2 = add_website('Expedia', 'https://www.expedia.co.uk/')
        user1 = add_user('john', 'travel123')
        user2 = add_user('gregory', 'gr1234')
        user3 = add_user('zack','win56')
        user4 = add_user('amy', 'lovej')
        website1_like1 = add_website_like(website1, user1)
        website1_like2 = add_website_like(website1, user2)
        website1_like3 = add_website_like(website1, user3)
        website2_like1 = add_website_like(website2, user4)
        website2_dislike1 = add_website_dislike(website2, user1)

        response = self.client.get(reverse('traveleverywhere:travel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Trivago')
        self.assertContains(response, 'Expedia')
        self.assertTrue(response.context['websites'][0][1] <= response.context['websites'][1][1])

    








