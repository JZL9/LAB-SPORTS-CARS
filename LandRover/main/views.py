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