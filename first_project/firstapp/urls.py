from django.urls import path
from .views import calculate_profit

urlpatterns = [
    path('', calculate_profit, name='calculate_profit'),
]
