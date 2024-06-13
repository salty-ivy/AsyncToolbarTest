from django.urls import path
from asyncapp.views import CarListView

app_name = "asyncapp"

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
]

