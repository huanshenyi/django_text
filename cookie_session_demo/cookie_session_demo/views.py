from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware

def index(request):
    response = HttpResponse('index')
    expires = datetime(year=2019, month=3, day=5, hour=23, minute=0, second=0)
    #タイムラインの変化
    expires = make_aware(expires)
    #max_age消えるまでの時間,       expiresはいつまで
    response.set_cookie('userid','12345', path="/cms/")

    return response

def my_list(request):
    cookies = request.COOKIES
    username = cookies.get('userid')
    return HttpResponse(username)

def cms_view(request):
    cookies = request.COOKIES
    username = cookies.get('userid')
    return HttpResponse(username)
