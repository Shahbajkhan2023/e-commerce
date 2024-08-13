from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>/brands/', views.brand_list, name='brand_list'),
    path('<slug:category_slug>/<slug:brand_slug>/subcategories/', views.subcategory_list, name='subcategory_list'),
    path('<slug:category_slug>/<slug:brand_slug>/<slug:subcategory_slug>/products/', views.product_list, name='product_list'),
]