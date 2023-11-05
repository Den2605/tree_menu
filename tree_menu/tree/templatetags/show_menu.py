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
        return mark_safe(_get_menu(root_items[0]))
        # return mark_safe(_get_menu(root_items))

    # имя тега не совпадает с названием таблицы
    current_items = Item.objects.filter(name=tag_name)
    child_current_items = Item.objects.filter(parent=current_items[0].id)
    if child_current_items.exists():
        next_child_current_items = Item.objects.filter(
            parent=child_current_items[0].id
        )
        if next_child_current_items.exists():
            stop_item = next_child_current_items[0].name
        else:
            stop_item = None

    # получаем id меню
    menu = current_items[0].menu
    print(menu)
    root_items = Item.objects.filter(parent__isnull=True, menu=menu.id)
    if stop_item:
        return mark_safe(_get_menu(root_items[0], stop_item=stop_item))
    return mark_safe(_get_menu(root_items[0]))


def _get_menu(menu, stop_item=None):
    html = "<ul>"
    html += "<li>"
    html += f'<a href="{menu.get_absolute_url()}">{menu.name}</a>'
    html += "</li>"
    if menu.childrens.exists():
        for sub_item_children in menu.childrens.all():
            print(sub_item_children.name)
            if sub_item_children.name == stop_item:
                return html
            html += _get_menu(sub_item_children, stop_item=stop_item)
    html += "</ul>"
    return html


# def _get_menu(menu, stop_item=None):
#     html = "<ul>"
#     for sub_items in menu:
#         html += "<li>"
#         html += (
#             f'<a href="{sub_items.get_absolute_url()}">{sub_items.name}</a>'
#         )
#         html += "</li>"
#         if sub_items.childrens.exists():
#             html += _get_menu(sub_items.childrens.all(), stop_item=stop_item)
#     html += "</ul>"
#     return html
