from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def get_registered(request):
    all_registered = User.objects.all()
    return render(request, 'social/registered.html', {'all_registered':all_registered})

@login_required(login_url='/login/')
def get_profile(request, user):
    user_info=request.user
    return render(request, 'social/userinfo.html', {'user_info':user_info})
