from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # or your existing app urls
    path('', include('accounts.urls')),  # Add the new app URLs here
]
