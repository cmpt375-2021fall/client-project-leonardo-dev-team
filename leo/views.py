from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import ListView, DetailView

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# register form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse


# Create your views here.
from .models import Post, Calender



def login(request):
    print(request.method)
    return render(request, template_name="login.html")

def error(request):
    context = {}
    return render(request, 'error.html')

def dashboard(request):
    context = {

    }
    return render(request, 'dashboard.html', context)


def newsletter(request):
    context = {}
    return render(request, 'newsletter.html', context)


def calendar(request):
    context = {}
    return render(request, 'calendar.html', context)

def account(request):
    context = {}
    return render(request, 'account.html', context)

def member(request):
    context = {}
    return render(request, 'membership.html', context)

def exclusive(request):
    context = {}
    return render(request, 'exclusive.html', context)

class exclusiveView(ListView):
    model = Post
    template_name = 'exclusive.html'
    ordering = ['-id']

class exclusiveDetailView(DetailView):
    model = Post
    template_name = 'exclusive_detail.html'

class calenderView(ListView):
    model = Calender
    template_name = 'calendar.html'
'''
def header(request):
    context = {

    }
    return render(request, 'Header.html', context)

def footer(request):
    context = {}
    return render(request, 'footer.html', context)
'''

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request)
            messages.success(request, "Registration successful.")
            return redirect("login_request")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                dashboard(request)
                print(request, f"You are now logged in as {username}.")
                return redirect("dashboard")
            else:
                print(request, "Invalid username or password.")
        else:
            print(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def homepage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("register")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})
