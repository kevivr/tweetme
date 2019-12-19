# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .forms import TweetModelForm
# Register your models here.
from .models import Tweet

class TweetModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Tweet

admin.site.register(Tweet, TweetModelAdmin)