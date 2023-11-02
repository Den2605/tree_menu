from django.shortcuts import render

from .models import Menu


def menu(request):
    return render(request, "tree/menu.html")
