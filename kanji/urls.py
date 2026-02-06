from django.contrib import admin
from django.urls import path
from kanji import views as kanji_views

urlpatterns = [
    # path("", kanji_views., name="Particle List"),
    path("<int:id>", kanji_views.kanjiInfo, name="Kanji Info")
]