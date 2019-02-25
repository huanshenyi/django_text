from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.views.generic import ListView

def add_article(request):
    articles = []
    for x in range(0, 102):
        article = Article(title='タイトル%s' % x, content='内容%s' % x)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse('success')

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    #一ページに表示される最大の内容数
    paginate_by = 10
    #ordering->並び替え
    ordering = 'create_time'
    """ページdefaultのキーワードはpage"""
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(*kwargs)
        context['username'] = 'zhiliao'
        return context
