from django.shortcuts import render
from particles.models import Particle
from app.scripts.reference import jref
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
def partInfo(request, id):
    part = Particle.objects.get(id=id)

    # test = jref(part.body)
    # part.body = test["body"]

    json_data = model_to_dict(part)
    return JsonResponse(json_data)