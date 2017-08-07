# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

@python_2_unicode_compatible
class user(models.Model):
	user_name=models.CharField(max_length=30)
	pass_word=models.CharField(max_length=30, default="workshop")
	active = models.BooleanField(default = False)
	def __str__(self):
		return self.user_name

	def name(self):
		return self.user_name
	

@python_2_unicode_compatible
class post(models.Model):
	post_text=models.CharField(max_length=1000)
	date_text=models.DateTimeField('post dated')
	likes_count=models.IntegerField(default=0)
	owner=models.ForeignKey(user)

	def __str__(self):
		return self.post_text

	def display_post(self):
		print self.date_text
		print self.post_text+'\n'
		print ".................... by "+self.owner.name()
		print "======================================================="
	
	def increment_likes(self):
		self.likes_count += 1
