from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from app.scripts.reference import jref

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Jeidikku")

def about(request):
    return HttpResponse("About Page")

@csrf_exempt
def ref_test(request):
    pattern = request.headers.get('pattern')
    test = jref(pattern)
    
    return HttpResponse(test, content_type="text/json-comment-filtered")