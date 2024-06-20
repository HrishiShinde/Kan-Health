from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from users.forms import CustomUserCreationForm, CustomAuthenticationForm

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home or another page
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or another page
    else:
        form = CustomAuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
