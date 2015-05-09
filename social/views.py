from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def get_registred(request):
    all_registred = User.objects.all()
    return render(request, 'social/registred.html', all_registred)
