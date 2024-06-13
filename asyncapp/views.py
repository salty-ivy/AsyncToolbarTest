from django.views.generic import ListView
from asyncapp.models import Car


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'





