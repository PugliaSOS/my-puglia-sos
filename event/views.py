from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from event.models import Event, Joining, Post
from poll.models import Submitting


@login_required(login_url='/login/')
def get_all(request):
    """ Return events user has not joined """

    # Get the list of events the user joined, and get the array of pks
    joined = Joining.objects.filter(
        user=request.user).values_list("event__pk", flat=True)

    # Get all events whose pk is not in joined
    events = Event.objects.exclude(pk__in=joined)

    return render(request, "event/list.html", {"events": events})


@login_required(login_url='/login/')
def get_joined(request):
    """ Return events user has joined """

    # Get the list of events the user joined, and get the array of pks
    joined = Joining.objects.filter(
        user=request.user).values_list("event__pk", flat=True)

    # Get all events whose pk is in joined
    events = Event.objects.filter(pk__in=joined)

    return render(
        request,
        "event/list.html",
        {
            "events": events,
            "joined": True
        })


@login_required(login_url='/login/')
def get_event(request, event):
    """ Get a specific event """
    
    res = Joining.objects.filter(user=request.user, event__pk=event)
    

    # If user joined the event, res will be greater than 0
    if len(res) == 0:
        res = Event.objects.get(pk=event)
        joined = False
        accepted = None
    else:
        posts = Post.objects.filter(event_pk=event)
        accepted = res[0].accepted
        res = res[0].event
        joined = True

    return render(
        request,
        "event/detail.html",
        {
            "posts": posts,
            "event": res,
            "joined": joined,
            "accepted": accepted
        })


@login_required(login_url='/login/')
def join(request, event):
    """ Join event """

    # Redirect if user already joined
    if len(Joining.objects.filter(user=request.user, event__pk=event)) != 0:
        return redirect('event', event=event)

    event = Event.objects.get(pk=event)

    # Check if event requires a poll to be filled out
    if event.poll:
        if len(Submitting.objects.filter(
                user=request.user,
                event=event)) == 0:
            return redirect('poll', poll=event.poll.id, event=event.id)

    # Now user can join event
    Joining.objects.create(event=event, user=request.user)
    return redirect('event', event=event.id)


@login_required(login_url='/login/')
def unjoin(request, event):
    """ Join event """

    # Redirect if user did not join
    if len(Joining.objects.filter(user=request.user, event__pk=event)) == 0:
        return redirect('index')

    event = Event.objects.get(pk=event)

    # Now user can join event
    Joining.objects.get(event=event, user=request.user).delete()
    return redirect('index')
