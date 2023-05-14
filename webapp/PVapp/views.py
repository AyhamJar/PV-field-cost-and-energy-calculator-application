from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def mono(request):
    return render(request, "mono.html")

def poly(request):
    return render(request, "poly.html")

def thin(request):
    return render(request, "thin.html")

def calculate(request):
    return render(request, "calculate.html")