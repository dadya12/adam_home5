from django.urls import path
from calculate_api.views import add, multiply, divide, subtract

app_name = 'calculate_api'

urlpatterns = [
    path('add/', add, name='add'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
    path('subtract/', subtract, name='subtract')
]