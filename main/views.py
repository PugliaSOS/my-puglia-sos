from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    """
    Index page
    Return dashboard if authenticated, else login page.
    """

    if request.user.is_authenticated():
        return render(request, 'main/dashboard.html', {'user': request.user})
    return redirect('login/')


def signup(request):
    """
    Signup page
    For POST requests: signup and redirect to index or return signup page
    showing errors.
    For GET requests: show signup page if not authenitcated, else redirect to
    index.
    """

    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        # Sign up
        if request.POST['password'] != request.POST['password_confirm']:
            return render(request, 'main/signup.html', {'errors': True})
        User.objects.create_user(request.POST['username'], None, request.POST['password'],
            first_name=request.POST['first_name'], last_name=request.POST['last_name']
            )
        return redirect('/')
    return render(request, 'main/signup.html')


@login_required(login_url='/login/')
def settings(request):
    """ Settings page """
    return render(request, 'main/settings.html')


@login_required(login_url='/login/')
def change_profile(request):
    pass


@login_required(login_url='/login/')
def association_status(request):
    """ Association status page """
    pass

@login_required(login_url='/login/')
def status(request):
    pass
