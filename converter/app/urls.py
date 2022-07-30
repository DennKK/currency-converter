from django.urls import path
from .views import Converter
urlpatterns = [
    path('', Converter.as_view(), name='converter'),
]