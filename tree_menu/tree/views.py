from django.views.generic import TemplateView


class TreeView(TemplateView):
    template_name = "tree/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получить имя меню из URL
        name_menu = self.kwargs["name_menu"]
        context["name_menu"] = name_menu
        return context
