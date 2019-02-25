from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

def index(request):
    return HttpResponse('index')

class BookListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('book list view')

class AddBookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_book.html')

    def post(self, request, *args, **kwargs):
        book_name = request.POST.get('name')
        book_author = request.POST.get('author')
        print("name:{},author:{}".format(book_name, book_author))
        return HttpResponse("success")

class BookDetailView(View):
    def get(self,request, book_id):
        print('書籍id%s' % book_id)
        return HttpResponse("success")
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('get以外の方法受付ません')