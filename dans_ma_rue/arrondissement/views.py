from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    test = "Test pour voir"
    return render(request, 'arrondissement/index.html', { 'test': test})

