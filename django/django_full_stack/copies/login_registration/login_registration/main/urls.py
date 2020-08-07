
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.regUpdate),
    path('login', views.loginProcess),
    path('logout', views.loggingOut),
    path('success', views.successView)
]