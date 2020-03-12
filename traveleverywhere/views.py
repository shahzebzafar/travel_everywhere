from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context_dict = {}
    return render(request, 'traveleverywhere/home.html', context=context_dict)

def blogs(request):
    context_dict = {}
    return render(request, 'traveleverywhere/blogs.html', context=context_dict)

def forum(request):
    context_dict = {}
    return render(request, 'traveleverywhere/forum.html', context=context_dict)

def travel(request):
    context_dict = {}
    return render(request, 'traveleverywhere/travel.html', context=context_dict)