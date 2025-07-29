from django.contrib import admin
from django.urls import path
from base_chars import views as base_views

urlpatterns = [
    path("hiragana/", base_views.ganaBaseList),
    path("katakana/", base_views.kanaBaseList)
]