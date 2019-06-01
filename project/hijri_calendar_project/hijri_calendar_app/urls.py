from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('page-<str:page_number>', views.paged_comments, name='paged_comments', kwargs = {'arg3': 'arg3_value', 'arg4': 'arg4_value'}),
    path('<str:comment_id>', views.comments, name='comments', kwargs = {'arg1': 'arg1_value', 'arg2': 'arg2_value'}),
    path('', views.index, name='index'),
]