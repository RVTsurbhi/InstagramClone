# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import datetime
from forms import SignUpForm, LoginForm, PostForm
from models import UserModel, SessionToken, PostModel
from imgurpython import ImgurClient
from InstaClone.settings import BASE_DIR
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


def post_view(request):
    user = check_validation(request)

    if user:
        if request.method == 'GET':
            form = PostForm()
            return render(request,'post.html', {'form': form })

        elif request.method == 'POST':
            form =PostForm(request.POST, request.FILES)
            if form.is_valid():
                image =form.cleaned_data.get('image')
                caption = form.cleaned_data.get('caption')

                post = PostModel(user=user, image=image, caption=caption)
                post.save()
                path = str(BASE_DIR + "/" + post.image.url)
                client = ImgurClient('b687dd6bf09e4cd', '69bbb8f5736512481ccd5dcf5082480146312fe1')
                post.image_url = client.upload_from_path(path, anon=True)["link"]
                post.save()
    else:
        return redirect('/login')


def feed_view(request):
    user = check_validation(request)
    if user:
        posts= PostModel.objects.all().order_by('created_on')
        return render(request, 'feed.html',{'posts': posts})
    else:
        redirect('/login/')
