from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404,HttpResponseRedirect, HttpResponse
from hyd_smartshop.models import Users
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render
import random 
import copy
from django.db.models import Count
from django.db.models import Max
import json
import re
import datetime
from datetime import timedelta
from datetime import datetime, date, time
from django.utils import timezone

def index(request):
	if 'uid' in request.session :
		uid=request.session['uid']
		luser=Users.objects.get(id=uid)
		return HttpResponse("Logged In  :" + " Store Name - " + luser.storename)

	else:
		return render(request,'hyd_smartshop/login.html')


def login(request):	
	return render(request,'hyd_smartshop/login.html')

def signin(request):
	try:
		m = Users.objects.get(email=request.POST['eid_signIn'])
	except Users.DoesNotExist:
		context = {
			'alerts': "invalid Email: u may SIGNUP",  
			'class': "error"
		}
		return render(request,'hyd_smartshop/login.html', context)
		
	if m.password == request.POST['passwd_signIn']:
		request.session['uid'] = m.id
		return index(request)
   	else:
		context = {
			'alerts': "Email and password did not match. Please try again.",  
			'class': "error"
		}
		return render(request,'hyd_smartshop/login.html', context)
	



def signup(request):

	name=request.POST['name']
	email=request.POST['eid']
	password=request.POST['passwd']
	sname=request.POST['sid']
	location=request.POST['lid']
	try:
		m = Users.objects.get(email=email)
		context = {
			'alerts': "Email already exists.",  
			'class': "error"
		}
		return render(request,'mcqportal/login.html', context)
	except Users.DoesNotExist:
		user=Users(username=name,email=email,password=password,storename=sname,location=location)
		user.save()
		request.session['uid']=user.id
		return index(request)

