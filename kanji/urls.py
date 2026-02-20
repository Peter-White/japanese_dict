from django.contrib import admin
from django.urls import path
from kanji.views import body_views
from kanji.views import pron_views

urlpatterns = [
    path("", body_views.kanji_post, name="Kanji Post / Update"),
    path("/", body_views.kanji_list, name="Kanji List"),
    path("/<int:id>", body_views.kanji_handler_id, name="Kanji Info"),
    path("/<int:id>/pron", pron_views.pron_post, name="Post Kanji Pronunciation"),
    path("/<int:id>/pron/", pron_views.pron_list, name="List Kanji Pronunciations"),
    path("/<int:id>/pron/<int:pron_id>", pron_views.pron_handler, name="Kanji Pronunciation Info / Delete / Update")
]