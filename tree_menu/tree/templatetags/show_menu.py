from django import template
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from tree.models import Item, Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, slug_menu):
    tag_name = context["slug_menu"]
    # имя тега совпадает с названием таблицы
    html = ""
    if tag_name == slug_menu:
        menu = get_object_or_404(Menu, slug=slug_menu)
        # получаем текущую корневую директорию
        root_items = Item.objects.filter(parent__isnull=True, menu=menu.id)
        for root_item in root_items:
            html += _get_menu(root_item, html)

        return mark_safe(html)

    # имя тега не совпадает с названием таблицы
    # получаем значение текущего подпункта
    current_items = get_object_or_404(Item, slug=tag_name)

    # получаем меню
    menu = current_items.menu

    # получаем корневые папки данного меню
    root_items = Item.objects.filter(parent__isnull=True, menu=menu)
    for root_item in root_items:
        stop_item = _get_stop(current_items)
        html += _get_menu(root_item, html, stop_item=stop_item)
    return mark_safe(html)


def _get_menu(menu, html, stop_item=None):
    html = "<ul>"
    html += "<li>"
    html += f'<a href="{menu.get_absolute_url()}">{menu.name}</a>'
    html += "</li>"
    children_items = menu.childrens.all()
    if children_items.exists():
        for sub_item_children in children_items:
            if sub_item_children.name == stop_item:
                return html
            html += _get_menu(sub_item_children, html, stop_item=stop_item)
    html += "</ul>"
    return html


def _get_stop(current_items):
    # проверяем сколько есть вложенных элементов
    # если их менее двух, значит отображается вся таблица
    child_current_items = Item.objects.filter(parent=current_items.id)
    if child_current_items.exists():
        next_child_current_items = Item.objects.filter(
            parent=child_current_items[0].id
        )
        if next_child_current_items.exists():
            return next_child_current_items[0].name
    return None
