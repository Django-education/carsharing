from django.urls import path
from .views import index, account, cars, contacts, information, region, tariffs

urlpatterns = [
    path('', index, name='index'),
    path('account', account, name='account'),
    path('cars', cars, name='cars'),
    path('contacts', contacts, name='contacts'),
    path('information', information, name='information'),
    path('region', region, name='region'),
    path('tariffs', tariffs, name='tariffs'),

]