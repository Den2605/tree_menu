from django.contrib import admin
from tree.models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "parent")
    list_filter = ("name",)
    search_fields = ("name", "url")
    ordering = ("id",)


admin.site.register(Menu, MenuAdmin)
