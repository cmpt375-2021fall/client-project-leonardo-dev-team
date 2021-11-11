from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from django.shortcuts import render

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


class exclusiveView(ListView):
    model = Post
    template_name = 'exclusive.html'
    ordering = ['-id']


class exclusiveDetailView(DetailView):
    model = Post
    template_name = 'exclusive_detail.html'
