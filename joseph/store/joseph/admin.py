from django.contrib import admin
from .models import Book, Portfolio, HomePageImage, Produce

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cover_image', 'price')

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

class ProduceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Book, BooksAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Produce, ProduceAdmin)
admin.site.register(HomePageImage)
