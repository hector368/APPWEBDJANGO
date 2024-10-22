from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.
def login_view(request):
    template_name= "auth-login.html"
    
    if not request.user.is_active:
        messages.error(request, 'User is not active')
        # Validación para usuarios ya autenticados
        if request.user.is_authenticated:
            return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login Credentials')
    return render (request,template_name)

# View for register
def register_view(request):
    template_name= "auth-register.html"
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está en uso.")
            return render(request, template_name)

        user = User(
            username=username, 
            email=email, 
            password=make_password(password),
            is_active = 0
            )
        user.save()
        messages.success(request, "Cuenta creada exitosamente")
    return render (request,template_name)

# View for forget
def forgot_view(request):
    template_name= "auth-forgot-password.html"
    return render (request,template_name)

#View for logout
def logout_view(request):
    logout(request)
    return redirect('login')