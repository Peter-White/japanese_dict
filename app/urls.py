from django.urls import include, path
from app import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("about/", views.about),
    path("base/", include("base_chars.urls")),
    path("particles/", include("particles.urls"))
]