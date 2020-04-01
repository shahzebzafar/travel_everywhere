import os
import re
import inspect
import tempfile
import traveleverywhere.models
from django.conf import settings
from django.test import TestCase
from traveleverywhere.models import Question, Blog, Answer, Airline, Agency, BookingWebsite, AirlineLike, AirlineDislike, AgencyLike, AgencyDislike, WebsiteLike, WebsiteDislike, BlogLike, Blog_Image, User_Profile
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.test import Client
from django.db import models
from django.forms import fields as django_fields
from traveleverywhere import forms
from django.forms import fields as django_fields



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

def create_super_user_object():
    """
    Helper function to create a super user (admin) account.
    """
    return User.objects.create_superuser('admin', 'admin@test.com', 'testpassword')

class UserProfileModelTests(TestCase):
    
    def test_user_profile_class_in_models(self):
        """
        Checks whether the User_Profile class exists in traveleverywhere models
        and if the attributes exist as we want them to.
        If we can't assign values to some of them, assertion fails.
        """
        self.assertTrue('User_Profile' in dir(traveleverywhere.models))
        user_profile = User_Profile()
        expected_attributes = {
            'user':add_user('test', 'test123'),
            'picture': tempfile.NamedTemporaryFile(suffix=".jpg").name,
            'about' : 'I come from Test file.'
        }
        expected_types = {
            'user': models.fields.related.OneToOneField,
            'picture':models.fields.files.ImageField,
            'about':models.fields.CharField,
        }
        count = 0
        for attr in user_profile._meta.fields:
            attr_name = attr.name
            for expected_attr_name in expected_attributes.keys():
                if expected_attr_name == attr_name:
                    count += 1
                    self.assertEqual(type(attr), expected_types[attr_name])
                    setattr(user_profile, attr_name, expected_attributes[attr_name])
        self.assertEqual(count, len(expected_attributes.keys()))
        user_profile.save()

    def test_model_admin_creation(self):
        """
        Checks for User_Profile interface instance.
        If we don't get Http 200, assume models have not been registered.
        """
        super_user = create_super_user_object()
        self.client.login(username='admin', password='testpassword')
        response = self.client.get('/admin/traveleverywhere/user_profile/')
        self.assertEqual(response.status_code, 200)

class UserUserProfileFormTests(TestCase):

    def test_user_form(self):
        """
        Checks if UserForm is in the correct place and has correct fields.
        """
        self.assertTrue('UserForm' in dir(forms))
        user_form = forms.UserForm()
        self.assertEqual(type(user_form.__dict__['instance']), User)
        fields = user_form.fields
        expected_fields = {
            'username': django_fields.CharField,
            'email': django_fields.EmailField,
            'password': django_fields.CharField,
        }
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys())
            self.assertEqual(expected_field, type(fields[expected_field_name]))

    def test_user_profile_form(self):
        """
        Checks if UserProfileForm is in the correct place and has correct fields.
        """
        self.assertTrue('UserProfileForm' in dir(forms))
        user_profile_form = forms.UserProfileForm()
        self.assertEqual(type(user_profile_form.__dict__['instance']), traveleverywhere.models.User_Profile)
        fields = user_profile_form.fields
        expected_fields = {
            'about':django_fields.CharField,
            'picture':django_fields.ImageField,
        }
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys())
            self.assertEqual(expected_field, type(fields[expected_field_name]))

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

def add_blog(title):
    blog = Blog.objects.get_or_create(title=title)[0]
    blog.save()
    return blog

def add_blog_like(blog, user):
    blog_like = BlogLike.objects.get_or_create(blog=blog, user=user)[0]
    blog_like.save()
    return blog_like

def add_blog_fully(title, body, bodySummary, location_country, location_city, location_place, user):
    blog = Blog.objects.get_or_create(title=title, body=body, bodySummary=bodySummary, location_country=location_country, location_city=location_city, location_place=location_place, user=user)[0]
    blog.save()
    return blog

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

