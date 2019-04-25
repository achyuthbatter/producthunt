from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def login(request):
    if(request.method == "POST"):
        user = auth.authenticate(username= request.POST['username'],password= request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect'})
    else:    
        return render(request, 'accounts/login.html')

def logout(request):
    if(request.method == "POST"):
        auth.logout(request)
        return redirect('home')
    else:
        return render(request, 'accounts/logout.html')

def signup(request):
    if(request.method == "POST"):
        if(request.POST['pass'] ==  request.POST['cpass'] ):
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['pass'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        return render(request, 'accounts/signup.html')