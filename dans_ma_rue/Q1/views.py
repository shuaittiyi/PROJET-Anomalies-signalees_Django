from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    test = "Test pour voir"
    return render(request, 'Q1/index.html', { 'test': test})

    return HttpResponse("Q2")
