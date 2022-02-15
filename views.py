from django.http import HttpResponse
from django.shortcuts import render
from dans_ma_rue.models import *

def index(request):
    test = ""
    return render(request,'index.html', {'test': test})