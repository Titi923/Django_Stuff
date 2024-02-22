from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In!")
            return redirect('acasa')
        else:
            messages.error(request, "Error logging in!")
            return redirect('acasa')
    else:
        return render(request, 'home.html', {})

# Create your views here.
def admin():
    pass

def logare_user(request):
    return redirect('acasa')

def delogare_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out!")
    return redirect('acasa')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been Registered")
            return redirect('acasa')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
