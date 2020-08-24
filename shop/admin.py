from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created_at', 'created_at']
    list_filter = ['available', 'created_at', 'created_at']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}

