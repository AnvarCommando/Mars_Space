from django.urls import path
from .views import *

urlpatterns = [
    path('give/coin/', GiveCoinView.as_view()),
]