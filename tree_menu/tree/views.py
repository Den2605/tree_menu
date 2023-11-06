from django.views.generic import TemplateView


class TreeView(TemplateView):
    """
    Функция для отображения отображения меню.
    """

    template_name = "tree/index.html"

    def get_context_data(self, **kwargs):
        """Формирует контекст, предаёт данные из запроса пользователя."""
        context = super().get_context_data(**kwargs)
        slug_menu = self.kwargs["slug"]
        context["slug_menu"] = slug_menu
        return context
