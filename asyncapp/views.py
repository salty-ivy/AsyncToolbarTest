import asyncio

from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from asyncapp.models import Car
import time
from contextvars import copy_context
import os
import threading
from django.db import connections


class CarListView(ListView):
    """
    return a list of cars
    """

    model = Car
    template_name = 'cars/car_list.html'

    def get(self, request, *args, **kwargs):
        # print("context in SYNC car view***: ", id(copy_context()))
        # print("thread_id in SYNC car view***: ", threading.get_ident())
        time.sleep(5)
        return super().get(self, request, *args, **kwargs)


def sleep_view(request):
    time.sleep(10)
    print(os.getpid())
    print("context in view***: ", id(copy_context()))
    return HttpResponse(f"sleep for 10 seconds {id(copy_context())}, thread_id: {threading.get_ident()}")


def sleep_view_small(request):
    time.sleep(1)
    print(os.getpid())
    print("context in view***: ", id(copy_context()))
    return HttpResponse(f"sleep for 1 seconds {id(copy_context())}, thread_id: {threading.get_ident()}")


async def get_car_list(request):
    cars = await Car.objects.aget(name="toyota")
    # print(cars)
    context = {'object_list': "car list"}
    # print("context in ASYNC car view***: ", id(copy_context()))
    # print("thread_id in ASYNC car view***: ", threading.get_ident())
    await asyncio.sleep(3)
    rendered = render(request, 'cars/car_list_async.html', context)
    return rendered


async def new_async_view(request):
    cars = Car.objects.all()
    context = {'object_list': "car list"}
    print("context in ASYNC car view***: ", id(copy_context()))
    print("thread_id in ASYNC car view***: ", threading.get_ident())
    await asyncio.sleep(1)
    return render(request, 'cars/car_list_async_new.html', context)