from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import random

# Create your views here.

def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('hello1.html')
    return HttpResponse(template.render({}, request))

def give_me_a_number(request):
    i = random.random()
    template = loader.get_template('number.html')
    context = { 'i': i }
    return HttpResponse(template.render(context, request))
