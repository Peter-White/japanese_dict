from django.shortcuts import render, HttpResponse
from base_chars.models import Hiragana, Katakana
from base_chars import scripts

def ganaList(request):
    return HttpResponse("List Hiragana")

def kanaList(request):
    return HttpResponse("List Kanagana")

def ganaInfo(request):
    return HttpResponse("Single Gana")

def kanaInfo(request):
    return HttpResponse("Single Kana")

