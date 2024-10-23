from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def login_view(request):
    template_name = "login.html"
    
        # Validación para usuarios ya autenticados
    if request.user.is_authenticated and request.user.is_active:
            return redirect('home')
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login Credentials or User is not active')
    return render (request,template_name)
    
def register_view(request):
    template_name = "register.html"
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "The passwords do not match.")
            return render(request, template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, "The username is already in use.")
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "The email is already in use")
            return render(request, template_name)

        user = User(
            username=username, 
            email=email, 
            password=make_password(password),
            is_active = 0
            )
        user.save()
        messages.success(request, "Account successfully created.")
    return render (request,template_name)

def forgot_view(request):
    template_name = "forgot.html"
    return render(request,template_name)

#View for logout
def logout_view(request):
    logout(request)
    return redirect('login')