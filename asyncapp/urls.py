from django.urls import path
from asyncapp.views import CarListView, get_car_list

app_name = "asyncapp"

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('async-cars/', get_car_list, name='async-cars'),
]

