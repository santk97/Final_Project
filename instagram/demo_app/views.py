# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.

def signup_view(request):
    #Business Logic
    return render(request,'signup.html')
