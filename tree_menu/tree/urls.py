from django.urls import path

from . import views

app_name = "tree"
urlpatterns = [
    path("<str:menu>/", views.menu, name="draw_menu"),
]
