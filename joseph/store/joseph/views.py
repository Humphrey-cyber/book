from django.shortcuts import render
from .models import Book
from .models import Portfolio
from .models import Contact
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem
from .models import HomePageImage,Book
from .models import Produce

def cart_summary(request):
    return render(request, "joseph/cart_view.html",{})

def cart_add(request):
    pass

def cart_delete(request):
    pass

def cart_update(request):
    pass



def home(request):
    return render(request, 'joseph/home.html')


def portfolio(request):
    pics=Portfolio.objects.all()
    return render(request, 'joseph/portfolio.html',{"pics":pics})


def contact(request):
    if request.method == "POST":
        pass
    return render(request, 'joseph/contact.html')


def home(request):
    homepage_image = HomePageImage.objects.last()

    return render(request,'joseph/home.html',{
        'homepage_image':homepage_image,
    })


def products(request):
    products = Produce.objects.all()
    return render(request, 'joseph/home.html', {'products': products})

 # Import the Book model

def home(request):
    books = Book.objects.all()[:3]  # Fetch only the first 3 books for the homepage
    return render(request, 'joseph/home.html', {'books': books})

def books_page(request):
    books = Book.objects.all()  # Fetch all books for the books page
    return render(request, 'joseph/books.html', {'books': books})

def books_view(request, pk): 
    book = Book.objects.get(id=pk) 
    return render(request, 'joseph/books_view.html', {'books': book})