class HomeViewTests(TestCase):

    def test_home_view_for_featured_blog(self):
        """
        Checks whether the featured blog is the one with most likes.
        """
        blog1 = add_blog("Trip to Japan")
        blog2 = add_blog("When in Rome")
        user1 = add_user('john', 'travel123')
        user2 = add_user('gregory', 'gr1234')
        blog1_like1 = add_blog_like(blog1, user1)
        blog1_like2 = add_blog_like(blog1, user2)

        response = self.client.get(reverse('traveleverywhere:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Trip to Japan')
        self.assertEquals(response.context['featured_blog_list'][0][0], blog1)

    def test_home_view_for_most_popular_questions(self):
        """
        Check whether the most popular questions on the home page are the three with most answers.
        """
        question1 = add_question("How to go to Japan?")
        question2 = add_question("When is the sunrise in Canada?")
        question3 = add_question("How far is Bulgaria from India?")
        question4 = add_question("How long would it take to go to Dundee from Glasgow?")
        add_answer("Have a look at TravelEverywhere's Travel page", question1)
        add_answer("By train from China.", question1)
        add_answer("Depends from where and when.", question1)
        add_answer("I have no idea.", question2)
        add_answer("At 3:30 pm", question2)
        add_answer("5000km", question3)
        most_popular_questions = [question3, question2, question1]

        response = self.client.get(reverse('traveleverywhere:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "How to go to Japan?")
        self.assertContains(response, "When is the sunrise in Canada?")
        self.assertContains(response, "How far is Bulgaria from India?")
        self.assertEquals(response.context['most_popular_questions'], most_popular_questions)

    def test_home_view_for_most_popular_destinations(self):
        """
        Check whether the most popular destinations are displayed on the home page.
        Those should be the cities or countries which appear in the blog titles most often.
        """
        add_blog("Trip to Japan")
        add_blog("When in Rome")
        add_blog("Venice - my dream")
        add_blog("Japan - the mistical country")

        response = self.client.get(reverse('traveleverywhere:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Japan")
        self.assertContains(response, "Rome")
        self.assertContains(response, "Venice")

class BlogViewTests(TestCase):

    def test_blog_view_shows_all_blog_titles(self):
        """
        Check whether blog titles are displayed on blog page correctly.
        """
        add_blog("Trip to Japan")
        add_blog("When in Rome")

        response = self.client.get(reverse('traveleverywhere:blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Trip to Japan")
        self.assertContains(response, "When in Rome")

    def test_blog_view_shows_body_summary(self):
        """
        Checks whether the body summary is displayed correctly on the blog page.
        """
        user1 = add_user('john', 'travel123')
        blog_info = {
        'title' : 'Glasgow – Former Murder Capital of Europe Today',
        'country' : 'UK',
        'city' : 'Glasgow',
        'place' : '',
        'body' : 'Not many people these days are aware of Glasgow’s infamous reputation as one of the most dangerous cities in the world where crime and violence were at an all-time high, gangs reigned supreme and knifing was a daily occurrence.\nFast forward to today and you’ll find that the city’s gone through a metamorphosis – putting much of its dark past behind it and becoming one of the more attractive places to live in the UK, provided of course you don’t linger around to seedier parts of the city after dark.\nSo what does this once-dangerous city offer to visitors? Quite a lot really. Divided into two halves by the River Clyde, Glasgow is a city with a blend of modern and classic Victorian architecture with many great spots for tourists to visit and enjoy.\nFor this little blog, I’ll focus mainly on the City Centre since that’s where you’ll spend a significant portion of your time. Fancy a shopping spree? There’s plenty of shopping centres and plazas with every possible store imaginable. Want a great dining experience? You’ll be hard pressed to not find a restaurant to suit your palate. Want to go on a romantic stroll with your significant other? An evening walk along the River Clyde is a breath-taking experience. Simply want a nice pint of the finest brew? We’ve got more pubs and bars than the number of people living here. Seriously, it feels like that sometimes.\nSo where to begin? You can start off by taking a train from where you’re staying to Glasgow Central. While a bus or a taxi are also good, I feel every visitor to Glasgow should visit the station at least once. There you’ll find yourself in the heart of the City Centre. Go north on Renfield Street for an amazing dining and theatre experience or west on Gordon Street and enter Buchanan Street for an excellent range of stores and the ever-popular Buchanan Galleries.\nYou can also south on Union Street and link up with Argyle Street which opens up even more avenue for you to explore. If you’re feeling lucky, you can visit one of the many casino’s which dot the City Centre and win big. But do try to not go broke since you still need to pay to go back home. Or if you’d rather just laze about and relax, there are many parks and gardens scattered around and anyone of them will fulfil your needs.\nMost importantly though, if you’re new to the UK and Glasgow is your first time ever in a British city, you have to indulge in a hot sausage roll at Greggs for they are divine and refusing to do so is akin to a crime against the crown. I’m not joking. We have special police to make sure you partake in such a divine delicacy. There’s a vegan option as well for those non-meat eating aliens among us.\nThat should cover the basics. If you have any questions, you can post them in the forum and I’ll do my best to answer them if you do your best and try to visit this reformed city that I’ve come to love.\n',
        }
        blog = add_blog_fully(blog_info['title'], blog_info['body'], blog_info['body'][:200] + "...", blog_info['country'], '', blog_info['city'], user1)
        
        response = self.client.get(reverse('traveleverywhere:blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Glasgow – Former Murder Capital of Europe Today')
        self.assertEquals(response.context['blogs'][0][1], blog.bodySummary)

class LoginViewTests(TestCase):

    def test_user_login_correctly(self):
        """
        Checks that when user is logged in, he is transferred to home page.
        """
        user1 = add_user('geri', '1234')
        client = Client()
        self.client.login(username = user1.username, password = '1234')
        response = self.client.post(reverse('traveleverywhere:home'), {'user_id':user1.id})
        self.assertEqual(response.status_code, 200)
    
def get_template(path_to_template):
    """
    Helper function to return the string representation of a template file.
    """
    f = open(path_to_template, 'r')
    template_str = ""
    for line in f:
        template_str = f"{template_str}{line}"
    f.close()
    return template_str

class SignupViewTests(TestCase):

    def test_signup_view_exists(self):
        """
        Checks if the signup view exists in the correct place.
        """
        url = ''
        try:
            url = reverse('traveleverywhere:signup')
        except:
            pass
        self.assertEqual(url, '/traveleverywhere/signup/')

    def test_signup_template(self):
        """
        Checks if the signup.html exists in he correct place and
        if it uses the template inheritance.
        """
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'traveleverywhere')
        template_path = os.path.join(template_base_path, 'signup.html')
        self.assertTrue(os.path.exists(template_path))
        template_str = get_template(template_path)
        title_pattern = r'{% block title_block %}(\s*|\n*)Sign Up - TravelEverywhere(\s*|\n*){% (endblock|endblock title_block) %}'
        self.assertTrue(re.search(title_pattern, template_str))

    def test_signup_get_response(self):
        """
        Checks the GET response of signup view.
        """
        request = self.client.get(reverse('traveleverywhere:signup'))
        content = request.content.decode('utf-8')
        self.assertTrue('<h1 class="text-center signup-title">Sign up for TravelEverywhere</h1>' in content)
        self.assertTrue('enctype="multipart/form-data"' in content)
        self.assertTrue('<button type="submit" class="btn btn-primary">Sign up</button>' in content)

    def test_form_creation(self):
        """
        Creates a UserProfileForm and UserForm and attempts to save them.
        Checks if we can login in with the details submited.
        """
        user_data = {'username': 'testuser', 'password': 'test123', 'email': 'test@test.com'}
        user_form = forms.UserForm(data=user_data)
        user_profile_data = {'about': 'I am a Test user.', 'picture': tempfile.NamedTemporaryFile(suffix=".jpg").name}
        user_profile_form = forms.UserProfileForm(data=user_profile_data)
        self.assertTrue(user_form.is_valid())
        self.assertTrue(user_profile_form.is_valid())
        user_object = user_form.save()
        user_object.set_password(user_data['password'])
        user_object.save()
        user_profile_object = user_profile_form.save(commit=False)
        user_profile_object.user = user_object
        user_profile_object.save()
        self.assertEqual(len(User.objects.all()), 1)
        self.assertEqual(len(User_Profile.objects.all()), 1)
        self.assertTrue(self.client.login(username='testuser', password='test123'))

    def test_signup_post_response(self):
        """
        Checks the POST response of the signp view.
        We should be able to log a user with the details.
        """
        post_data = {'username': 'webformuser', 'password': 'test123', 'email': 'test@test.com', 'about': 'I am a Test user.', 'picture': tempfile.NamedTemporaryFile(suffix=".jpg").name}
        request = self.client.post(reverse('traveleverywhere:signup'), post_data)
        content = request.content.decode('utf-8')
        self.assertTrue('<h1 class="text-center signup-title">Sign up for TravelEverywhere</h1>' in content)
        self.assertTrue('<h2>Thank you for signing up!</h2>' in content)
        self.assertTrue('Return to homepage.' in content)
        self.assertTrue(self.client.login(username='webformuser', password='test123'))



    








