from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def topten(request):
    return render(request, 'topten.html')
