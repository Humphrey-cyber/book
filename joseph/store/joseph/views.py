from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Portfolio, Contact, Product, Cart, CartItem, HomePageImage, Produce

def cart_summary(request):
    return render(request, "joseph/cart_view.html", {})

def cart_add(request):
    pass

def cart_delete(request):
    pass

def cart_update(request):
    pass

def home(request):
    homepage_image = HomePageImage.objects.last()
    books = Book.objects.all()[:3]  # Fetch the first 3 books for the homepage
    products = Produce.objects.all()  # Fetch all products for display

    return render(request, 'joseph/home.html', {
        'homepage_image': homepage_image,
        'books': books,
        'products': products,
    })

def portfolio(request):
    pics = Portfolio.objects.all()
    return render(request, 'joseph/portfolio.html', {"pics": pics})

def contact(request):
    if request.method == "POST":
        pass
    return render(request, 'joseph/contact.html')

def books_page(request):
    books = Book.objects.all()  # Fetch all books for the books page
    return render(request, 'joseph/books.html', {'books': books})

def books_view(request, pk): 
    book = get_object_or_404(Book, id=pk)
    return render(request, 'joseph/books_view.html', {'book': book})
