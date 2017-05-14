from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['verify-password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',
                    {'error': 'Username already taken'})

            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],
                request.POST['password'], request.POST['verify-password'])
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',
                {'error': 'Passwords didn\'t match'})
    else:
        return render(request, 'accounts/signup.html')


def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',
                {'error': 'The username and/or password didn\'t match'})
    else:
        return render(request, 'accounts/login.html')


def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
