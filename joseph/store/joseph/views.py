from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Portfolio, Contact, Product,HomePageImage, Produce, HomePageContent, Service, Project
from django.core.mail import send_mail
from django.contrib import messages


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



def books_page(request):
    books = Book.objects.all()  # Fetch all books for the books page
    return render(request, 'joseph/books.html', {'books': books})

def books_view(request, pk):
   
    book = get_object_or_404(Book, id=pk)
    
    # Calculate the amount in KES
    amount_in_kes = book.price * 130  
    
    # Pass both the book and the calculated KES amount to the template
    return render(request, 'joseph/books_view.html', {'book': book, 'amount_in_kes': amount_in_kes})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Construct the email subject and message
        subject = f"New Contact Form Submission from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send the email
        try:
            send_mail(
                subject,
                full_message,
                email,  # From email (sender's email)
                ['calemale360@gmail.com'],  # Replace with the company's email address
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "An error occurred while sending your message. Please try again later.")

    return render(request, 'joseph/contact.html')