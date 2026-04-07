from django.shortcuts import render, HttpResponse
from kanji.models import KanjiPronunciation, KanjiBody
from app.scripts.reference import jref
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from kanji.scripts.prop_scripts import order_manage

def pron_info(id):
    pron = KanjiPronunciation.objects.get(id=id)
    json_data = pron.to_dict
    json_data["body"] = jref(json_data["body"])

    return json_data

@csrf_exempt
def pron_list(request, id):
    pron_list = KanjiPronunciation.objects.all().filter(kanji=id)
    json_list = []

    for pron in pron_list:
        json_data = pron.to_dict
        json_data["body"] = jref(json_data["body"])
        
        json_list.append(json_data)

    return JsonResponse(json_list, safe=False)

@csrf_exempt
def pron_post(request, id):
    try:
        kanji = KanjiBody.objects.get(id=id)
        type = request.POST["type"]
        body = request.POST["body"]

        prons = KanjiPronunciation.objects.all().filter(kanji=kanji).order_by("order")

        order_manage(prons, id)

        new_pron = KanjiPronunciation(body=body, order=len(prons)+1, kanji=kanji, type=type)
        new_pron.save()

        return HttpResponse(new_pron.get_kanji().get_body() + " pron posted")
    except:
        return HttpResponse("Error")


def pron_delete(id):
        pron = KanjiPronunciation.objects.get(id=id)
        pron.delete()
    
@csrf_exempt
def pron_handler(request, id, pron_id):
    try:
        kan_bod = KanjiBody.objects.get(id=id)
        if (request.method == 'GET'):
            return JsonResponse(pron_info(pron_id))
        elif (request.method == 'POST'):
            kan_pron = KanjiPronunciation.objects.get(id=pron_id)

            if "kanji" in request.POST:
                kan_pron.set_body(request.POST["kanji"])
            
            if "pron" in request.POST:
                kan_pron.set_strokes(request.POST["pron"])

            kan_pron.save()
            return HttpResponse("Updated")
        elif (request.method == 'DELETE'):
            pron_delete(pron_id)
            return HttpResponse(kan_bod.get_body() + " pron delete")
        else:
            return HttpResponse("Not Valid")
    except:
        return HttpResponse("Error")

@csrf_exempt
def test(request):
    prons = KanjiPronunciation.objects.all().filter(kanji=3).order_by("order")
    riont = set(prons.values_list("order", flat=True))

    set_match = len(riont) == len(prons)
    numbered_corr = prons[0].get_order() == 1 and prons[len(prons)-1].get_order() == len(prons)

    if not set_match or not numbered_corr:
        for ind, val in enumerate(prons):
            index = ind + 1

            if(val.get_order() != index):
                val.set_order(index)
                val.save()

    return HttpResponse("Test")
