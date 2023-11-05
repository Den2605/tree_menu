from django.urls import path

from tree.views import TreeView

app_name = "tree"

urlpatterns = [
    path("tree/<str:name_menu>/", TreeView.as_view(), name="tree"),
]
