from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def privacy_page(request):
    return render(request, 'privacy.html')

def plans_page(request):
    return render(request, 'plans.html')