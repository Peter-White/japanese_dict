from django.contrib import admin
from django.urls import path
from base_chars import views as base_views

gana_url = "hiragana/"
kana_url = "katakana/"

urlpatterns = [
    path(gana_url, base_views.ganaBaseList),
    path(kana_url, base_views.kanaBaseList),
    path(gana_url + "post", base_views.postHiragana),
    path(kana_url + "post", base_views.postKatakana)
]