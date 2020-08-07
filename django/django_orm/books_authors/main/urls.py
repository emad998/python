
from django.urls import path

from . import views

urlpatterns = [
    path('add_book', views.addingBook),
    path('', views.index),
    path('books/<int:id>', views.bookView),
    path('<int:id2>', views.authorToBook),
    path('authors', views.addAuthor),
    path('add_author', views.realAddAuthor),
    path('authors/<int:id3>', views.showAuthor),
    path('processing/<int:id4>', views.bookToAuthor)
]