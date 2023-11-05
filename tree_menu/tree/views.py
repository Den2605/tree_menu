from django.views.generic import TemplateView

from tree.models import Menu


class TreeView(TemplateView):
    template_name = "tree/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получить имя меню из URL или использовать main_menu
        name_menu = self.kwargs["name_menu"]
        # menu_items = Menu.objects.filter(name=name_menu).first()
        # context["name_menu"] = menu_items
        context["name_menu"] = name_menu
        return context


# def show_menu(request):
#     return render(request, "tree/index.html", {"name": "main_menu"})
