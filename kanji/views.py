from django.shortcuts import render
from kanji.models import KanjiBody, KanjiComprised, KanjiDefinition, KanjiPronunciation
from app.scripts.reference import jref
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

def kanjiInfo(id, request):
    kan_bod = KanjiBody.objects.get(id=id)

    json_data = model_to_dict(kan_bod)

