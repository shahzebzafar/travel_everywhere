from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse 
from django.urls import reverse 
from django.shortcuts import redirect
from traveleverywhere.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from datetime import datetime



def home(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'traveleverywhere/home.html', context=context_dict)
    return response

def blogs(request):
    context_dict = {}
    return render(request, 'traveleverywhere/blogs.html', context=context_dict)

def forum(request):
    context_dict = {}
    return render(request, 'traveleverywhere/forum.html', context=context_dict)

def travel(request):
    context_dict = {}
    return render(request, 'traveleverywhere/travel.html', context=context_dict)
	
# def signup(request):
#     context_dict = {}
#     return render(request, 'traveleverywhere/signup.html', context=context_dict)
	
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


	