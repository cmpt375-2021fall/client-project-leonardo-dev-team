from django.shortcuts import render, redirect
from .forms import MyCustomLoginForm, MyCustomSignupForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# register form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse


# Create your views here.
from .models import Post

@login_required
def dashboard(request):
    context = {

    }
    return render(request, 'dashboard.html', context)


@login_required
def newsletter(request):
    context = {}
    return render(request, 'newsletter.html', context)


@login_required
def calendar(request):
    context = {}
    return render(request, 'calendar.html', context)

@login_required
def account(request):
    context = {}
    return render(request, 'account.html', context)

@login_required
def exclusive(request):
    context = {}
    return render(request, 'exclusive.html', context)

@login_required
class exclusiveView(ListView):
    model = Post
    template_name = 'exclusive.html'
    ordering = ['-id']

@login_required
class exclusiveDetailView(DetailView):
    model = Post
    template_name = 'exclusive_detail.html'
'''
def header(request):
    context = {

    }
    return render(request, 'Header.html', context)

def footer(request):
    context = {}
    return render(request, 'footer.html', context)
'''
