"""Define URLS for users aplications."""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # Page register
    path('register/', views.register, name='register'),
]
