from django.shortcuts import render
from particles.models import Particle
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
def partInfo(request, id):
    part = Particle.objects.get(id=id)
    json_data = model_to_dict(part)
    return JsonResponse(json_data)