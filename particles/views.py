from django.shortcuts import render
from particles.models import Particle
from app.scripts.reference import jref
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

def partList(request):
    part_list = Particle.objects.all()

    json_data = []

    for part in part_list:
        part_obj = model_to_dict(part)
        ref_bod = jref(part_obj["body"])
        part_obj["body"] = ref_bod
        json_data.append(part_obj)

    return JsonResponse(json_data, safe=False)

def partInfo(request, id):
    part = Particle.objects.get(id=id)

    json_data = model_to_dict(part)
    json_data["body"] = jref(part.body)

    return JsonResponse(json_data)