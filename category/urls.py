from django.urls import path
from .views import *

app_name = 'category'

urlpatterns = [
    path('', home, name='home'),
]
