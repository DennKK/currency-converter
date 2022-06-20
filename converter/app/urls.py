from django.urls import path
from . import views

urlpatterns = [
    path('', views.Converter.as_view(), name='converter'),
]