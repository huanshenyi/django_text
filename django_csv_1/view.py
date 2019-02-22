from django.http import HttpResponse
import csv
from django.template import loader


"""基本のcsv処理"""
def index(request):
    """リスポンスのタイプ指定"""
    response = HttpResponse(content_type='text/csv')
    """ファイルの処理方を指定  attaachment->送付ファイルとして処理"""
    response['Content-Disposition'] = "attaachment;filename=abc.csv"

    writer = csv.writer(response)
    writer.writerow(['username', 'age'])
    writer.writerow(['haha', '20'])
    return response

"""djangoモジュール使用"""
def template_csv_view(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attaachment;filename=abc.csv"
    context = {
        'rows': [
            ['username', 'age'],
            ['python', '20'],
        ]
    }
    """テンプレートファイルを読み取り"""
    template = loader.get_template('abc.txt')
    csv_template = template.render(context)
    response.content = csv_template
    return response