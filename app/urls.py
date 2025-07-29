from django.urls import path
from app import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("about/", views.about)
]