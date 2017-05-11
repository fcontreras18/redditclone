from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


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
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html',
                {'error': 'Passwords didn\'t match'})
    else:
        return render(request, 'accounts/signup.html')
