from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Include pages app URLs
    path('accounts/', include('accounts.urls')),  # Accounts app
    # Add other app URLs here
]