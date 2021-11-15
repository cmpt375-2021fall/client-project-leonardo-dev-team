from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from django.shortcuts import render

from .models import Post


@login_required
def dashboard(request):
    context = {
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def newsletter(request):
    context = {}
    return render(request, 'dashboard/newsletter.html', context)


@login_required
def calendar(request):
    context = {}
    return render(request, 'dashboard/calendar.html', context)


@login_required
def profile(request):
    context = {}
    return render(request, 'dashboard/profile.html', context)


@login_required
def exclusive(request):
    context = {}
    return render(request, 'dashboard/exclusive.html', context)


class exclusiveView(ListView):
    model = Post
    template_name = 'dashboard/exclusive.html'
    ordering = ['-id']


class exclusiveDetailView(DetailView):
    model = Post
    template_name = 'dashboard/exclusive_detail.html'
