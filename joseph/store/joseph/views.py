from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Portfolio, Contact, Product,HomePageImage, Produce, HomePageContent, Service, Project


# def cart_summary(request):
#     # Ensure the session key is set
#     if not request.session.session_key:
#         request.session.create()
    
#     # Try to get or create a cart based on the session key
#     cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
#     cart_items = cart.cartitem_set.all()
#     return render(request, "joseph/cart_view.html", {'cart_items': cart_items, 'cart': cart})

# def cart_add(request, product_id):
#     cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
#     product = get_object_or_404(Product, id=product_id)
#     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect('cart_summary')

# def cart_delete(request, item_id):
#     cart_item = get_object_or_404(CartItem, id=item_id)
#     cart_item.delete()
#     return redirect('cart_summary')

# def cart_update(request, item_id):
#     cart_item = get_object_or_404(CartItem, id=item_id)
#     if request.method == 'POST':
#         cart_item.quantity = int(request.POST.get('quantity', cart_item.quantity))
#         cart_item.save()
#     return redirect('cart_summary')

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
