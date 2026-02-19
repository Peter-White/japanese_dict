from django.contrib import admin
from django.urls import path
from kanji.views import body_views

urlpatterns = [
    path("", body_views.kanji_post, name="Kanji Post / Update"),
    path("/", body_views.kanji_list, name="Kanji List"),
    path("/<int:id>", body_views.kanji_handler_id, name="Kanji Info")
]