from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books_page, name='books'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'), 
#    path('cart/', views.cart_summary, name='cart_summary'),
#     path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
#     path('cart/delete/<int:item_id>/', views.cart_delete, name='cart_delete'),
#     path('cart/update/<int:item_id>/', views.cart_update, name='cart_update'),
    path('books_view/<int:pk>', views.books_view, name='books_view'),
    path('featured-books/', views.all_featured_books, name='all_featured_books'),
    ]