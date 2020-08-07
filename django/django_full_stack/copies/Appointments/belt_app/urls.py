from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('register_user', views.register_user),
    path('login_user', views.login_user),
    path('dashboard', views.success),
    path('logout', views.logout),
    path('add_appointment', views.addAppointment),
    path('create_appointment', views.create_appointment),
    path('edit_appointment/<int:Val>', views.edit_appointment),
    path('edit/<int:Val>', views.edit),
    path('remove_appointment/<int:Val>', views.remove_appointment),
    path('view/<int:x>', views.view_appointment)



]
