from django.shortcuts import render
from django.http import HttpResponse
import random

import string
import datetime  
    
# Create your views here.
def home (request):
    return render(request,'generator/home.html')

def about(request):
    # using now() to get current time  
    current_time = datetime.datetime.now()
    return render(request, 'generator/about.html',{'time': current_time})

def password(request):
    characters = list(string.ascii_lowercase)

    lenght= int(request.GET.get('length','12'))
    uppercase= request.GET.get('uppercase')
    special= request.GET.get('special')
    numbers= request.GET.get('numbers')

    if uppercase:
        upper_list= list(string.ascii_uppercase)
        characters.extend(upper_list)
    if special:
        special_list = list('!$%&=?@*#')
        characters.extend(special_list)
    if numbers:
        numbers_list= list('0123456789')
        characters.extend(numbers_list)

    thepassword = ''
    for x in range(lenght):
        thepassword+= random.choice(characters)
    return render(request,'generator/password.html',    {'password': thepassword})
