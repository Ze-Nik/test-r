from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def titul_page(response):
    return render(response, "main/titul_page.html")


def auto_page(response):
    return render(response, "main/auto_page.html")


def user_page(response):
    return render(response, "main/user_page.html")


def reg_page(response):
    return render(response, "main/reg_page.html")

