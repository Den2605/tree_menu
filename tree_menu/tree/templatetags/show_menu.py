from django import template
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from tree.models import Menu

register = template.Library()


@register.inclusion_tag("tree/tree_menu.html", takes_context=True)
def draw_menu(context, menu):
    # items = Menu.objects.filter(name=menu)
    menu_items = Menu.objects.filter(name=menu)
    return {"menu": menu_items}
    # menu_html = _new_get_menu(menu_items)
    # return mark_safe(menu_html)


# # @register.simple_tag
# @register.inclusion_tag("tree/tree_menu.html", takes_context=True)
# def draw_menu(context, name):
#     # print(context)
#     print(">>>")
#     # print(name)
#     menu_items = Menu.objects.filter(name=name)
#     # menu = get_object_or_404(Menu, name=name)
#     # new_menu_position = menu.position + 1
#     # menu_1 = Menu.objects.filter(
#     #     position__gte=1, position__lte=new_menu_position
#     # )
#     # print(menu_items)
#     return mark_safe(_new_get_menu(menu_items, depth=1, max_depth=2))
#     # return _new_get_menu(menu_items, depth=1, max_depth=2)


# def _new_get_menu(menu_items, depth, max_depth):
#     if depth > max_depth:
#         return ""
#     html = "<ul>"
#     for item in menu_items:
#         # print(item)
#         if item.url:
#             html += "<li>"
#             html += f'<a href="{item.url}">{item.name}</a>'
#             html += "</li>"
#             # print(html)
#         if item.heir.exists():
#             html += _new_get_menu(
#                 item.heir.all(), depth=depth + 1, max_depth=max_depth
#             )
#     html += "</ul>"
#     return html
