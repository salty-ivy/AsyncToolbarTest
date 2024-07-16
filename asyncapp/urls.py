from django.urls import path
from asyncapp.views import CarListView, get_car_list, sleep_view, sleep_view_small, new_async_view

app_name = "asyncapp"

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('sleep/', sleep_view, name='sleep'),
    path('sleep-small/', sleep_view_small, name='sleep'),

    # async views
    path('async-cars/', get_car_list, name='async-cars'),
    path('async-small/', new_async_view, name='async-small'),

]

