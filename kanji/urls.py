from django.contrib import admin
from django.urls import path
from kanji import views as kanji_views

urlpatterns = [
    path("", kanji_views.kanji_post_update, name="Kanji Post / Update"),
    path("/", kanji_views.kanji_list, name="Kanji List"),
    path("/<int:id>", kanji_views.kanji_info, name="Kanji Info")
]