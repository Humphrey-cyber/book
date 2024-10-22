from django.contrib import admin
from .models import Book
from .models import Portfolio
from .models import HomePageImage
from .models import Produce

# Register your models here.
class Booksadmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cover_image', 'price')

admin.site.register(Book, Booksadmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

admin.site.register(Portfolio, PortfolioAdmin)

class ProduceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )


admin.site.register(Produce, ProduceAdmin)

admin.site.register(HomePageImage)



