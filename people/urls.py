from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.index, name='index'),
    path('<str:name>/', views.results, name='results'),
]