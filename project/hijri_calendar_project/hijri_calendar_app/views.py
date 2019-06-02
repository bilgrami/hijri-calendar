from django.shortcuts import render
import datetime

# Create your views here.
from django.http import HttpResponse

def _get_date():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prefix = "[{}] - ".format(now)
    return prefix

def _get_kwargs(**kwargs):
    return ', '.join("{}={}".format(key, value) for key, value in kwargs.items())

def index(request, name = 'world'):
    return HttpResponse(_get_date() + "Hello " + name + "! You're at the Hijri Calendar App index.")

def comments(request, comment_id, **kwargs):
    return HttpResponse(_get_date() + "You want to see comment #" + comment_id + '. Arguments: ' + _get_kwargs(**kwargs))

def paged_comments(request, page_number, **kwargs):
    return HttpResponse(_get_date() + "You want to see comments on page number " + page_number + '. Arguments: ' + _get_kwargs(**kwargs))