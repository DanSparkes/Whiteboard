from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/accounts/login")
    return render(request, "frontend/index.html")

