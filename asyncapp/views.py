from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import render
from asyncapp.models import Car


class CarListView(ListView):
    """
    return a list of cars
    """

    model = Car
    template_name = 'cars/car_list.html'


async def get_car_list(request):
    cars = Car.objects.all()
    context = {'object_list': "cars list"}
    return render(request, 'cars/car_list.html', context)
