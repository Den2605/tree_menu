from django import template
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from tree.models import Item, Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, slug_menu):
    tag_name = context["slug_menu"]
    menu = get_object_or_404(Menu, slug=slug_menu)

    if tag_name == slug_menu:
        root_items = Item.objects.filter(parent__isnull=True, menu=menu)
    else:
        current_items = get_object_or_404(Item, slug=tag_name)
        root_items = Item.objects.filter(
            parent__isnull=True, menu=current_items.menu
        )

    html = ""
    for root_item in root_items:
        if tag_name == slug_menu:
            stop_item = None
        else:
            stop_item = _get_stop(current_items)
        html += _get_menu(root_item, stop_item)

    return mark_safe(html)


def _get_menu(menu, stop_item=None):
    html = "<ul>"
    html += "<li>"
    html += f'<a href="{menu.get_absolute_url()}">{menu.name}</a>'
    html += "</li>"
    children_items = menu.childrens.all()
    for sub_item_children in children_items:
        if sub_item_children.name == stop_item:
            break
        html += _get_menu(sub_item_children, stop_item)
    html += "</ul>"
    return html


def _get_stop(current_items):
    child_current_items = Item.objects.filter(parent=current_items)
    if child_current_items:
        next_child_current_items = Item.objects.filter(
            parent=child_current_items[0]
        )
        if next_child_current_items:
            return next_child_current_items[0].name
    return None
