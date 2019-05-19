from django.http import HttpResponse
from django.shortcuts import render

from .models import User

def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return  render(request, 'people/index.html', context)

def search(request):
    name = request.GET.get('name')
    if name is not None :
      users = User.objects.filter(name__contains=name)
    else :
      users = None

    context = {
        'users': users,
    }
    return  render(request, 'people/search.html', context)