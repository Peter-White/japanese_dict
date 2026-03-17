from django.shortcuts import render, HttpResponse
from kanji.models import KanjiDefinition, KanjiBody
from app.scripts.reference import jref
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers

def deft_info(id):
    deft = KanjiDefinition.objects.get(id=id)
    json_data = deft.to_dict

    return json_data

@csrf_exempt
def deft_list(request, id):
    deft_list = KanjiDefinition.objects.all().filter(kanji=id)
    json_list = []

    for deft in deft_list:
        json_list.append(deft.to_dict)

    return JsonResponse(json_list, safe=False)

@csrf_exempt
def deft_post(request, id):
    try:
        kanji = KanjiBody.objects.get(id=id)
        type = request.POST["type"]
        body = request.POST["body"]
        lang = request.POST["lang"]

        new_deft = KanjiDefinition(body=body, kanji=kanji, lang=lang, type=type)
        new_deft.save()

        return HttpResponse(new_deft.get_kanji() + " deft posted")
    except:
        return HttpResponse("Error")


def deft_delete(id):
        deft = KanjiDefinition.objects.get(id=id)
        deft.delete()
    
@csrf_exempt
def deft_handler(request, id):
    try:
        if (request.method == 'GET'):
            return JsonResponse(deft_info(id))
        elif (request.method == 'POST'):
            kan_deft = KanjiDefinition.objects.get(id=id)

            if "kanji" in request.POST:
                kan_deft.set_body(request.POST["kanji"])
            
            if "deft" in request.POST:
                kan_deft.set_strokes(request.POST["deft"])

            kan_deft.save()
            return HttpResponse("Updated")
        elif (request.method == 'DELETE'):
            deft_delete(id)
            return HttpResponse(id + " deft delete")
        else:
            return HttpResponse("Not Valid")
    except:
        return HttpResponse("Error")