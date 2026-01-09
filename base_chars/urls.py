from django.contrib import admin
from django.urls import path
from base_chars import views as base_views

gana_url = "hiragana/"
kana_url = "katakana/"

urlpatterns = [
    path(gana_url, base_views.ganaList, name="List of Hiragana"),
    path(kana_url, base_views.kanaList, name="List of Katakana"),
    path(gana_url + "<int:id>", base_views.ganaInfo, name="Info on Gana character"),
    path(kana_url + "<int:id>", base_views.kanaInfo, name="Info on Kana character")
]