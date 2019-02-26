from django.http import HttpResponse
from django.shortcuts import render

def view_405(request):
    return render(request, 'errors/405.html', status=405)

def view_403(request):
    return render(request, 'errors/403.html', status=403)

def view_404(request):
    return render(request, 'errors/../templates/404.html', status=404)