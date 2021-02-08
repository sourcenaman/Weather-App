from .views import *
from django.urls import path

app_name = 'weather'
urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:city_id>/', delete, name='delete'),
]
