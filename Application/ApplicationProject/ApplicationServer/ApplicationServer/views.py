from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def linregress(request):
    return render(request, "linregress.html")

def polyregress(request):
    return render(request, "polyregress.html")

def neuraln(request):
    return render(request, "neuraln.html")