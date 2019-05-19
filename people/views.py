from django.http import HttpResponse
from django.shortcuts import render

from .models import User


def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return  render(request, 'people/index.html', context)

def results(request, name):
    response = "You're looking at the results of name %s."
    return HttpResponse(response % name)