"""Define URLS for coworkings aplications."""

from django.urls import path

from . import views

app_name = 'coworkings'
urlpatterns = [
    path('', views.index, name='index'),
    path('reservs/', views.reservs, name='reservs'),
    path('place/<int:place_id>', views.place, name='place'),
    path('look_vacant_offices/', views.look_vacant_offices, name='look_vacant_offices'),
    # TODO: добавить урлы на просмотр забронированых офисов
]