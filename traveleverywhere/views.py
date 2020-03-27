from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse 
from django.urls import reverse 
from django.shortcuts import redirect
from traveleverywhere.forms import UserForm, UserProfileForm, QuestionForm, AnswerForm, BlogForm, BlogImageForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from traveleverywhere.models import Question, Answer, Airline, Agency, BookingWebsite, Blog, Blog_Image, User_Profile
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.utils.decorators import method_decorator


def home(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'traveleverywhere/home.html', context=context_dict)
    return response

@login_required
def add_blog(request):
    form = BlogForm()
    if request.method=='POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.bodySummary = blog.body[:200]
            # blog.publish_date = datetime.datetime.now()
            blog.save()
            return redirect('/traveleverywhere/blogs/')
        else:
            print(form.errors)
    return render(request, 'traveleverywhere/add_blog.html', {'form':form})
    # BlogImages = modelformset_factory(Blog_Image, form = BlogImageForm, extra = 10)
    # if request.method == 'POST':
    #     blog_form = BlogForm(request.POST)
    #     images_set = BlogImages(request.POST, request.FILES, queryset = Blog_Image.objects.none())
    #     if blog_form.is_valid() and images_set.is_valid():
    #         blog = blog_form.save(commit = False)
    #         blog.user = request.user
    #         blog.bodySummary = blog.body[:200]
    #         blog.save()
    #         for im in images_set.cleaned_data:
    #             if im:
    #                 image = im['image']
    #                 picture = Blog_Image(add_blog = blog, image = image)
    #                 picture.save()
    #         return redirect(reverse('traveleverywhere:blogs', kwargs={'category_name_slug': category_name_slug}))
    #     else:
    #         print(blog_form.errors, images_set.errors)
    # else:
    #     blog_form = BlogForm()
    #     images_set = BlogImages(queryset = Blog_Image.objects.none())
    #     context_dict['blog'] = blog_form
    #     context_dict['images'] = images_set
    #     return render(request, 'traveleverywhere/add_blog.html', context=context_dict)

@login_required
def add_image(request, blog_name_slug):
    try:
        blog = Blog.objects.get(slug=blog_name_slug)
    except Blog.DoesNotExist:
        blog = None
    if blog is None:
        return redirect('/traveleverywhere/blogs/')
    form = BlogImageForm()
    if request.method=='POST':
        form = BlogImageForm(request.POST, request.FILES)
        if form.is_valid():
            if blog:
                image = form.save(commit=False)
                image.blog = blog
                image.save()
                return redirect(reverse('traveleverywhere:show_blog', kwargs={'blog_name_slug':blog_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form' : form, 'blog' : blog}
    return render(request, 'traveleverywhere/add_image.html', context=context_dict)
        
def blogs(request):
    blogs_list = Blog.objects.all()
    context_dict = {}
    blogs = []
    for blog in blogs_list:
        blogSummary = blog.bodySummary
        blogs.append((blog, blogSummary))
    context_dict['blogs'] = blogs
    return render(request, 'traveleverywhere/blogs.html', context = context_dict)

def show_blog(request, blog_name_slug):
    context_dict = {}
    try:
        blog = Blog.objects.get(slug = blog_name_slug)
        images = Blog_Image.objects.filter(blog = blog)
        context_dict['blog'] = blog
        context_dict['images'] = images
    except Blog.DoesNotExist:
        context_dict['blog'] = None
        context_dict['images'] = None
    return render(request, 'traveleverywhere/show_blog.html', context = context_dict)
    

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
            question = form.save(commit=False)
            question.user = request.user
            question.save()
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
                answer.user = request.user
                answer.save()
                return redirect(reverse('traveleverywhere:show_question', kwargs={'question_name_slug':question_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form' : form, 'question' : question}
    return render(request, 'traveleverywhere/add_answer.html', context=context_dict)

def travel(request):
    context_dict = {}
    airline_list = Airline.objects.all()
    agency_list = Agency.objects.all()
    website_list = BookingWebsite.objects.all()
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

class MyAccountView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        user_profile = User_Profile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'about':user_profile.about, 'picture':user_profile.picture})
        return (user, user_profile, form)
    
    @method_decorator(login_required) 
    def get(self, request, username): 
        try: 
            (user, user_profile, form) = self.get_user_details(username) 
        except TypeError: 
            return redirect(reverse('traveleverywhere:home'))
        context_dict = {'user_profile': user_profile, 'selected_user': user, 'form': form}
        return render(request, 'traveleverywhere/my_account.html', context_dict)

    @method_decorator(login_required) 
    def post(self, request, username): 
        try: 
            (user, user_profile, form) = self.get_user_details(username) 
        except TypeError: 
            return redirect(reverse('traveleverywhere:home'))
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid(): 
            form.save(commit=True) 
            return redirect('traveleverywhere:my_account', user.username) 
        else: 
            print(form.errors)
        context_dict = {'user_profile': user_profile, 'selected_user': user, 'form': form}
        return render(request, 'traveleverywhere/my_account.html', context_dict)

class LikeBLogView(View):
    @method_decorator(login_required)
    def get(self, request):
        blog_id = request.GET['blog_id']
        try:
            blog = Blog.objects.get(id=int(blog_id))
        except Blog.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        blog.likes = blog.likes + 1
        blog.save()
        return HttpResponse(blog.likes)

class LikeAirline(View):
    @method_decorator(login_required)
    def post(self, request):
        airline_id = request.POST['airline_id']
        try:
            airline = Airline.objects.get(id=int(airline_id))
        except Airline.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        airline.likes = airline.likes + 1
        airline.save()
        return HttpResponse(airline.likes)

class LikeAgency(View):
    @method_decorator(login_required)
    def post(self, request):
        agency_id = request.POST['agency_id']
        try:
            agency = Agency.objects.get(id=int(agency_id))
        except Agency.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        agency.likes = agency.likes + 1
        agency.save()
        return HttpResponse(agency.likes)






	