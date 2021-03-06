# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from DjangoUeditor.models import UEditorField

# 模型是Django提供一个抽象层（Models）以构建和操作你的web应用中的数据

# Create your models here.
class Article(models.Model):
    title = models.CharField(u"博客标题", max_length=100)  # 博客标题
    category = models.CharField(u"博客标签", max_length=50, blank=True)  # 博客标签
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)  # 博客发布日期
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    #content = models.TextField(blank=True, null=True)  # 博客文章正文
    content = UEditorField(u"文章正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                       toolbars='besttome', filePath='uploads/blog/files/')

    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"

