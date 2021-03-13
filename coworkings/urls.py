"""Define URLS for coworkings aplications."""

from django.urls import path

from . import views

app_name = 'coworking'
urlpatterns = [
    path('', views.index, name='index'),
]