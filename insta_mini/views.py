# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import datetime
from forms import SignUpForm
from models import UserModel
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password



# Create your views here.
def signup_view(request):
    date = datetime.datetime.now()
    if request.method == "POST":
        print 'Sign up form submitted'
    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'index.html', {'created': date,'form': form, })
