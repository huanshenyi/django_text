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

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleListView, self).get_context_data(*kwargs)
    #     paginator = context.get('paginator')
    #
    #     """ countデータの数,num_pagesページの数,page_rangeページの区間"""
    #    # print(paginator.page_range)
    #
    #     page_obj = context.get('page_obj')
    #     """ has_next次のページあるかどうか"""
    #
    #     #print(page_obj.has_next())
    #     """next_page_number次のページの番号"""
    #     #print(page_obj.next_page_number())
    #
    #     return context

    # has_previous 前のページあるかどうか
    # next_page_number 次のページのナンバー
    # previous_page_number 前のページの番号
    # number 現在のページ
    # start_index 現在ページの最初のデータのindex
    # end_index 現在ページの最後のデータのindex
