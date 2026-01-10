from django.shortcuts import render, HttpResponse
from base_chars.models import Hiragana, Katakana
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict
from base_chars import scripts

def ganaList(request):
    if('group_num' in request.GET):
        ganaList = Hiragana.objects.all().filter(group_num=request.GET['group_num'])
    else:
        ganaList = Hiragana.objects.all()

    json_data = serializers.serialize("json", ganaList)
    return HttpResponse(json_data, content_type="text/json-comment-filtered")

def kanaList(request):
    kanaList = Katakana.objects.all()
    json_data = serializers.serialize("json", kanaList)
    return HttpResponse(json_data, content_type="text/json-comment-filtered")

def ganaInfo(request, id):
    gana = Hiragana.objects.get(id=id)
    json_data = model_to_dict(gana)
    return JsonResponse(json_data)

def kanaInfo(request, id):
    kana = Katakana.objects.get(id=id)
    json_data = model_to_dict(kana)
    return JsonResponse(json_data)

# def ganaByGroup(request, group_num):
#     ganaList = Hiragana.objects.all().filter(group_num=group_num)
#     json_data = serializers.serialize("json", ganaList)
#     return HttpResponse(json_data, content_type="text/json-comment-filtered")
