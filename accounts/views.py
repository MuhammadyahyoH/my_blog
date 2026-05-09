from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Username yoki password xato'})
    return render(request, 'login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return render(request, 'register.html', {'error': "Barcha maydonlarni to'ldiring"})
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Bu username band'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')