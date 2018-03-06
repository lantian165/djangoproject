# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import BlogPost

# set the admin page for BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')


# register the model (especially important)
admin.site.register(BlogPost)