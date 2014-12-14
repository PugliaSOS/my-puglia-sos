from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from event.models import Event, Joining
from poll.models import Submitting

@login_required(login_url='/login/')
def get_all(request):
    # Return events user has not joined
    joined = Joining.objects.filter(
        user=request.user).values_list("event__pk", flat=True)
    events = Event.objects.exclude(pk__in=joined)
    return render(request, "event/list.html", {"events": events})

@login_required(login_url='/login/')
def get_joined(request):
    # Return events user has joined
    events = Joining.objects.filter(
        user=request.user).values_list("event", flat=True)
    return render(
        request,
        "event/list.html",
        {
            "events": events,
            "joined": True
        })

@login_required(login_url='/login/')
def get_event(request, event):
    res = Joining.objects.filter(user=request.user, event__pk=event)
    if len(res) == 0:
        res = Event.objects.get(pk=event)
        joined = False
        accepted = None
    else:
        accepted = res[0].accepted
        res = res[0].event
        joined = True
    return render(
        request,
        "event/detail.html",
        {
            "event": res,
            "joined": joined,
            "accepted": accepted
        })

@login_required(login_url='/login/')
def join(request, event):
    if len(Joining.objects.filter(user=request.user, event__pk=event)) != 0:
        return redirect('event', event=event)
    event = Event.objects.get(pk=event)
    if event.poll:
        if len(Submitting.objects.filter(
            user=request.user,
            event=event
            )) == 0:
            return redirect('poll', poll=event.poll.id, event=event.id)
    Joining.objects.create(event=event, user=request.user)
    return redirect('event', event=event.id)
