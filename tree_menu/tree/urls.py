from django.urls import path

from tree.views import TreeView

app_name = "tree"

urlpatterns = [
    path("tree/<slug:slug>/", TreeView.as_view(), name="tree"),
]
