from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio , name="inicio"),
    path('loggi', loggi, name='loggi'),
    path('admi', admi , name="admi")
]
