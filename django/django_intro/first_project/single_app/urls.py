from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_func),
    path('new', views.new),
    path('create', views.create),
    path("<int:my_num>", views.show),
    path("<int:edit_num>/edit", views.edit),
    path("destroy", views.destroy)
    # path('admin/', admin.site.urls),
]