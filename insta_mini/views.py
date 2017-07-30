# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import datetime
from forms import SignUpForm, LoginForm
from models import UserModel, SessionToken
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from datetime import timedelta
from django.utils import timezone



# Create your views here.
def signup_view(request):
    date = datetime.datetime.now()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = UserModel(name=name, password=make_password(password), email=email, username=username)
            user.save()
            return render(request, 'success.html')

    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'index.html', {"created": date, 'form': form })

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():

            user = UserModel.objects.filter(username= form.cleaned_data['username']).first()
            if user:
                #check the password
                if check_password(form.cleaned_data['password'], user.password):
                    SESSION = SessionToken(user= user)
                    SESSION.create_session_token()
                    SESSION.save()
                    response = redirect('feed/')
                    response.set_cookie(key='session_token',value=SESSION.session_token)
                    return response
                else:
                    print 'password is not correct'
            else:
                print 'user does not exist'
            return render(request, 'index.html')
    elif request.method == "GET":
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


#For validating the session
def check_validation(request):
  if request.COOKIES.get('session_token'):
    session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
    if session:
      return session.user
  else:
    return None

def feed_view(request):
    return render(request,'feed.html', {})
