from django.urls import path
from .views import *

urlpatterns = [
    path('', copy_message, name='home'),
]