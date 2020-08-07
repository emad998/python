
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add_dojo', views.addingDojo),
    path('add_ninja', views.addingNinja)
]