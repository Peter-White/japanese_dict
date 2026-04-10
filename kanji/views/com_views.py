from django.shortcuts import render, HttpResponse
from kanji.models import KanjiComprised, KanjiBody
from app.scripts.reference import jref
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from kanji.scripts.prop_scripts import order_manage

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
        body = KanjiBody.objects.get(id=request.POST["body"])

        coms = KanjiComprised.objects.all().filter(kanji=kanji).order_by("order")

        order_manage(coms, id);

        new_com = KanjiComprised(body=body, kanji=kanji, order=len(coms)+1)
        new_com.save()

        return HttpResponse(kanji.get_body() + " com posted")
    except:
        return HttpResponse("Error")


def deft_delete(id):
        com = KanjiComprised.objects.get(id=id)
        com.delete()

@csrf_exempt
def com_handler(request, id, com_id):
    try:
        kan_bod = KanjiBody.objects.get(id=id)
        if (request.method == 'GET'):
            return JsonResponse(com_info(com_id))
        elif (request.method == 'DELETE'):
            deft_delete(com_id)
            return HttpResponse(kan_bod.get_body() + " com delete")
        else:
            return HttpResponse("Not Valid")
    except:
        return HttpResponse("Error")