from django.shortcuts import render, redirect

#register form
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {

    }
    return render(request, 'dashboard.html', context)

#Register page adds to admin user if valid and saves form
def registerPage(request):
    form = UserCreationForm()

    #processes form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
    'form': form
    }
    return render(request, 'register.html', context)

#Login page (not yet implemented)
def loginPage(request):
    context = {

    }
    return render(request, 'login.html', context)

def newsletter(request):
    context = {}
    return render(request, 'newsletter.html', context)

def calendar(request):
    context = {}
    return render(request, 'calendar.html', context)

def header(request):
    context = {

    }
    return render(request, 'Header.html', context)

def footer(request):
    context = {}
    return render(request, 'footer.html', context)