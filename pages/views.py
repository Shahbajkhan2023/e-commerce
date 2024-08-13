from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Brand, SubCategory, Product


def home(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 10)  # Show 10 categories per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        categories_data = list(page_obj.object_list.values('id', 'name', 'description', 'image'))
        return JsonResponse({'categories': categories_data, 'has_next': page_obj.has_next()})

    return render(request, 'home.html', {'categories': page_obj})


def brand_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    brands = Brand.objects.filter(category=category)
    return render(request, 'pages/brand_list.html', {'category': category, 'brands': brands})


def subcategory_list(request, category_slug, brand_slug):
    brand = get_object_or_404(Brand, category__slug=category_slug, slug=brand_slug)
    subcategories = brand.subcategories.all()
    return render(request, 'pages/subcategory_list.html', {'brand': brand, 'subcategories': subcategories})


def product_list(request, category_slug, brand_slug, subcategory_slug):
    subcategory = get_object_or_404(SubCategory, brand__category__slug=category_slug, brand__slug=brand_slug, slug=subcategory_slug)
    products = subcategory.products.all()
    return render(request, 'pages/product_list.html', {'subcategory': subcategory, 'products': products})
