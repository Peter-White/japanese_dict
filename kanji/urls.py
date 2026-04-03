from django.contrib import admin
from django.urls import path
from kanji.views import body_views
from kanji.views import pron_views
from kanji.views import deft_views
from kanji.views import com_views

urlpatterns = [
    path("", body_views.kanji_post, name="Kanji Post / Update"),
    path("/", body_views.kanji_list, name="Kanji List"),
    path("/<int:id>", body_views.kanji_handler_id, name="Kanji Info"),
    path("/<int:id>/pron", pron_views.pron_post, name="Post Kanji Pronunciation"),
    path("/<int:id>/pron/", pron_views.pron_list, name="List Kanji Pronunciations"),
    path("/<int:id>/pron/<int:pron_id>", pron_views.pron_handler, name="Kanji Pronunciation Info / Delete / Update"),
    path("/<int:id>/deft", deft_views.deft_post, name="Post Kanji Definitions"),
    path("/<int:id>/deft/", deft_views.deft_list, name="List Kanji Definitions"),
    path("/<int:id>/deft/<int:deft_id>", deft_views.deft_handler, name="Kanji Definitions Info / Delete / Update"),
    path("/<int:id>/com", com_views.com_post, name="Post Kanji Comprised"),
    path("/<int:id>/com/", com_views.com_list, name="List Kanji Comprised"),
    path("/<int:id>/com/<int:com_id>", com_views.com_handler, name="Kanji Comprised Info / Delete / Update"),
    path("/test", pron_views.test, name="Delete Soon")
]