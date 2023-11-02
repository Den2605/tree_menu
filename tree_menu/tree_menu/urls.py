from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("tree/", include("tree.urls", namespace="tree")),
    path("admin/", admin.site.urls),
]
