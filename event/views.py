from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from event.models import Event, Joining

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
    event = Joining.objects.get(user=request.user, event__pk=event)
    return render(
        request,
        "event/detail.html",
        {
            "event": event
        })

@login_required(login_url='/login/')
def join(request, event):
    pass
