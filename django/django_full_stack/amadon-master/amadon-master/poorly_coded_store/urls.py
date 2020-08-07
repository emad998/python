from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkoutPage', views.checkoutPage),
    path('checkout', views.checkout)
]
