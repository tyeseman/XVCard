from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, 'profiles/home.html')

def about(request):
    return render(request, 'profiles/contact.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Replace with your dashboard URL name
    else:
        form = UserCreationForm()
    return render(request, 'profiles/signup.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'profiles/dashboard.html', {'user': request.user})
