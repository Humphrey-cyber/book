from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    file_size = models.CharField(max_length=50, blank=True, null=True)  # For PDF file size
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class HomePageContent(models.Model):
    heading = models.CharField(max_length=255)
    subheading = models.TextField()
    banner_image = models.ImageField(upload_to='banner_images/', blank=True, null=True)  # New banner image field


    def __str__(self):
        return self.heading

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    project_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# class Cart(models.Model):
#     session_key = models.CharField(max_length=40, default='', blank=True)

#     def __str__(self):
#         return f"Cart {self.id}"

#     def total_price(self):
#         return sum(item.total_price() for item in self.cartitem_set.all())

# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def total_price(self):
#         return self.quantity * self.product.price

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name}"

class HomePageImage(models.Model):
    profile = models.ImageField(upload_to='home_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption if self.caption else "Home Page Image"

class Produce(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='home_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    project_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
