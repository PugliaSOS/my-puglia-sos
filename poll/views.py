from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from poll.models import Submitting, Poll
from event.models import Event

@login_required(login_url='/login/')
def get_poll(request, poll, event):
    # Check if user did fill out the poll
    if len(Submitting.objects.filter(
        user=request.user,
        event__id=event,
        poll__id=poll)) != 0:
        return redirect('event', event=event)
    # Submit if a post request has been sent
    if request.method == 'POST':
        e = Event.objects.get(pk=event)
        s = ''
        for k, v in request.POST.items():
            if k != 'csrfmiddlewaretoken':
                s += "%s : %r\n" % (k, v)
        Submitting.objects.create(
            poll=Poll.objects.get(pk=poll),
            user=request.user,
            event=e,
            answer=s)
        # If poll was a requirement for joining an event, join
        if int(e.poll.id) == int(poll):
            return redirect('join_event', event=event)
        return redirect('event', event=event)
    return render(request, 'poll/poll.html', {
        'poll': Poll.objects.get(id=poll)
        })
