
from django.shortcuts import render


def Home_Page(request):
    return render(request, "home.html")
