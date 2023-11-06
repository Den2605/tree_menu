from django import template
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from tree.models import Item, Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, slug_menu):
    tag_name = context["slug_menu"]
    # имя тега совпадает с названием таблицы
    if tag_name == slug_menu:
        menu = get_object_or_404(Menu, slug=slug_menu)
        root_items = Item.objects.filter(
            parent__isnull=True, menu=menu.id
        ).first()
        return mark_safe(_get_menu(root_items))

    # имя тега не совпадает с названием таблицы
    # получаем значение текущего подпункта
    current_items = Item.objects.filter(slug=tag_name).first()

    # проверяем сколько есть вложенных элементов
    # если их менее двух, значит отображается вся таблица
    child_current_items = Item.objects.filter(parent=current_items.id)
    if child_current_items.exists():
        next_child_current_items = Item.objects.filter(
            parent=child_current_items[0].id
        )
        if next_child_current_items.exists():
            stop_item = next_child_current_items[0].name
        else:
            stop_item = None
    else:
        stop_item = None

    # получаем id меню
    menu = current_items.menu

    root_items = Item.objects.filter(parent__isnull=True, menu=menu)
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
            if sub_item_children.name == stop_item:
                return html
            html += _get_menu(sub_item_children, stop_item=stop_item)
    html += "</ul>"
    return html
