from django.contrib import admin
from .models import Category, Brand, SubCategory, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'description', 'image')
    search_fields = ['name', 'description']
    list_filter = ['name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'category', 'slug')
    search_fields = ['name']
    list_filter = ['category']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'brand', 'slug')
    search_fields = ['name']
    list_filter = ['brand']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'subcategory', 'price', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'brand', 'subcategory', 'description', 'price', 'image', 'slug')
    search_fields = ['name', 'description']
    list_filter = ['brand', 'subcategory', 'price']
    list_editable = ['price']
