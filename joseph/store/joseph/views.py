from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Portfolio, Contact, Product,HomePageImage, Produce, HomePageContent, Service, Project
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def mpesa_checkout(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Handle the payment processing here with Mpesa
        # For simplicity, let's return a success response
        return JsonResponse({'success': True, 'message': 'Payment initiated successfully'})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)



def home(request):
    homepage_image = HomePageImage.objects.last()
    homepage_content = HomePageContent.objects.last()
    books = Book.objects.all()[:3]  # Fetch the first 3 books for the homepage
    products = Produce.objects.all()  # Fetch all products for display
    services = Service.objects.all()  # Fetch all services
    projects = Project.objects.all()  # Fetch all projects

    return render(request, 'joseph/home.html', {
        'homepage_image': homepage_image,
        'homepage_content': homepage_content,
        'books': books,
        'products': products,
        'services': services,
        'projects': projects,
    })
    
def all_featured_books(request):
    books = Book.objects.all()  # Fetch all books for the featured books page
    return render(request, 'joseph/featured_books.html', {'books': books})

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
