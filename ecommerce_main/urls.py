from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # or your existing app urls
    path('', include('accounts.urls')),  # Add the new app URLs here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
