from django.contrib import admin

# Register your models here.
from asyncapp.models import Car

admin.site.register(Car)