from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated():
        return render(request, 'main/logged.html', {'user': request.user})
    return redirect('login/')

def signup(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        # Sign up
        if request.POST['password'] != request.POST['password_confirm']:
            return render(request, 'main/signup.html', {'errors': True})
        User.objects.create_user(
            request.POST['username'],
            None,
            request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name']
            )
        return redirect('/')
    return render(request, 'main/signup.html')
