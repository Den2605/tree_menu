from django.shortcuts import render
from django.views.generic import TemplateView

from tree.models import Menu


class TreeView(TemplateView):
    template_name = "tree/index.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["menu"] = Menu.objects.filter(name="main_menu").first()
        return context


# def show_menu(request, name, url=None):
#     return render(request, "tree/menu.html", {"name": name})
