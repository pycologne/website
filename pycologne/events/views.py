# -*- encoding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from . import models


def view_events(request):
    events = models.Event.objects.order_by('date').all()
    return TemplateResponse(
        request=request,
        context={
            'events': events
        },
        template='events/events.html'
    )


def view_event(request, pk):
    """
    Shows details of a specific event.
    """
    evt = get_object_or_404(models.Event, pk=pk)
    return TemplateResponse(
        request=request,
        context={
            'event': evt
        },
        template='events/event.html'
    )

