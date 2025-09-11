from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')
    #return HttpResponse("Welcome to the Homepage!")


def about(request):
    #return HttpResponse("Welcome to about page")
    return render(request, 'about.html')
    