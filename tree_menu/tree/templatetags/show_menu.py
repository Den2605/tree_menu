from django import template
from django.utils.safestring import mark_safe
from tree.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(name):
    print(name)
    menu_items = Menu.objects.filter(name=name).select_related("parent")

    if menu_items:
        return mark_safe(_get_menu(menu_items))


def _get_menu(menu_items):
    html = "<ul>"
    for item in menu_items:
        html += "<li>"
        if item.url:
            html += f'<a href="{item.url}">{item.name}</a>'
        else:
            html += item.name
        if item.heir.exists():
            html += _get_menu(item.heir.all())
        html += "</li>"
    html += "</ul>"
    return html
