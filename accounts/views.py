from django.shortcuts import render, redirect
from django.contrib.auth import  logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileUpdateForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    print("Request method:", request.method)  # Debug line
    print("Is AJAX:", request.headers.get('x-requested-with'))  # Debug line

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Handle AJAX request
                return JsonResponse({'success': True, 'message': 'Login successful!'})
            else:
                # Handle normal POST request
                return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Handle AJAX request with errors
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = AuthenticationForm()
    
    # Render the login form for GET requests
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def user_profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def update_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page or another page
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'accounts/update_profile.html', {'form': form})