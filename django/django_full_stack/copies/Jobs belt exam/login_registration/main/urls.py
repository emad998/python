
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.regUpdate),
    path('login', views.loginProcess),
    path('logout', views.loggingOut),
    path('dashboard', views.dashboardView),
    path('jobs/<int:id1>', views.jobViewPage),
    path('jobs/new', views.createPage),
    path('addJob', views.addingJob),
    path('jobs/remove/<int:id2>', views.removeJob),
    path('jobs/edit/<int:id3>', views.editPageView),
    path('editJob/<int:id4>', views.editingJob)
]