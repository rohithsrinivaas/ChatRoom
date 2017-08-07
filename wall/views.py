# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.template import loader
from django.http import HttpResponse
from .models import user, post
from django.core.urlresolvers import reverse


class current_user:
	def __init__(self):
		self.user=user(user_name="dummy.")

	def set_user(self, obj):
		self.user=obj

	def current_user(self):
		return self.user 

	def change_state(self):
		self.user.active = True
cu=current_user()


def index(request):
	if(request.POST('Your post')):
		print(True)
	posts=tuple(post.objects.all())
	t=loader.get_template('wall/index.html')
	context={
		'posts':posts,
		'active':True,
	}
	return HttpResponse(t.render(context, request))

def user_wall(request, user_name):
	users=tuple(user.objects.all())
	for u in users:
		if u.user_name==user_name:
			break
	return render(request, 'wall/user_wall.html', {'username':user_name, 'posts': tuple(u.post_set.all()) } )


def login(request):
	return render(request, 'wall/login.html', {})


def logInHandler(request):
	from .models import user , post
	un=request.POST['name']
	pw=request.POST['password']
	
	users=tuple(user.objects.all())
	found=False
	for user in users:
		if user.user_name==un:
			if user.pass_word==pw:
				found=True
				break

	#print user 
	#print '\n\n'
	if found:
		cu.set_user(user)
		cu.change_state()
	user_url = '/wall/users/' + cu.current_user().user_name
	print(user_url)
	return render(request, 'wall/index.html', { 'posts': tuple(post.objects.all()), 'username': un,'active' : cu.current_user().active, 'user_url':user_url })

def signup(request):
	return render(request, 'wall/signup.html', {} )

def signUpHandler(request):
	un=request.POST['name']
	pw=request.POST['password']
	
	u=user(user_name=un, pass_word=pw)
	u.save()
	return render(request,'wall/signUpHandler.html',{'username' : un })


def logout(request):

	cu.current_user().active = False
	print("Activity",cu.current_user().active)
	print("Username",cu.current_user().user_name)
	return render(request, 'wall/logout.html', {})

def posting(request):
	return render(request, 'wall/posting.html', {} )

