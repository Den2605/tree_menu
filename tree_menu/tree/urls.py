from django.urls import path

from . import views

app_name = "tree"
urlpatterns = [
    path("<str:name>/", views.menu, name="draw_menu"),
]
