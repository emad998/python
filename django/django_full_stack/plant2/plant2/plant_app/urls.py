from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register_user', views.register_user),
    path('login_user', views.login_user),
    path('dashboard', views.success),
    path('logout', views.logout),
    path('fern', views.fern_page),
    path('succulent', views.succulent_page),
    path('tree', views.tree_page),
    path('vine', views.vine_page),
    path('createPlantPage', views.createPlantPageView),
    path('createPlantProcess', views.createPlantProcessing),
    path('dashboardAll', views.dashboardAllView),
    path('addComment/<int:id>', views.addingComment),
    path('addCommentSucculent/<int:id2>', views.addingCommentSucculent),
    path('addCommentTree/<int:id3>', views.addingCommentTree),
    path('addCommentVine/<int:id4>', views.addingCommentVine)
    


]
