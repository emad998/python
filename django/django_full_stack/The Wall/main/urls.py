
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.regUpdate),
    path('login', views.loginProcess),
    path('logout', views.loggingOut),
    path('addMessage', views.addingMessage),
    path('success', views.successView),
    path('addComment/<int:id1>', views.addingComment)
    
]