# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# create the view for blog show
from django.shortcuts import render_to_response
from .models import BlogPost

def myBlogs(request):
    blog_list = BlogPost.objects.all()
    return render_to_response('MyBlog/BlogTemplate.html',{'blog_list':blog_list})

# 需要注意的就是模板中的模板标签以及模板变量都应该与views.py文件对应的函数中的字典变量相一致，
# 否则django虽然不会报错，但也是不会显示数据的

