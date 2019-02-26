from django.shortcuts import render
from django.views.generic import View
from .forms import MessageBoardForm
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        form = MessageBoardForm()
        return render(request, 'index.html', context={"form": form})

    def post(self, request):
        form = MessageBoardForm(request.POST)
        if form.is_valid():
           title = form.cleaned_data.get('title')
           content = form.cleaned_data.get('content')
           reply = form.cleaned_data.get('reply')
           print('='*30)
           print(title)
           print(content)
           print(reply)
           print('=' * 30)
           return HttpResponse('success')
        else:
           print(form.errors.get_json_data())
           for key,val in (form.errors.get_json_data()).items():
               print(key,val[0]['message'])
           return HttpResponse('fail')

