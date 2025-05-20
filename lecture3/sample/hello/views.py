from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def ernesto(request):
    return HttpResponse("Hello, Ernesto!")

def saludos(request):
    return HttpResponse("Saludos, Ernesto!")

def greet(request):
    return render(request, "Hello/greet.html", {
        "name": name.capitalize()
    })
