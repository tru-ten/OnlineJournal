from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Article

def home(request):
    return render(request, 'journal/home_without_login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматичний вхід після реєстрації
            return redirect('home_with_login')  # Перенаправлення на головну сторінку після реєстрації
    else:
        form = UserCreationForm()
    return render(request, 'journal/registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_with_login')  # Перенаправлення на головну сторінку
        else:
            messages.error(request, 'Неправильний логін або пароль.')
    return render(request, 'journal/registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('home_without_login')  # Перенаправлення на головну сторінку після виходу

def home_with_login(request):
    return render(request, 'journal/home_with_login.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'journal/articles/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'journal/articles/article_detail.html', {'article': article})