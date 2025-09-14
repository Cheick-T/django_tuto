from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, 'users/user_register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        # Handle login logic here
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            auth_login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            return redirect('posts:list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('posts:list')
    #return render(request, 'users/logout.html')

