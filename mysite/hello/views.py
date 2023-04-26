from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)

def cookie(request):
    # print("========================================================")
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view - the zap cookie value is '+str(oldval))
    if oldval:
        # No expired date = until browser close
        resp.set_cookie('zap', int(oldval)+1)
    else:
        resp.set_cookie('zap', 42)  # No expired date = until browser close
    resp.set_cookie('sakaicar', 42, max_age=1000)  # seconds until expire
    resp.set_cookie('dj4e_cookie', '876dcde3', max_age=1000)
    return resp

# https://www.youtube.com/watch?v=Ye8mB6VsUHw


def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    res = HttpResponse(f"view count={num_visits}")
    if num_visits > 4:
        del(request.session['num_visits'])
    res.set_cookie('dj4e_cookie', '876dcde3')
    # res = HttpResponse('view count='+str(num_visits))
    return res

def index(request):
    # response = cookie(request)
    request = sessfun(request)
    return request
