from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile
from shoping_cart.models import Order



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form,})



def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        message = 'This account is not varified yet!'
    return render(request, 'users/login.html', {'message': message})



def logout_view(request):
    logout(request)
    return redirect('home')



def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    orders = Order.objects.filter(is_ordered=True, owner=profile)
    return render(request, 'users/profile.html', {'profile': profile, 'orders': orders})
