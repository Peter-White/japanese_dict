from django.shortcuts import render, HttpResponse
from base_chars.models import Hiragna, Kataganas
from base_chars import scripts

def ganaBaseList(request):
    return HttpResponse("List Hiragana")

def kanaBaseList(request):
    return HttpResponse("List Kanagana")



