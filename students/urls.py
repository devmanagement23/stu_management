
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('home/',home),
    path('add_student/',add_student),
]
