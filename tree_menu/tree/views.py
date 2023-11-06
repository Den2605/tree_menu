from django.views.generic import TemplateView


class TreeView(TemplateView):
    template_name = "tree/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получить slug меню из URL
        slug_menu = self.kwargs["slug"]
        print(slug_menu)
        context["slug_menu"] = slug_menu
        return context
