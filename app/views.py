from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Jeidikku")

def about(request):
    return HttpResponse("About Page")