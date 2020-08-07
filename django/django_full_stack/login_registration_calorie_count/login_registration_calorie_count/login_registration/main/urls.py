
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.regUpdate),
    path('login', views.loginProcess),
    path('logout', views.loggingOut),
    path('success', views.successView),
    path('create', views.createView), #create page view
    path('realCreate', views.realCreating), #creating form
    path('edit/<int:id>', views.edit_pageView),
    path('real_edit/<int:id2>', views.real_editing),
    path('delete/<int:id3>', views.destroy), #delete food item 
    path('view-cart', views.view_cart), #link to view cart
    path ('add/<int:id4>', views.adding_order), #adding to cart
    path('deleteOrder/<int:id4>', views.destroyOrder),
    path('orders', views.viewOrders)

]
