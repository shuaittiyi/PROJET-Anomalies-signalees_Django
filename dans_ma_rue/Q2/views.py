from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'Q2/index.html')

    return HttpResponse("Q2")