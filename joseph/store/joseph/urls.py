from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books_page, name='books'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'), 
    path('books_view/<int:pk>', views.books_view, name='books_view'),
    path('featured-books/', views.all_featured_books, name='all_featured_books'),
    path('mpesa-checkout/', views.mpesa_checkout, name='mpesa_checkout'),
    
    ]