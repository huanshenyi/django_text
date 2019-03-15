from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.generic import View
from .forms import SignupForm, SigninForm
from .models import User
from django.contrib import messages



def index(request):
    users = User.objects.all()
    for user in users:
        print(user)
    return render(request, 'index.html')


class SigninView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('home'))
            else:
               # messages.add_message(request, messages.INFO, 'データ確認できません!')
                messages.info(request, 'データ確認できません')
                return redirect(reverse('signin'))
        else:
            errors = form.errors.get_json_data()
            # print(errors)
            # print(form.get_error())
            # messages.info(request, '入力に誤りあります')
            errors = form.get_error()
            for error in errors:
                messages.info(request, error)
            return redirect(reverse('signin'))




class SignupView(View):
    def get(self, request):
       return render(request, 'signup.html')

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
        else:
            errors = form.errors.get_json_data()
            return redirect(reverse('signup', kwargs={'errors': errors}))


def blog(request):
    return render(request,'blog.html')


def video(request):
    return render(request,'video.html')