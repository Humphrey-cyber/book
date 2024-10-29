from django.contrib import admin
from .models import Book, Portfolio, HomePageImage, Produce, HomePageContent, Service, Project

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cover_image', 'price')

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

class ProduceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading', 'banner_image')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'project_link')

admin.site.register(Book, BooksAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Produce, ProduceAdmin)
admin.site.register(HomePageImage)
admin.site.register(HomePageContent, HomePageContentAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin)
