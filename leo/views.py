from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'leo\login.html')

def footer(request):
    return render(request, 'leo\\footer.html')

def header(request):
    return render(request, 'leo\\Header.html')