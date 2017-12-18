# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate

from .forms import SignUpForm, ProfileForm

from .models import Profile

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'registration_app_html/profile_create.html')
    else:
        form = SignUpForm()
    return render(request,'registration_app_html/signup.html',{'form':form})

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/registration_app/profile_details/')
    else:
        form = ProfileForm()
        return render(request,'registration_app_html/profile.html',{'form':form})

def profile_details(request):
    try:
        profile=Profile.objects.get(user=request.user)
        context={'profile':profile}
    except:
        context={'errmsg':'You have no profile'}
    return render(request,'registration_app_html/profile_details.html',context)

def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/registration_app/profile_details/')
    else:
        form = ProfileForm(instance=profile)
        return render(request,'registration_app_html/profile.html',{'form':form})
# Create your views here.
