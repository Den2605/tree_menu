from django.shortcuts import render


def show_menu(request, name):
    return render(request, "tree/menu.html", {"name": name})
