from django.urls import path
from asyncapp.views import simple_response_view

app_name = "asyncapp"

urlpatterns = [
    path('simple-response', simple_response_view, name='simple_response'),
]

