from django.http import HttpResponse,StreamingHttpResponse
from django.template import loader
import csv


def larage_csv_view(request):
    """StreamingHttpResponse使用すれば,リスポンスが見やすく"""
    response = StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename=larage.csv"

    rows = ("Row{},{}\n".format(row,row) for row in range(0, 100000))

    response.streaming_content = rows
    return response