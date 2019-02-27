from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddBookForm,RegisterForm
from django.views.decorators.http import require_POST

def index(request):
    return HttpResponse('index')

def add_book(request):
    form = AddBookForm(request.POST)
    if form.is_valid():
        # title = form.cleaned_data.get('title')
        # page = form.cleaned_data.get('page')
        # price = form.cleaned_data.get("price")
        # print(title, page, price)
        """form使用の直接save"""
        form.save()
        return HttpResponse('success')
    else:
        print(form.errors.get_json_data())
        return HttpResponse('FALL')

@require_POST
def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        """commit=False userをインスタンス化するけど,dbへ保存しない"""
        user = form.save(commit=False)
        user.password = form.cleaned_data.get('pwd1')
        user.save()
        return HttpResponse('success')
    else:
        print(form.errors.get_json_data())
        return HttpResponse('fail')
