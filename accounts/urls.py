from django.urls import path
from .views import signup, login_view, logout_view, user_profile_view, update_profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_profile/', user_profile_view, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
]
