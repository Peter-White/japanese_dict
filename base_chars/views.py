from django.shortcuts import render, HttpResponse
from base_chars.models import Hiragana, Katakana
from base_chars import scripts

def ganaBaseList(request):
    return HttpResponse("List Hiragana")

def kanaBaseList(request):
    return HttpResponse("List Kanagana")

def postHiragana(request):
    return HttpResponse(request)

def postKatakana(request):
    return HttpResponse(request)

