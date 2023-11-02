from django.urls import path

from . import views

app_name = "tree"

urlpatterns = [
    path("<str:name>/", views.show_menu, name="draw_menu"),
]
