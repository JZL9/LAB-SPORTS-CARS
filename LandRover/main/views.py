from django.shortcuts import render, redirect
from django.http import HttpRequest


def home_view(request: HttpRequest):
    return render(request, "main/home.html")


def all_cars_view(request: HttpRequest):
    return render(request, "main/all_cars.html")


def about_view(request: HttpRequest):
    return render(request, "main/about.html")


def range_rover_view(request: HttpRequest):
    return render(request, "main/range_rover.html")


def defender_view(request: HttpRequest):
    return render(request, "main/defender.html")


def discovery_view(request: HttpRequest):
    return render(request, "main/discovery.html")

def toggle_theme_view(request: HttpRequest):
    current = request.COOKIES.get("theme", "light")
    new_theme = "dark" if current == "light" else "light"

    response = redirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie("theme", new_theme)
    return response