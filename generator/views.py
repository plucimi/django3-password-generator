from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    print(request)
    length = int(request.GET.get('length',12))
    upper_case = request.GET.get('uppercase')
    nums = request.GET.get('numbers')
    special = request.GET.get('special')

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if upper_case == 'on':
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if special == 'on':
        characters.extend(list('~!@#$%^&*()_-`'))
    if nums == 'on':
        characters.extend(list('0123456789'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
    
def scoreboard(request):
    return render(request, 'generator/scoreboard.html')
