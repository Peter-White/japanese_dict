from django.shortcuts import render
from kanji.models import KanjiBody, KanjiComprised, KanjiDefinition, KanjiPronunciation
from app.scripts.reference import jref
from django.http import JsonResponse
from django.core import serializers

def kanjiInfo(request, id):
    kan_bod = KanjiBody.objects.get(id=id)
    json_data = kan_bod.to_dict
    
    kan_pron = KanjiPronunciation.objects.all().filter(kanji=kan_bod.get_id)
    for pron in kan_pron:
        pron = pron.to_dict
        
        pron[]
    
    kan_def = KanjiDefinition.objects.all().filter(kanji=kan_bod.get_id)
    kan_com = KanjiComprised.objects.all().filter(kanji=kan_bod.get_id)
    
    

    return JsonResponse(json_data)

def postKanjiBody(request):
    return JsonResponse()