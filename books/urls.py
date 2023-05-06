from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('new/', views.add_book, name='add_book'),
    path('<int:id>/edit/', views.update_book, name='update_book'),
    path('<int:id>/delete/', views.delete_book, name='delete_book'),
    path('search/', views.search_books, name='search_books'),
    path('search_results/<str:query>/<int:page>', views.search_results, name='search_results')
]
