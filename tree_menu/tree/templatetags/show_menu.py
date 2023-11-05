from django import template
from django.shortcuts import get_object_or_404
from django.urls import resolve
from django.utils.safestring import mark_safe

from tree.models import Item, Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, name_menu):
    tag_name = context["name_menu"]
    # имя тега совпадает с названием таблицы
    if tag_name == name_menu:
        menu = get_object_or_404(Menu, name=name_menu)
        root_items = Item.objects.filter(parent__isnull=True, menu=menu.id)
        print(root_items)
        return mark_safe(_get_menu(root_items))

    # имя тега не совпадает с названием таблицы
    current_items = Item.objects.filter(name=tag_name)
    # получаем id меню
    menu = current_items[0].menu
    print(menu)
    root_items = Item.objects.filter(parent=current_items[0].parent)
    root_items = Item.objects.filter(parent__isnull=True, menu=menu.id)
    print(current_items[0].parent)
    print(root_items)

    html_list = _get_menu(root_items)

    return mark_safe(html_list)


def _get_menu(menu):
    html = "<ul>"
    for sub_items in menu:
        html += "<li>"
        html += (
            f'<a href="{sub_items.get_absolute_url()}">{sub_items.name}</a>'
        )
        html += "</li>"
        if sub_items.childrens.exists():
            html += _get_menu(
                sub_items.childrens.all(),
            )
    html += "</ul>"
    return html
