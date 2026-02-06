from django.shortcuts import render, HttpResponse
from kanji.models import KanjiBody, KanjiComprised, KanjiDefinition, KanjiPronunciation
from app.scripts.reference import jref
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers

def prop_populate(coll):
    json_list = []

    for obj in coll:
        obj = obj.to_dict
        
        obj["body"] = jref(obj["body"])
        json_list.append(obj)

    return json_list

def kanji_info(request, id):
    kan_bod = KanjiBody.objects.get(id=id)
    json_data = kan_bod.to_dict
    
    kan_pron = KanjiPronunciation.objects.all().filter(kanji=kan_bod.get_id)
    json_data["prons"] = prop_populate(kan_pron)
    
    kan_def = KanjiDefinition.objects.all().filter(kanji=kan_bod.get_id)
    json_data["defs"] = prop_populate(kan_def)

    kan_com = KanjiComprised.objects.all().filter(kanji=kan_bod.get_id)
    json_data["com"] = prop_populate(kan_com)

    return JsonResponse(json_data)

def kanji_list(request):
    return JsonResponse({})

@csrf_exempt
def kanji_post_update(request):
    if (request.method == 'POST'):
        body = request.POST["body"]
        strokes = request.POST["strokes"]

        new_kan = KanjiBody(body=body, strokes=strokes)
        new_kan.save()

        return HttpResponse(new_kan.get_body + " posted")
    # elif (request.method = "UPDATE"):
    #     return JsonResponse([])
    else:
        return HttpResponse("Not Valid")