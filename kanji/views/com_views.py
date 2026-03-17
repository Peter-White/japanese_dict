from django.shortcuts import render, HttpResponse
from kanji.models import KanjiComprised, KanjiBody
from app.scripts.reference import jref
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers

def com_info(id):
    com_id = KanjiComprised.objects.get(id=id).get_body()
    json_data = KanjiBody.objects.get(id=com_id).to_dict

    return json_data

@csrf_exempt
def com_list(request, id):
    com_list = KanjiComprised.objects.all().filter(kanji=id)
    json_list = []

    for com in com_list:
        json_list.append(com_info(com.get_body()))

    return JsonResponse(json_list, safe=False)

@csrf_exempt
def com_post(request, id):
    try:
        kanji = KanjiBody.objects.get(id=id)
        body = request.POST["body"]

        new_com = KanjiComprised(body=body, kanji=kanji)
        new_com.save()

        return HttpResponse(new_com.get_kanji() + " com posted")
    except:
        return HttpResponse("Error")


def deft_delete(id):
        com = KanjiComprised.objects.get(id=id)
        com.delete()

@csrf_exempt
def com_handler(request, id):
    try:
        if (request.method == 'GET'):
            return JsonResponse(com_info(id))
        elif (request.method == 'DELETE'):
            deft_delete(id)
            return HttpResponse(id + " com delete")
        else:
            return HttpResponse("Not Valid")
    except:
        return HttpResponse("Error")