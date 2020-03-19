from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse 
from django.urls import reverse 
from django.shortcuts import redirect
from traveleverywhere.forms import UserForm, UserProfileForm, QuestionForm, AnswerForm, BlogForm, BlogImageForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from traveleverywhere.models import Question, Answer, Airline, Agency, BookingWebsite, Blog, Blog_Image
from django.forms import modelformset_factory
from django.contrib import messages



def home(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'traveleverywhere/home.html', context=context_dict)
    return response

@login_required
def blogs(request):
    BlogImages = modelformset_factory
    context_dict = {}
    return render(request, 'traveleverywhere/blogs.html', context=context_dict)

def forum(request):
    question_list = Question.objects.all()
    context_dict = {}
    quest_answ_count = []
    for question in question_list:
        answers = Answer.objects.filter(question=question).count()
        quest_answ_count.append((question,answers))
    context_dict['questions'] = quest_answ_count
    return render(request, 'traveleverywhere/forum.html', context=context_dict)

def show_question(request, question_name_slug):
    context_dict = {}
    try:
        question = Question.objects.get(slug=question_name_slug)
        answers = Answer.objects.filter(question=question)
        context_dict['answers'] = answers
        context_dict['question'] = question
    except Question.DoesNotExist:
        context_dict['answers'] = None
        context_dict['question'] = None
    return render(request, 'traveleverywhere/question.html', context=context_dict)

@login_required
def add_question(request):
    form = QuestionForm()
    if request.method=='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/traveleverywhere/forum/')
        else:
            print(form.errors)
    return render(request, 'traveleverywhere/add_question.html', {'form':form})

@login_required
def add_answer(request, question_name_slug):
    try:
        question = Question.objects.get(slug=question_name_slug)
    except Question.DoesNotExist:
        question = None
    if question is None:
        return redirect('/traveleverywhere/forum/')
    form = AnswerForm()
    if request.method=='POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            if question:
                answer = form.save(commit=False)
                answer.question = question
                answer.save()
                return redirect(reverse('traveleverywhere:show_question', kwargs={'question_name_slug':question_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form' : form, 'question' : question}
    return render(request, 'traveleverywhere/add_answer.html', context=context_dict)

def travel(request):
    context_dict = {}
    airline_list = Airline.objects.order_by('-rating')[:10]
    agency_list = Agency.objects.order_by('-rating')[:10]
    website_list = BookingWebsite.objects.order_by('-rating')[:10]
    context_dict['airlines'] = airline_list
    context_dict['agencies'] = agency_list
    context_dict['websites'] = website_list
    return render(request, 'traveleverywhere/travel.html', context=context_dict)
	
def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('traveleverywhere:home'))
            else:
                return HttpResponse("Your TravelEverywhere account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'traveleverywhere/login.html')

def signup(request):
    registered = False
    if request.method=='POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'traveleverywhere/signup.html', context={'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('traveleverywhere:home'))


def get_server_side_cookie(request, cookie, default_val=None): 
    val = request.session.get(cookie) 
    if not val: 
        val = default_val 
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits


	