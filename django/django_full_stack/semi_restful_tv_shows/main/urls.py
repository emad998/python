
from django.urls import path

from . import views

urlpatterns = [
    path('shows', views.allShows),
    path('shows/new', views.addingShow),
    path('create', views.realAddingShow),
    path('shows/<int:id>', views.showShow),
    path('shows/<int:id2>/edit', views.editingShowPage),
    path('shows/<int:id3>/update', views.updatingShow),
    path('shows/<int:id4>/destroy', views.destroyingShow),
    path('', views.index)
]

