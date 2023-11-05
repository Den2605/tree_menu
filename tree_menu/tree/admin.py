from django.contrib import admin

from tree.models import Item, Menu


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Пункты меню."""

    list_display = ("id", "name", "slug", "parent", "menu")
    list_filter = ("menu",)
    search_fields = ("name", "slug")
    ordering = ("id",)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Меню."""

    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    ordering = ("id",)
