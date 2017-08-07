# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import user,post
# Register your models here.
admin.site.register(user)
admin.site.register(post)