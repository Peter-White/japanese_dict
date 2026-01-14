from django.contrib import admin
from django.urls import path
from particles import views as part_views

part_url = "particles/"

urlpatterns = [
    path(part_url + "<int:id>", part_views.partInfo, name="Particle Inffo")
]