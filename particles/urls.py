from django.contrib import admin
from django.urls import path
from particles import views as part_views

urlpatterns = [
    path("<int:id>", part_views.partInfo, name="Particle Inffo")
]