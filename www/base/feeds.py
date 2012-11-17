# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from forum.models import Post
from rendertext import render_text

class PostFeed(Feed):
    title = 'fiveprime.kr posts'
    link = '/'
    description = u'파이브프라임 새 글 목록'
    def items(self):
        return Post.objects.order_by('-created_on')[:30]
    def item_title(self, obj):
        return u'[%s] %s' % (obj.category.name, obj.title)
    def item_description(self, obj):
        return render_text(obj.text)
    def item_link(self, obj):
        return obj.get_absolute_url()
