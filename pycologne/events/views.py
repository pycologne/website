# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.views import generic
from django.utils.translation import ugettext_lazy as _

from . import models


class DetailView(generic.DetailView):
    """
    Shows details of a specific event.
    """
    model = models.Event
    template_name = 'events/event.html'

    def get_queryset(self):
        """
        List all events.
        """
        return models.Event.objects.all()

    def get(self, request, *args, **kwargs):
        event_id = kwargs.get('pk')
        request.toolbar.populate()

        menu = request.toolbar.get_or_create_menu('events-app', _('events'))
        menu.add_modal_item(_('Add Event'), url=reverse('admin:events_event_add', args=[]))
        menu.add_modal_item(_('Edit Event'), url=reverse('admin:events_event_change', args=[event_id]))
        menu.add_link_item(_('List Events'), url=reverse('events.all', args=[]))
        menu.add_sideframe_item(_('Show History of this Event'), url=reverse('admin:events_event_history', args=[event_id]))
        menu.add_sideframe_item(_('Delete this Event'), url=reverse('admin:events_event_delete', args=[event_id]))

        return super(DetailView, self).get(request, *args, **kwargs)


# TODO: use generic list view (!?)

def view_events(request):
    events = models.Event.objects.order_by('date').all()
    return TemplateResponse(
        request=request,
        context={
            'events': events
        },
        template='events/events.html'
    )
